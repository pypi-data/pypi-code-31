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


class FieldList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, assistant_sid, intent_sid):
        """
        Initialize the FieldList

        :param Version version: Version that contains the resource
        :param assistant_sid: The unique ID of the parent Assistant.
        :param intent_sid: The unique ID of the Intent associated with this Field.

        :returns: twilio.rest.preview.understand.assistant.intent.field.FieldList
        :rtype: twilio.rest.preview.understand.assistant.intent.field.FieldList
        """
        super(FieldList, self).__init__(version)

        # Path Solution
        self._solution = {'assistant_sid': assistant_sid, 'intent_sid': intent_sid, }
        self._uri = '/Assistants/{assistant_sid}/Intents/{intent_sid}/Fields'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams FieldInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.preview.understand.assistant.intent.field.FieldInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists FieldInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.understand.assistant.intent.field.FieldInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of FieldInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FieldInstance
        :rtype: twilio.rest.preview.understand.assistant.intent.field.FieldPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return FieldPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FieldInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FieldInstance
        :rtype: twilio.rest.preview.understand.assistant.intent.field.FieldPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return FieldPage(self._version, response, self._solution)

    def create(self, field_type, unique_name):
        """
        Create a new FieldInstance

        :param unicode field_type: The unique name or sid of the FieldType. It can be any Built-in Field Type or the unique_name or sid of a custom Field Type.
        :param unicode unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.

        :returns: Newly created FieldInstance
        :rtype: twilio.rest.preview.understand.assistant.intent.field.FieldInstance
        """
        data = values.of({'FieldType': field_type, 'UniqueName': unique_name, })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return FieldInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            intent_sid=self._solution['intent_sid'],
        )

    def get(self, sid):
        """
        Constructs a FieldContext

        :param sid: The sid

        :returns: twilio.rest.preview.understand.assistant.intent.field.FieldContext
        :rtype: twilio.rest.preview.understand.assistant.intent.field.FieldContext
        """
        return FieldContext(
            self._version,
            assistant_sid=self._solution['assistant_sid'],
            intent_sid=self._solution['intent_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a FieldContext

        :param sid: The sid

        :returns: twilio.rest.preview.understand.assistant.intent.field.FieldContext
        :rtype: twilio.rest.preview.understand.assistant.intent.field.FieldContext
        """
        return FieldContext(
            self._version,
            assistant_sid=self._solution['assistant_sid'],
            intent_sid=self._solution['intent_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Understand.FieldList>'


class FieldPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the FieldPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param assistant_sid: The unique ID of the parent Assistant.
        :param intent_sid: The unique ID of the Intent associated with this Field.

        :returns: twilio.rest.preview.understand.assistant.intent.field.FieldPage
        :rtype: twilio.rest.preview.understand.assistant.intent.field.FieldPage
        """
        super(FieldPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FieldInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.understand.assistant.intent.field.FieldInstance
        :rtype: twilio.rest.preview.understand.assistant.intent.field.FieldInstance
        """
        return FieldInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            intent_sid=self._solution['intent_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Understand.FieldPage>'


class FieldContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, assistant_sid, intent_sid, sid):
        """
        Initialize the FieldContext

        :param Version version: Version that contains the resource
        :param assistant_sid: The assistant_sid
        :param intent_sid: The intent_sid
        :param sid: The sid

        :returns: twilio.rest.preview.understand.assistant.intent.field.FieldContext
        :rtype: twilio.rest.preview.understand.assistant.intent.field.FieldContext
        """
        super(FieldContext, self).__init__(version)

        # Path Solution
        self._solution = {'assistant_sid': assistant_sid, 'intent_sid': intent_sid, 'sid': sid, }
        self._uri = '/Assistants/{assistant_sid}/Intents/{intent_sid}/Fields/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a FieldInstance

        :returns: Fetched FieldInstance
        :rtype: twilio.rest.preview.understand.assistant.intent.field.FieldInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return FieldInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            intent_sid=self._solution['intent_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the FieldInstance

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
        return '<Twilio.Preview.Understand.FieldContext {}>'.format(context)


class FieldInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, assistant_sid, intent_sid, sid=None):
        """
        Initialize the FieldInstance

        :returns: twilio.rest.preview.understand.assistant.intent.field.FieldInstance
        :rtype: twilio.rest.preview.understand.assistant.intent.field.FieldInstance
        """
        super(FieldInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'field_type': payload['field_type'],
            'intent_sid': payload['intent_sid'],
            'assistant_sid': payload['assistant_sid'],
            'sid': payload['sid'],
            'unique_name': payload['unique_name'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {
            'assistant_sid': assistant_sid,
            'intent_sid': intent_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: FieldContext for this FieldInstance
        :rtype: twilio.rest.preview.understand.assistant.intent.field.FieldContext
        """
        if self._context is None:
            self._context = FieldContext(
                self._version,
                assistant_sid=self._solution['assistant_sid'],
                intent_sid=self._solution['intent_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The unique ID of the Account that created this Field.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def date_created(self):
        """
        :returns: The date that this resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def field_type(self):
        """
        :returns: The Field Type of this field. It can be any Built-in Field Type or unique_name or the Field Type sid of a custom Field Type.
        :rtype: unicode
        """
        return self._properties['field_type']

    @property
    def intent_sid(self):
        """
        :returns: The unique ID of the Intent associated with this Field.
        :rtype: unicode
        """
        return self._properties['intent_sid']

    @property
    def assistant_sid(self):
        """
        :returns: The unique ID of the parent Assistant.
        :rtype: unicode
        """
        return self._properties['assistant_sid']

    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def unique_name(self):
        """
        :returns: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a FieldInstance

        :returns: Fetched FieldInstance
        :rtype: twilio.rest.preview.understand.assistant.intent.field.FieldInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the FieldInstance

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
        return '<Twilio.Preview.Understand.FieldInstance {}>'.format(context)
