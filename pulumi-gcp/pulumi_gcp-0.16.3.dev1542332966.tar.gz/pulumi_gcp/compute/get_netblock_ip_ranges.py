# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetNetblockIPRangesResult(object):
    """
    A collection of values returned by getNetblockIPRanges.
    """
    def __init__(__self__, cidr_blocks=None, cidr_blocks_ipv4s=None, cidr_blocks_ipv6s=None, id=None):
        if cidr_blocks and not isinstance(cidr_blocks, list):
            raise TypeError('Expected argument cidr_blocks to be a list')
        __self__.cidr_blocks = cidr_blocks
        """
        Retrieve list of all CIDR blocks.
        """
        if cidr_blocks_ipv4s and not isinstance(cidr_blocks_ipv4s, list):
            raise TypeError('Expected argument cidr_blocks_ipv4s to be a list')
        __self__.cidr_blocks_ipv4s = cidr_blocks_ipv4s
        """
        Retrieve list of the IP4 CIDR blocks
        """
        if cidr_blocks_ipv6s and not isinstance(cidr_blocks_ipv6s, list):
            raise TypeError('Expected argument cidr_blocks_ipv6s to be a list')
        __self__.cidr_blocks_ipv6s = cidr_blocks_ipv6s
        """
        Retrieve list of the IP6 CIDR blocks.
        """
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_netblock_ip_ranges():
    """
    Use this data source to get the IP ranges from the sender policy framework (SPF) record of \_cloud-netblocks.googleusercontent
    
    https://cloud.google.com/compute/docs/faq#where_can_i_find_product_name_short_ip_ranges
    """
    __args__ = dict()

    __ret__ = await pulumi.runtime.invoke('gcp:compute/getNetblockIPRanges:getNetblockIPRanges', __args__)

    return GetNetblockIPRangesResult(
        cidr_blocks=__ret__.get('cidrBlocks'),
        cidr_blocks_ipv4s=__ret__.get('cidrBlocksIpv4s'),
        cidr_blocks_ipv6s=__ret__.get('cidrBlocksIpv6s'),
        id=__ret__.get('id'))
