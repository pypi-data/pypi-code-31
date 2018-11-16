import time
import traceback
import urllib.parse as urlparse
from typing import List

import json
import requests
from steampy import guard
from steampy.confirmation import ConfirmationExecutor
from steampy.exceptions import SevenDaysHoldException, LoginRequired, ApiException
from steampy.login import LoginExecutor, InvalidCredentials, fast_login
from steampy.models import Asset, TradeOfferState, SteamUrl, GameOptions
from steampy.utils import text_between, texts_between, merge_items_with_descriptions_from_inventory, \
    steam_id_to_account_id, merge_items_with_descriptions_from_offers, get_description_key, \
    merge_items_with_descriptions_from_offer, account_id_to_steam_id, get_key_value_from_url, \
    merge_items_with_descriptions_by_eshao


def login_required(func):
    def func_wrapper(self, *args, **kwargs):
        if not self.was_login_executed:
            raise LoginRequired('Use login method first')
        else:
            return func(self, *args, **kwargs)

    return func_wrapper


class SteamClient:
    def __init__(self, api_key: str, username=None, _guard=None, config=None) -> None:
        self._api_key = api_key
        self._session = requests.Session()
        self.steam_guard = _guard
        self.was_login_executed = False
        self.username = username
        self._session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        if config:
            _id = _guard['steamid']
            token = config['Session']['OAuthToken']
            if fast_login(_id, token, self._session) and self.is_session_alive():
                self.was_login_executed = True
                print('Fast login success!')

    def login(self, username: str, password: str, steam_guard: str) -> None:
        self.steam_guard = guard.load_steam_guard(steam_guard)
        self.username = username
        LoginExecutor(username, password, self.steam_guard['shared_secret'], self._session).login()
        self.was_login_executed = True

    @login_required
    def logout(self) -> None:
        url = LoginExecutor.STORE_URL + '/logout/'
        params = {'sessionid': self._get_session_id()}
        self._session.post(url, params)
        if self.is_session_alive():
            raise Exception("Logout unsuccessful")
        self.was_login_executed = False

    def is_session_alive(self):
        steam_login = self.username
        main_page_response = self._session.get(SteamUrl.COMMUNITY_URL)
        return steam_login.lower() in main_page_response.text.lower()

    def api_call(self, request_method: str, interface: str, api_method: str, version: str,
                 params: dict = None) -> requests.Response:
        url = '/'.join([SteamUrl.API_URL, interface, api_method, version])
        if request_method == 'GET':
            response = requests.get(url, params=params)
        else:
            response = requests.post(url, data=params)
        if self.is_invalid_api_key(response):
            raise InvalidCredentials('Invalid API key')
        return response

    @staticmethod
    def is_invalid_api_key(response: requests.Response) -> bool:
        msg = 'Access is denied. Retrying will not help. Please verify your <pre>key=</pre> parameter'
        return msg in response.text

    @login_required
    def get_my_inventory(self, game: GameOptions, merge: bool = True) -> dict:
        url = SteamUrl.COMMUNITY_URL + '/my/inventory/json/' + \
              game.app_id + '/' + \
              game.context_id
        response_dict = self._session.get(url).json()
        if merge:
            return merge_items_with_descriptions_from_inventory(response_dict, game)
        return response_dict

    def get_inventory_asset(self, game: GameOptions = GameOptions.DOTA2, merge: bool = True, steam_id=None) -> dict:
        count = 1000
        start_assetid = ''
        result = []
        while True:
            url = '{SteamUrl}/inventory/{steamid}/{app_id}/{context_id}/?count={count}&start_assetid={assetid}'.format(
                SteamUrl=SteamUrl.COMMUNITY_URL,
                steamid=steam_id if steam_id else self.steam_guard['steamid'],
                app_id=game.app_id,
                context_id=game.context_id,
                count=count,
                assetid=start_assetid,
            )
            try:
                resp = self._session.get(url)
            except Exception as e:
                print('读取steam库存出错,等待重试', e)
                time.sleep(5)
                continue
            response_dict = resp.json()
            if 'success' not in response_dict:
                print('Get steam inventory api error', url)
                print(response_dict)
                time.sleep(5)
                continue
            if merge:
                result += merge_items_with_descriptions_by_eshao(response_dict)
            else:
                result += response_dict['assets']

            if 'last_assetid' in response_dict.keys():
                start_assetid = response_dict['last_assetid']
            else:
                return result

    @login_required
    def get_partner_inventory(self, partner_steam_id: str, game: GameOptions, merge: bool = True) -> dict:
        params = {'sessionid': self._get_session_id(),
                  'partner': partner_steam_id,
                  'appid': int(game.app_id),
                  'contextid': game.context_id}
        partner_account_id = steam_id_to_account_id(partner_steam_id)
        headers = {'X-Requested-With': 'XMLHttpRequest',
                   'Referer': SteamUrl.COMMUNITY_URL + '/tradeoffer/new/?partner=' + partner_account_id,
                   'X-Prototype-Version': '1.7'}
        response_dict = self._session.get(SteamUrl.COMMUNITY_URL + '/tradeoffer/new/partnerinventory/',
                                          params=params,
                                          headers=headers).json()
        if merge:
            return merge_items_with_descriptions_from_inventory(response_dict, game)
        return response_dict

    def _get_session_id(self) -> str:
        return self._session.cookies.get_dict()['sessionid']

    def get_trade_offers_summary(self) -> dict:
        params = {'key': self._api_key}
        return self.api_call('GET', 'IEconService', 'GetTradeOffersSummary', 'v1', params).json()

    def get_trade_offers(self, merge: bool = True) -> dict:
        params = {'key': self._api_key,
                  'get_sent_offers': 1,
                  'get_received_offers': 1,
                  'get_descriptions': 1,
                  'language': 'english',
                  'active_only': 1,
                  'historical_only': 0,
                  'time_historical_cutoff': ''}
        response = self.api_call('GET', 'IEconService', 'GetTradeOffers', 'v1', params).json()
        response = self._filter_non_active_offers(response)
        if merge:
            response = merge_items_with_descriptions_from_offers(response)
        return response

    @staticmethod
    def _filter_non_active_offers(offers_response):
        offers_received = offers_response['response'].get('trade_offers_received', [])
        offers_sent = offers_response['response'].get('trade_offers_sent', [])
        offers_response['response']['trade_offers_received'] = list(
            filter(lambda offer: offer['trade_offer_state'] == TradeOfferState.Active, offers_received))
        offers_response['response']['trade_offers_sent'] = list(
            filter(lambda offer: offer['trade_offer_state'] == TradeOfferState.Active, offers_sent))
        return offers_response

    def get_trade_offer(self, trade_offer_id: str, merge: bool = True) -> dict:
        params = {'key': self._api_key,
                  'tradeofferid': trade_offer_id,
                  'language': 'english'}
        response = self.api_call('GET', 'IEconService', 'GetTradeOffer', 'v1', params).json()
        if merge and "descriptions" in response['response']:
            descriptions = {get_description_key(offer): offer for offer in response['response']['descriptions']}
            offer = response['response']['offer']
            response['response']['offer'] = merge_items_with_descriptions_from_offer(offer, descriptions)
        return response

    def get_trade_history(self,
                          max_trades=100,
                          start_after_time=None,
                          start_after_tradeid=None,
                          get_descriptions=True,
                          navigating_back=True,
                          include_failed=True,
                          include_total=True) -> dict:
        params = {
            'key': self._api_key,
            'max_trades': max_trades,
            'start_after_time': start_after_time,
            'start_after_tradeid': start_after_tradeid,
            'get_descriptions': get_descriptions,
            'navigating_back': navigating_back,
            'include_failed': include_failed,
            'include_total': include_total
        }
        response = self.api_call('GET', 'IEconService', 'GetTradeHistory', 'v1', params).json()
        return response

    @login_required
    def get_trade_receipt(self, trade_id: str) -> list:
        html = self._session.get("https://steamcommunity.com/trade/{}/receipt".format(trade_id)).content.decode()
        items = []
        for item in texts_between(html, "oItem = ", ";\r\n\toItem"):
            items.append(json.loads(item))
        return items

    @login_required
    def accept_trade_offer(self, trade_offer_id: str, allow_2fa=False) -> dict:
        trade = self.get_trade_offer(trade_offer_id)
        trade_offer_state = TradeOfferState(trade['response']['offer']['trade_offer_state'])
        if trade_offer_state is not TradeOfferState.Active:
            raise ApiException("Invalid trade offer state: {} ({})".format(trade_offer_state.name,
                                                                           trade_offer_state.value))
        # partner = self._fetch_trade_partner_id(trade_offer_id)
        partner = account_id_to_steam_id(str(trade['response']['offer']['accountid_other']))
        session_id = self._get_session_id()
        accept_url = SteamUrl.COMMUNITY_URL + '/tradeoffer/' + trade_offer_id + '/accept'
        params = {'sessionid': session_id,
                  'tradeofferid': trade_offer_id,
                  'serverid': '1',
                  'partner': partner,
                  'captcha': ''}
        headers = {'Referer': self._get_trade_offer_url(trade_offer_id)}
        response = self._session.post(accept_url, data=params, headers=headers).json()
        if allow_2fa and 'needs_mobile_confirmation' in response:
            while True:
                try:
                    return self._confirm_transaction(trade_offer_id)
                except:
                    traceback.print_exc()
                    print('手机确实出错，10秒后重试')
                    time.sleep(10)
        return response

    def _confirm_transaction(self, trade_offer_id: str) -> dict:
        confirmation_executor = ConfirmationExecutor(self.steam_guard['identity_secret'], self.steam_guard['steamid'],
                                                     self._session)
        return confirmation_executor.send_trade_allow_request(trade_offer_id)

    def decline_trade_offer(self, trade_offer_id: str) -> dict:
        params = {'key': self._api_key,
                  'tradeofferid': trade_offer_id}
        return self.api_call('POST', 'IEconService', 'DeclineTradeOffer', 'v1', params).json()

    def cancel_trade_offer(self, trade_offer_id: str) -> dict:
        params = {'key': self._api_key,
                  'tradeofferid': trade_offer_id}
        return self.api_call('POST', 'IEconService', 'CancelTradeOffer', 'v1', params).json()

    @login_required
    def make_offer(self, items_from_me: List[Asset], items_from_them: List[Asset], partner_steam_id: str,
                   message: str = '') -> dict:
        offer = self._create_offer_dict(items_from_me, items_from_them)
        session_id = self._get_session_id()
        url = SteamUrl.COMMUNITY_URL + '/tradeoffer/new/send'
        server_id = 1
        params = {
            'sessionid': session_id,
            'serverid': server_id,
            'partner': partner_steam_id,
            'tradeoffermessage': message,
            'json_tradeoffer': json.dumps(offer),
            'captcha': '',
            'trade_offer_create_params': '{}'
        }
        partner_account_id = steam_id_to_account_id(partner_steam_id)
        headers = {'Referer': SteamUrl.COMMUNITY_URL + '/tradeoffer/new/?partner=' + partner_account_id,
                   'Origin': SteamUrl.COMMUNITY_URL}
        response = self._session.post(url, data=params, headers=headers).json()
        if response.get('needs_mobile_confirmation'):
            response.update(self._confirm_transaction(response['tradeofferid']))
        return response

    def get_profile(self, steam_id: str) -> dict:
        params = {'steamids': steam_id, 'key': self._api_key}
        response = self.api_call('GET', 'ISteamUser', 'GetPlayerSummaries', 'v0002', params)
        data = response.json()
        return data['response']['players'][0]

    def get_friend_list(self, steam_id: str, relationship_filter: str = "all") -> dict:
        params = {
            'key': self._api_key,
            'steamid': steam_id,
            'relationship': relationship_filter
        }
        resp = self.api_call("GET", "ISteamUser", "GetFriendList", "v1", params)
        data = resp.json()
        return data['friendslist']['friends']

    @staticmethod
    def _create_offer_dict(items_from_me: List[Asset], items_from_them: List[Asset]) -> dict:
        return {
            'newversion': True,
            'version': 2,
            'me': {
                'assets': [asset.to_dict() for asset in items_from_me],
                'currency': [],
                'ready': False
            },
            'them': {
                'assets': [asset.to_dict() for asset in items_from_them],
                'currency': [],
                'ready': False
            }
        }

    @login_required
    def get_escrow_duration(self, trade_offer_url: str) -> int:
        headers = {'Referer': SteamUrl.COMMUNITY_URL + urlparse.urlparse(trade_offer_url).path,
                   'Origin': SteamUrl.COMMUNITY_URL}
        response = self._session.get(trade_offer_url, headers=headers).text
        my_escrow_duration = int(text_between(response, "var g_daysMyEscrow = ", ";"))
        their_escrow_duration = int(text_between(response, "var g_daysTheirEscrow = ", ";"))
        return max(my_escrow_duration, their_escrow_duration)

    @login_required
    def make_offer_with_url(self, items_from_me: List[Asset], items_from_them: List[Asset],
                            trade_offer_url: str, message: str = '') -> dict:
        token = get_key_value_from_url(trade_offer_url, 'token')
        partner_account_id = get_key_value_from_url(trade_offer_url, 'partner')
        partner_steam_id = account_id_to_steam_id(partner_account_id)
        offer = self._create_offer_dict(items_from_me, items_from_them)
        session_id = self._get_session_id()
        url = SteamUrl.COMMUNITY_URL + '/tradeoffer/new/send'
        server_id = 1
        trade_offer_create_params = {'trade_offer_access_token': token}
        params = {
            'sessionid': session_id,
            'serverid': server_id,
            'partner': partner_steam_id,
            'tradeoffermessage': message,
            'json_tradeoffer': json.dumps(offer),
            'captcha': '',
            'trade_offer_create_params': json.dumps(trade_offer_create_params)
        }
        headers = {'Referer': SteamUrl.COMMUNITY_URL + urlparse.urlparse(trade_offer_url).path,
                   'Origin': SteamUrl.COMMUNITY_URL}
        response = self._session.post(url, data=params, headers=headers).json()
        if response.get('needs_mobile_confirmation'):
            finish = False
            while not finish:
                try:
                    response.update(self._confirm_transaction(response['tradeofferid']))
                    finish = True
                except Exception:
                    traceback.print_exc()
                    print('Retry again 10s later')
                    time.sleep(10)
        if 'strError' in response:
            print(response)
            time.sleep(10)
            return self.make_offer_with_url(items_from_me, items_from_them, trade_offer_url, message)
        return response

    @staticmethod
    def _get_trade_offer_url(trade_offer_id: str) -> str:
        return SteamUrl.COMMUNITY_URL + '/tradeoffer/' + trade_offer_id

    @login_required
    def check_bot_is_ban(self, trade_url):
        resp = self._session.get(trade_url)
        if 'error_msg' in resp.text:
            return True
        else:
            return False
