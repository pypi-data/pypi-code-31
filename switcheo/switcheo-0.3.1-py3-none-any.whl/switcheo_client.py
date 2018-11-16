# -*- coding:utf-8 -*-
"""
Description:
    Switcheo Client is designed to standardize interactions with the Python Client.  It can access the Public and Authenticated Clients and is designed to be more user friendly than the forward facing REST API's.
Usage:
    from switcheo.switcheo_client import SwitcheoClient
"""

from switcheo.utils import current_contract_hash
from switcheo.authenticated_client import AuthenticatedClient
from switcheo.neo.utils import neo_get_scripthash_from_address


class SwitcheoClient(AuthenticatedClient):

    def order_history(self, address, pair=None):
        return self.get_orders(neo_get_scripthash_from_address(address=address), pair=pair)

    def balance_current_contract(self, *addresses):
        address_list = []
        contract_dict = {}
        for address in addresses:
            address_list.append(neo_get_scripthash_from_address(address=address))
        current_contract = current_contract_hash(self.contracts)
        for chain in current_contract.keys():
            contract_dict[chain] =\
                self.get_balance(addresses=address_list, contracts=current_contract[chain])
        return contract_dict

    def balance_by_contract(self, *addresses):
        address_list = []
        contract_dict = {}
        for address in addresses:
            address_list.append(neo_get_scripthash_from_address(address=address))
        contracts = self.get_contracts()
        for blockchain in contracts:
            contract_dict[blockchain] = {}
            for key in contracts[blockchain]:
                contract_dict[blockchain][key] =\
                    self.get_balance(addresses=address_list, contracts=contracts[blockchain][key])
        return contract_dict

    def balance_by_address_by_contract(self, *addresses):
        contract_dict = {}
        for address in addresses:
            contract_dict[address] = self.balance_by_contract(address)
        return contract_dict
