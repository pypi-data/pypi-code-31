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


class ImageIdCreateEntry(Model):
    """ImageIdCreateEntry.

    :param id:
    :type id: str
    :param tag_ids:
    :type tag_ids: list[str]
    :param regions:
    :type regions:
     list[~azure.cognitiveservices.vision.customvision.training.models.Region]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'tag_ids': {'key': 'tagIds', 'type': '[str]'},
        'regions': {'key': 'regions', 'type': '[Region]'},
    }

    def __init__(self, *, id: str=None, tag_ids=None, regions=None, **kwargs) -> None:
        super(ImageIdCreateEntry, self).__init__(**kwargs)
        self.id = id
        self.tag_ids = tag_ids
        self.regions = regions
