# -*- coding:utf-8 -*-
"""
Description:
    Functions for signing data to send to the Switcheo API by using NEO Utilities to cryptographically sign
    data that gets authenticated on the NEO network.
Usage:
    from switcheo.neo.signatures import <function_name>
"""

from switcheo.utils import get_epoch_milliseconds
from switcheo.neo.utils import sign_message, sign_transaction, sign_txn_array, encode_message,\
    neo_get_scripthash_from_private_key, private_key_to_hex


def sign_create_cancellation(cancellation_params, key_pair):
    """
    Function to sign the parameters required to create a cancellation request from the Switcheo Exchange.
    Execution of this function is as follows::

        sign_create_cancellation(cancellation_params=signable_params, key_pair=key_pair)

    The expected return result for this function is as follows::

        {
            'order_id': 'aa647b95-d546-4d29-961e-bd62b18b07bf',
            'timestamp': 1542092600331,
            'address': 'fea2b883725ef2d194c9060f606cd0a0468a2c59',
            'signature': '475bc3ecd2310201a3b5357b52b1866aaf5a5618932500e43503ebb....'
        }

    :param cancellation_params: Dictionary with Order ID and timestamp to sign for creating the cancellation.
    :type cancellation_params: dict
    :param key_pair: The KeyPair for the wallet being used to sign deposit message.
    :type key_pair: KeyPair
    :return: Dictionary of signed message to send to the Switcheo API.
    """
    encoded_message = encode_message(cancellation_params)
    create_params = cancellation_params.copy()
    create_params['address'] = neo_get_scripthash_from_private_key(private_key=key_pair.PrivateKey).ToString()
    create_params['signature'] = sign_message(encoded_message=encoded_message,
                                              private_key_hex=private_key_to_hex(key_pair=key_pair))
    return create_params


def sign_execute_cancellation(cancellation_params, key_pair):
    """
    Function to sign the parameters required to execute a cancellation request on the Switcheo Exchange.
    Execution of this function is as follows::

        sign_execute_cancellation(cancellation_params=signable_params, key_pair=key_pair)

    The expected return result for this function is as follows::

        {
            'signature': '6a40d6c011b7517f8fd3f2d0de32dd486adfd1d424d06d56c80eb....'
        }

    :param cancellation_params: Parameters the Switcheo Exchange returns from the create cancellation.
    :type cancellation_params: dict
    :param key_pair: The KeyPair for the wallet being used to sign deposit message.
    :type key_pair: KeyPair
    :return: Dictionary of signed message to send to the Switcheo API.
    """
    signature = sign_transaction(transaction=cancellation_params['transaction'],
                                 private_key_hex=private_key_to_hex(key_pair=key_pair))
    return {'signature': signature}


def sign_create_deposit(deposit_params, key_pair):
    """
    Function to create a deposit request by generating a transaction request from the Switcheo API.
    Execution of this function is as follows::

        sign_create_deposit(deposit_details=create_deposit, key_pair=key_pair)

    The expected return result for this function is as follows::

        {
            'blockchain': 'neo',
            'asset_id': 'SWTH',
            'amount': '100',
            'timestamp': 1542091927575,
            'contract_hash': 'a195c1549e7da61b8da315765a790ac7e7633b82',
            'address': 'fea2b883725ef2d194c9060f606cd0a0468a2c59',
            'signature': '24ef6c63964988a2efe5fe67f04f46fdc2f1504fb5....'
        }

    :param deposit_params: The parameters generated by the create deposit function that now requires signature.
    :type deposit_params: dict
    :param key_pair: The KeyPair for the wallet being used to sign deposit message.
    :type key_pair: KeyPair
    :return: Dictionary response of signed deposit request that is ready to be executed on the NEO blockchain.
    """
    encoded_message = encode_message(deposit_params)
    create_params = deposit_params.copy()
    create_params['address'] = neo_get_scripthash_from_private_key(private_key=key_pair.PrivateKey).ToString()
    create_params['signature'] = sign_message(encoded_message=encoded_message,
                                              private_key_hex=private_key_to_hex(key_pair=key_pair))
    return create_params


def sign_execute_deposit(deposit_params, key_pair):
    """
    Function to execute the deposit request by signing the transaction generated by the create deposit function.
    Execution of this function is as follows::

        sign_execute_deposit(deposit_details=create_deposit, key_pair=key_pair)

    The expected return result for this function is as follows::

        {
            'signature': '3cc4a5cb7b7d50383e799add2ba35382b6f2f1b2e3b97802....'
        }

    :param deposit_params: The parameters generated by the create deposit function that now requires signature.
    :type deposit_params: dict
    :param key_pair: The KeyPair for the wallet being used to sign deposit message.
    :type key_pair: KeyPair
    :return: Dictionary with the result status of the deposit attempt.
    """
    signature = sign_transaction(transaction=deposit_params['transaction'],
                                 private_key_hex=private_key_to_hex(key_pair=key_pair))
    return {'signature': signature}


def sign_create_order(order_params, key_pair):
    """
    Function to sign the create order parameters and send to the Switcheo API.
    Execution of this function is as follows::

        sign_create_order(order_params=signable_params, key_pair=key_pair)

    The expected return result for this function is as follows::

        {
            'blockchain': 'neo',
            'pair': 'SWTH_NEO',
            'side': 'buy',
            'price': '0.00001000',
            'want_amount': '1000000000000',
            'use_native_tokens': True,
            'order_type': 'limit',
            'timestamp': 1542091535839,
            'contract_hash': 'a195c1549e7da61b8da315765a790ac7e7633b82',
            'address': 'fea2b883725ef2d194c9060f606cd0a0468a2c59',
            'signature': '88e93c14a7d3c2cf30dec012ad5cb69f5ff26fe2a....'
        }

    :param order_params: Parameters to create an order to be submitted to the Switcheo Order Book.
    :type order_params: dict
    :param key_pair: The NEO key pair to be used to sign messages for the NEO Blockchain.
    :type key_pair: KeyPair
    :return: Dictionary of signed message to send to the Switcheo API.
    """
    encoded_message = encode_message(order_params)
    create_params = order_params.copy()
    create_params['address'] = neo_get_scripthash_from_private_key(private_key=key_pair.PrivateKey).ToString()
    create_params['signature'] = sign_message(encoded_message=encoded_message,
                                              private_key_hex=private_key_to_hex(key_pair=key_pair))
    return create_params


def sign_execute_order(order_params, key_pair):
    """
    Function to execute the order request by signing the transaction generated from the create order function.
    Execution of this function is as follows::

        sign_execute_order(order_params=signable_params, key_pair=key_pair)

    The expected return result for this function is as follows::

        {
            'signatures': {
                'fill_groups': {},
                'fills': {},
                'makes': {
                    '952defd3-ad8a-4db3-bbd1-27d58ff6c7bd': '3f5aa331a731a808fe260502421cbb06ae3d5ea5ddfb1....'
                }
            }
        }

    :param order_params: The parameters generated by the create function that now require signing.
    :type order_params: dict
    :param key_pair: The NEO key pair to be used to sign messages for the NEO Blockchain.
    :type key_pair: KeyPair
    :return: Dictionary of the signed transaction to place an order on the Switcheo Order Book.
    """
    execute_params = {
        'signatures': {
            'fill_groups': {},
            'fills': sign_txn_array(messages=order_params['fills'],
                                    private_key_hex=private_key_to_hex(key_pair=key_pair)),
            'makes': sign_txn_array(messages=order_params['makes'],
                                    private_key_hex=private_key_to_hex(key_pair=key_pair))
        }
    }
    return execute_params


def sign_create_withdrawal(withdrawal_params, key_pair):
    """
    Function to create the withdrawal request by signing the parameters necessary for withdrawal.
    Execution of this function is as follows::

        sign_create_withdrawal(withdrawal_params=signable_params, private_key=eth_private_key)

    The expected return result for this function is as follows::

        {
            'blockchain': 'neo',
            'asset_id': 'SWTH',
            'amount': '100',
            'timestamp': 1542090737236,
            'contract_hash': 'a195c1549e7da61b8da315765a790ac7e7633b82',
            'address': 'fea2b883725ef2d194c9060f606cd0a0468a2c59',
            'signature': 'f66d604c0a80940bf70ce9e13c0fd47bc79de....'
        }

    :param withdrawal_params: Dictionary specifications for withdrawal from the Switcheo Smart Contract.
    :type withdrawal_params: dict
    :param key_pair: The NEO key pair to be used to sign messages for the NEO Blockchain.
    :type key_pair: KeyPair
    :return: Dictionary of parameters to be sent to the Switcheo API
    """
    encoded_message = encode_message(withdrawal_params)
    create_params = withdrawal_params.copy()
    create_params['address'] = neo_get_scripthash_from_private_key(private_key=key_pair.PrivateKey).ToString()
    create_params['signature'] = sign_message(encoded_message=encoded_message,
                                              private_key_hex=private_key_to_hex(key_pair=key_pair))
    return create_params


def sign_execute_withdrawal(withdrawal_params, key_pair):
    """
    Function to execute the withdrawal request by signing the transaction generated from the create withdrawal function.
    Execution of this function is as follows::

        sign_execute_withdrawal(withdrawal_params=signable_params, private_key=eth_private_key)

    The expected return result for this function is as follows::

        {
            'id': '3e1c0802-b44e-4681-a94d-29c1dec2f518',
            'timestamp': 1542090738192,
            'signature': 'e05a7b7bd30eb85959d75ea634cee06ad35d96502a763ae40....'
        }

    :param withdrawal_params: Parameters passed from the create withdrawal function to be signed and confirmed.
    :type withdrawal_params: dict
    :param key_pair: The NEO key pair to be used to sign messages for the NEO Blockchain.
    :type key_pair: KeyPair
    :return: Dictionary of parameters to be sent to the Switcheo API
    """
    withdrawal_id = withdrawal_params['id']
    signable_params = {
        'id': withdrawal_id,
        'timestamp': get_epoch_milliseconds()
    }
    encoded_message = encode_message(signable_params)
    execute_params = signable_params.copy()
    execute_params['signature'] = sign_message(encoded_message=encoded_message,
                                               private_key_hex=private_key_to_hex(key_pair=key_pair))
    return execute_params
