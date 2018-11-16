# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from . import utilities, tables

class GetDatacenterResult(object):
    """
    A collection of values returned by getDatacenter.
    """
    def __init__(__self__, id=None):
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_datacenter(name=None):
    """
    The `vsphere_datacenter` data source can be used to discover the ID of a
    vSphere datacenter. This can then be used with resources or data sources that
    require a datacenter, such as the [`vsphere_host`][data-source-vsphere-host]
    data source.
    
    [data-source-vsphere-host]: /docs/providers/vsphere/d/host.html
    """
    __args__ = dict()

    __args__['name'] = name
    __ret__ = await pulumi.runtime.invoke('vsphere:index/getDatacenter:getDatacenter', __args__)

    return GetDatacenterResult(
        id=__ret__.get('id'))
