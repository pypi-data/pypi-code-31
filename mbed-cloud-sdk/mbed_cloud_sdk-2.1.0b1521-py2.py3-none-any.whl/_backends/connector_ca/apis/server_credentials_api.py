# coding: utf-8

"""
    Connect CA API

    Connect CA API allows services to get device credentials.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ..api_client import ApiClient


class ServerCredentialsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_server_credentials(self, authorization, **kwargs):  # noqa: E501
        """Fetch all (Bootstrap and LwM2M) server credentials.  # noqa: E501

        This REST API is intended to be used by customers to fetch all (Bootstrap and LwM2M) server credentials that they will need to use with their clients to connect to bootstrap or LwM2M server.  **Example usage:** curl -X GET \"http://api.us-east-1.mbedcloud.com/v3/server-credentials\" -H \"accept: application/json\" -H \"Authorization: Bearer THE_ACCESS_TOKEN\"   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.get_all_server_credentials(authorization, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str authorization: Bearer {Access Token}.  (required)
        :return: AllServerCredentialsResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.get_all_server_credentials_with_http_info(authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.get_all_server_credentials_with_http_info(authorization, **kwargs)  # noqa: E501
            return data

    def get_all_server_credentials_with_http_info(self, authorization, **kwargs):  # noqa: E501
        """Fetch all (Bootstrap and LwM2M) server credentials.  # noqa: E501

        This REST API is intended to be used by customers to fetch all (Bootstrap and LwM2M) server credentials that they will need to use with their clients to connect to bootstrap or LwM2M server.  **Example usage:** curl -X GET \"http://api.us-east-1.mbedcloud.com/v3/server-credentials\" -H \"accept: application/json\" -H \"Authorization: Bearer THE_ACCESS_TOKEN\"   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.get_all_server_credentials_with_http_info(authorization, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str authorization: Bearer {Access Token}.  (required)
        :return: AllServerCredentialsResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_server_credentials" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_all_server_credentials`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v3/server-credentials', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AllServerCredentialsResponseData',  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_bootstrap_server_credentials(self, authorization, **kwargs):  # noqa: E501
        """Fetch bootstrap server credentials.  # noqa: E501

        This REST API is intended to be used by customers to fetch bootstrap server credentials that they will need to use with their clients to connect to bootstrap server.  **Example usage:** curl -X GET \"http://api.us-east-1.mbedcloud.com/v3/server-credentials/bootstrap\" -H \"accept: application/json\" -H \"Authorization: Bearer THE_ACCESS_TOKEN\"   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.get_bootstrap_server_credentials(authorization, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str authorization: Bearer {Access Token}.  (required)
        :return: ServerCredentialsResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.get_bootstrap_server_credentials_with_http_info(authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.get_bootstrap_server_credentials_with_http_info(authorization, **kwargs)  # noqa: E501
            return data

    def get_bootstrap_server_credentials_with_http_info(self, authorization, **kwargs):  # noqa: E501
        """Fetch bootstrap server credentials.  # noqa: E501

        This REST API is intended to be used by customers to fetch bootstrap server credentials that they will need to use with their clients to connect to bootstrap server.  **Example usage:** curl -X GET \"http://api.us-east-1.mbedcloud.com/v3/server-credentials/bootstrap\" -H \"accept: application/json\" -H \"Authorization: Bearer THE_ACCESS_TOKEN\"   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.get_bootstrap_server_credentials_with_http_info(authorization, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str authorization: Bearer {Access Token}.  (required)
        :return: ServerCredentialsResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bootstrap_server_credentials" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_bootstrap_server_credentials`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v3/server-credentials/bootstrap', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServerCredentialsResponseData',  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_l2_m2_m_server_credentials(self, authorization, **kwargs):  # noqa: E501
        """Fetch LwM2M server credentials.  # noqa: E501

        This REST API is intended to be used by customers to fetch LwM2M server credentials that they will need to use with their clients to connect to LwM2M server.  **Example usage:** curl -X GET \"http://api.us-east-1.mbedcloud.com/v3/server-credentials/lwm2m\" -H \"accept: application/json\" -H \"Authorization: Bearer THE_ACCESS_TOKEN\"   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.get_l2_m2_m_server_credentials(authorization, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str authorization: Bearer {Access Token}.  (required)
        :return: ServerCredentialsResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.get_l2_m2_m_server_credentials_with_http_info(authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.get_l2_m2_m_server_credentials_with_http_info(authorization, **kwargs)  # noqa: E501
            return data

    def get_l2_m2_m_server_credentials_with_http_info(self, authorization, **kwargs):  # noqa: E501
        """Fetch LwM2M server credentials.  # noqa: E501

        This REST API is intended to be used by customers to fetch LwM2M server credentials that they will need to use with their clients to connect to LwM2M server.  **Example usage:** curl -X GET \"http://api.us-east-1.mbedcloud.com/v3/server-credentials/lwm2m\" -H \"accept: application/json\" -H \"Authorization: Bearer THE_ACCESS_TOKEN\"   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.get_l2_m2_m_server_credentials_with_http_info(authorization, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str authorization: Bearer {Access Token}.  (required)
        :return: ServerCredentialsResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_l2_m2_m_server_credentials" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_l2_m2_m_server_credentials`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v3/server-credentials/lwm2m', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServerCredentialsResponseData',  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
