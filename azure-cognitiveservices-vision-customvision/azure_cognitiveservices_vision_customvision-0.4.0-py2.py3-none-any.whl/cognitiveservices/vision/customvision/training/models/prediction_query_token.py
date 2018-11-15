# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PredictionQueryToken(Model):
    """PredictionQueryToken.

    :param session:
    :type session: str
    :param continuation:
    :type continuation: str
    :param max_count:
    :type max_count: int
    :param order_by: Possible values include: 'Newest', 'Oldest', 'Suggested'
    :type order_by: str or
     ~azure.cognitiveservices.vision.customvision.training.models.OrderBy
    :param tags:
    :type tags:
     list[~azure.cognitiveservices.vision.customvision.training.models.PredictionQueryTag]
    :param iteration_id:
    :type iteration_id: str
    :param start_time:
    :type start_time: datetime
    :param end_time:
    :type end_time: datetime
    :param application:
    :type application: str
    """

    _attribute_map = {
        'session': {'key': 'session', 'type': 'str'},
        'continuation': {'key': 'continuation', 'type': 'str'},
        'max_count': {'key': 'maxCount', 'type': 'int'},
        'order_by': {'key': 'orderBy', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[PredictionQueryTag]'},
        'iteration_id': {'key': 'iterationId', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'application': {'key': 'application', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PredictionQueryToken, self).__init__(**kwargs)
        self.session = kwargs.get('session', None)
        self.continuation = kwargs.get('continuation', None)
        self.max_count = kwargs.get('max_count', None)
        self.order_by = kwargs.get('order_by', None)
        self.tags = kwargs.get('tags', None)
        self.iteration_id = kwargs.get('iteration_id', None)
        self.start_time = kwargs.get('start_time', None)
        self.end_time = kwargs.get('end_time', None)
        self.application = kwargs.get('application', None)
