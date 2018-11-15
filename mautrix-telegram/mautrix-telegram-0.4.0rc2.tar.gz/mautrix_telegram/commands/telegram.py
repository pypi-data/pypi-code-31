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
from typing import Awaitable, Dict, List, Optional, Tuple
import re

from telethon.errors import (
    InviteHashInvalidError, InviteHashExpiredError, UserAlreadyParticipantError)
from telethon.tl.types import User as TLUser
from telethon.tl.types import TypeUpdates
from telethon.tl.functions.messages import ImportChatInviteRequest, CheckChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest

from .. import puppet as pu, portal as po
from . import command_handler, CommandEvent, SECTION_MISC, SECTION_CREATING_PORTALS


@command_handler(help_section=SECTION_MISC,
                 help_args="[_-r|--remote_] <_query_>",
                 help_text="Search your contacts or the Telegram servers for users.")
async def search(evt: CommandEvent) -> Optional[Dict]:
    if len(evt.args) == 0:
        return await evt.reply("**Usage:** `$cmdprefix+sp search [-r|--remote] <query>`")

    force_remote = False
    if evt.args[0] in {"-r", "--remote"}:
        force_remote = True
        evt.args.pop(0)

    query = " ".join(evt.args)
    if force_remote and len(query) < 5:
        return await evt.reply("Minimum length of query for remote search is 5 characters.")

    results, remote = await evt.sender.search(query, force_remote)

    if not results:
        if len(query) < 5 and remote:
            return await evt.reply("No local results. "
                                   "Minimum length of remote query is 5 characters.")
        return await evt.reply("No results 3:")

    reply = []  # type: List[str]
    if remote:
        reply += ["**Results from Telegram server:**", ""]
    else:
        reply += ["**Results in contacts:**", ""]
    reply += [(f"* [{puppet.displayname}](https://matrix.to/#/{puppet.mxid}): "
               f"{puppet.id} ({similarity}% match)")
              for puppet, similarity in results]

    # TODO somehow show remote channel results when joining by alias is possible?

    return await evt.reply("\n".join(reply))


@command_handler(name="pm",
                 help_section=SECTION_CREATING_PORTALS,
                 help_args="<_identifier_>",
                 help_text="Open a private chat with the given Telegram user. The identifier is "
                           "either the internal user ID, the username or the phone number. "
                           "**N.B.** The phone numbers you start chats with must already be in "
                           "your contacts.")
async def private_message(evt: CommandEvent) -> Optional[Dict]:
    if len(evt.args) == 0:
        return await evt.reply("**Usage:** `$cmdprefix+sp pm <user identifier>`")

    try:
        user = await evt.sender.client.get_entity(evt.args[0])
    except ValueError:
        return await evt.reply("Invalid user identifier or user not found.")

    if not user:
        return await evt.reply("User not found.")
    elif not isinstance(user, TLUser):
        return await evt.reply("That doesn't seem to be a user.")
    portal = po.Portal.get_by_entity(user, evt.sender.tgid)
    await portal.create_matrix_room(evt.sender, user, [evt.sender.mxid])
    return await evt.reply("Created private chat room with "
                           f"{pu.Puppet.get_displayname(user, False)}")


async def _join(evt: CommandEvent, arg: str) -> Tuple[Optional[TypeUpdates], Optional[Dict]]:
    if arg.startswith("joinchat/"):
        invite_hash = arg[len("joinchat/"):]
        try:
            await evt.sender.client(CheckChatInviteRequest(invite_hash))
        except InviteHashInvalidError:
            return None, await evt.reply("Invalid invite link.")
        except InviteHashExpiredError:
            return None, await evt.reply("Invite link expired.")
        try:
            return (await evt.sender.client(ImportChatInviteRequest(invite_hash))), None
        except UserAlreadyParticipantError:
            return None, await evt.reply("You are already in that chat.")
    else:
        channel = await evt.sender.client.get_entity(arg)
        if not channel:
            return None, await evt.reply("Channel/supergroup not found.")
        return await evt.sender.client(JoinChannelRequest(channel)), None


@command_handler(help_section=SECTION_CREATING_PORTALS,
                 help_args="<_link_>",
                 help_text="Join a chat with an invite link.")
async def join(evt: CommandEvent) -> Optional[Dict]:
    if len(evt.args) == 0:
        return await evt.reply("**Usage:** `$cmdprefix+sp join <invite link>`")

    regex = re.compile(r"(?:https?://)?t(?:elegram)?\.(?:dog|me)(?:joinchat/)?/(.+)")
    arg = regex.match(evt.args[0])
    if not arg:
        return await evt.reply("That doesn't look like a Telegram invite link.")

    updates, _ = await _join(evt, arg.group(1))
    if not updates:
        return None

    for chat in updates.chats:
        portal = po.Portal.get_by_entity(chat)
        if portal.mxid:
            await portal.invite_to_matrix([evt.sender.mxid])
            return await evt.reply(f"Invited you to portal of {portal.title}")
        else:
            await evt.reply(f"Creating room for {chat.title}... This might take a while.")
            await portal.create_matrix_room(evt.sender, chat, [evt.sender.mxid])
            return await evt.reply(f"Created room for {portal.title}")
    return None


@command_handler(help_section=SECTION_MISC,
                 help_args="[`chats`|`contacts`|`me`]",
                 help_text="Synchronize your chat portals, contacts and/or own info.")
async def sync(evt: CommandEvent) -> Optional[Dict]:
    if len(evt.args) > 0:
        sync_only = evt.args[0]
        if sync_only not in ("chats", "contacts", "me"):
            return await evt.reply("**Usage:** `$cmdprefix+sp sync [chats|contacts|me]`")
    else:
        sync_only = None

    if not sync_only or sync_only == "chats":
        await evt.sender.sync_dialogs(synchronous_create=True)
    if not sync_only or sync_only == "contacts":
        await evt.sender.sync_contacts()
    if not sync_only or sync_only == "me":
        await evt.sender.update_info()
    return await evt.reply("Synchronization complete.")
