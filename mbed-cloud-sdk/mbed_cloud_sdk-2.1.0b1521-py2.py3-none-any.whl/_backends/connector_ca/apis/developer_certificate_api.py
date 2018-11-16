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


class DeveloperCertificateApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_developer_certificate(self, authorization, body, **kwargs):  # noqa: E501
        """Create a new developer certificate to connect to the bootstrap server.  # noqa: E501

        This REST API is intended to be used by customers to get a developer certificate (a certificate that can be flashed into multiple devices to connect to bootstrap server).  **Note:** The number of developer certificates allowed per account is limited. Please see [Using your own certificate authority](/docs/current/mbed-cloud-deploy/instructions-for-factory-setup-and-device-provision.html#using-your-own-certificate-authority-with-mbed-cloud).  **Example usage:** curl -X POST \"http://api.us-east-1.mbedcloud.com/v3/developer-certificates\" -H \"accept: application/json\" -H \"Authorization: Bearer THE_ACCESS_TOKEN\" -H \"content-type: application/json\" -d \"{ \\\"name\\\": \\\"THE_CERTIFICATE_NAME\\\", \\\"description\\\": \\\"THE_CERTIFICATE_DESCRIPTION\\\"}\"   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.create_developer_certificate(authorization, body, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str authorization: Bearer {Access Token}.  (required)
        :param DeveloperCertificateRequestData body: (required)
        :return: DeveloperCertificateResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.create_developer_certificate_with_http_info(authorization, body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_developer_certificate_with_http_info(authorization, body, **kwargs)  # noqa: E501
            return data

    def create_developer_certificate_with_http_info(self, authorization, body, **kwargs):  # noqa: E501
        """Create a new developer certificate to connect to the bootstrap server.  # noqa: E501

        This REST API is intended to be used by customers to get a developer certificate (a certificate that can be flashed into multiple devices to connect to bootstrap server).  **Note:** The number of developer certificates allowed per account is limited. Please see [Using your own certificate authority](/docs/current/mbed-cloud-deploy/instructions-for-factory-setup-and-device-provision.html#using-your-own-certificate-authority-with-mbed-cloud).  **Example usage:** curl -X POST \"http://api.us-east-1.mbedcloud.com/v3/developer-certificates\" -H \"accept: application/json\" -H \"Authorization: Bearer THE_ACCESS_TOKEN\" -H \"content-type: application/json\" -d \"{ \\\"name\\\": \\\"THE_CERTIFICATE_NAME\\\", \\\"description\\\": \\\"THE_CERTIFICATE_DESCRIPTION\\\"}\"   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.create_developer_certificate_with_http_info(authorization, body, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str authorization: Bearer {Access Token}.  (required)
        :param DeveloperCertificateRequestData body: (required)
        :return: DeveloperCertificateResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'body']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_developer_certificate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `create_developer_certificate`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_developer_certificate`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v3/developer-certificates', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeveloperCertificateResponseData',  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_developer_certificate(self, developer_certificate_id, authorization, **kwargs):  # noqa: E501
        """Fetch an existing developer certificate to connect to the bootstrap server.  # noqa: E501

        This REST API is intended to be used by customers to fetch an existing developer certificate (a certificate that can be flashed into multiple devices to connect to bootstrap server).  **Example usage:** curl -X GET \"http://api.us-east-1.mbedcloud.com/v3/developer-certificates/THE_CERTIFICATE_ID\" -H \"accept: application/json\" -H \"Authorization: Bearer THE_ACCESS_TOKEN\"   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.get_developer_certificate(developer_certificate_id, authorization, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str developer_certificate_id: A unique identifier for the developer certificate.  (required)
        :param str authorization: Bearer {Access Token}.  (required)
        :return: DeveloperCertificateResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.get_developer_certificate_with_http_info(developer_certificate_id, authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.get_developer_certificate_with_http_info(developer_certificate_id, authorization, **kwargs)  # noqa: E501
            return data

    def get_developer_certificate_with_http_info(self, developer_certificate_id, authorization, **kwargs):  # noqa: E501
        """Fetch an existing developer certificate to connect to the bootstrap server.  # noqa: E501

        This REST API is intended to be used by customers to fetch an existing developer certificate (a certificate that can be flashed into multiple devices to connect to bootstrap server).  **Example usage:** curl -X GET \"http://api.us-east-1.mbedcloud.com/v3/developer-certificates/THE_CERTIFICATE_ID\" -H \"accept: application/json\" -H \"Authorization: Bearer THE_ACCESS_TOKEN\"   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.get_developer_certificate_with_http_info(developer_certificate_id, authorization, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param str developer_certificate_id: A unique identifier for the developer certificate.  (required)
        :param str authorization: Bearer {Access Token}.  (required)
        :return: DeveloperCertificateResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['developer_certificate_id', 'authorization']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_developer_certificate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'developer_certificate_id' is set
        if ('developer_certificate_id' not in params or
                params['developer_certificate_id'] is None):
            raise ValueError("Missing the required parameter `developer_certificate_id` when calling `get_developer_certificate`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_developer_certificate`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'developer_certificate_id' in params:
            path_params['developerCertificateId'] = params['developer_certificate_id']  # noqa: E501

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
            '/v3/developer-certificates/{developerCertificateId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeveloperCertificateResponseData',  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
