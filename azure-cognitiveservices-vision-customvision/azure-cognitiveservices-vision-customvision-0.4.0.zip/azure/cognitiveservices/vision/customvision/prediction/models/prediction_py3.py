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


class Prediction(Model):
    """Prediction.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar probability:
    :vartype probability: float
    :ivar tag_id:
    :vartype tag_id: str
    :ivar tag_name:
    :vartype tag_name: str
    :ivar bounding_box:
    :vartype bounding_box:
     ~azure.cognitiveservices.vision.customvision.prediction.models.BoundingBox
    """

    _validation = {
        'probability': {'readonly': True},
        'tag_id': {'readonly': True},
        'tag_name': {'readonly': True},
        'bounding_box': {'readonly': True},
    }

    _attribute_map = {
        'probability': {'key': 'probability', 'type': 'float'},
        'tag_id': {'key': 'tagId', 'type': 'str'},
        'tag_name': {'key': 'tagName', 'type': 'str'},
        'bounding_box': {'key': 'boundingBox', 'type': 'BoundingBox'},
    }

    def __init__(self, **kwargs) -> None:
        super(Prediction, self).__init__(**kwargs)
        self.probability = None
        self.tag_id = None
        self.tag_name = None
        self.bounding_box = None
