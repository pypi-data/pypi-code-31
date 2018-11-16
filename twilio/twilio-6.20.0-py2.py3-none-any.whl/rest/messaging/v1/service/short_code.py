# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class ShortCodeList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid):
        """
        Initialize the ShortCodeList

        :param Version version: Version that contains the resource
        :param service_sid: The 34 character unique sid of the Service.

        :returns: twilio.rest.messaging.v1.service.short_code.ShortCodeList
        :rtype: twilio.rest.messaging.v1.service.short_code.ShortCodeList
        """
        super(ShortCodeList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, }
        self._uri = '/Services/{service_sid}/ShortCodes'.format(**self._solution)

    def create(self, short_code_sid):
        """
        Create a new ShortCodeInstance

        :param unicode short_code_sid: ShortCodeSid for the Shortcode being added to the Service.

        :returns: Newly created ShortCodeInstance
        :rtype: twilio.rest.messaging.v1.service.short_code.ShortCodeInstance
        """
        data = values.of({'ShortCodeSid': short_code_sid, })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return ShortCodeInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def stream(self, limit=None, page_size=None):
        """
        Streams ShortCodeInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.messaging.v1.service.short_code.ShortCodeInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ShortCodeInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.messaging.v1.service.short_code.ShortCodeInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of ShortCodeInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ShortCodeInstance
        :rtype: twilio.rest.messaging.v1.service.short_code.ShortCodePage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return ShortCodePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ShortCodeInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ShortCodeInstance
        :rtype: twilio.rest.messaging.v1.service.short_code.ShortCodePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return ShortCodePage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a ShortCodeContext

        :param sid: The sid

        :returns: twilio.rest.messaging.v1.service.short_code.ShortCodeContext
        :rtype: twilio.rest.messaging.v1.service.short_code.ShortCodeContext
        """
        return ShortCodeContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a ShortCodeContext

        :param sid: The sid

        :returns: twilio.rest.messaging.v1.service.short_code.ShortCodeContext
        :rtype: twilio.rest.messaging.v1.service.short_code.ShortCodeContext
        """
        return ShortCodeContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.ShortCodeList>'


class ShortCodePage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the ShortCodePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The 34 character unique sid of the Service.

        :returns: twilio.rest.messaging.v1.service.short_code.ShortCodePage
        :rtype: twilio.rest.messaging.v1.service.short_code.ShortCodePage
        """
        super(ShortCodePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ShortCodeInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.messaging.v1.service.short_code.ShortCodeInstance
        :rtype: twilio.rest.messaging.v1.service.short_code.ShortCodeInstance
        """
        return ShortCodeInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.ShortCodePage>'


class ShortCodeContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, sid):
        """
        Initialize the ShortCodeContext

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param sid: The sid

        :returns: twilio.rest.messaging.v1.service.short_code.ShortCodeContext
        :rtype: twilio.rest.messaging.v1.service.short_code.ShortCodeContext
        """
        super(ShortCodeContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'sid': sid, }
        self._uri = '/Services/{service_sid}/ShortCodes/{sid}'.format(**self._solution)

    def delete(self):
        """
        Deletes the ShortCodeInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def fetch(self):
        """
        Fetch a ShortCodeInstance

        :returns: Fetched ShortCodeInstance
        :rtype: twilio.rest.messaging.v1.service.short_code.ShortCodeInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return ShortCodeInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.ShortCodeContext {}>'.format(context)


class ShortCodeInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload, service_sid, sid=None):
        """
        Initialize the ShortCodeInstance

        :returns: twilio.rest.messaging.v1.service.short_code.ShortCodeInstance
        :rtype: twilio.rest.messaging.v1.service.short_code.ShortCodeInstance
        """
        super(ShortCodeInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'short_code': payload['short_code'],
            'country_code': payload['country_code'],
            'capabilities': payload['capabilities'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ShortCodeContext for this ShortCodeInstance
        :rtype: twilio.rest.messaging.v1.service.short_code.ShortCodeContext
        """
        if self._context is None:
            self._context = ShortCodeContext(
                self._version,
                service_sid=self._solution['service_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The 34 character unique sid of the Short Code
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The 34 character unique sid of the Account.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The 34 character unique sid of the Service.
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def date_created(self):
        """
        :returns: he date that this resource was created.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated.
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def short_code(self):
        """
        :returns: The E.164 format of the short code.
        :rtype: unicode
        """
        return self._properties['short_code']

    @property
    def country_code(self):
        """
        :returns: The 2 character ISO Country Code of the number.
        :rtype: unicode
        """
        return self._properties['country_code']

    @property
    def capabilities(self):
        """
        :returns: Any array of values that indicate whether the number can receive calls or messages.
        :rtype: dict
        """
        return self._properties['capabilities']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def delete(self):
        """
        Deletes the ShortCodeInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def fetch(self):
        """
        Fetch a ShortCodeInstance

        :returns: Fetched ShortCodeInstance
        :rtype: twilio.rest.messaging.v1.service.short_code.ShortCodeInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.ShortCodeInstance {}>'.format(context)
