# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class WebhookList(ListResource):
    """  """

    def __init__(self, version, service_sid, channel_sid):
        """
        Initialize the WebhookList

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param channel_sid: The channel_sid

        :returns: twilio.rest.chat.v2.service.channel.webhook.WebhookList
        :rtype: twilio.rest.chat.v2.service.channel.webhook.WebhookList
        """
        super(WebhookList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'channel_sid': channel_sid, }
        self._uri = '/Services/{service_sid}/Channels/{channel_sid}/Webhooks'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams WebhookInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.chat.v2.service.channel.webhook.WebhookInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists WebhookInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v2.service.channel.webhook.WebhookInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of WebhookInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of WebhookInstance
        :rtype: twilio.rest.chat.v2.service.channel.webhook.WebhookPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return WebhookPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of WebhookInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of WebhookInstance
        :rtype: twilio.rest.chat.v2.service.channel.webhook.WebhookPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return WebhookPage(self._version, response, self._solution)

    def create(self, type, configuration_url=values.unset,
               configuration_method=values.unset,
               configuration_filters=values.unset,
               configuration_triggers=values.unset,
               configuration_flow_sid=values.unset,
               configuration_retry_count=values.unset):
        """
        Create a new WebhookInstance

        :param WebhookInstance.Type type: The type
        :param unicode configuration_url: The configuration.url
        :param WebhookInstance.Method configuration_method: The configuration.method
        :param unicode configuration_filters: The configuration.filters
        :param unicode configuration_triggers: The configuration.triggers
        :param unicode configuration_flow_sid: The configuration.flow_sid
        :param unicode configuration_retry_count: The configuration.retry_count

        :returns: Newly created WebhookInstance
        :rtype: twilio.rest.chat.v2.service.channel.webhook.WebhookInstance
        """
        data = values.of({
            'Type': type,
            'Configuration.Url': configuration_url,
            'Configuration.Method': configuration_method,
            'Configuration.Filters': serialize.map(configuration_filters, lambda e: e),
            'Configuration.Triggers': serialize.map(configuration_triggers, lambda e: e),
            'Configuration.FlowSid': configuration_flow_sid,
            'Configuration.RetryCount': configuration_retry_count,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return WebhookInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
        )

    def get(self, sid):
        """
        Constructs a WebhookContext

        :param sid: The sid

        :returns: twilio.rest.chat.v2.service.channel.webhook.WebhookContext
        :rtype: twilio.rest.chat.v2.service.channel.webhook.WebhookContext
        """
        return WebhookContext(
            self._version,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a WebhookContext

        :param sid: The sid

        :returns: twilio.rest.chat.v2.service.channel.webhook.WebhookContext
        :rtype: twilio.rest.chat.v2.service.channel.webhook.WebhookContext
        """
        return WebhookContext(
            self._version,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Chat.V2.WebhookList>'


class WebhookPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the WebhookPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The service_sid
        :param channel_sid: The channel_sid

        :returns: twilio.rest.chat.v2.service.channel.webhook.WebhookPage
        :rtype: twilio.rest.chat.v2.service.channel.webhook.WebhookPage
        """
        super(WebhookPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of WebhookInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.chat.v2.service.channel.webhook.WebhookInstance
        :rtype: twilio.rest.chat.v2.service.channel.webhook.WebhookInstance
        """
        return WebhookInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Chat.V2.WebhookPage>'


class WebhookContext(InstanceContext):
    """  """

    def __init__(self, version, service_sid, channel_sid, sid):
        """
        Initialize the WebhookContext

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param channel_sid: The channel_sid
        :param sid: The sid

        :returns: twilio.rest.chat.v2.service.channel.webhook.WebhookContext
        :rtype: twilio.rest.chat.v2.service.channel.webhook.WebhookContext
        """
        super(WebhookContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'channel_sid': channel_sid, 'sid': sid, }
        self._uri = '/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a WebhookInstance

        :returns: Fetched WebhookInstance
        :rtype: twilio.rest.chat.v2.service.channel.webhook.WebhookInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return WebhookInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=self._solution['sid'],
        )

    def update(self, configuration_url=values.unset,
               configuration_method=values.unset,
               configuration_filters=values.unset,
               configuration_triggers=values.unset,
               configuration_flow_sid=values.unset,
               configuration_retry_count=values.unset):
        """
        Update the WebhookInstance

        :param unicode configuration_url: The configuration.url
        :param WebhookInstance.Method configuration_method: The configuration.method
        :param unicode configuration_filters: The configuration.filters
        :param unicode configuration_triggers: The configuration.triggers
        :param unicode configuration_flow_sid: The configuration.flow_sid
        :param unicode configuration_retry_count: The configuration.retry_count

        :returns: Updated WebhookInstance
        :rtype: twilio.rest.chat.v2.service.channel.webhook.WebhookInstance
        """
        data = values.of({
            'Configuration.Url': configuration_url,
            'Configuration.Method': configuration_method,
            'Configuration.Filters': serialize.map(configuration_filters, lambda e: e),
            'Configuration.Triggers': serialize.map(configuration_triggers, lambda e: e),
            'Configuration.FlowSid': configuration_flow_sid,
            'Configuration.RetryCount': configuration_retry_count,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return WebhookInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the WebhookInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Chat.V2.WebhookContext {}>'.format(context)


class WebhookInstance(InstanceResource):
    """  """

    class Type(object):
        WEBHOOK = "webhook"
        TRIGGER = "trigger"
        STUDIO = "studio"

    class Method(object):
        GET = "GET"
        POST = "POST"

    def __init__(self, version, payload, service_sid, channel_sid, sid=None):
        """
        Initialize the WebhookInstance

        :returns: twilio.rest.chat.v2.service.channel.webhook.WebhookInstance
        :rtype: twilio.rest.chat.v2.service.channel.webhook.WebhookInstance
        """
        super(WebhookInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'channel_sid': payload['channel_sid'],
            'type': payload['type'],
            'url': payload['url'],
            'configuration': payload['configuration'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
        }

        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'channel_sid': channel_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: WebhookContext for this WebhookInstance
        :rtype: twilio.rest.chat.v2.service.channel.webhook.WebhookContext
        """
        if self._context is None:
            self._context = WebhookContext(
                self._version,
                service_sid=self._solution['service_sid'],
                channel_sid=self._solution['channel_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The service_sid
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def channel_sid(self):
        """
        :returns: The channel_sid
        :rtype: unicode
        """
        return self._properties['channel_sid']

    @property
    def type(self):
        """
        :returns: The type
        :rtype: unicode
        """
        return self._properties['type']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def configuration(self):
        """
        :returns: The configuration
        :rtype: dict
        """
        return self._properties['configuration']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    def fetch(self):
        """
        Fetch a WebhookInstance

        :returns: Fetched WebhookInstance
        :rtype: twilio.rest.chat.v2.service.channel.webhook.WebhookInstance
        """
        return self._proxy.fetch()

    def update(self, configuration_url=values.unset,
               configuration_method=values.unset,
               configuration_filters=values.unset,
               configuration_triggers=values.unset,
               configuration_flow_sid=values.unset,
               configuration_retry_count=values.unset):
        """
        Update the WebhookInstance

        :param unicode configuration_url: The configuration.url
        :param WebhookInstance.Method configuration_method: The configuration.method
        :param unicode configuration_filters: The configuration.filters
        :param unicode configuration_triggers: The configuration.triggers
        :param unicode configuration_flow_sid: The configuration.flow_sid
        :param unicode configuration_retry_count: The configuration.retry_count

        :returns: Updated WebhookInstance
        :rtype: twilio.rest.chat.v2.service.channel.webhook.WebhookInstance
        """
        return self._proxy.update(
            configuration_url=configuration_url,
            configuration_method=configuration_method,
            configuration_filters=configuration_filters,
            configuration_triggers=configuration_triggers,
            configuration_flow_sid=configuration_flow_sid,
            configuration_retry_count=configuration_retry_count,
        )

    def delete(self):
        """
        Deletes the WebhookInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Chat.V2.WebhookInstance {}>'.format(context)
