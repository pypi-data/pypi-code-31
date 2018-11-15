# -*- coding: future_fstrings -*-
# mautrix-telegram - A Matrix-Telegram puppeting bridge
# Copyright (C) 2018 Tulir Asokan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from typing import Coroutine, Dict, List, Match, NewType, Optional, Tuple, cast, TYPE_CHECKING
import logging
import asyncio
import re

from telethon.tl.types import (
    TypeUpdate, UpdateNewMessage, UpdateNewChannelMessage, PeerUser,
    UpdateShortChatMessage, UpdateShortMessage)
from telethon.tl.types import User as TLUser
from telethon.tl.types.contacts import ContactsNotModified
from telethon.tl.functions.contacts import GetContactsRequest, SearchRequest
from telethon.tl.functions.account import UpdateStatusRequest
from mautrix_appservice import MatrixRequestError

from .types import MatrixUserID, TelegramID
from .db import User as DBUser, Contact as DBContact, Portal as DBPortal
from .abstract_user import AbstractUser
from . import portal as po, puppet as pu

if TYPE_CHECKING:
    from .config import Config
    from .context import Context

config = None  # type: Config

SearchResult = NewType('SearchResult', Tuple['pu.Puppet', int])


class User(AbstractUser):
    log = logging.getLogger("mau.user")  # type: logging.Logger
    by_mxid = {}  # type: Dict[str, User]
    by_tgid = {}  # type: Dict[int, User]

    def __init__(self, mxid: MatrixUserID, tgid: Optional[TelegramID] = None,
                 username: Optional[str] = None, phone: Optional[str] = None,
                 db_contacts: Optional[List[DBContact]] = None,
                 saved_contacts: int = 0, is_bot: bool = False,
                 db_portals: Optional[List[DBPortal]] = None,
                 db_instance: Optional[DBUser] = None) -> None:
        super().__init__()
        self.mxid = mxid  # type: MatrixUserID
        self.tgid = tgid  # type: TelegramID
        self.is_bot = is_bot  # type: bool
        self.username = username  # type: str
        self.phone = phone  # type: str
        self.contacts = []  # type: List[pu.Puppet]
        self.saved_contacts = saved_contacts  # type: int
        self.db_contacts = db_contacts  # type: List[DBContact]
        self.portals = {}  # type: Dict[Tuple[int, int], po.Portal]
        self.db_portals = db_portals or []  # type: List[DBPortal]
        self._db_instance = db_instance  # type: Optional[DBUser]

        self.command_status = None  # type: Dict

        (self.relaybot_whitelisted,
         self.whitelisted,
         self.puppet_whitelisted,
         self.matrix_puppet_whitelisted,
         self.is_admin,
         self.permissions) = config.get_permissions(self.mxid)

        self.by_mxid[mxid] = self
        if tgid:
            self.by_tgid[tgid] = self

    @property
    def name(self) -> str:
        return self.mxid

    @property
    def mxid_localpart(self) -> str:
        match = re.compile("@(.+):(.+)").match(self.mxid)  # type: Match
        return match.group(1)

    @property
    def human_tg_id(self) -> str:
        return f"@{self.username}" if self.username else f"+{self.phone}" or None

    # TODO replace with proper displayname getting everywhere
    @property
    def displayname(self) -> str:
        return self.mxid_localpart

    @property
    def db_contacts(self) -> List[DBContact]:
        return [self.db.merge(DBContact(user=self.tgid, contact=puppet.id))
                for puppet in self.contacts]

    @db_contacts.setter
    def db_contacts(self, contacts: List[DBContact]) -> None:
        self.contacts = [pu.Puppet.get(entry.contact) for entry in contacts] if contacts else []

    @property
    def db_portals(self) -> List[DBPortal]:
        return [portal.db_instance for portal in self.portals.values() if not portal.deleted]

    @db_portals.setter
    def db_portals(self, portals: List[DBPortal]) -> None:
        self.portals = {
            (portal.tgid, portal.tg_receiver): po.Portal.get_by_tgid(portal.tgid,
                                                                     portal.tg_receiver)
            for portal in portals
        } if portals else {}

    # region Database conversion

    @property
    def db_instance(self) -> DBUser:
        if not self._db_instance:
            self._db_instance = self.new_db_instance()
        return self._db_instance

    def new_db_instance(self) -> DBUser:
        return DBUser(mxid=self.mxid, tgid=self.tgid, tg_username=self.username,
                      contacts=self.db_contacts, saved_contacts=self.saved_contacts,
                      portals=self.db_portals)

    def save(self) -> None:
        self.db_instance.tgid = self.tgid
        self.db_instance.tg_username = self.username
        self.db_instance.tg_phone = self.phone
        self.db_instance.contacts = self.db_contacts
        self.db_instance.saved_contacts = self.saved_contacts
        self.db_instance.portals = self.db_portals
        self.db.commit()

    def delete(self) -> None:
        try:
            del self.by_mxid[self.mxid]
            del self.by_tgid[self.tgid]
        except KeyError:
            pass
        if self._db_instance:
            self.db.delete(self._db_instance)
            self.db.commit()

    @classmethod
    def from_db(cls, db_user: DBUser) -> 'User':
        return User(db_user.mxid, db_user.tgid, db_user.tg_username, db_user.tg_phone,
                    db_user.contacts, db_user.saved_contacts, False, db_user.portals,
                    db_instance=db_user)

    # endregion
    # region Telegram connection management

    async def start(self, delete_unless_authenticated: bool = False) -> 'User':
        await super().start()
        if await self.is_logged_in():
            self.log.debug(f"Ensuring post_login() for {self.name}")
            asyncio.ensure_future(self.post_login(), loop=self.loop)
        elif delete_unless_authenticated:
            self.log.debug(f"Unauthenticated user {self.name} start()ed, deleting session...")
            await self.client.disconnect()
            self.client.session.delete()
        return self

    async def post_login(self, info: TLUser = None) -> None:
        try:
            await self.update_info(info)
            if not self.is_bot:
                await self.sync_dialogs()
                await self.sync_contacts()
            if config["bridge.catch_up"]:
                await self.client.catch_up()
        except Exception:
            self.log.exception("Failed to run post-login functions for %s", self.mxid)

    async def update(self, update: TypeUpdate) -> bool:
        if not self.is_bot:
            return False

        if isinstance(update, (UpdateNewMessage, UpdateNewChannelMessage)):
            message = update.message
            if isinstance(message.to_id, PeerUser) and not message.out:
                portal = po.Portal.get_by_tgid(message.from_id, peer_type="user",
                                               tg_receiver=self.tgid)
            else:
                portal = po.Portal.get_by_entity(message.to_id, receiver_id=self.tgid)
        elif isinstance(update, UpdateShortChatMessage):
            portal = po.Portal.get_by_tgid(TelegramID(update.chat_id), peer_type="chat")
        elif isinstance(update, UpdateShortMessage):
            portal = po.Portal.get_by_tgid(TelegramID(update.user_id), self.tgid, "user")
        else:
            return False

        if portal:
            self.register_portal(portal)

        return True

    # endregion
    # region Telegram actions that need custom methods

    def ensure_started(self, even_if_no_session: bool = False) -> Coroutine[None, None, 'User']:
        return cast(Coroutine[None, None, 'User'], super().ensure_started(even_if_no_session))

    async def set_presence(self, online: bool = True) -> None:
        if not self.is_bot:
            await self.client(UpdateStatusRequest(offline=not online))

    async def update_info(self, info: TLUser = None) -> None:
        info = info or await self.client.get_me()
        changed = False
        if self.is_bot != info.bot:
            self.is_bot = info.bot
            changed = True
        if self.username != info.username:
            self.username = info.username
            changed = True
        if self.phone != info.phone:
            self.phone = info.phone
            changed = True
        if self.tgid != info.id:
            self.tgid = info.id
            self.by_tgid[self.tgid] = self
        if changed:
            self.save()

    async def log_out(self) -> bool:
        puppet = pu.Puppet.get(self.tgid)
        if puppet.is_real_user:
            await puppet.switch_mxid(None, None)
        for _, portal in self.portals.items():
            if not portal.mxid or portal.has_bot:
                continue
            try:
                await portal.main_intent.kick(portal.mxid, self.mxid, "Logged out of Telegram.")
            except MatrixRequestError:
                pass
        self.portals = {}
        self.contacts = []
        self.save()
        if self.tgid:
            try:
                del self.by_tgid[self.tgid]
            except KeyError:
                pass
            self.tgid = None
            self.save()
        ok = await self.client.log_out()
        if not ok:
            return False
        self.delete()
        return True

    def _search_local(self, query: str, max_results: int = 5, min_similarity: int = 45
                      ) -> List[SearchResult]:
        results = []  # type: List[SearchResult]
        for contact in self.contacts:
            similarity = contact.similarity(query)
            if similarity >= min_similarity:
                results.append(SearchResult((contact, similarity)))
        results.sort(key=lambda tup: tup[1], reverse=True)
        return results[0:max_results]

    async def _search_remote(self, query: str, max_results: int = 5) -> List[SearchResult]:
        if len(query) < 5:
            return []
        server_results = await self.client(SearchRequest(q=query, limit=max_results))
        results = []  # type: List[SearchResult]
        for user in server_results.users:
            puppet = pu.Puppet.get(user.id)
            await puppet.update_info(self, user)
            results.append(SearchResult((puppet, puppet.similarity(query))))
        results.sort(key=lambda tup: tup[1], reverse=True)
        return results[0:max_results]

    async def search(self, query: str, force_remote: bool = False
                     ) -> Tuple[List[SearchResult], bool]:
        if force_remote:
            return await self._search_remote(query), True

        results = self._search_local(query)
        if results:
            return results, False

        return await self._search_remote(query), True

    async def sync_dialogs(self, synchronous_create: bool = False) -> None:
        creators = []
        for entity in await self.get_dialogs(limit=30):
            portal = po.Portal.get_by_entity(entity)
            self.portals[portal.tgid_full] = portal
            creators.append(
                portal.create_matrix_room(self, entity, invites=[self.mxid],
                                          synchronous=synchronous_create))
        self.save()
        await asyncio.gather(*creators, loop=self.loop)

    def register_portal(self, portal: po.Portal) -> None:
        try:
            if self.portals[portal.tgid_full] == portal:
                return
        except KeyError:
            pass
        self.portals[portal.tgid_full] = portal
        self.save()

    def unregister_portal(self, portal: po.Portal) -> None:
        try:
            del self.portals[portal.tgid_full]
            self.save()
        except KeyError:
            pass

    async def needs_relaybot(self, portal: po.Portal) -> bool:
        return not await self.is_logged_in() or (
            self.is_bot and portal.tgid_full not in self.portals)

    def _hash_contacts(self) -> int:
        acc = 0
        for id in sorted([self.saved_contacts] + [contact.id for contact in self.contacts]):
            acc = (acc * 20261 + id) & 0xffffffff
        return acc & 0x7fffffff

    async def sync_contacts(self) -> None:
        response = await self.client(GetContactsRequest(hash=self._hash_contacts()))
        if isinstance(response, ContactsNotModified):
            return
        self.log.debug("Updating contacts...")
        self.contacts = []
        self.saved_contacts = response.saved_count
        for user in response.users:
            puppet = pu.Puppet.get(user.id)
            await puppet.update_info(self, user)
            self.contacts.append(puppet)
        self.save()

    # endregion
    # region Class instance lookup

    @classmethod
    def get_by_mxid(cls, mxid: MatrixUserID, create: bool = True) -> Optional['User']:
        if not mxid:
            raise ValueError("Matrix ID can't be empty")

        try:
            return cls.by_mxid[mxid]
        except KeyError:
            pass

        user = DBUser.query.get(mxid)
        if user:
            user = cls.from_db(user)
            return user

        if create:
            user = cls(mxid)
            cls.db.add(user.db_instance)
            cls.db.commit()
            return user

        return None

    @classmethod
    def get_by_tgid(cls, tgid: int) -> Optional['User']:
        try:
            return cls.by_tgid[tgid]
        except KeyError:
            pass

        user = DBUser.query.filter(DBUser.tgid == tgid).one_or_none()
        if user:
            user = cls.from_db(user)
            return user

        return None

    @classmethod
    def find_by_username(cls, username: str) -> Optional['User']:
        if not username:
            return None

        for _, user in cls.by_tgid.items():
            if user.username and user.username.lower() == username.lower():
                return user

        puppet = DBUser.query.filter(DBUser.tg_username == username).one_or_none()
        if puppet:
            return cls.from_db(puppet)

        return None
    # endregion


def init(context: 'Context') -> List[Coroutine]:  # [None, None, AbstractUser]
    global config
    config = context.config

    users = [User.from_db(user) for user in DBUser.query.all()]
    return [user.ensure_started() for user in users]
