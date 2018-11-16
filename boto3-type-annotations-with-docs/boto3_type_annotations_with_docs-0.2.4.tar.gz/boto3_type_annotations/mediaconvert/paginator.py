from typing import Dict
from botocore.paginate import Paginator


class DescribeEndpoints(Paginator):
    def paginate(self, Mode: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediaconvert-2017-08-29/DescribeEndpoints>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Mode=\'DEFAULT\'|\'GET_ONLY\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Mode: string
        :param Mode: Optional field, defaults to DEFAULT. Specify DEFAULT for this operation to return your endpoints if any exist, or to create an endpoint for you and return it if one doesn\'t already exist. Specify GET_ONLY to return your endpoints if any exist, or an empty list if none exist.
        
        :type PaginationConfig: dict
        :param PaginationConfig: 
        
          A dictionary that provides parameters to control pagination.
        
          - **MaxItems** *(integer) --* 
        
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
        
          - **PageSize** *(integer) --* 
        
            The size of each page.
        
          - **StartingToken** *(string) --* 
        
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Endpoints\': [
                    {
                        \'Url\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Endpoints** *(list) --* List of endpoints
              
              - *(dict) --* Describes an account-specific API endpoint.
                
                - **Url** *(string) --* URL of endpoint
            
        """
        pass


class ListJobTemplates(Paginator):
    def paginate(self, Category: str = None, ListBy: str = None, Order: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediaconvert-2017-08-29/ListJobTemplates>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Category=\'string\',
              ListBy=\'NAME\'|\'CREATION_DATE\'|\'SYSTEM\',
              Order=\'ASCENDING\'|\'DESCENDING\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Category: string
        :param Category: Optionally, specify a job template category to limit responses to only job templates from that category.
        
        :type ListBy: string
        :param ListBy: Optional. When you request a list of job templates, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don\'t specify, the service will list them by name.
        
        :type Order: string
        :param Order: When you request lists of resources, you can optionally specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.
        
        :type PaginationConfig: dict
        :param PaginationConfig: 
        
          A dictionary that provides parameters to control pagination.
        
          - **MaxItems** *(integer) --* 
        
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
        
          - **PageSize** *(integer) --* 
        
            The size of each page.
        
          - **StartingToken** *(string) --* 
        
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'JobTemplates\': [
                    {
                        \'Arn\': \'string\',
                        \'Category\': \'string\',
                        \'CreatedAt\': datetime(2015, 1, 1),
                        \'Description\': \'string\',
                        \'LastUpdated\': datetime(2015, 1, 1),
                        \'Name\': \'string\',
                        \'Queue\': \'string\',
                        \'Settings\': {
                            \'AdAvailOffset\': 123,
                            \'AvailBlanking\': {
                                \'AvailBlankingImage\': \'string\'
                            },
                            \'Inputs\': [
                                {
                                    \'AudioSelectorGroups\': {
                                        \'string\': {
                                            \'AudioSelectorNames\': [
                                                \'string\',
                                            ]
                                        }
                                    },
                                    \'AudioSelectors\': {
                                        \'string\': {
                                            \'CustomLanguageCode\': \'string\',
                                            \'DefaultSelection\': \'DEFAULT\'|\'NOT_DEFAULT\',
                                            \'ExternalAudioFileInput\': \'string\',
                                            \'LanguageCode\': \'ENG\'|\'SPA\'|\'FRA\'|\'DEU\'|\'GER\'|\'ZHO\'|\'ARA\'|\'HIN\'|\'JPN\'|\'RUS\'|\'POR\'|\'ITA\'|\'URD\'|\'VIE\'|\'KOR\'|\'PAN\'|\'ABK\'|\'AAR\'|\'AFR\'|\'AKA\'|\'SQI\'|\'AMH\'|\'ARG\'|\'HYE\'|\'ASM\'|\'AVA\'|\'AVE\'|\'AYM\'|\'AZE\'|\'BAM\'|\'BAK\'|\'EUS\'|\'BEL\'|\'BEN\'|\'BIH\'|\'BIS\'|\'BOS\'|\'BRE\'|\'BUL\'|\'MYA\'|\'CAT\'|\'KHM\'|\'CHA\'|\'CHE\'|\'NYA\'|\'CHU\'|\'CHV\'|\'COR\'|\'COS\'|\'CRE\'|\'HRV\'|\'CES\'|\'DAN\'|\'DIV\'|\'NLD\'|\'DZO\'|\'ENM\'|\'EPO\'|\'EST\'|\'EWE\'|\'FAO\'|\'FIJ\'|\'FIN\'|\'FRM\'|\'FUL\'|\'GLA\'|\'GLG\'|\'LUG\'|\'KAT\'|\'ELL\'|\'GRN\'|\'GUJ\'|\'HAT\'|\'HAU\'|\'HEB\'|\'HER\'|\'HMO\'|\'HUN\'|\'ISL\'|\'IDO\'|\'IBO\'|\'IND\'|\'INA\'|\'ILE\'|\'IKU\'|\'IPK\'|\'GLE\'|\'JAV\'|\'KAL\'|\'KAN\'|\'KAU\'|\'KAS\'|\'KAZ\'|\'KIK\'|\'KIN\'|\'KIR\'|\'KOM\'|\'KON\'|\'KUA\'|\'KUR\'|\'LAO\'|\'LAT\'|\'LAV\'|\'LIM\'|\'LIN\'|\'LIT\'|\'LUB\'|\'LTZ\'|\'MKD\'|\'MLG\'|\'MSA\'|\'MAL\'|\'MLT\'|\'GLV\'|\'MRI\'|\'MAR\'|\'MAH\'|\'MON\'|\'NAU\'|\'NAV\'|\'NDE\'|\'NBL\'|\'NDO\'|\'NEP\'|\'SME\'|\'NOR\'|\'NOB\'|\'NNO\'|\'OCI\'|\'OJI\'|\'ORI\'|\'ORM\'|\'OSS\'|\'PLI\'|\'FAS\'|\'POL\'|\'PUS\'|\'QUE\'|\'QAA\'|\'RON\'|\'ROH\'|\'RUN\'|\'SMO\'|\'SAG\'|\'SAN\'|\'SRD\'|\'SRB\'|\'SNA\'|\'III\'|\'SND\'|\'SIN\'|\'SLK\'|\'SLV\'|\'SOM\'|\'SOT\'|\'SUN\'|\'SWA\'|\'SSW\'|\'SWE\'|\'TGL\'|\'TAH\'|\'TGK\'|\'TAM\'|\'TAT\'|\'TEL\'|\'THA\'|\'BOD\'|\'TIR\'|\'TON\'|\'TSO\'|\'TSN\'|\'TUR\'|\'TUK\'|\'TWI\'|\'UIG\'|\'UKR\'|\'UZB\'|\'VEN\'|\'VOL\'|\'WLN\'|\'CYM\'|\'FRY\'|\'WOL\'|\'XHO\'|\'YID\'|\'YOR\'|\'ZHA\'|\'ZUL\'|\'ORJ\'|\'QPC\'|\'TNG\',
                                            \'Offset\': 123,
                                            \'Pids\': [
                                                123,
                                            ],
                                            \'ProgramSelection\': 123,
                                            \'RemixSettings\': {
                                                \'ChannelMapping\': {
                                                    \'OutputChannels\': [
                                                        {
                                                            \'InputChannels\': [
                                                                123,
                                                            ]
                                                        },
                                                    ]
                                                },
                                                \'ChannelsIn\': 123,
                                                \'ChannelsOut\': 123
                                            },
                                            \'SelectorType\': \'PID\'|\'TRACK\'|\'LANGUAGE_CODE\',
                                            \'Tracks\': [
                                                123,
                                            ]
                                        }
                                    },
                                    \'CaptionSelectors\': {
                                        \'string\': {
                                            \'CustomLanguageCode\': \'string\',
                                            \'LanguageCode\': \'ENG\'|\'SPA\'|\'FRA\'|\'DEU\'|\'GER\'|\'ZHO\'|\'ARA\'|\'HIN\'|\'JPN\'|\'RUS\'|\'POR\'|\'ITA\'|\'URD\'|\'VIE\'|\'KOR\'|\'PAN\'|\'ABK\'|\'AAR\'|\'AFR\'|\'AKA\'|\'SQI\'|\'AMH\'|\'ARG\'|\'HYE\'|\'ASM\'|\'AVA\'|\'AVE\'|\'AYM\'|\'AZE\'|\'BAM\'|\'BAK\'|\'EUS\'|\'BEL\'|\'BEN\'|\'BIH\'|\'BIS\'|\'BOS\'|\'BRE\'|\'BUL\'|\'MYA\'|\'CAT\'|\'KHM\'|\'CHA\'|\'CHE\'|\'NYA\'|\'CHU\'|\'CHV\'|\'COR\'|\'COS\'|\'CRE\'|\'HRV\'|\'CES\'|\'DAN\'|\'DIV\'|\'NLD\'|\'DZO\'|\'ENM\'|\'EPO\'|\'EST\'|\'EWE\'|\'FAO\'|\'FIJ\'|\'FIN\'|\'FRM\'|\'FUL\'|\'GLA\'|\'GLG\'|\'LUG\'|\'KAT\'|\'ELL\'|\'GRN\'|\'GUJ\'|\'HAT\'|\'HAU\'|\'HEB\'|\'HER\'|\'HMO\'|\'HUN\'|\'ISL\'|\'IDO\'|\'IBO\'|\'IND\'|\'INA\'|\'ILE\'|\'IKU\'|\'IPK\'|\'GLE\'|\'JAV\'|\'KAL\'|\'KAN\'|\'KAU\'|\'KAS\'|\'KAZ\'|\'KIK\'|\'KIN\'|\'KIR\'|\'KOM\'|\'KON\'|\'KUA\'|\'KUR\'|\'LAO\'|\'LAT\'|\'LAV\'|\'LIM\'|\'LIN\'|\'LIT\'|\'LUB\'|\'LTZ\'|\'MKD\'|\'MLG\'|\'MSA\'|\'MAL\'|\'MLT\'|\'GLV\'|\'MRI\'|\'MAR\'|\'MAH\'|\'MON\'|\'NAU\'|\'NAV\'|\'NDE\'|\'NBL\'|\'NDO\'|\'NEP\'|\'SME\'|\'NOR\'|\'NOB\'|\'NNO\'|\'OCI\'|\'OJI\'|\'ORI\'|\'ORM\'|\'OSS\'|\'PLI\'|\'FAS\'|\'POL\'|\'PUS\'|\'QUE\'|\'QAA\'|\'RON\'|\'ROH\'|\'RUN\'|\'SMO\'|\'SAG\'|\'SAN\'|\'SRD\'|\'SRB\'|\'SNA\'|\'III\'|\'SND\'|\'SIN\'|\'SLK\'|\'SLV\'|\'SOM\'|\'SOT\'|\'SUN\'|\'SWA\'|\'SSW\'|\'SWE\'|\'TGL\'|\'TAH\'|\'TGK\'|\'TAM\'|\'TAT\'|\'TEL\'|\'THA\'|\'BOD\'|\'TIR\'|\'TON\'|\'TSO\'|\'TSN\'|\'TUR\'|\'TUK\'|\'TWI\'|\'UIG\'|\'UKR\'|\'UZB\'|\'VEN\'|\'VOL\'|\'WLN\'|\'CYM\'|\'FRY\'|\'WOL\'|\'XHO\'|\'YID\'|\'YOR\'|\'ZHA\'|\'ZUL\'|\'ORJ\'|\'QPC\'|\'TNG\',
                                            \'SourceSettings\': {
                                                \'AncillarySourceSettings\': {
                                                    \'SourceAncillaryChannelNumber\': 123
                                                },
                                                \'DvbSubSourceSettings\': {
                                                    \'Pid\': 123
                                                },
                                                \'EmbeddedSourceSettings\': {
                                                    \'Convert608To708\': \'UPCONVERT\'|\'DISABLED\',
                                                    \'Source608ChannelNumber\': 123,
                                                    \'Source608TrackNumber\': 123
                                                },
                                                \'FileSourceSettings\': {
                                                    \'Convert608To708\': \'UPCONVERT\'|\'DISABLED\',
                                                    \'SourceFile\': \'string\',
                                                    \'TimeDelta\': 123
                                                },
                                                \'SourceType\': \'ANCILLARY\'|\'DVB_SUB\'|\'EMBEDDED\'|\'SCC\'|\'TTML\'|\'STL\'|\'SRT\'|\'TELETEXT\'|\'NULL_SOURCE\',
                                                \'TeletextSourceSettings\': {
                                                    \'PageNumber\': \'string\'
                                                }
                                            }
                                        }
                                    },
                                    \'DeblockFilter\': \'ENABLED\'|\'DISABLED\',
                                    \'DenoiseFilter\': \'ENABLED\'|\'DISABLED\',
                                    \'FilterEnable\': \'AUTO\'|\'DISABLE\'|\'FORCE\',
                                    \'FilterStrength\': 123,
                                    \'InputClippings\': [
                                        {
                                            \'EndTimecode\': \'string\',
                                            \'StartTimecode\': \'string\'
                                        },
                                    ],
                                    \'ProgramNumber\': 123,
                                    \'PsiControl\': \'IGNORE_PSI\'|\'USE_PSI\',
                                    \'TimecodeSource\': \'EMBEDDED\'|\'ZEROBASED\'|\'SPECIFIEDSTART\',
                                    \'VideoSelector\': {
                                        \'ColorSpace\': \'FOLLOW\'|\'REC_601\'|\'REC_709\'|\'HDR10\'|\'HLG_2020\',
                                        \'ColorSpaceUsage\': \'FORCE\'|\'FALLBACK\',
                                        \'Hdr10Metadata\': {
                                            \'BluePrimaryX\': 123,
                                            \'BluePrimaryY\': 123,
                                            \'GreenPrimaryX\': 123,
                                            \'GreenPrimaryY\': 123,
                                            \'MaxContentLightLevel\': 123,
                                            \'MaxFrameAverageLightLevel\': 123,
                                            \'MaxLuminance\': 123,
                                            \'MinLuminance\': 123,
                                            \'RedPrimaryX\': 123,
                                            \'RedPrimaryY\': 123,
                                            \'WhitePointX\': 123,
                                            \'WhitePointY\': 123
                                        },
                                        \'Pid\': 123,
                                        \'ProgramNumber\': 123
                                    }
                                },
                            ],
                            \'NielsenConfiguration\': {
                                \'BreakoutCode\': 123,
                                \'DistributorId\': \'string\'
                            },
                            \'OutputGroups\': [
                                {
                                    \'CustomName\': \'string\',
                                    \'Name\': \'string\',
                                    \'OutputGroupSettings\': {
                                        \'CmafGroupSettings\': {
                                            \'BaseUrl\': \'string\',
                                            \'ClientCache\': \'DISABLED\'|\'ENABLED\',
                                            \'CodecSpecification\': \'RFC_6381\'|\'RFC_4281\',
                                            \'Destination\': \'string\',
                                            \'Encryption\': {
                                                \'ConstantInitializationVector\': \'string\',
                                                \'EncryptionMethod\': \'SAMPLE_AES\',
                                                \'InitializationVectorInManifest\': \'INCLUDE\'|\'EXCLUDE\',
                                                \'StaticKeyProvider\': {
                                                    \'KeyFormat\': \'string\',
                                                    \'KeyFormatVersions\': \'string\',
                                                    \'StaticKeyValue\': \'string\',
                                                    \'Url\': \'string\'
                                                },
                                                \'Type\': \'STATIC_KEY\'
                                            },
                                            \'FragmentLength\': 123,
                                            \'ManifestCompression\': \'GZIP\'|\'NONE\',
                                            \'ManifestDurationFormat\': \'FLOATING_POINT\'|\'INTEGER\',
                                            \'MinBufferTime\': 123,
                                            \'MinFinalSegmentLength\': 123.0,
                                            \'SegmentControl\': \'SINGLE_FILE\'|\'SEGMENTED_FILES\',
                                            \'SegmentLength\': 123,
                                            \'StreamInfResolution\': \'INCLUDE\'|\'EXCLUDE\',
                                            \'WriteDashManifest\': \'DISABLED\'|\'ENABLED\',
                                            \'WriteHlsManifest\': \'DISABLED\'|\'ENABLED\'
                                        },
                                        \'DashIsoGroupSettings\': {
                                            \'BaseUrl\': \'string\',
                                            \'Destination\': \'string\',
                                            \'Encryption\': {
                                                \'SpekeKeyProvider\': {
                                                    \'ResourceId\': \'string\',
                                                    \'SystemIds\': [
                                                        \'string\',
                                                    ],
                                                    \'Url\': \'string\'
                                                }
                                            },
                                            \'FragmentLength\': 123,
                                            \'HbbtvCompliance\': \'HBBTV_1_5\'|\'NONE\',
                                            \'MinBufferTime\': 123,
                                            \'SegmentControl\': \'SINGLE_FILE\'|\'SEGMENTED_FILES\',
                                            \'SegmentLength\': 123,
                                            \'WriteSegmentTimelineInRepresentation\': \'ENABLED\'|\'DISABLED\'
                                        },
                                        \'FileGroupSettings\': {
                                            \'Destination\': \'string\'
                                        },
                                        \'HlsGroupSettings\': {
                                            \'AdMarkers\': [
                                                \'ELEMENTAL\'|\'ELEMENTAL_SCTE35\',
                                            ],
                                            \'BaseUrl\': \'string\',
                                            \'CaptionLanguageMappings\': [
                                                {
                                                    \'CaptionChannel\': 123,
                                                    \'CustomLanguageCode\': \'string\',
                                                    \'LanguageCode\': \'ENG\'|\'SPA\'|\'FRA\'|\'DEU\'|\'GER\'|\'ZHO\'|\'ARA\'|\'HIN\'|\'JPN\'|\'RUS\'|\'POR\'|\'ITA\'|\'URD\'|\'VIE\'|\'KOR\'|\'PAN\'|\'ABK\'|\'AAR\'|\'AFR\'|\'AKA\'|\'SQI\'|\'AMH\'|\'ARG\'|\'HYE\'|\'ASM\'|\'AVA\'|\'AVE\'|\'AYM\'|\'AZE\'|\'BAM\'|\'BAK\'|\'EUS\'|\'BEL\'|\'BEN\'|\'BIH\'|\'BIS\'|\'BOS\'|\'BRE\'|\'BUL\'|\'MYA\'|\'CAT\'|\'KHM\'|\'CHA\'|\'CHE\'|\'NYA\'|\'CHU\'|\'CHV\'|\'COR\'|\'COS\'|\'CRE\'|\'HRV\'|\'CES\'|\'DAN\'|\'DIV\'|\'NLD\'|\'DZO\'|\'ENM\'|\'EPO\'|\'EST\'|\'EWE\'|\'FAO\'|\'FIJ\'|\'FIN\'|\'FRM\'|\'FUL\'|\'GLA\'|\'GLG\'|\'LUG\'|\'KAT\'|\'ELL\'|\'GRN\'|\'GUJ\'|\'HAT\'|\'HAU\'|\'HEB\'|\'HER\'|\'HMO\'|\'HUN\'|\'ISL\'|\'IDO\'|\'IBO\'|\'IND\'|\'INA\'|\'ILE\'|\'IKU\'|\'IPK\'|\'GLE\'|\'JAV\'|\'KAL\'|\'KAN\'|\'KAU\'|\'KAS\'|\'KAZ\'|\'KIK\'|\'KIN\'|\'KIR\'|\'KOM\'|\'KON\'|\'KUA\'|\'KUR\'|\'LAO\'|\'LAT\'|\'LAV\'|\'LIM\'|\'LIN\'|\'LIT\'|\'LUB\'|\'LTZ\'|\'MKD\'|\'MLG\'|\'MSA\'|\'MAL\'|\'MLT\'|\'GLV\'|\'MRI\'|\'MAR\'|\'MAH\'|\'MON\'|\'NAU\'|\'NAV\'|\'NDE\'|\'NBL\'|\'NDO\'|\'NEP\'|\'SME\'|\'NOR\'|\'NOB\'|\'NNO\'|\'OCI\'|\'OJI\'|\'ORI\'|\'ORM\'|\'OSS\'|\'PLI\'|\'FAS\'|\'POL\'|\'PUS\'|\'QUE\'|\'QAA\'|\'RON\'|\'ROH\'|\'RUN\'|\'SMO\'|\'SAG\'|\'SAN\'|\'SRD\'|\'SRB\'|\'SNA\'|\'III\'|\'SND\'|\'SIN\'|\'SLK\'|\'SLV\'|\'SOM\'|\'SOT\'|\'SUN\'|\'SWA\'|\'SSW\'|\'SWE\'|\'TGL\'|\'TAH\'|\'TGK\'|\'TAM\'|\'TAT\'|\'TEL\'|\'THA\'|\'BOD\'|\'TIR\'|\'TON\'|\'TSO\'|\'TSN\'|\'TUR\'|\'TUK\'|\'TWI\'|\'UIG\'|\'UKR\'|\'UZB\'|\'VEN\'|\'VOL\'|\'WLN\'|\'CYM\'|\'FRY\'|\'WOL\'|\'XHO\'|\'YID\'|\'YOR\'|\'ZHA\'|\'ZUL\'|\'ORJ\'|\'QPC\'|\'TNG\',
                                                    \'LanguageDescription\': \'string\'
                                                },
                                            ],
                                            \'CaptionLanguageSetting\': \'INSERT\'|\'OMIT\'|\'NONE\',
                                            \'ClientCache\': \'DISABLED\'|\'ENABLED\',
                                            \'CodecSpecification\': \'RFC_6381\'|\'RFC_4281\',
                                            \'Destination\': \'string\',
                                            \'DirectoryStructure\': \'SINGLE_DIRECTORY\'|\'SUBDIRECTORY_PER_STREAM\',
                                            \'Encryption\': {
                                                \'ConstantInitializationVector\': \'string\',
                                                \'EncryptionMethod\': \'AES128\'|\'SAMPLE_AES\',
                                                \'InitializationVectorInManifest\': \'INCLUDE\'|\'EXCLUDE\',
                                                \'SpekeKeyProvider\': {
                                                    \'ResourceId\': \'string\',
                                                    \'SystemIds\': [
                                                        \'string\',
                                                    ],
                                                    \'Url\': \'string\'
                                                },
                                                \'StaticKeyProvider\': {
                                                    \'KeyFormat\': \'string\',
                                                    \'KeyFormatVersions\': \'string\',
                                                    \'StaticKeyValue\': \'string\',
                                                    \'Url\': \'string\'
                                                },
                                                \'Type\': \'SPEKE\'|\'STATIC_KEY\'
                                            },
                                            \'ManifestCompression\': \'GZIP\'|\'NONE\',
                                            \'ManifestDurationFormat\': \'FLOATING_POINT\'|\'INTEGER\',
                                            \'MinFinalSegmentLength\': 123.0,
                                            \'MinSegmentLength\': 123,
                                            \'OutputSelection\': \'MANIFESTS_AND_SEGMENTS\'|\'SEGMENTS_ONLY\',
                                            \'ProgramDateTime\': \'INCLUDE\'|\'EXCLUDE\',
                                            \'ProgramDateTimePeriod\': 123,
                                            \'SegmentControl\': \'SINGLE_FILE\'|\'SEGMENTED_FILES\',
                                            \'SegmentLength\': 123,
                                            \'SegmentsPerSubdirectory\': 123,
                                            \'StreamInfResolution\': \'INCLUDE\'|\'EXCLUDE\',
                                            \'TimedMetadataId3Frame\': \'NONE\'|\'PRIV\'|\'TDRL\',
                                            \'TimedMetadataId3Period\': 123,
                                            \'TimestampDeltaMilliseconds\': 123
                                        },
                                        \'MsSmoothGroupSettings\': {
                                            \'AudioDeduplication\': \'COMBINE_DUPLICATE_STREAMS\'|\'NONE\',
                                            \'Destination\': \'string\',
                                            \'Encryption\': {
                                                \'SpekeKeyProvider\': {
                                                    \'ResourceId\': \'string\',
                                                    \'SystemIds\': [
                                                        \'string\',
                                                    ],
                                                    \'Url\': \'string\'
                                                }
                                            },
                                            \'FragmentLength\': 123,
                                            \'ManifestEncoding\': \'UTF8\'|\'UTF16\'
                                        },
                                        \'Type\': \'HLS_GROUP_SETTINGS\'|\'DASH_ISO_GROUP_SETTINGS\'|\'FILE_GROUP_SETTINGS\'|\'MS_SMOOTH_GROUP_SETTINGS\'|\'CMAF_GROUP_SETTINGS\'
                                    },
                                    \'Outputs\': [
                                        {
                                            \'AudioDescriptions\': [
                                                {
                                                    \'AudioNormalizationSettings\': {
                                                        \'Algorithm\': \'ITU_BS_1770_1\'|\'ITU_BS_1770_2\',
                                                        \'AlgorithmControl\': \'CORRECT_AUDIO\'|\'MEASURE_ONLY\',
                                                        \'CorrectionGateLevel\': 123,
                                                        \'LoudnessLogging\': \'LOG\'|\'DONT_LOG\',
                                                        \'PeakCalculation\': \'TRUE_PEAK\'|\'NONE\',
                                                        \'TargetLkfs\': 123.0
                                                    },
                                                    \'AudioSourceName\': \'string\',
                                                    \'AudioType\': 123,
                                                    \'AudioTypeControl\': \'FOLLOW_INPUT\'|\'USE_CONFIGURED\',
                                                    \'CodecSettings\': {
                                                        \'AacSettings\': {
                                                            \'AudioDescriptionBroadcasterMix\': \'BROADCASTER_MIXED_AD\'|\'NORMAL\',
                                                            \'Bitrate\': 123,
                                                            \'CodecProfile\': \'LC\'|\'HEV1\'|\'HEV2\',
                                                            \'CodingMode\': \'AD_RECEIVER_MIX\'|\'CODING_MODE_1_0\'|\'CODING_MODE_1_1\'|\'CODING_MODE_2_0\'|\'CODING_MODE_5_1\',
                                                            \'RateControlMode\': \'CBR\'|\'VBR\',
                                                            \'RawFormat\': \'LATM_LOAS\'|\'NONE\',
                                                            \'SampleRate\': 123,
                                                            \'Specification\': \'MPEG2\'|\'MPEG4\',
                                                            \'VbrQuality\': \'LOW\'|\'MEDIUM_LOW\'|\'MEDIUM_HIGH\'|\'HIGH\'
                                                        },
                                                        \'Ac3Settings\': {
                                                            \'Bitrate\': 123,
                                                            \'BitstreamMode\': \'COMPLETE_MAIN\'|\'COMMENTARY\'|\'DIALOGUE\'|\'EMERGENCY\'|\'HEARING_IMPAIRED\'|\'MUSIC_AND_EFFECTS\'|\'VISUALLY_IMPAIRED\'|\'VOICE_OVER\',
                                                            \'CodingMode\': \'CODING_MODE_1_0\'|\'CODING_MODE_1_1\'|\'CODING_MODE_2_0\'|\'CODING_MODE_3_2_LFE\',
                                                            \'Dialnorm\': 123,
                                                            \'DynamicRangeCompressionProfile\': \'FILM_STANDARD\'|\'NONE\',
                                                            \'LfeFilter\': \'ENABLED\'|\'DISABLED\',
                                                            \'MetadataControl\': \'FOLLOW_INPUT\'|\'USE_CONFIGURED\',
                                                            \'SampleRate\': 123
                                                        },
                                                        \'AiffSettings\': {
                                                            \'BitDepth\': 123,
                                                            \'Channels\': 123,
                                                            \'SampleRate\': 123
                                                        },
                                                        \'Codec\': \'AAC\'|\'MP2\'|\'WAV\'|\'AIFF\'|\'AC3\'|\'EAC3\'|\'PASSTHROUGH\',
                                                        \'Eac3Settings\': {
                                                            \'AttenuationControl\': \'ATTENUATE_3_DB\'|\'NONE\',
                                                            \'Bitrate\': 123,
                                                            \'BitstreamMode\': \'COMPLETE_MAIN\'|\'COMMENTARY\'|\'EMERGENCY\'|\'HEARING_IMPAIRED\'|\'VISUALLY_IMPAIRED\',
                                                            \'CodingMode\': \'CODING_MODE_1_0\'|\'CODING_MODE_2_0\'|\'CODING_MODE_3_2\',
                                                            \'DcFilter\': \'ENABLED\'|\'DISABLED\',
                                                            \'Dialnorm\': 123,
                                                            \'DynamicRangeCompressionLine\': \'NONE\'|\'FILM_STANDARD\'|\'FILM_LIGHT\'|\'MUSIC_STANDARD\'|\'MUSIC_LIGHT\'|\'SPEECH\',
                                                            \'DynamicRangeCompressionRf\': \'NONE\'|\'FILM_STANDARD\'|\'FILM_LIGHT\'|\'MUSIC_STANDARD\'|\'MUSIC_LIGHT\'|\'SPEECH\',
                                                            \'LfeControl\': \'LFE\'|\'NO_LFE\',
                                                            \'LfeFilter\': \'ENABLED\'|\'DISABLED\',
                                                            \'LoRoCenterMixLevel\': 123.0,
                                                            \'LoRoSurroundMixLevel\': 123.0,
                                                            \'LtRtCenterMixLevel\': 123.0,
                                                            \'LtRtSurroundMixLevel\': 123.0,
                                                            \'MetadataControl\': \'FOLLOW_INPUT\'|\'USE_CONFIGURED\',
                                                            \'PassthroughControl\': \'WHEN_POSSIBLE\'|\'NO_PASSTHROUGH\',
                                                            \'PhaseControl\': \'SHIFT_90_DEGREES\'|\'NO_SHIFT\',
                                                            \'SampleRate\': 123,
                                                            \'StereoDownmix\': \'NOT_INDICATED\'|\'LO_RO\'|\'LT_RT\'|\'DPL2\',
                                                            \'SurroundExMode\': \'NOT_INDICATED\'|\'ENABLED\'|\'DISABLED\',
                                                            \'SurroundMode\': \'NOT_INDICATED\'|\'ENABLED\'|\'DISABLED\'
                                                        },
                                                        \'Mp2Settings\': {
                                                            \'Bitrate\': 123,
                                                            \'Channels\': 123,
                                                            \'SampleRate\': 123
                                                        },
                                                        \'WavSettings\': {
                                                            \'BitDepth\': 123,
                                                            \'Channels\': 123,
                                                            \'Format\': \'RIFF\'|\'RF64\',
                                                            \'SampleRate\': 123
                                                        }
                                                    },
                                                    \'CustomLanguageCode\': \'string\',
                                                    \'LanguageCode\': \'ENG\'|\'SPA\'|\'FRA\'|\'DEU\'|\'GER\'|\'ZHO\'|\'ARA\'|\'HIN\'|\'JPN\'|\'RUS\'|\'POR\'|\'ITA\'|\'URD\'|\'VIE\'|\'KOR\'|\'PAN\'|\'ABK\'|\'AAR\'|\'AFR\'|\'AKA\'|\'SQI\'|\'AMH\'|\'ARG\'|\'HYE\'|\'ASM\'|\'AVA\'|\'AVE\'|\'AYM\'|\'AZE\'|\'BAM\'|\'BAK\'|\'EUS\'|\'BEL\'|\'BEN\'|\'BIH\'|\'BIS\'|\'BOS\'|\'BRE\'|\'BUL\'|\'MYA\'|\'CAT\'|\'KHM\'|\'CHA\'|\'CHE\'|\'NYA\'|\'CHU\'|\'CHV\'|\'COR\'|\'COS\'|\'CRE\'|\'HRV\'|\'CES\'|\'DAN\'|\'DIV\'|\'NLD\'|\'DZO\'|\'ENM\'|\'EPO\'|\'EST\'|\'EWE\'|\'FAO\'|\'FIJ\'|\'FIN\'|\'FRM\'|\'FUL\'|\'GLA\'|\'GLG\'|\'LUG\'|\'KAT\'|\'ELL\'|\'GRN\'|\'GUJ\'|\'HAT\'|\'HAU\'|\'HEB\'|\'HER\'|\'HMO\'|\'HUN\'|\'ISL\'|\'IDO\'|\'IBO\'|\'IND\'|\'INA\'|\'ILE\'|\'IKU\'|\'IPK\'|\'GLE\'|\'JAV\'|\'KAL\'|\'KAN\'|\'KAU\'|\'KAS\'|\'KAZ\'|\'KIK\'|\'KIN\'|\'KIR\'|\'KOM\'|\'KON\'|\'KUA\'|\'KUR\'|\'LAO\'|\'LAT\'|\'LAV\'|\'LIM\'|\'LIN\'|\'LIT\'|\'LUB\'|\'LTZ\'|\'MKD\'|\'MLG\'|\'MSA\'|\'MAL\'|\'MLT\'|\'GLV\'|\'MRI\'|\'MAR\'|\'MAH\'|\'MON\'|\'NAU\'|\'NAV\'|\'NDE\'|\'NBL\'|\'NDO\'|\'NEP\'|\'SME\'|\'NOR\'|\'NOB\'|\'NNO\'|\'OCI\'|\'OJI\'|\'ORI\'|\'ORM\'|\'OSS\'|\'PLI\'|\'FAS\'|\'POL\'|\'PUS\'|\'QUE\'|\'QAA\'|\'RON\'|\'ROH\'|\'RUN\'|\'SMO\'|\'SAG\'|\'SAN\'|\'SRD\'|\'SRB\'|\'SNA\'|\'III\'|\'SND\'|\'SIN\'|\'SLK\'|\'SLV\'|\'SOM\'|\'SOT\'|\'SUN\'|\'SWA\'|\'SSW\'|\'SWE\'|\'TGL\'|\'TAH\'|\'TGK\'|\'TAM\'|\'TAT\'|\'TEL\'|\'THA\'|\'BOD\'|\'TIR\'|\'TON\'|\'TSO\'|\'TSN\'|\'TUR\'|\'TUK\'|\'TWI\'|\'UIG\'|\'UKR\'|\'UZB\'|\'VEN\'|\'VOL\'|\'WLN\'|\'CYM\'|\'FRY\'|\'WOL\'|\'XHO\'|\'YID\'|\'YOR\'|\'ZHA\'|\'ZUL\'|\'ORJ\'|\'QPC\'|\'TNG\',
                                                    \'LanguageCodeControl\': \'FOLLOW_INPUT\'|\'USE_CONFIGURED\',
                                                    \'RemixSettings\': {
                                                        \'ChannelMapping\': {
                                                            \'OutputChannels\': [
                                                                {
                                                                    \'InputChannels\': [
                                                                        123,
                                                                    ]
                                                                },
                                                            ]
                                                        },
                                                        \'ChannelsIn\': 123,
                                                        \'ChannelsOut\': 123
                                                    },
                                                    \'StreamName\': \'string\'
                                                },
                                            ],
                                            \'CaptionDescriptions\': [
                                                {
                                                    \'CaptionSelectorName\': \'string\',
                                                    \'CustomLanguageCode\': \'string\',
                                                    \'DestinationSettings\': {
                                                        \'BurninDestinationSettings\': {
                                                            \'Alignment\': \'CENTERED\'|\'LEFT\',
                                                            \'BackgroundColor\': \'NONE\'|\'BLACK\'|\'WHITE\',
                                                            \'BackgroundOpacity\': 123,
                                                            \'FontColor\': \'WHITE\'|\'BLACK\'|\'YELLOW\'|\'RED\'|\'GREEN\'|\'BLUE\',
                                                            \'FontOpacity\': 123,
                                                            \'FontResolution\': 123,
                                                            \'FontSize\': 123,
                                                            \'OutlineColor\': \'BLACK\'|\'WHITE\'|\'YELLOW\'|\'RED\'|\'GREEN\'|\'BLUE\',
                                                            \'OutlineSize\': 123,
                                                            \'ShadowColor\': \'NONE\'|\'BLACK\'|\'WHITE\',
                                                            \'ShadowOpacity\': 123,
                                                            \'ShadowXOffset\': 123,
                                                            \'ShadowYOffset\': 123,
                                                            \'TeletextSpacing\': \'FIXED_GRID\'|\'PROPORTIONAL\',
                                                            \'XPosition\': 123,
                                                            \'YPosition\': 123
                                                        },
                                                        \'DestinationType\': \'BURN_IN\'|\'DVB_SUB\'|\'EMBEDDED\'|\'SCC\'|\'SRT\'|\'TELETEXT\'|\'TTML\'|\'WEBVTT\',
                                                        \'DvbSubDestinationSettings\': {
                                                            \'Alignment\': \'CENTERED\'|\'LEFT\',
                                                            \'BackgroundColor\': \'NONE\'|\'BLACK\'|\'WHITE\',
                                                            \'BackgroundOpacity\': 123,
                                                            \'FontColor\': \'WHITE\'|\'BLACK\'|\'YELLOW\'|\'RED\'|\'GREEN\'|\'BLUE\',
                                                            \'FontOpacity\': 123,
                                                            \'FontResolution\': 123,
                                                            \'FontSize\': 123,
                                                            \'OutlineColor\': \'BLACK\'|\'WHITE\'|\'YELLOW\'|\'RED\'|\'GREEN\'|\'BLUE\',
                                                            \'OutlineSize\': 123,
                                                            \'ShadowColor\': \'NONE\'|\'BLACK\'|\'WHITE\',
                                                            \'ShadowOpacity\': 123,
                                                            \'ShadowXOffset\': 123,
                                                            \'ShadowYOffset\': 123,
                                                            \'TeletextSpacing\': \'FIXED_GRID\'|\'PROPORTIONAL\',
                                                            \'XPosition\': 123,
                                                            \'YPosition\': 123
                                                        },
                                                        \'SccDestinationSettings\': {
                                                            \'Framerate\': \'FRAMERATE_23_97\'|\'FRAMERATE_24\'|\'FRAMERATE_29_97_DROPFRAME\'|\'FRAMERATE_29_97_NON_DROPFRAME\'
                                                        },
                                                        \'TeletextDestinationSettings\': {
                                                            \'PageNumber\': \'string\'
                                                        },
                                                        \'TtmlDestinationSettings\': {
                                                            \'StylePassthrough\': \'ENABLED\'|\'DISABLED\'
                                                        }
                                                    },
                                                    \'LanguageCode\': \'ENG\'|\'SPA\'|\'FRA\'|\'DEU\'|\'GER\'|\'ZHO\'|\'ARA\'|\'HIN\'|\'JPN\'|\'RUS\'|\'POR\'|\'ITA\'|\'URD\'|\'VIE\'|\'KOR\'|\'PAN\'|\'ABK\'|\'AAR\'|\'AFR\'|\'AKA\'|\'SQI\'|\'AMH\'|\'ARG\'|\'HYE\'|\'ASM\'|\'AVA\'|\'AVE\'|\'AYM\'|\'AZE\'|\'BAM\'|\'BAK\'|\'EUS\'|\'BEL\'|\'BEN\'|\'BIH\'|\'BIS\'|\'BOS\'|\'BRE\'|\'BUL\'|\'MYA\'|\'CAT\'|\'KHM\'|\'CHA\'|\'CHE\'|\'NYA\'|\'CHU\'|\'CHV\'|\'COR\'|\'COS\'|\'CRE\'|\'HRV\'|\'CES\'|\'DAN\'|\'DIV\'|\'NLD\'|\'DZO\'|\'ENM\'|\'EPO\'|\'EST\'|\'EWE\'|\'FAO\'|\'FIJ\'|\'FIN\'|\'FRM\'|\'FUL\'|\'GLA\'|\'GLG\'|\'LUG\'|\'KAT\'|\'ELL\'|\'GRN\'|\'GUJ\'|\'HAT\'|\'HAU\'|\'HEB\'|\'HER\'|\'HMO\'|\'HUN\'|\'ISL\'|\'IDO\'|\'IBO\'|\'IND\'|\'INA\'|\'ILE\'|\'IKU\'|\'IPK\'|\'GLE\'|\'JAV\'|\'KAL\'|\'KAN\'|\'KAU\'|\'KAS\'|\'KAZ\'|\'KIK\'|\'KIN\'|\'KIR\'|\'KOM\'|\'KON\'|\'KUA\'|\'KUR\'|\'LAO\'|\'LAT\'|\'LAV\'|\'LIM\'|\'LIN\'|\'LIT\'|\'LUB\'|\'LTZ\'|\'MKD\'|\'MLG\'|\'MSA\'|\'MAL\'|\'MLT\'|\'GLV\'|\'MRI\'|\'MAR\'|\'MAH\'|\'MON\'|\'NAU\'|\'NAV\'|\'NDE\'|\'NBL\'|\'NDO\'|\'NEP\'|\'SME\'|\'NOR\'|\'NOB\'|\'NNO\'|\'OCI\'|\'OJI\'|\'ORI\'|\'ORM\'|\'OSS\'|\'PLI\'|\'FAS\'|\'POL\'|\'PUS\'|\'QUE\'|\'QAA\'|\'RON\'|\'ROH\'|\'RUN\'|\'SMO\'|\'SAG\'|\'SAN\'|\'SRD\'|\'SRB\'|\'SNA\'|\'III\'|\'SND\'|\'SIN\'|\'SLK\'|\'SLV\'|\'SOM\'|\'SOT\'|\'SUN\'|\'SWA\'|\'SSW\'|\'SWE\'|\'TGL\'|\'TAH\'|\'TGK\'|\'TAM\'|\'TAT\'|\'TEL\'|\'THA\'|\'BOD\'|\'TIR\'|\'TON\'|\'TSO\'|\'TSN\'|\'TUR\'|\'TUK\'|\'TWI\'|\'UIG\'|\'UKR\'|\'UZB\'|\'VEN\'|\'VOL\'|\'WLN\'|\'CYM\'|\'FRY\'|\'WOL\'|\'XHO\'|\'YID\'|\'YOR\'|\'ZHA\'|\'ZUL\'|\'ORJ\'|\'QPC\'|\'TNG\',
                                                    \'LanguageDescription\': \'string\'
                                                },
                                            ],
                                            \'ContainerSettings\': {
                                                \'Container\': \'F4V\'|\'ISMV\'|\'M2TS\'|\'M3U8\'|\'CMFC\'|\'MOV\'|\'MP4\'|\'MPD\'|\'MXF\'|\'RAW\',
                                                \'F4vSettings\': {
                                                    \'MoovPlacement\': \'PROGRESSIVE_DOWNLOAD\'|\'NORMAL\'
                                                },
                                                \'M2tsSettings\': {
                                                    \'AudioBufferModel\': \'DVB\'|\'ATSC\',
                                                    \'AudioFramesPerPes\': 123,
                                                    \'AudioPids\': [
                                                        123,
                                                    ],
                                                    \'Bitrate\': 123,
                                                    \'BufferModel\': \'MULTIPLEX\'|\'NONE\',
                                                    \'DvbNitSettings\': {
                                                        \'NetworkId\': 123,
                                                        \'NetworkName\': \'string\',
                                                        \'NitInterval\': 123
                                                    },
                                                    \'DvbSdtSettings\': {
                                                        \'OutputSdt\': \'SDT_FOLLOW\'|\'SDT_FOLLOW_IF_PRESENT\'|\'SDT_MANUAL\'|\'SDT_NONE\',
                                                        \'SdtInterval\': 123,
                                                        \'ServiceName\': \'string\',
                                                        \'ServiceProviderName\': \'string\'
                                                    },
                                                    \'DvbSubPids\': [
                                                        123,
                                                    ],
                                                    \'DvbTdtSettings\': {
                                                        \'TdtInterval\': 123
                                                    },
                                                    \'DvbTeletextPid\': 123,
                                                    \'EbpAudioInterval\': \'VIDEO_AND_FIXED_INTERVALS\'|\'VIDEO_INTERVAL\',
                                                    \'EbpPlacement\': \'VIDEO_AND_AUDIO_PIDS\'|\'VIDEO_PID\',
                                                    \'EsRateInPes\': \'INCLUDE\'|\'EXCLUDE\',
                                                    \'FragmentTime\': 123.0,
                                                    \'MaxPcrInterval\': 123,
                                                    \'MinEbpInterval\': 123,
                                                    \'NielsenId3\': \'INSERT\'|\'NONE\',
                                                    \'NullPacketBitrate\': 123.0,
                                                    \'PatInterval\': 123,
                                                    \'PcrControl\': \'PCR_EVERY_PES_PACKET\'|\'CONFIGURED_PCR_PERIOD\',
                                                    \'PcrPid\': 123,
                                                    \'PmtInterval\': 123,
                                                    \'PmtPid\': 123,
                                                    \'PrivateMetadataPid\': 123,
                                                    \'ProgramNumber\': 123,
                                                    \'RateMode\': \'VBR\'|\'CBR\',
                                                    \'Scte35Pid\': 123,
                                                    \'Scte35Source\': \'PASSTHROUGH\'|\'NONE\',
                                                    \'SegmentationMarkers\': \'NONE\'|\'RAI_SEGSTART\'|\'RAI_ADAPT\'|\'PSI_SEGSTART\'|\'EBP\'|\'EBP_LEGACY\',
                                                    \'SegmentationStyle\': \'MAINTAIN_CADENCE\'|\'RESET_CADENCE\',
                                                    \'SegmentationTime\': 123.0,
                                                    \'TimedMetadataPid\': 123,
                                                    \'TransportStreamId\': 123,
                                                    \'VideoPid\': 123
                                                },
                                                \'M3u8Settings\': {
                                                    \'AudioFramesPerPes\': 123,
                                                    \'AudioPids\': [
                                                        123,
                                                    ],
                                                    \'NielsenId3\': \'INSERT\'|\'NONE\',
                                                    \'PatInterval\': 123,
                                                    \'PcrControl\': \'PCR_EVERY_PES_PACKET\'|\'CONFIGURED_PCR_PERIOD\',
                                                    \'PcrPid\': 123,
                                                    \'PmtInterval\': 123,
                                                    \'PmtPid\': 123,
                                                    \'PrivateMetadataPid\': 123,
                                                    \'ProgramNumber\': 123,
                                                    \'Scte35Pid\': 123,
                                                    \'Scte35Source\': \'PASSTHROUGH\'|\'NONE\',
                                                    \'TimedMetadata\': \'PASSTHROUGH\'|\'NONE\',
                                                    \'TimedMetadataPid\': 123,
                                                    \'TransportStreamId\': 123,
                                                    \'VideoPid\': 123
                                                },
                                                \'MovSettings\': {
                                                    \'ClapAtom\': \'INCLUDE\'|\'EXCLUDE\',
                                                    \'CslgAtom\': \'INCLUDE\'|\'EXCLUDE\',
                                                    \'Mpeg2FourCCControl\': \'XDCAM\'|\'MPEG\',
                                                    \'PaddingControl\': \'OMNEON\'|\'NONE\',
                                                    \'Reference\': \'SELF_CONTAINED\'|\'EXTERNAL\'
                                                },
                                                \'Mp4Settings\': {
                                                    \'CslgAtom\': \'INCLUDE\'|\'EXCLUDE\',
                                                    \'FreeSpaceBox\': \'INCLUDE\'|\'EXCLUDE\',
                                                    \'MoovPlacement\': \'PROGRESSIVE_DOWNLOAD\'|\'NORMAL\',
                                                    \'Mp4MajorBrand\': \'string\'
                                                }
                                            },
                                            \'Extension\': \'string\',
                                            \'NameModifier\': \'string\',
                                            \'OutputSettings\': {
                                                \'HlsSettings\': {
                                                    \'AudioGroupId\': \'string\',
                                                    \'AudioRenditionSets\': \'string\',
                                                    \'AudioTrackType\': \'ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT\'|\'ALTERNATE_AUDIO_AUTO_SELECT\'|\'ALTERNATE_AUDIO_NOT_AUTO_SELECT\'|\'AUDIO_ONLY_VARIANT_STREAM\',
                                                    \'IFrameOnlyManifest\': \'INCLUDE\'|\'EXCLUDE\',
                                                    \'SegmentModifier\': \'string\'
                                                }
                                            },
                                            \'Preset\': \'string\',
                                            \'VideoDescription\': {
                                                \'AfdSignaling\': \'NONE\'|\'AUTO\'|\'FIXED\',
                                                \'AntiAlias\': \'DISABLED\'|\'ENABLED\',
                                                \'CodecSettings\': {
                                                    \'Codec\': \'FRAME_CAPTURE\'|\'H_264\'|\'H_265\'|\'MPEG2\'|\'PRORES\',
                                                    \'FrameCaptureSettings\': {
                                                        \'FramerateDenominator\': 123,
                                                        \'FramerateNumerator\': 123,
                                                        \'MaxCaptures\': 123,
                                                        \'Quality\': 123
                                                    },
                                                    \'H264Settings\': {
                                                        \'AdaptiveQuantization\': \'OFF\'|\'LOW\'|\'MEDIUM\'|\'HIGH\'|\'HIGHER\'|\'MAX\',
                                                        \'Bitrate\': 123,
                                                        \'CodecLevel\': \'AUTO\'|\'LEVEL_1\'|\'LEVEL_1_1\'|\'LEVEL_1_2\'|\'LEVEL_1_3\'|\'LEVEL_2\'|\'LEVEL_2_1\'|\'LEVEL_2_2\'|\'LEVEL_3\'|\'LEVEL_3_1\'|\'LEVEL_3_2\'|\'LEVEL_4\'|\'LEVEL_4_1\'|\'LEVEL_4_2\'|\'LEVEL_5\'|\'LEVEL_5_1\'|\'LEVEL_5_2\',
                                                        \'CodecProfile\': \'BASELINE\'|\'HIGH\'|\'HIGH_10BIT\'|\'HIGH_422\'|\'HIGH_422_10BIT\'|\'MAIN\',
                                                        \'DynamicSubGop\': \'ADAPTIVE\'|\'STATIC\',
                                                        \'EntropyEncoding\': \'CABAC\'|\'CAVLC\',
                                                        \'FieldEncoding\': \'PAFF\'|\'FORCE_FIELD\',
                                                        \'FlickerAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\',
                                                        \'FramerateControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                                        \'FramerateConversionAlgorithm\': \'DUPLICATE_DROP\'|\'INTERPOLATE\',
                                                        \'FramerateDenominator\': 123,
                                                        \'FramerateNumerator\': 123,
                                                        \'GopBReference\': \'DISABLED\'|\'ENABLED\',
                                                        \'GopClosedCadence\': 123,
                                                        \'GopSize\': 123.0,
                                                        \'GopSizeUnits\': \'FRAMES\'|\'SECONDS\',
                                                        \'HrdBufferInitialFillPercentage\': 123,
                                                        \'HrdBufferSize\': 123,
                                                        \'InterlaceMode\': \'PROGRESSIVE\'|\'TOP_FIELD\'|\'BOTTOM_FIELD\'|\'FOLLOW_TOP_FIELD\'|\'FOLLOW_BOTTOM_FIELD\',
                                                        \'MaxBitrate\': 123,
                                                        \'MinIInterval\': 123,
                                                        \'NumberBFramesBetweenReferenceFrames\': 123,
                                                        \'NumberReferenceFrames\': 123,
                                                        \'ParControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                                        \'ParDenominator\': 123,
                                                        \'ParNumerator\': 123,
                                                        \'QualityTuningLevel\': \'SINGLE_PASS\'|\'SINGLE_PASS_HQ\'|\'MULTI_PASS_HQ\',
                                                        \'QvbrSettings\': {
                                                            \'MaxAverageBitrate\': 123,
                                                            \'QvbrQualityLevel\': 123
                                                        },
                                                        \'RateControlMode\': \'VBR\'|\'CBR\'|\'QVBR\',
                                                        \'RepeatPps\': \'DISABLED\'|\'ENABLED\',
                                                        \'SceneChangeDetect\': \'DISABLED\'|\'ENABLED\',
                                                        \'Slices\': 123,
                                                        \'SlowPal\': \'DISABLED\'|\'ENABLED\',
                                                        \'Softness\': 123,
                                                        \'SpatialAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\',
                                                        \'Syntax\': \'DEFAULT\'|\'RP2027\',
                                                        \'Telecine\': \'NONE\'|\'SOFT\'|\'HARD\',
                                                        \'TemporalAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\',
                                                        \'UnregisteredSeiTimecode\': \'DISABLED\'|\'ENABLED\'
                                                    },
                                                    \'H265Settings\': {
                                                        \'AdaptiveQuantization\': \'OFF\'|\'LOW\'|\'MEDIUM\'|\'HIGH\'|\'HIGHER\'|\'MAX\',
                                                        \'AlternateTransferFunctionSei\': \'DISABLED\'|\'ENABLED\',
                                                        \'Bitrate\': 123,
                                                        \'CodecLevel\': \'AUTO\'|\'LEVEL_1\'|\'LEVEL_2\'|\'LEVEL_2_1\'|\'LEVEL_3\'|\'LEVEL_3_1\'|\'LEVEL_4\'|\'LEVEL_4_1\'|\'LEVEL_5\'|\'LEVEL_5_1\'|\'LEVEL_5_2\'|\'LEVEL_6\'|\'LEVEL_6_1\'|\'LEVEL_6_2\',
                                                        \'CodecProfile\': \'MAIN_MAIN\'|\'MAIN_HIGH\'|\'MAIN10_MAIN\'|\'MAIN10_HIGH\'|\'MAIN_422_8BIT_MAIN\'|\'MAIN_422_8BIT_HIGH\'|\'MAIN_422_10BIT_MAIN\'|\'MAIN_422_10BIT_HIGH\',
                                                        \'DynamicSubGop\': \'ADAPTIVE\'|\'STATIC\',
                                                        \'FlickerAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\',
                                                        \'FramerateControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                                        \'FramerateConversionAlgorithm\': \'DUPLICATE_DROP\'|\'INTERPOLATE\',
                                                        \'FramerateDenominator\': 123,
                                                        \'FramerateNumerator\': 123,
                                                        \'GopBReference\': \'DISABLED\'|\'ENABLED\',
                                                        \'GopClosedCadence\': 123,
                                                        \'GopSize\': 123.0,
                                                        \'GopSizeUnits\': \'FRAMES\'|\'SECONDS\',
                                                        \'HrdBufferInitialFillPercentage\': 123,
                                                        \'HrdBufferSize\': 123,
                                                        \'InterlaceMode\': \'PROGRESSIVE\'|\'TOP_FIELD\'|\'BOTTOM_FIELD\'|\'FOLLOW_TOP_FIELD\'|\'FOLLOW_BOTTOM_FIELD\',
                                                        \'MaxBitrate\': 123,
                                                        \'MinIInterval\': 123,
                                                        \'NumberBFramesBetweenReferenceFrames\': 123,
                                                        \'NumberReferenceFrames\': 123,
                                                        \'ParControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                                        \'ParDenominator\': 123,
                                                        \'ParNumerator\': 123,
                                                        \'QualityTuningLevel\': \'SINGLE_PASS\'|\'SINGLE_PASS_HQ\'|\'MULTI_PASS_HQ\',
                                                        \'QvbrSettings\': {
                                                            \'MaxAverageBitrate\': 123,
                                                            \'QvbrQualityLevel\': 123
                                                        },
                                                        \'RateControlMode\': \'VBR\'|\'CBR\'|\'QVBR\',
                                                        \'SampleAdaptiveOffsetFilterMode\': \'DEFAULT\'|\'ADAPTIVE\'|\'OFF\',
                                                        \'SceneChangeDetect\': \'DISABLED\'|\'ENABLED\',
                                                        \'Slices\': 123,
                                                        \'SlowPal\': \'DISABLED\'|\'ENABLED\',
                                                        \'SpatialAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\',
                                                        \'Telecine\': \'NONE\'|\'SOFT\'|\'HARD\',
                                                        \'TemporalAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\',
                                                        \'TemporalIds\': \'DISABLED\'|\'ENABLED\',
                                                        \'Tiles\': \'DISABLED\'|\'ENABLED\',
                                                        \'UnregisteredSeiTimecode\': \'DISABLED\'|\'ENABLED\',
                                                        \'WriteMp4PackagingType\': \'HVC1\'|\'HEV1\'
                                                    },
                                                    \'Mpeg2Settings\': {
                                                        \'AdaptiveQuantization\': \'OFF\'|\'LOW\'|\'MEDIUM\'|\'HIGH\',
                                                        \'Bitrate\': 123,
                                                        \'CodecLevel\': \'AUTO\'|\'LOW\'|\'MAIN\'|\'HIGH1440\'|\'HIGH\',
                                                        \'CodecProfile\': \'MAIN\'|\'PROFILE_422\',
                                                        \'DynamicSubGop\': \'ADAPTIVE\'|\'STATIC\',
                                                        \'FramerateControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                                        \'FramerateConversionAlgorithm\': \'DUPLICATE_DROP\'|\'INTERPOLATE\',
                                                        \'FramerateDenominator\': 123,
                                                        \'FramerateNumerator\': 123,
                                                        \'GopClosedCadence\': 123,
                                                        \'GopSize\': 123.0,
                                                        \'GopSizeUnits\': \'FRAMES\'|\'SECONDS\',
                                                        \'HrdBufferInitialFillPercentage\': 123,
                                                        \'HrdBufferSize\': 123,
                                                        \'InterlaceMode\': \'PROGRESSIVE\'|\'TOP_FIELD\'|\'BOTTOM_FIELD\'|\'FOLLOW_TOP_FIELD\'|\'FOLLOW_BOTTOM_FIELD\',
                                                        \'IntraDcPrecision\': \'AUTO\'|\'INTRA_DC_PRECISION_8\'|\'INTRA_DC_PRECISION_9\'|\'INTRA_DC_PRECISION_10\'|\'INTRA_DC_PRECISION_11\',
                                                        \'MaxBitrate\': 123,
                                                        \'MinIInterval\': 123,
                                                        \'NumberBFramesBetweenReferenceFrames\': 123,
                                                        \'ParControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                                        \'ParDenominator\': 123,
                                                        \'ParNumerator\': 123,
                                                        \'QualityTuningLevel\': \'SINGLE_PASS\'|\'MULTI_PASS\',
                                                        \'RateControlMode\': \'VBR\'|\'CBR\',
                                                        \'SceneChangeDetect\': \'DISABLED\'|\'ENABLED\',
                                                        \'SlowPal\': \'DISABLED\'|\'ENABLED\',
                                                        \'Softness\': 123,
                                                        \'SpatialAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\',
                                                        \'Syntax\': \'DEFAULT\'|\'D_10\',
                                                        \'Telecine\': \'NONE\'|\'SOFT\'|\'HARD\',
                                                        \'TemporalAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\'
                                                    },
                                                    \'ProresSettings\': {
                                                        \'CodecProfile\': \'APPLE_PRORES_422\'|\'APPLE_PRORES_422_HQ\'|\'APPLE_PRORES_422_LT\'|\'APPLE_PRORES_422_PROXY\',
                                                        \'FramerateControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                                        \'FramerateConversionAlgorithm\': \'DUPLICATE_DROP\'|\'INTERPOLATE\',
                                                        \'FramerateDenominator\': 123,
                                                        \'FramerateNumerator\': 123,
                                                        \'InterlaceMode\': \'PROGRESSIVE\'|\'TOP_FIELD\'|\'BOTTOM_FIELD\'|\'FOLLOW_TOP_FIELD\'|\'FOLLOW_BOTTOM_FIELD\',
                                                        \'ParControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                                        \'ParDenominator\': 123,
                                                        \'ParNumerator\': 123,
                                                        \'SlowPal\': \'DISABLED\'|\'ENABLED\',
                                                        \'Telecine\': \'NONE\'|\'HARD\'
                                                    }
                                                },
                                                \'ColorMetadata\': \'IGNORE\'|\'INSERT\',
                                                \'Crop\': {
                                                    \'Height\': 123,
                                                    \'Width\': 123,
                                                    \'X\': 123,
                                                    \'Y\': 123
                                                },
                                                \'DropFrameTimecode\': \'DISABLED\'|\'ENABLED\',
                                                \'FixedAfd\': 123,
                                                \'Height\': 123,
                                                \'Position\': {
                                                    \'Height\': 123,
                                                    \'Width\': 123,
                                                    \'X\': 123,
                                                    \'Y\': 123
                                                },
                                                \'RespondToAfd\': \'NONE\'|\'RESPOND\'|\'PASSTHROUGH\',
                                                \'ScalingBehavior\': \'DEFAULT\'|\'STRETCH_TO_OUTPUT\',
                                                \'Sharpness\': 123,
                                                \'TimecodeInsertion\': \'DISABLED\'|\'PIC_TIMING_SEI\',
                                                \'VideoPreprocessors\': {
                                                    \'ColorCorrector\': {
                                                        \'Brightness\': 123,
                                                        \'ColorSpaceConversion\': \'NONE\'|\'FORCE_601\'|\'FORCE_709\'|\'FORCE_HDR10\'|\'FORCE_HLG_2020\',
                                                        \'Contrast\': 123,
                                                        \'Hdr10Metadata\': {
                                                            \'BluePrimaryX\': 123,
                                                            \'BluePrimaryY\': 123,
                                                            \'GreenPrimaryX\': 123,
                                                            \'GreenPrimaryY\': 123,
                                                            \'MaxContentLightLevel\': 123,
                                                            \'MaxFrameAverageLightLevel\': 123,
                                                            \'MaxLuminance\': 123,
                                                            \'MinLuminance\': 123,
                                                            \'RedPrimaryX\': 123,
                                                            \'RedPrimaryY\': 123,
                                                            \'WhitePointX\': 123,
                                                            \'WhitePointY\': 123
                                                        },
                                                        \'Hue\': 123,
                                                        \'Saturation\': 123
                                                    },
                                                    \'Deinterlacer\': {
                                                        \'Algorithm\': \'INTERPOLATE\'|\'INTERPOLATE_TICKER\'|\'BLEND\'|\'BLEND_TICKER\',
                                                        \'Control\': \'FORCE_ALL_FRAMES\'|\'NORMAL\',
                                                        \'Mode\': \'DEINTERLACE\'|\'INVERSE_TELECINE\'|\'ADAPTIVE\'
                                                    },
                                                    \'ImageInserter\': {
                                                        \'InsertableImages\': [
                                                            {
                                                                \'Duration\': 123,
                                                                \'FadeIn\': 123,
                                                                \'FadeOut\': 123,
                                                                \'Height\': 123,
                                                                \'ImageInserterInput\': \'string\',
                                                                \'ImageX\': 123,
                                                                \'ImageY\': 123,
                                                                \'Layer\': 123,
                                                                \'Opacity\': 123,
                                                                \'StartTime\': \'string\',
                                                                \'Width\': 123
                                                            },
                                                        ]
                                                    },
                                                    \'NoiseReducer\': {
                                                        \'Filter\': \'BILATERAL\'|\'MEAN\'|\'GAUSSIAN\'|\'LANCZOS\'|\'SHARPEN\'|\'CONSERVE\'|\'SPATIAL\',
                                                        \'FilterSettings\': {
                                                            \'Strength\': 123
                                                        },
                                                        \'SpatialFilterSettings\': {
                                                            \'PostFilterSharpenStrength\': 123,
                                                            \'Speed\': 123,
                                                            \'Strength\': 123
                                                        }
                                                    },
                                                    \'TimecodeBurnin\': {
                                                        \'FontSize\': 123,
                                                        \'Position\': \'TOP_CENTER\'|\'TOP_LEFT\'|\'TOP_RIGHT\'|\'MIDDLE_LEFT\'|\'MIDDLE_CENTER\'|\'MIDDLE_RIGHT\'|\'BOTTOM_LEFT\'|\'BOTTOM_CENTER\'|\'BOTTOM_RIGHT\',
                                                        \'Prefix\': \'string\'
                                                    }
                                                },
                                                \'Width\': 123
                                            }
                                        },
                                    ]
                                },
                            ],
                            \'TimecodeConfig\': {
                                \'Anchor\': \'string\',
                                \'Source\': \'EMBEDDED\'|\'ZEROBASED\'|\'SPECIFIEDSTART\',
                                \'Start\': \'string\',
                                \'TimestampOffset\': \'string\'
                            },
                            \'TimedMetadataInsertion\': {
                                \'Id3Insertions\': [
                                    {
                                        \'Id3\': \'string\',
                                        \'Timecode\': \'string\'
                                    },
                                ]
                            }
                        },
                        \'Type\': \'SYSTEM\'|\'CUSTOM\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **JobTemplates** *(list) --* List of Job templates.
              
              - *(dict) --* A job template is a pre-made set of encoding instructions that you can use to quickly create a job.
                
                - **Arn** *(string) --* An identifier for this resource that is unique within all of AWS.
                
                - **Category** *(string) --* An optional category you create to organize your job templates.
                
                - **CreatedAt** *(datetime) --* The timestamp in epoch seconds for Job template creation.
                
                - **Description** *(string) --* An optional description you create for each job template.
                
                - **LastUpdated** *(datetime) --* The timestamp in epoch seconds when the Job template was last updated.
                
                - **Name** *(string) --* A name you create for each job template. Each name must be unique within your account.
                
                - **Queue** *(string) --* Optional. The queue that jobs created from this template are assigned to. If you don\'t specify this, jobs will go to the default queue.
                
                - **Settings** *(dict) --* JobTemplateSettings contains all the transcode settings saved in the template that will be applied to jobs created from it.
                  
                  - **AdAvailOffset** *(integer) --* When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time.
                  
                  - **AvailBlanking** *(dict) --* Settings for ad avail blanking. Video can be blanked or overlaid with an image, and audio muted during SCTE-35 triggered ad avails.
                    
                    - **AvailBlankingImage** *(string) --* Blanking image to be used. Leave empty for solid black. Only bmp and png images are supported.
                
                  - **Inputs** *(list) --* Use Inputs (inputs) to define the source file used in the transcode job. There can only be one input in a job template. Using the API, you can include multiple inputs when referencing a job template.
                    
                    - *(dict) --* Specified video input in a template.
                      
                      - **AudioSelectorGroups** *(dict) --* Specifies set of audio selectors within an input to combine. An input may have multiple audio selector groups. See \"Audio Selector Group\":#inputs-audio_selector_group for more information.
                        
                        - *(string) --* 
                          
                          - *(dict) --* Group of Audio Selectors
                            
                            - **AudioSelectorNames** *(list) --* Name of an Audio Selector within the same input to include in the group. Audio selector names are standardized, based on their order within the input (e.g., \"Audio Selector 1\"). The audio selector name parameter can be repeated to add any number of audio selectors to the group.
                              
                              - *(string) --* 
                          
                      - **AudioSelectors** *(dict) --* Use Audio selectors (AudioSelectors) to specify a track or set of tracks from the input that you will use in your outputs. You can use mutiple Audio selectors per input.
                        
                        - *(string) --* 
                          
                          - *(dict) --* Selector for Audio
                            
                            - **CustomLanguageCode** *(string) --* Selects a specific language code from within an audio source, using the ISO 639-2 or ISO 639-3 three-letter language code
                            
                            - **DefaultSelection** *(string) --* Enable this setting on one audio selector to set it as the default for the job. The service uses this default for outputs where it can\'t find the specified input audio. If you don\'t set a default, those outputs have no audio.
                            
                            - **ExternalAudioFileInput** *(string) --* Specifies audio data from an external file source.
                            
                            - **LanguageCode** *(string) --* Selects a specific language code from within an audio source.
                            
                            - **Offset** *(integer) --* Specifies a time delta in milliseconds to offset the audio from the input video.
                            
                            - **Pids** *(list) --* Selects a specific PID from within an audio source (e.g. 257 selects PID 0x101).
                              
                              - *(integer) --* 
                          
                            - **ProgramSelection** *(integer) --* Use this setting for input streams that contain Dolby E, to have the service extract specific program data from the track. To select multiple programs, create multiple selectors with the same Track and different Program numbers. In the console, this setting is visible when you set Selector type to Track. Choose the program number from the dropdown list. If you are sending a JSON file, provide the program ID, which is part of the audio metadata. If your input file has incorrect metadata, you can choose All channels instead of a program number to have the service ignore the program IDs and include all the programs in the track.
                            
                            - **RemixSettings** *(dict) --* Use these settings to reorder the audio channels of one input to match those of another input. This allows you to combine the two files into a single output, one after the other.
                              
                              - **ChannelMapping** *(dict) --* Channel mapping (ChannelMapping) contains the group of fields that hold the remixing value for each channel. Units are in dB. Acceptable values are within the range from -60 (mute) through 6. A setting of 0 passes the input channel unchanged to the output channel (no attenuation or amplification).
                                
                                - **OutputChannels** *(list) --* List of output channels
                                  
                                  - *(dict) --* OutputChannel mapping settings.
                                    
                                    - **InputChannels** *(list) --* List of input channels
                                      
                                      - *(integer) --* 
                                  
                              - **ChannelsIn** *(integer) --* Specify the number of audio channels from your input that you want to use in your output. With remixing, you might combine or split the data in these channels, so the number of channels in your final output might be different.
                              
                              - **ChannelsOut** *(integer) --* Specify the number of channels in this output after remixing. Valid values: 1, 2, 4, 6, 8
                          
                            - **SelectorType** *(string) --* Specifies the type of the audio selector.
                            
                            - **Tracks** *(list) --* Identify a track from the input audio to include in this selector by entering the track index number. To include several tracks in a single audio selector, specify multiple tracks as follows. Using the console, enter a comma-separated list. For examle, type \"1,2,3\" to include tracks 1 through 3. Specifying directly in your JSON job file, provide the track numbers in an array. For example, \"tracks\": [1,2,3].
                              
                              - *(integer) --* 
                          
                      - **CaptionSelectors** *(dict) --* Use Captions selectors (CaptionSelectors) to specify the captions data from the input that you will use in your outputs. You can use mutiple captions selectors per input.
                        
                        - *(string) --* 
                          
                          - *(dict) --* Set up captions in your outputs by first selecting them from your input here.
                            
                            - **CustomLanguageCode** *(string) --* The specific language to extract from source, using the ISO 639-2 or ISO 639-3 three-letter language code. If input is SCTE-27, complete this field and/or PID to select the caption language to extract. If input is DVB-Sub and output is Burn-in or SMPTE-TT, complete this field and/or PID to select the caption language to extract. If input is DVB-Sub that is being passed through, omit this field (and PID field); there is no way to extract a specific language with pass-through captions.
                            
                            - **LanguageCode** *(string) --* The specific language to extract from source. If input is SCTE-27, complete this field and/or PID to select the caption language to extract. If input is DVB-Sub and output is Burn-in or SMPTE-TT, complete this field and/or PID to select the caption language to extract. If input is DVB-Sub that is being passed through, omit this field (and PID field); there is no way to extract a specific language with pass-through captions.
                            
                            - **SourceSettings** *(dict) --* Source settings (SourceSettings) contains the group of settings for captions in the input.
                              
                              - **AncillarySourceSettings** *(dict) --* Settings for ancillary captions source.
                                
                                - **SourceAncillaryChannelNumber** *(integer) --* Specifies the 608 channel number in the ancillary data track from which to extract captions. Unused for passthrough.
                            
                              - **DvbSubSourceSettings** *(dict) --* DVB Sub Source Settings
                                
                                - **Pid** *(integer) --* When using DVB-Sub with Burn-In or SMPTE-TT, use this PID for the source content. Unused for DVB-Sub passthrough. All DVB-Sub content is passed through, regardless of selectors.
                            
                              - **EmbeddedSourceSettings** *(dict) --* Settings for embedded captions Source
                                
                                - **Convert608To708** *(string) --* When set to UPCONVERT, 608 data is both passed through via the \"608 compatibility bytes\" fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded.
                                
                                - **Source608ChannelNumber** *(integer) --* Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough.
                                
                                - **Source608TrackNumber** *(integer) --* Specifies the video track index used for extracting captions. The system only supports one input video track, so this should always be set to \'1\'.
                            
                              - **FileSourceSettings** *(dict) --* Settings for File-based Captions in Source
                                
                                - **Convert608To708** *(string) --* If set to UPCONVERT, 608 caption data is both passed through via the \"608 compatibility bytes\" fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded.
                                
                                - **SourceFile** *(string) --* External caption file used for loading captions. Accepted file extensions are \'scc\', \'ttml\', \'dfxp\', \'stl\', \'srt\', and \'smi\'.
                                
                                - **TimeDelta** *(integer) --* Specifies a time delta in seconds to offset the captions from the source file.
                            
                              - **SourceType** *(string) --* Use Source (SourceType) to identify the format of your input captions. The service cannot auto-detect caption format.
                              
                              - **TeletextSourceSettings** *(dict) --* Settings specific to Teletext caption sources, including Page number.
                                
                                - **PageNumber** *(string) --* Use Page Number (PageNumber) to specify the three-digit hexadecimal page number that will be used for Teletext captions. Do not use this setting if you are passing through teletext from the input source to output.
                            
                      - **DeblockFilter** *(string) --* Enable Deblock (InputDeblockFilter) to produce smoother motion in the output. Default is disabled. Only manaully controllable for MPEG2 and uncompressed video inputs.
                      
                      - **DenoiseFilter** *(string) --* Enable Denoise (InputDenoiseFilter) to filter noise from the input. Default is disabled. Only applicable to MPEG2, H.264, H.265, and uncompressed video inputs.
                      
                      - **FilterEnable** *(string) --* Use Filter enable (InputFilterEnable) to specify how the transcoding service applies the denoise and deblock filters. You must also enable the filters separately, with Denoise (InputDenoiseFilter) and Deblock (InputDeblockFilter). * Auto - The transcoding service determines whether to apply filtering, depending on input type and quality. * Disable - The input is not filtered. This is true even if you use the API to enable them in (InputDeblockFilter) and (InputDeblockFilter). * Force - The in put is filtered regardless of input type.
                      
                      - **FilterStrength** *(integer) --* Use Filter strength (FilterStrength) to adjust the magnitude the input filter settings (Deblock and Denoise). The range is -5 to 5. Default is 0.
                      
                      - **InputClippings** *(list) --* (InputClippings) contains sets of start and end times that together specify a portion of the input to be used in the outputs. If you provide only a start time, the clip will be the entire input from that point to the end. If you provide only an end time, it will be the entire input up to that point. When you specify more than one input clip, the transcoding service creates the job outputs by stringing the clips together in the order you specify them.
                        
                        - *(dict) --* To transcode only portions of your input (clips), include one Input clipping (one instance of InputClipping in the JSON job file) for each input clip. All input clips you specify will be included in every output of the job.
                          
                          - **EndTimecode** *(string) --* Set End timecode (EndTimecode) to the end of the portion of the input you are clipping. The frame corresponding to the End timecode value is included in the clip. Start timecode or End timecode may be left blank, but not both. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When choosing this value, take into account your setting for timecode source under input settings (InputTimecodeSource). For example, if you have embedded timecodes that start at 01:00:00:00 and you want your clip to end six minutes into the video, use 01:06:00:00.
                          
                          - **StartTimecode** *(string) --* Set Start timecode (StartTimecode) to the beginning of the portion of the input you are clipping. The frame corresponding to the Start timecode value is included in the clip. Start timecode or End timecode may be left blank, but not both. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When choosing this value, take into account your setting for Input timecode source. For example, if you have embedded timecodes that start at 01:00:00:00 and you want your clip to begin five minutes into the video, use 01:05:00:00.
                      
                      - **ProgramNumber** *(integer) --* Use Program (programNumber) to select a specific program from within a multi-program transport stream. Note that Quad 4K is not currently supported. Default is the first program within the transport stream. If the program you specify doesn\'t exist, the transcoding service will use this default.
                      
                      - **PsiControl** *(string) --* Set PSI control (InputPsiControl) for transport stream inputs to specify which data the demux process to scans. * Ignore PSI - Scan all PIDs for audio and video. * Use PSI - Scan only PSI data.
                      
                      - **TimecodeSource** *(string) --* Timecode source under input settings (InputTimecodeSource) only affects the behavior of features that apply to a single input at a time, such as input clipping and synchronizing some captions formats. Use this setting to specify whether the service counts frames by timecodes embedded in the video (EMBEDDED) or by starting the first frame at zero (ZEROBASED). In both cases, the timecode format is HH:MM:SS:FF or HH:MM:SS;FF, where FF is the frame number. Only set this to EMBEDDED if your source video has embedded timecodes.
                      
                      - **VideoSelector** *(dict) --* Selector for video.
                        
                        - **ColorSpace** *(string) --* If your input video has accurate color space metadata, or if you don\'t know about color space, leave this set to the default value FOLLOW. The service will automatically detect your input color space. If your input video has metadata indicating the wrong color space, or if your input video is missing color space metadata that should be there, specify the accurate color space here. If you choose HDR10, you can also correct inaccurate color space coefficients, using the HDR master display information controls. You must also set Color space usage (ColorSpaceUsage) to FORCE for the service to use these values.
                        
                        - **ColorSpaceUsage** *(string) --* There are two sources for color metadata, the input file and the job configuration (in the Color space and HDR master display informaiton settings). The Color space usage setting controls which takes precedence. FORCE: The system will use color metadata supplied by user, if any. If the user does not supply color metadata, the system will use data from the source. FALLBACK: The system will use color metadata from the source. If source has no color metadata, the system will use user-supplied color metadata values if available.
                        
                        - **Hdr10Metadata** *(dict) --* Use the HDR master display (Hdr10Metadata) settings to correct HDR metadata or to provide missing metadata. These values vary depending on the input video and must be provided by a color grader. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that these settings are not color correction. Note that if you are creating HDR outputs inside of an HLS CMAF package, to comply with the Apple specification, you must use the HVC1 for H.265 setting.
                          
                          - **BluePrimaryX** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                          
                          - **BluePrimaryY** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                          
                          - **GreenPrimaryX** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                          
                          - **GreenPrimaryY** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                          
                          - **MaxContentLightLevel** *(integer) --* Maximum light level among all samples in the coded video sequence, in units of candelas per square meter.
                          
                          - **MaxFrameAverageLightLevel** *(integer) --* Maximum average light level of any frame in the coded video sequence, in units of candelas per square meter.
                          
                          - **MaxLuminance** *(integer) --* Nominal maximum mastering display luminance in units of of 0.0001 candelas per square meter.
                          
                          - **MinLuminance** *(integer) --* Nominal minimum mastering display luminance in units of of 0.0001 candelas per square meter
                          
                          - **RedPrimaryX** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                          
                          - **RedPrimaryY** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                          
                          - **WhitePointX** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                          
                          - **WhitePointY** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                      
                        - **Pid** *(integer) --* Use PID (Pid) to select specific video data from an input file. Specify this value as an integer; the system automatically converts it to the hexidecimal value. For example, 257 selects PID 0x101. A PID, or packet identifier, is an identifier for a set of data in an MPEG-2 transport stream container.
                        
                        - **ProgramNumber** *(integer) --* Selects a specific program from within a multi-program transport stream. Note that Quad 4K is not currently supported.
                    
                  - **NielsenConfiguration** *(dict) --* Settings for Nielsen Configuration
                    
                    - **BreakoutCode** *(integer) --* Use Nielsen Configuration (NielsenConfiguration) to set the Nielsen measurement system breakout code. Supported values are 0, 3, 7, and 9.
                    
                    - **DistributorId** *(string) --* Use Distributor ID (DistributorID) to specify the distributor ID that is assigned to your organization by Neilsen.
                
                  - **OutputGroups** *(list) --* (OutputGroups) contains one group of settings for each set of outputs that share a common package type. All unpackaged files (MPEG-4, MPEG-2 TS, Quicktime, MXF, and no container) are grouped in a single output group as well. Required in (OutputGroups) is a group of settings that apply to the whole group. This required object depends on the value you set for (Type) under (OutputGroups)>(OutputGroupSettings). Type, settings object pairs are as follows. * FILE_GROUP_SETTINGS, FileGroupSettings * HLS_GROUP_SETTINGS, HlsGroupSettings * DASH_ISO_GROUP_SETTINGS, DashIsoGroupSettings * MS_SMOOTH_GROUP_SETTINGS, MsSmoothGroupSettings * CMAF_GROUP_SETTINGS, CmafGroupSettings
                    
                    - *(dict) --* Group of outputs
                      
                      - **CustomName** *(string) --* Use Custom Group Name (CustomName) to specify a name for the output group. This value is displayed on the console and can make your job settings JSON more human-readable. It does not affect your outputs. Use up to twelve characters that are either letters, numbers, spaces, or underscores.
                      
                      - **Name** *(string) --* Name of the output group
                      
                      - **OutputGroupSettings** *(dict) --* Output Group settings, including type
                        
                        - **CmafGroupSettings** *(dict) --* Required when you set (Type) under (OutputGroups)>(OutputGroupSettings) to CMAF_GROUP_SETTINGS. Each output in a CMAF Output Group may only contain a single video, audio, or caption output.
                          
                          - **BaseUrl** *(string) --* A partial URI prefix that will be put in the manifest file at the top level BaseURL element. Can be used if streams are delivered from a different URL than the manifest file.
                          
                          - **ClientCache** *(string) --* When set to ENABLED, sets #EXT-X-ALLOW-CACHE:no tag, which prevents client from saving media segments for later replay.
                          
                          - **CodecSpecification** *(string) --* Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation.
                          
                          - **Destination** *(string) --* Use Destination (Destination) to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file.
                          
                          - **Encryption** *(dict) --* DRM settings.
                            
                            - **ConstantInitializationVector** *(string) --* This is a 128-bit, 16-byte hex value represented by a 32-character text string. If this parameter is not set then the Initialization Vector will follow the segment number by default.
                            
                            - **EncryptionMethod** *(string) --* Encrypts the segments with the given encryption scheme. Leave blank to disable. Selecting \'Disabled\' in the web interface also disables encryption.
                            
                            - **InitializationVectorInManifest** *(string) --* The Initialization Vector is a 128-bit number used in conjunction with the key for encrypting blocks. If set to INCLUDE, Initialization Vector is listed in the manifest. Otherwise Initialization Vector is not in the manifest.
                            
                            - **StaticKeyProvider** *(dict) --* Settings for use with a SPEKE key provider.
                              
                              - **KeyFormat** *(string) --* Relates to DRM implementation. Sets the value of the KEYFORMAT attribute. Must be \'identity\' or a reverse DNS string. May be omitted to indicate an implicit value of \'identity\'.
                              
                              - **KeyFormatVersions** *(string) --* Relates to DRM implementation. Either a single positive integer version value or a slash delimited list of version values (1/2/3).
                              
                              - **StaticKeyValue** *(string) --* Relates to DRM implementation. Use a 32-character hexidecimal string to specify Key Value (StaticKeyValue).
                              
                              - **Url** *(string) --* Relates to DRM implementation. The location of the license server used for protecting content.
                          
                            - **Type** *(string) --* Indicates which type of key provider is used for encryption.
                        
                          - **FragmentLength** *(integer) --* Length of fragments to generate (in seconds). Fragment length must be compatible with GOP size and Framerate. Note that fragments will end on the next keyframe after this number of seconds, so actual fragment length may be longer. When Emit Single File is checked, the fragmentation is internal to a single output file and it does not cause the creation of many output files as in other output types.
                          
                          - **ManifestCompression** *(string) --* When set to GZIP, compresses HLS playlist.
                          
                          - **ManifestDurationFormat** *(string) --* Indicates whether the output manifest should use floating point values for segment duration.
                          
                          - **MinBufferTime** *(integer) --* Minimum time of initially buffered media that is needed to ensure smooth playout.
                          
                          - **MinFinalSegmentLength** *(float) --* Keep this setting at the default value of 0, unless you are troubleshooting a problem with how devices play back the end of your video asset. If you know that player devices are hanging on the final segment of your video because the length of your final segment is too short, use this setting to specify a minimum final segment length, in seconds. Choose a value that is greater than or equal to 1 and less than your segment length. When you specify a value for this setting, the encoder will combine any final segment that is shorter than the length that you specify with the previous segment. For example, your segment length is 3 seconds and your final segment is .5 seconds without a minimum final segment length; when you set the minimum final segment length to 1, your final segment is 3.5 seconds.
                          
                          - **SegmentControl** *(string) --* When set to SINGLE_FILE, a single output file is generated, which is internally segmented using the Fragment Length and Segment Length. When set to SEGMENTED_FILES, separate segment files will be created.
                          
                          - **SegmentLength** *(integer) --* Use this setting to specify the length, in seconds, of each individual CMAF segment. This value applies to the whole package; that is, to every output in the output group. Note that segments end on the first keyframe after this number of seconds, so the actual segment length might be slightly longer. If you set Segment control (CmafSegmentControl) to single file, the service puts the content of each output in a single file that has metadata that marks these segments. If you set it to segmented files, the service creates multiple files for each output, each with the content of one segment.
                          
                          - **StreamInfResolution** *(string) --* Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest.
                          
                          - **WriteDashManifest** *(string) --* When set to ENABLED, a DASH MPD manifest will be generated for this output.
                          
                          - **WriteHlsManifest** *(string) --* When set to ENABLED, an Apple HLS manifest will be generated for this output.
                      
                        - **DashIsoGroupSettings** *(dict) --* Required when you set (Type) under (OutputGroups)>(OutputGroupSettings) to DASH_ISO_GROUP_SETTINGS.
                          
                          - **BaseUrl** *(string) --* A partial URI prefix that will be put in the manifest (.mpd) file at the top level BaseURL element. Can be used if streams are delivered from a different URL than the manifest file.
                          
                          - **Destination** *(string) --* Use Destination (Destination) to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file.
                          
                          - **Encryption** *(dict) --* DRM settings.
                            
                            - **SpekeKeyProvider** *(dict) --* Settings for use with a SPEKE key provider
                              
                              - **ResourceId** *(string) --* The SPEKE-compliant server uses Resource ID (ResourceId) to identify content.
                              
                              - **SystemIds** *(list) --* Relates to SPEKE implementation. DRM system identifiers. DASH output groups support a max of two system ids. Other group types support one system id.
                                
                                - *(string) --* 
                            
                              - **Url** *(string) --* Use URL (Url) to specify the SPEKE-compliant server that will provide keys for content.
                          
                          - **FragmentLength** *(integer) --* Length of fragments to generate (in seconds). Fragment length must be compatible with GOP size and Framerate. Note that fragments will end on the next keyframe after this number of seconds, so actual fragment length may be longer. When Emit Single File is checked, the fragmentation is internal to a single output file and it does not cause the creation of many output files as in other output types.
                          
                          - **HbbtvCompliance** *(string) --* Supports HbbTV specification as indicated
                          
                          - **MinBufferTime** *(integer) --* Minimum time of initially buffered media that is needed to ensure smooth playout.
                          
                          - **SegmentControl** *(string) --* When set to SINGLE_FILE, a single output file is generated, which is internally segmented using the Fragment Length and Segment Length. When set to SEGMENTED_FILES, separate segment files will be created.
                          
                          - **SegmentLength** *(integer) --* Length of mpd segments to create (in seconds). Note that segments will end on the next keyframe after this number of seconds, so actual segment length may be longer. When Emit Single File is checked, the segmentation is internal to a single output file and it does not cause the creation of many output files as in other output types.
                          
                          - **WriteSegmentTimelineInRepresentation** *(string) --* When ENABLED, segment durations are indicated in the manifest using SegmentTimeline and SegmentTimeline will be promoted down into Representation from AdaptationSet.
                      
                        - **FileGroupSettings** *(dict) --* Required when you set (Type) under (OutputGroups)>(OutputGroupSettings) to FILE_GROUP_SETTINGS.
                          
                          - **Destination** *(string) --* Use Destination (Destination) to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file.
                      
                        - **HlsGroupSettings** *(dict) --* Required when you set (Type) under (OutputGroups)>(OutputGroupSettings) to HLS_GROUP_SETTINGS.
                          
                          - **AdMarkers** *(list) --* Choose one or more ad marker types to pass SCTE35 signals through to this group of Apple HLS outputs.
                            
                            - *(string) --* 
                        
                          - **BaseUrl** *(string) --* A partial URI prefix that will be prepended to each output in the media .m3u8 file. Can be used if base manifest is delivered from a different URL than the main .m3u8 file.
                          
                          - **CaptionLanguageMappings** *(list) --* Language to be used on Caption outputs
                            
                            - *(dict) --* Caption Language Mapping
                              
                              - **CaptionChannel** *(integer) --* Caption channel.
                              
                              - **CustomLanguageCode** *(string) --* Specify the language for this caption channel, using the ISO 639-2 or ISO 639-3 three-letter language code
                              
                              - **LanguageCode** *(string) --* Specify the language, using the ISO 639-2 three-letter code listed at https://www.loc.gov/standards/iso639-2/php/code_list.php.
                              
                              - **LanguageDescription** *(string) --* Caption language description.
                          
                          - **CaptionLanguageSetting** *(string) --* Applies only to 608 Embedded output captions. Insert: Include CLOSED-CAPTIONS lines in the manifest. Specify at least one language in the CC1 Language Code field. One CLOSED-CAPTION line is added for each Language Code you specify. Make sure to specify the languages in the order in which they appear in the original source (if the source is embedded format) or the order of the caption selectors (if the source is other than embedded). Otherwise, languages in the manifest will not match up properly with the output captions. None: Include CLOSED-CAPTIONS=NONE line in the manifest. Omit: Omit any CLOSED-CAPTIONS line from the manifest.
                          
                          - **ClientCache** *(string) --* When set to ENABLED, sets #EXT-X-ALLOW-CACHE:no tag, which prevents client from saving media segments for later replay.
                          
                          - **CodecSpecification** *(string) --* Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation.
                          
                          - **Destination** *(string) --* Use Destination (Destination) to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file.
                          
                          - **DirectoryStructure** *(string) --* Indicates whether segments should be placed in subdirectories.
                          
                          - **Encryption** *(dict) --* DRM settings.
                            
                            - **ConstantInitializationVector** *(string) --* This is a 128-bit, 16-byte hex value represented by a 32-character text string. If this parameter is not set then the Initialization Vector will follow the segment number by default.
                            
                            - **EncryptionMethod** *(string) --* Encrypts the segments with the given encryption scheme. Leave blank to disable. Selecting \'Disabled\' in the web interface also disables encryption.
                            
                            - **InitializationVectorInManifest** *(string) --* The Initialization Vector is a 128-bit number used in conjunction with the key for encrypting blocks. If set to INCLUDE, Initialization Vector is listed in the manifest. Otherwise Initialization Vector is not in the manifest.
                            
                            - **SpekeKeyProvider** *(dict) --* Settings for use with a SPEKE key provider
                              
                              - **ResourceId** *(string) --* The SPEKE-compliant server uses Resource ID (ResourceId) to identify content.
                              
                              - **SystemIds** *(list) --* Relates to SPEKE implementation. DRM system identifiers. DASH output groups support a max of two system ids. Other group types support one system id.
                                
                                - *(string) --* 
                            
                              - **Url** *(string) --* Use URL (Url) to specify the SPEKE-compliant server that will provide keys for content.
                          
                            - **StaticKeyProvider** *(dict) --* Settings for use with a SPEKE key provider.
                              
                              - **KeyFormat** *(string) --* Relates to DRM implementation. Sets the value of the KEYFORMAT attribute. Must be \'identity\' or a reverse DNS string. May be omitted to indicate an implicit value of \'identity\'.
                              
                              - **KeyFormatVersions** *(string) --* Relates to DRM implementation. Either a single positive integer version value or a slash delimited list of version values (1/2/3).
                              
                              - **StaticKeyValue** *(string) --* Relates to DRM implementation. Use a 32-character hexidecimal string to specify Key Value (StaticKeyValue).
                              
                              - **Url** *(string) --* Relates to DRM implementation. The location of the license server used for protecting content.
                          
                            - **Type** *(string) --* Indicates which type of key provider is used for encryption.
                        
                          - **ManifestCompression** *(string) --* When set to GZIP, compresses HLS playlist.
                          
                          - **ManifestDurationFormat** *(string) --* Indicates whether the output manifest should use floating point values for segment duration.
                          
                          - **MinFinalSegmentLength** *(float) --* Keep this setting at the default value of 0, unless you are troubleshooting a problem with how devices play back the end of your video asset. If you know that player devices are hanging on the final segment of your video because the length of your final segment is too short, use this setting to specify a minimum final segment length, in seconds. Choose a value that is greater than or equal to 1 and less than your segment length. When you specify a value for this setting, the encoder will combine any final segment that is shorter than the length that you specify with the previous segment. For example, your segment length is 3 seconds and your final segment is .5 seconds without a minimum final segment length; when you set the minimum final segment length to 1, your final segment is 3.5 seconds.
                          
                          - **MinSegmentLength** *(integer) --* When set, Minimum Segment Size is enforced by looking ahead and back within the specified range for a nearby avail and extending the segment size if needed.
                          
                          - **OutputSelection** *(string) --* Indicates whether the .m3u8 manifest file should be generated for this HLS output group.
                          
                          - **ProgramDateTime** *(string) --* Includes or excludes EXT-X-PROGRAM-DATE-TIME tag in .m3u8 manifest files. The value is calculated as follows: either the program date and time are initialized using the input timecode source, or the time is initialized using the input timecode source and the date is initialized using the timestamp_offset.
                          
                          - **ProgramDateTimePeriod** *(integer) --* Period of insertion of EXT-X-PROGRAM-DATE-TIME entry, in seconds.
                          
                          - **SegmentControl** *(string) --* When set to SINGLE_FILE, emits program as a single media resource (.ts) file, uses #EXT-X-BYTERANGE tags to index segment for playback.
                          
                          - **SegmentLength** *(integer) --* Length of MPEG-2 Transport Stream segments to create (in seconds). Note that segments will end on the next keyframe after this number of seconds, so actual segment length may be longer.
                          
                          - **SegmentsPerSubdirectory** *(integer) --* Number of segments to write to a subdirectory before starting a new one. directoryStructure must be SINGLE_DIRECTORY for this setting to have an effect.
                          
                          - **StreamInfResolution** *(string) --* Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest.
                          
                          - **TimedMetadataId3Frame** *(string) --* Indicates ID3 frame that has the timecode.
                          
                          - **TimedMetadataId3Period** *(integer) --* Timed Metadata interval in seconds.
                          
                          - **TimestampDeltaMilliseconds** *(integer) --* Provides an extra millisecond delta offset to fine tune the timestamps.
                      
                        - **MsSmoothGroupSettings** *(dict) --* Required when you set (Type) under (OutputGroups)>(OutputGroupSettings) to MS_SMOOTH_GROUP_SETTINGS.
                          
                          - **AudioDeduplication** *(string) --* COMBINE_DUPLICATE_STREAMS combines identical audio encoding settings across a Microsoft Smooth output group into a single audio stream.
                          
                          - **Destination** *(string) --* Use Destination (Destination) to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file.
                          
                          - **Encryption** *(dict) --* If you are using DRM, set DRM System (MsSmoothEncryptionSettings) to specify the value SpekeKeyProvider.
                            
                            - **SpekeKeyProvider** *(dict) --* Settings for use with a SPEKE key provider
                              
                              - **ResourceId** *(string) --* The SPEKE-compliant server uses Resource ID (ResourceId) to identify content.
                              
                              - **SystemIds** *(list) --* Relates to SPEKE implementation. DRM system identifiers. DASH output groups support a max of two system ids. Other group types support one system id.
                                
                                - *(string) --* 
                            
                              - **Url** *(string) --* Use URL (Url) to specify the SPEKE-compliant server that will provide keys for content.
                          
                          - **FragmentLength** *(integer) --* Use Fragment length (FragmentLength) to specify the mp4 fragment sizes in seconds. Fragment length must be compatible with GOP size and framerate.
                          
                          - **ManifestEncoding** *(string) --* Use Manifest encoding (MsSmoothManifestEncoding) to specify the encoding format for the server and client manifest. Valid options are utf8 and utf16.
                      
                        - **Type** *(string) --* Type of output group (File group, Apple HLS, DASH ISO, Microsoft Smooth Streaming, CMAF)
                    
                      - **Outputs** *(list) --* This object holds groups of encoding settings, one group of settings per output.
                        
                        - *(dict) --* An output object describes the settings for a single output file or stream in an output group.
                          
                          - **AudioDescriptions** *(list) --* (AudioDescriptions) contains groups of audio encoding settings organized by audio codec. Include one instance of (AudioDescriptions) per output. (AudioDescriptions) can contain multiple groups of encoding settings.
                            
                            - *(dict) --* Description of audio output
                              
                              - **AudioNormalizationSettings** *(dict) --* Advanced audio normalization settings.
                                
                                - **Algorithm** *(string) --* Audio normalization algorithm to use. 1770-1 conforms to the CALM Act specification, 1770-2 conforms to the EBU R-128 specification.
                                
                                - **AlgorithmControl** *(string) --* When enabled the output audio is corrected using the chosen algorithm. If disabled, the audio will be measured but not adjusted.
                                
                                - **CorrectionGateLevel** *(integer) --* Content measuring above this level will be corrected to the target level. Content measuring below this level will not be corrected. Gating only applies when not using real_time_correction.
                                
                                - **LoudnessLogging** *(string) --* If set to LOG, log each output\'s audio track loudness to a CSV file.
                                
                                - **PeakCalculation** *(string) --* If set to TRUE_PEAK, calculate and log the TruePeak for each output\'s audio track loudness.
                                
                                - **TargetLkfs** *(float) --* Target LKFS(loudness) to adjust volume to. If no value is entered, a default value will be used according to the chosen algorithm. The CALM Act (1770-1) recommends a target of -24 LKFS. The EBU R-128 specification (1770-2) recommends a target of -23 LKFS.
                            
                              - **AudioSourceName** *(string) --* Specifies which audio data to use from each input. In the simplest case, specify an \"Audio Selector\":#inputs-audio_selector by name based on its order within each input. For example if you specify \"Audio Selector 3\", then the third audio selector will be used from each input. If an input does not have an \"Audio Selector 3\", then the audio selector marked as \"default\" in that input will be used. If there is no audio selector marked as \"default\", silence will be inserted for the duration of that input. Alternatively, an \"Audio Selector Group\":#inputs-audio_selector_group name may be specified, with similar default/silence behavior. If no audio_source_name is specified, then \"Audio Selector 1\" will be chosen automatically.
                              
                              - **AudioType** *(integer) --* Applies only if Follow Input Audio Type is unchecked (false). A number between 0 and 255. The following are defined in ISO-IEC 13818-1: 0 = Undefined, 1 = Clean Effects, 2 = Hearing Impaired, 3 = Visually Impaired Commentary, 4-255 = Reserved.
                              
                              - **AudioTypeControl** *(string) --* When set to FOLLOW_INPUT, if the input contains an ISO 639 audio_type, then that value is passed through to the output. If the input contains no ISO 639 audio_type, the value in Audio Type is included in the output. Otherwise the value in Audio Type is included in the output. Note that this field and audioType are both ignored if audioDescriptionBroadcasterMix is set to BROADCASTER_MIXED_AD.
                              
                              - **CodecSettings** *(dict) --* Audio codec settings (CodecSettings) under (AudioDescriptions) contains the group of settings related to audio encoding. The settings in this group vary depending on the value you choose for Audio codec (Codec). For each codec enum you choose, define the corresponding settings object. The following lists the codec enum, settings object pairs. * AAC, AacSettings * MP2, Mp2Settings * WAV, WavSettings * AIFF, AiffSettings * AC3, Ac3Settings * EAC3, Eac3Settings
                                
                                - **AacSettings** *(dict) --* Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the value AAC. The service accepts one of two mutually exclusive groups of AAC settings--VBR and CBR. To select one of these modes, set the value of Bitrate control mode (rateControlMode) to \"VBR\" or \"CBR\". In VBR mode, you control the audio quality with the setting VBR quality (vbrQuality). In CBR mode, you use the setting Bitrate (bitrate). Defaults and valid values depend on the rate control mode.
                                  
                                  - **AudioDescriptionBroadcasterMix** *(string) --* Choose BROADCASTER_MIXED_AD when the input contains pre-mixed main audio + audio description (AD) as a stereo pair. The value for AudioType will be set to 3, which signals to downstream systems that this stream contains \"broadcaster mixed AD\". Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. When you choose BROADCASTER_MIXED_AD, the encoder ignores any values you provide in AudioType and FollowInputAudioType. Choose NORMAL when the input does not contain pre-mixed audio + audio description (AD). In this case, the encoder will use any values you provide for AudioType and FollowInputAudioType.
                                  
                                  - **Bitrate** *(integer) --* Average bitrate in bits/second. Defaults and valid values depend on rate control mode and profile.
                                  
                                  - **CodecProfile** *(string) --* AAC Profile.
                                  
                                  - **CodingMode** *(string) --* Mono (Audio Description), Mono, Stereo, or 5.1 channel layout. Valid values depend on rate control mode and profile. \"1.0 - Audio Description (Receiver Mix)\" setting receives a stereo description plus control track and emits a mono AAC encode of the description track, with control data emitted in the PES header as per ETSI TS 101 154 Annex E.
                                  
                                  - **RateControlMode** *(string) --* Rate Control Mode.
                                  
                                  - **RawFormat** *(string) --* Enables LATM/LOAS AAC output. Note that if you use LATM/LOAS AAC in an output, you must choose \"No container\" for the output container.
                                  
                                  - **SampleRate** *(integer) --* Sample rate in Hz. Valid values depend on rate control mode and profile.
                                  
                                  - **Specification** *(string) --* Use MPEG-2 AAC instead of MPEG-4 AAC audio for raw or MPEG-2 Transport Stream containers.
                                  
                                  - **VbrQuality** *(string) --* VBR Quality Level - Only used if rate_control_mode is VBR.
                              
                                - **Ac3Settings** *(dict) --* Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the value AC3.
                                  
                                  - **Bitrate** *(integer) --* Average bitrate in bits/second. Valid bitrates depend on the coding mode.
                                  
                                  - **BitstreamMode** *(string) --* Specifies the \"Bitstream Mode\" (bsmod) for the emitted AC-3 stream. See ATSC A/52-2012 for background on these values.
                                  
                                  - **CodingMode** *(string) --* Dolby Digital coding mode. Determines number of channels.
                                  
                                  - **Dialnorm** *(integer) --* Sets the dialnorm for the output. If blank and input audio is Dolby Digital, dialnorm will be passed through.
                                  
                                  - **DynamicRangeCompressionProfile** *(string) --* If set to FILM_STANDARD, adds dynamic range compression signaling to the output bitstream as defined in the Dolby Digital specification.
                                  
                                  - **LfeFilter** *(string) --* Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3_2_LFE coding mode.
                                  
                                  - **MetadataControl** *(string) --* When set to FOLLOW_INPUT, encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.
                                  
                                  - **SampleRate** *(integer) --* Sample rate in hz. Sample rate is always 48000.
                              
                                - **AiffSettings** *(dict) --* Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the value AIFF.
                                  
                                  - **BitDepth** *(integer) --* Specify Bit depth (BitDepth), in bits per sample, to choose the encoding quality for this audio track.
                                  
                                  - **Channels** *(integer) --* Set Channels to specify the number of channels in this output audio track. Choosing Mono in the console will give you 1 output channel; choosing Stereo will give you 2. In the API, valid values are 1 and 2.
                                  
                                  - **SampleRate** *(integer) --* Sample rate in hz.
                              
                                - **Codec** *(string) --* Type of Audio codec.
                                
                                - **Eac3Settings** *(dict) --* Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the value EAC3.
                                  
                                  - **AttenuationControl** *(string) --* If set to ATTENUATE_3_DB, applies a 3 dB attenuation to the surround channels. Only used for 3/2 coding mode.
                                  
                                  - **Bitrate** *(integer) --* Average bitrate in bits/second. Valid bitrates depend on the coding mode.
                                  
                                  - **BitstreamMode** *(string) --* Specifies the \"Bitstream Mode\" (bsmod) for the emitted E-AC-3 stream. See ATSC A/52-2012 (Annex E) for background on these values.
                                  
                                  - **CodingMode** *(string) --* Dolby Digital Plus coding mode. Determines number of channels.
                                  
                                  - **DcFilter** *(string) --* Activates a DC highpass filter for all input channels.
                                  
                                  - **Dialnorm** *(integer) --* Sets the dialnorm for the output. If blank and input audio is Dolby Digital Plus, dialnorm will be passed through.
                                  
                                  - **DynamicRangeCompressionLine** *(string) --* Enables Dynamic Range Compression that restricts the absolute peak level for a signal.
                                  
                                  - **DynamicRangeCompressionRf** *(string) --* Enables Heavy Dynamic Range Compression, ensures that the instantaneous signal peaks do not exceed specified levels.
                                  
                                  - **LfeControl** *(string) --* When encoding 3/2 audio, controls whether the LFE channel is enabled
                                  
                                  - **LfeFilter** *(string) --* Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3_2_LFE coding mode.
                                  
                                  - **LoRoCenterMixLevel** *(float) --* Left only/Right only center mix level. Only used for 3/2 coding mode. Valid values: 3.0, 1.5, 0.0, -1.5 -3.0 -4.5 -6.0 -60
                                  
                                  - **LoRoSurroundMixLevel** *(float) --* Left only/Right only surround mix level. Only used for 3/2 coding mode. Valid values: -1.5 -3.0 -4.5 -6.0 -60
                                  
                                  - **LtRtCenterMixLevel** *(float) --* Left total/Right total center mix level. Only used for 3/2 coding mode. Valid values: 3.0, 1.5, 0.0, -1.5 -3.0 -4.5 -6.0 -60
                                  
                                  - **LtRtSurroundMixLevel** *(float) --* Left total/Right total surround mix level. Only used for 3/2 coding mode. Valid values: -1.5 -3.0 -4.5 -6.0 -60
                                  
                                  - **MetadataControl** *(string) --* When set to FOLLOW_INPUT, encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.
                                  
                                  - **PassthroughControl** *(string) --* When set to WHEN_POSSIBLE, input DD+ audio will be passed through if it is present on the input. this detection is dynamic over the life of the transcode. Inputs that alternate between DD+ and non-DD+ content will have a consistent DD+ output as the system alternates between passthrough and encoding.
                                  
                                  - **PhaseControl** *(string) --* Controls the amount of phase-shift applied to the surround channels. Only used for 3/2 coding mode.
                                  
                                  - **SampleRate** *(integer) --* Sample rate in hz. Sample rate is always 48000.
                                  
                                  - **StereoDownmix** *(string) --* Stereo downmix preference. Only used for 3/2 coding mode.
                                  
                                  - **SurroundExMode** *(string) --* When encoding 3/2 audio, sets whether an extra center back surround channel is matrix encoded into the left and right surround channels.
                                  
                                  - **SurroundMode** *(string) --* When encoding 2/0 audio, sets whether Dolby Surround is matrix encoded into the two channels.
                              
                                - **Mp2Settings** *(dict) --* Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the value MP2.
                                  
                                  - **Bitrate** *(integer) --* Average bitrate in bits/second.
                                  
                                  - **Channels** *(integer) --* Set Channels to specify the number of channels in this output audio track. Choosing Mono in the console will give you 1 output channel; choosing Stereo will give you 2. In the API, valid values are 1 and 2.
                                  
                                  - **SampleRate** *(integer) --* Sample rate in hz.
                              
                                - **WavSettings** *(dict) --* Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the value WAV.
                                  
                                  - **BitDepth** *(integer) --* Specify Bit depth (BitDepth), in bits per sample, to choose the encoding quality for this audio track.
                                  
                                  - **Channels** *(integer) --* Set Channels to specify the number of channels in this output audio track. With WAV, valid values 1, 2, 4, and 8. In the console, these values are Mono, Stereo, 4-Channel, and 8-Channel, respectively.
                                  
                                  - **Format** *(string) --* The service defaults to using RIFF for WAV outputs. If your output audio is likely to exceed 4 GB in file size, or if you otherwise need the extended support of the RF64 format, set your output WAV file format to RF64.
                                  
                                  - **SampleRate** *(integer) --* Sample rate in Hz.
                              
                              - **CustomLanguageCode** *(string) --* Specify the language for this audio output track, using the ISO 639-2 or ISO 639-3 three-letter language code. The language specified will be used when \'Follow Input Language Code\' is not selected or when \'Follow Input Language Code\' is selected but there is no ISO 639 language code specified by the input.
                              
                              - **LanguageCode** *(string) --* Indicates the language of the audio output track. The ISO 639 language specified in the \'Language Code\' drop down will be used when \'Follow Input Language Code\' is not selected or when \'Follow Input Language Code\' is selected but there is no ISO 639 language code specified by the input.
                              
                              - **LanguageCodeControl** *(string) --* Choosing FOLLOW_INPUT will cause the ISO 639 language code of the output to follow the ISO 639 language code of the input. The language specified for languageCode\' will be used when USE_CONFIGURED is selected or when FOLLOW_INPUT is selected but there is no ISO 639 language code specified by the input.
                              
                              - **RemixSettings** *(dict) --* Advanced audio remixing settings.
                                
                                - **ChannelMapping** *(dict) --* Channel mapping (ChannelMapping) contains the group of fields that hold the remixing value for each channel. Units are in dB. Acceptable values are within the range from -60 (mute) through 6. A setting of 0 passes the input channel unchanged to the output channel (no attenuation or amplification).
                                  
                                  - **OutputChannels** *(list) --* List of output channels
                                    
                                    - *(dict) --* OutputChannel mapping settings.
                                      
                                      - **InputChannels** *(list) --* List of input channels
                                        
                                        - *(integer) --* 
                                    
                                - **ChannelsIn** *(integer) --* Specify the number of audio channels from your input that you want to use in your output. With remixing, you might combine or split the data in these channels, so the number of channels in your final output might be different.
                                
                                - **ChannelsOut** *(integer) --* Specify the number of channels in this output after remixing. Valid values: 1, 2, 4, 6, 8
                            
                              - **StreamName** *(string) --* Used for MS Smooth and Apple HLS outputs. Indicates the name displayed by the player (eg. English, or Director Commentary). Alphanumeric characters, spaces, and underscore are legal.
                          
                          - **CaptionDescriptions** *(list) --* (CaptionDescriptions) contains groups of captions settings. For each output that has captions, include one instance of (CaptionDescriptions). (CaptionDescriptions) can contain multiple groups of captions settings.
                            
                            - *(dict) --* Description of Caption output
                              
                              - **CaptionSelectorName** *(string) --* Specifies which \"Caption Selector\":#inputs-caption_selector to use from each input when generating captions. The name should be of the format \"Caption Selector \", which denotes that the Nth Caption Selector will be used from each input.
                              
                              - **CustomLanguageCode** *(string) --* Indicates the language of the caption output track, using the ISO 639-2 or ISO 639-3 three-letter language code
                              
                              - **DestinationSettings** *(dict) --* Specific settings required by destination type. Note that burnin_destination_settings are not available if the source of the caption data is Embedded or Teletext.
                                
                                - **BurninDestinationSettings** *(dict) --* Burn-In Destination Settings.
                                  
                                  - **Alignment** *(string) --* If no explicit x_position or y_position is provided, setting alignment to centered will place the captions at the bottom center of the output. Similarly, setting a left alignment will align captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **BackgroundColor** *(string) --* Specifies the color of the rectangle behind the captions. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **BackgroundOpacity** *(integer) --* Specifies the opacity of the background rectangle. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
                                  
                                  - **FontColor** *(string) --* Specifies the color of the burned-in captions. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **FontOpacity** *(integer) --* Specifies the opacity of the burned-in captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **FontResolution** *(integer) --* Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **FontSize** *(integer) --* A positive integer indicates the exact font size in points. Set to 0 for automatic font size selection. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **OutlineColor** *(string) --* Specifies font outline color. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **OutlineSize** *(integer) --* Specifies font outline size in pixels. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **ShadowColor** *(string) --* Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **ShadowOpacity** *(integer) --* Specifies the opacity of the shadow. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
                                  
                                  - **ShadowXOffset** *(integer) --* Specifies the horizontal offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **ShadowYOffset** *(integer) --* Specifies the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **TeletextSpacing** *(string) --* Only applies to jobs with input captions in Teletext or STL formats. Specify whether the spacing between letters in your captions is set by the captions grid or varies depending on letter width. Choose fixed grid to conform to the spacing specified in the captions file more accurately. Choose proportional to make the text easier to read if the captions are closed caption.
                                  
                                  - **XPosition** *(integer) --* Specifies the horizontal position of the caption relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit x_position is provided, the horizontal caption position will be determined by the alignment parameter. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **YPosition** *(integer) --* Specifies the vertical position of the caption relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit y_position is provided, the caption will be positioned towards the bottom of the output. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                              
                                - **DestinationType** *(string) --* Type of Caption output, including Burn-In, Embedded, SCC, SRT, TTML, WebVTT, DVB-Sub, Teletext.
                                
                                - **DvbSubDestinationSettings** *(dict) --* DVB-Sub Destination Settings
                                  
                                  - **Alignment** *(string) --* If no explicit x_position or y_position is provided, setting alignment to centered will place the captions at the bottom center of the output. Similarly, setting a left alignment will align captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **BackgroundColor** *(string) --* Specifies the color of the rectangle behind the captions. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **BackgroundOpacity** *(integer) --* Specifies the opacity of the background rectangle. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
                                  
                                  - **FontColor** *(string) --* Specifies the color of the burned-in captions. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **FontOpacity** *(integer) --* Specifies the opacity of the burned-in captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **FontResolution** *(integer) --* Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **FontSize** *(integer) --* A positive integer indicates the exact font size in points. Set to 0 for automatic font size selection. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **OutlineColor** *(string) --* Specifies font outline color. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **OutlineSize** *(integer) --* Specifies font outline size in pixels. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **ShadowColor** *(string) --* Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **ShadowOpacity** *(integer) --* Specifies the opacity of the shadow. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
                                  
                                  - **ShadowXOffset** *(integer) --* Specifies the horizontal offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **ShadowYOffset** *(integer) --* Specifies the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **TeletextSpacing** *(string) --* Only applies to jobs with input captions in Teletext or STL formats. Specify whether the spacing between letters in your captions is set by the captions grid or varies depending on letter width. Choose fixed grid to conform to the spacing specified in the captions file more accurately. Choose proportional to make the text easier to read if the captions are closed caption.
                                  
                                  - **XPosition** *(integer) --* Specifies the horizontal position of the caption relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit x_position is provided, the horizontal caption position will be determined by the alignment parameter. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **YPosition** *(integer) --* Specifies the vertical position of the caption relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit y_position is provided, the caption will be positioned towards the bottom of the output. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                              
                                - **SccDestinationSettings** *(dict) --* Settings for SCC caption output.
                                  
                                  - **Framerate** *(string) --* Set Framerate (SccDestinationFramerate) to make sure that the captions and the video are synchronized in the output. Specify a framerate that matches the framerate of the associated video. If the video framerate is 29.97, choose 29.97 dropframe (FRAMERATE_29_97_DROPFRAME) only if the video has video_insertion=true and drop_frame_timecode=true; otherwise, choose 29.97 non-dropframe (FRAMERATE_29_97_NON_DROPFRAME).
                              
                                - **TeletextDestinationSettings** *(dict) --* Settings for Teletext caption output
                                  
                                  - **PageNumber** *(string) --* Set pageNumber to the Teletext page number for the destination captions for this output. This value must be a three-digit hexadecimal string; strings ending in -FF are invalid. If you are passing through the entire set of Teletext data, do not use this field.
                              
                                - **TtmlDestinationSettings** *(dict) --* Settings specific to TTML caption outputs, including Pass style information (TtmlStylePassthrough).
                                  
                                  - **StylePassthrough** *(string) --* Pass through style and position information from a TTML-like input source (TTML, SMPTE-TT, CFF-TT) to the CFF-TT output or TTML output.
                              
                              - **LanguageCode** *(string) --* Indicates the language of the caption output track.
                              
                              - **LanguageDescription** *(string) --* Human readable information to indicate captions available for players (eg. English, or Spanish). Alphanumeric characters, spaces, and underscore are legal.
                          
                          - **ContainerSettings** *(dict) --* Container specific settings.
                            
                            - **Container** *(string) --* Container for this output. Some containers require a container settings object. If not specified, the default object will be created.
                            
                            - **F4vSettings** *(dict) --* Settings for F4v container
                              
                              - **MoovPlacement** *(string) --* If set to PROGRESSIVE_DOWNLOAD, the MOOV atom is relocated to the beginning of the archive as required for progressive downloading. Otherwise it is placed normally at the end.
                          
                            - **M2tsSettings** *(dict) --* Settings for M2TS Container.
                              
                              - **AudioBufferModel** *(string) --* Selects between the DVB and ATSC buffer models for Dolby Digital audio.
                              
                              - **AudioFramesPerPes** *(integer) --* The number of audio frames to insert for each PES packet.
                              
                              - **AudioPids** *(list) --* Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation.
                                
                                - *(integer) --* 
                            
                              - **Bitrate** *(integer) --* The output bitrate of the transport stream in bits per second. Setting to 0 lets the muxer automatically determine the appropriate bitrate. Other common values are 3750000, 7500000, and 15000000.
                              
                              - **BufferModel** *(string) --* Controls what buffer model to use for accurate interleaving. If set to MULTIPLEX, use multiplex buffer model. If set to NONE, this can lead to lower latency, but low-memory devices may not be able to play back the stream without interruptions.
                              
                              - **DvbNitSettings** *(dict) --* Inserts DVB Network Information Table (NIT) at the specified table repetition interval.
                                
                                - **NetworkId** *(integer) --* The numeric value placed in the Network Information Table (NIT).
                                
                                - **NetworkName** *(string) --* The network name text placed in the network_name_descriptor inside the Network Information Table. Maximum length is 256 characters.
                                
                                - **NitInterval** *(integer) --* The number of milliseconds between instances of this table in the output transport stream.
                            
                              - **DvbSdtSettings** *(dict) --* Inserts DVB Service Description Table (NIT) at the specified table repetition interval.
                                
                                - **OutputSdt** *(string) --* Selects method of inserting SDT information into output stream. \"Follow input SDT\" copies SDT information from input stream to output stream. \"Follow input SDT if present\" copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. Enter \"SDT Manually\" means user will enter the SDT information. \"No SDT\" means output stream will not contain SDT information.
                                
                                - **SdtInterval** *(integer) --* The number of milliseconds between instances of this table in the output transport stream.
                                
                                - **ServiceName** *(string) --* The service name placed in the service_descriptor in the Service Description Table. Maximum length is 256 characters.
                                
                                - **ServiceProviderName** *(string) --* The service provider name placed in the service_descriptor in the Service Description Table. Maximum length is 256 characters.
                            
                              - **DvbSubPids** *(list) --* Packet Identifier (PID) for input source DVB Subtitle data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation.
                                
                                - *(integer) --* 
                            
                              - **DvbTdtSettings** *(dict) --* Inserts DVB Time and Date Table (TDT) at the specified table repetition interval.
                                
                                - **TdtInterval** *(integer) --* The number of milliseconds between instances of this table in the output transport stream.
                            
                              - **DvbTeletextPid** *(integer) --* Packet Identifier (PID) for input source DVB Teletext data to this output.
                              
                              - **EbpAudioInterval** *(string) --* When set to VIDEO_AND_FIXED_INTERVALS, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. When set to VIDEO_INTERVAL, these additional markers will not be inserted. Only applicable when EBP segmentation markers are is selected (segmentationMarkers is EBP or EBP_LEGACY).
                              
                              - **EbpPlacement** *(string) --* Selects which PIDs to place EBP markers on. They can either be placed only on the video PID, or on both the video PID and all audio PIDs. Only applicable when EBP segmentation markers are is selected (segmentationMarkers is EBP or EBP_LEGACY).
                              
                              - **EsRateInPes** *(string) --* Controls whether to include the ES Rate field in the PES header.
                              
                              - **FragmentTime** *(float) --* The length in seconds of each fragment. Only used with EBP markers.
                              
                              - **MaxPcrInterval** *(integer) --* Maximum time in milliseconds between Program Clock References (PCRs) inserted into the transport stream.
                              
                              - **MinEbpInterval** *(integer) --* When set, enforces that Encoder Boundary Points do not come within the specified time interval of each other by looking ahead at input video. If another EBP is going to come in within the specified time interval, the current EBP is not emitted, and the segment is \"stretched\" to the next marker. The lookahead value does not add latency to the system. The Live Event must be configured elsewhere to create sufficient latency to make the lookahead accurate.
                              
                              - **NielsenId3** *(string) --* If INSERT, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.
                              
                              - **NullPacketBitrate** *(float) --* Value in bits per second of extra null packets to insert into the transport stream. This can be used if a downstream encryption system requires periodic null packets.
                              
                              - **PatInterval** *(integer) --* The number of milliseconds between instances of this table in the output transport stream.
                              
                              - **PcrControl** *(string) --* When set to PCR_EVERY_PES_PACKET, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This is effective only when the PCR PID is the same as the video or audio elementary stream.
                              
                              - **PcrPid** *(integer) --* Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID.
                              
                              - **PmtInterval** *(integer) --* The number of milliseconds between instances of this table in the output transport stream.
                              
                              - **PmtPid** *(integer) --* Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream.
                              
                              - **PrivateMetadataPid** *(integer) --* Packet Identifier (PID) of the private metadata stream in the transport stream.
                              
                              - **ProgramNumber** *(integer) --* The value of the program number field in the Program Map Table.
                              
                              - **RateMode** *(string) --* When set to CBR, inserts null packets into transport stream to fill specified bitrate. When set to VBR, the bitrate setting acts as the maximum bitrate, but the output will not be padded up to that bitrate.
                              
                              - **Scte35Pid** *(integer) --* Packet Identifier (PID) of the SCTE-35 stream in the transport stream.
                              
                              - **Scte35Source** *(string) --* Enables SCTE-35 passthrough (scte35Source) to pass any SCTE-35 signals from input to output.
                              
                              - **SegmentationMarkers** *(string) --* Inserts segmentation markers at each segmentation_time period. rai_segstart sets the Random Access Indicator bit in the adaptation field. rai_adapt sets the RAI bit and adds the current timecode in the private data bytes. psi_segstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebp_legacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format.
                              
                              - **SegmentationStyle** *(string) --* The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of \"reset_cadence\" is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of of $segmentation_time seconds. When a segmentation style of \"maintain_cadence\" is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentation_time seconds. Note that EBP lookahead is a slight exception to this rule.
                              
                              - **SegmentationTime** *(float) --* The length in seconds of each segment. Required unless markers is set to _none_.
                              
                              - **TimedMetadataPid** *(integer) --* Packet Identifier (PID) of the timed metadata stream in the transport stream.
                              
                              - **TransportStreamId** *(integer) --* The value of the transport stream ID field in the Program Map Table.
                              
                              - **VideoPid** *(integer) --* Packet Identifier (PID) of the elementary video stream in the transport stream.
                          
                            - **M3u8Settings** *(dict) --* Settings for TS segments in HLS
                              
                              - **AudioFramesPerPes** *(integer) --* The number of audio frames to insert for each PES packet.
                              
                              - **AudioPids** *(list) --* Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation.
                                
                                - *(integer) --* 
                            
                              - **NielsenId3** *(string) --* If INSERT, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.
                              
                              - **PatInterval** *(integer) --* The number of milliseconds between instances of this table in the output transport stream.
                              
                              - **PcrControl** *(string) --* When set to PCR_EVERY_PES_PACKET a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.
                              
                              - **PcrPid** *(integer) --* Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID.
                              
                              - **PmtInterval** *(integer) --* The number of milliseconds between instances of this table in the output transport stream.
                              
                              - **PmtPid** *(integer) --* Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream.
                              
                              - **PrivateMetadataPid** *(integer) --* Packet Identifier (PID) of the private metadata stream in the transport stream.
                              
                              - **ProgramNumber** *(integer) --* The value of the program number field in the Program Map Table.
                              
                              - **Scte35Pid** *(integer) --* Packet Identifier (PID) of the SCTE-35 stream in the transport stream.
                              
                              - **Scte35Source** *(string) --* Enables SCTE-35 passthrough (scte35Source) to pass any SCTE-35 signals from input to output.
                              
                              - **TimedMetadata** *(string) --* Applies only to HLS outputs. Use this setting to specify whether the service inserts the ID3 timed metadata from the input in this output.
                              
                              - **TimedMetadataPid** *(integer) --* Packet Identifier (PID) of the timed metadata stream in the transport stream.
                              
                              - **TransportStreamId** *(integer) --* The value of the transport stream ID field in the Program Map Table.
                              
                              - **VideoPid** *(integer) --* Packet Identifier (PID) of the elementary video stream in the transport stream.
                          
                            - **MovSettings** *(dict) --* Settings for MOV Container.
                              
                              - **ClapAtom** *(string) --* When enabled, include \'clap\' atom if appropriate for the video output settings.
                              
                              - **CslgAtom** *(string) --* When enabled, file composition times will start at zero, composition times in the \'ctts\' (composition time to sample) box for B-frames will be negative, and a \'cslg\' (composition shift least greatest) box will be included per 14496-1 amendment 1. This improves compatibility with Apple players and tools.
                              
                              - **Mpeg2FourCCControl** *(string) --* When set to XDCAM, writes MPEG2 video streams into the QuickTime file using XDCAM fourcc codes. This increases compatibility with Apple editors and players, but may decrease compatibility with other players. Only applicable when the video codec is MPEG2.
                              
                              - **PaddingControl** *(string) --* If set to OMNEON, inserts Omneon-compatible padding
                              
                              - **Reference** *(string) --* A value of \'external\' creates separate media files and the wrapper file (.mov) contains references to these media files. A value of \'self_contained\' creates only a wrapper (.mov) file and this file contains all of the media.
                          
                            - **Mp4Settings** *(dict) --* Settings for MP4 Container
                              
                              - **CslgAtom** *(string) --* When enabled, file composition times will start at zero, composition times in the \'ctts\' (composition time to sample) box for B-frames will be negative, and a \'cslg\' (composition shift least greatest) box will be included per 14496-1 amendment 1. This improves compatibility with Apple players and tools.
                              
                              - **FreeSpaceBox** *(string) --* Inserts a free-space box immediately after the moov box.
                              
                              - **MoovPlacement** *(string) --* If set to PROGRESSIVE_DOWNLOAD, the MOOV atom is relocated to the beginning of the archive as required for progressive downloading. Otherwise it is placed normally at the end.
                              
                              - **Mp4MajorBrand** *(string) --* Overrides the \"Major Brand\" field in the output file. Usually not necessary to specify.
                          
                          - **Extension** *(string) --* Use Extension (Extension) to specify the file extension for outputs in File output groups. If you do not specify a value, the service will use default extensions by container type as follows * MPEG-2 transport stream, m2ts * Quicktime, mov * MXF container, mxf * MPEG-4 container, mp4 * No Container, the service will use codec extensions (e.g. AAC, H265, H265, AC3)
                          
                          - **NameModifier** *(string) --* Use Name modifier (NameModifier) to have the service add a string to the end of each output filename. You specify the base filename as part of your destination URI. When you create multiple outputs in the same output group, Name modifier (NameModifier) is required. Name modifier also accepts format identifiers. For DASH ISO outputs, if you use the format identifiers $Number$ or $Time$ in one output, you must use them in the same way in all outputs of the output group.
                          
                          - **OutputSettings** *(dict) --* Specific settings for this type of output.
                            
                            - **HlsSettings** *(dict) --* Settings for HLS output groups
                              
                              - **AudioGroupId** *(string) --* Specifies the group to which the audio Rendition belongs.
                              
                              - **AudioRenditionSets** *(string) --* List all the audio groups that are used with the video output stream. Input all the audio GROUP-IDs that are associated to the video, separate by \',\'.
                              
                              - **AudioTrackType** *(string) --* Four types of audio-only tracks are supported: Audio-Only Variant Stream The client can play back this audio-only stream instead of video in low-bandwidth scenarios. Represented as an EXT-X-STREAM-INF in the HLS manifest. Alternate Audio, Auto Select, Default Alternate rendition that the client should try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=YES, AUTOSELECT=YES Alternate Audio, Auto Select, Not Default Alternate rendition that the client may try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=YES Alternate Audio, not Auto Select Alternate rendition that the client will not try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=NO
                              
                              - **IFrameOnlyManifest** *(string) --* When set to INCLUDE, writes I-Frame Only Manifest in addition to the HLS manifest
                              
                              - **SegmentModifier** *(string) --* String concatenated to end of segment filenames. Accepts \"Format Identifiers\":#format_identifier_parameters.
                          
                          - **Preset** *(string) --* Use Preset (Preset) to specifiy a preset for your transcoding settings. Provide the system or custom preset name. You can specify either Preset (Preset) or Container settings (ContainerSettings), but not both.
                          
                          - **VideoDescription** *(dict) --* (VideoDescription) contains a group of video encoding settings. The specific video settings depend on the video codec you choose when you specify a value for Video codec (codec). Include one instance of (VideoDescription) per output.
                            
                            - **AfdSignaling** *(string) --* This setting only applies to H.264 and MPEG2 outputs. Use Insert AFD signaling (AfdSignaling) to specify whether the service includes AFD values in the output video data and what those values are. * Choose None to remove all AFD values from this output. * Choose Fixed to ignore input AFD values and instead encode the value specified in the job. * Choose Auto to calculate output AFD values based on the input AFD scaler data.
                            
                            - **AntiAlias** *(string) --* Enable Anti-alias (AntiAlias) to enhance sharp edges in video output when your input resolution is much larger than your output resolution. Default is enabled.
                            
                            - **CodecSettings** *(dict) --* Video codec settings, (CodecSettings) under (VideoDescription), contains the group of settings related to video encoding. The settings in this group vary depending on the value you choose for Video codec (Codec). For each codec enum you choose, define the corresponding settings object. The following lists the codec enum, settings object pairs. * H_264, H264Settings * H_265, H265Settings * MPEG2, Mpeg2Settings * PRORES, ProresSettings * FRAME_CAPTURE, FrameCaptureSettings
                              
                              - **Codec** *(string) --* Type of video codec
                              
                              - **FrameCaptureSettings** *(dict) --* Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the value FRAME_CAPTURE.
                                
                                - **FramerateDenominator** *(integer) --* Frame capture will encode the first frame of the output stream, then one frame every framerateDenominator/framerateNumerator seconds. For example, settings of framerateNumerator = 1 and framerateDenominator = 3 (a rate of 1/3 frame per second) will capture the first frame, then 1 frame every 3s. Files will be named as filename.n.jpg where n is the 0-based sequence number of each Capture.
                                
                                - **FramerateNumerator** *(integer) --* Frame capture will encode the first frame of the output stream, then one frame every framerateDenominator/framerateNumerator seconds. For example, settings of framerateNumerator = 1 and framerateDenominator = 3 (a rate of 1/3 frame per second) will capture the first frame, then 1 frame every 3s. Files will be named as filename.NNNNNNN.jpg where N is the 0-based frame sequence number zero padded to 7 decimal places.
                                
                                - **MaxCaptures** *(integer) --* Maximum number of captures (encoded jpg output files).
                                
                                - **Quality** *(integer) --* JPEG Quality - a higher value equals higher quality.
                            
                              - **H264Settings** *(dict) --* Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the value H_264.
                                
                                - **AdaptiveQuantization** *(string) --* Adaptive quantization. Allows intra-frame quantizers to vary to improve visual quality.
                                
                                - **Bitrate** *(integer) --* Average bitrate in bits/second. Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique when rounded down to the nearest multiple of 1000.
                                
                                - **CodecLevel** *(string) --* H.264 Level.
                                
                                - **CodecProfile** *(string) --* H.264 Profile. High 4:2:2 and 10-bit profiles are only available with the AVC-I License.
                                
                                - **DynamicSubGop** *(string) --* Choose Adaptive to improve subjective video quality for high-motion content. This will cause the service to use fewer B-frames (which infer information based on other frames) for high-motion portions of the video and more B-frames for low-motion portions. The maximum number of B-frames is limited by the value you provide for the setting B frames between reference frames (numberBFramesBetweenReferenceFrames).
                                
                                - **EntropyEncoding** *(string) --* Entropy encoding mode. Use CABAC (must be in Main or High profile) or CAVLC.
                                
                                - **FieldEncoding** *(string) --* Choosing FORCE_FIELD disables PAFF encoding for interlaced outputs.
                                
                                - **FlickerAdaptiveQuantization** *(string) --* Adjust quantization within each frame to reduce flicker or \'pop\' on I-frames.
                                
                                - **FramerateControl** *(string) --* If you are using the console, use the Framerate setting to specify the framerate for this output. If you want to keep the same framerate as the input video, choose Follow source. If you want to do framerate conversion, choose a framerate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your framerate as a fraction. If you are creating your transcoding job specification as a JSON file without the console, use FramerateControl to specify which value the service uses for the framerate for this output. Choose INITIALIZE_FROM_SOURCE if you want the service to use the framerate from the input. Choose SPECIFIED if you want the service to use the framerate you specify in the settings FramerateNumerator and FramerateDenominator.
                                
                                - **FramerateConversionAlgorithm** *(string) --* When set to INTERPOLATE, produces smoother motion during framerate conversion.
                                
                                - **FramerateDenominator** *(integer) --* When you use the API for transcode jobs that use framerate conversion, specify the framerate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use framerate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.
                                
                                - **FramerateNumerator** *(integer) --* Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps.
                                
                                - **GopBReference** *(string) --* If enable, use reference B frames for GOP structures that have B frames > 1.
                                
                                - **GopClosedCadence** *(integer) --* Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting.
                                
                                - **GopSize** *(float) --* GOP Length (keyframe interval) in frames or seconds. Must be greater than zero.
                                
                                - **GopSizeUnits** *(string) --* Indicates if the GOP Size in H264 is specified in frames or seconds. If seconds the system will convert the GOP Size into a frame count at run time.
                                
                                - **HrdBufferInitialFillPercentage** *(integer) --* Percentage of the buffer that should initially be filled (HRD buffer model).
                                
                                - **HrdBufferSize** *(integer) --* Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000.
                                
                                - **InterlaceMode** *(string) --* Use Interlace mode (InterlaceMode) to choose the scan line type for the output. * Top Field First (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce interlaced output with the entire output having the same field polarity (top or bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow, Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as the source. Therefore, behavior depends on the input scan type, as follows. - If the source is interlaced, the output will be interlaced with the same polarity as the source (it will follow the source). The output could therefore be a mix of \"top field first\" and \"bottom field first\". - If the source is progressive, the output will be interlaced with \"top field first\" or \"bottom field first\" polarity, depending on which of the Follow options you chose.
                                
                                - **MaxBitrate** *(integer) --* Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. Required when Rate control mode is QVBR.
                                
                                - **MinIInterval** *(integer) --* Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. This setting is only used when Scene Change Detect is enabled. Note: Maximum GOP stretch = GOP size + Min-I-interval - 1
                                
                                - **NumberBFramesBetweenReferenceFrames** *(integer) --* Number of B-frames between reference frames.
                                
                                - **NumberReferenceFrames** *(integer) --* Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding.
                                
                                - **ParControl** *(string) --* Using the API, enable ParFollowSource if you want the service to use the pixel aspect ratio from the input. Using the console, do this by choosing Follow source for Pixel aspect ratio.
                                
                                - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.
                                
                                - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.
                                
                                - **QualityTuningLevel** *(string) --* Use Quality tuning level (H264QualityTuningLevel) to specifiy whether to use fast single-pass, high-quality singlepass, or high-quality multipass video encoding.
                                
                                - **QvbrSettings** *(dict) --* Settings for quality-defined variable bitrate encoding with the H.264 codec. Required when you set Rate control mode to QVBR. Not valid when you set Rate control mode to a value other than QVBR, or when you don\'t define Rate control mode.
                                  
                                  - **MaxAverageBitrate** *(integer) --* Use this setting only when Rate control mode is QVBR and Quality tuning level is Multi-pass HQ. For Max average bitrate values suited to the complexity of your input video, the service limits the average bitrate of the video part of this output to the value you choose. That is, the total size of the video element is less than or equal to the value you set multiplied by the number of seconds of encoded output.
                                  
                                  - **QvbrQualityLevel** *(integer) --* Required when you use QVBR rate control mode. That is, when you specify qvbrSettings within h264Settings. Specify the target quality level for this output, from 1 to 10. Use higher numbers for greater quality. Level 10 results in nearly lossless compression. The quality level for most broadcast-quality transcodes is between 6 and 9.
                              
                                - **RateControlMode** *(string) --* Use this setting to specify whether this output has a variable bitrate (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR).
                                
                                - **RepeatPps** *(string) --* Places a PPS header on each encoded picture, even if repeated.
                                
                                - **SceneChangeDetect** *(string) --* Scene change detection (inserts I-frames on scene changes).
                                
                                - **Slices** *(integer) --* Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures.
                                
                                - **SlowPal** *(string) --* Enables Slow PAL rate conversion. 23.976fps and 24fps input is relabeled as 25fps, and audio is sped up correspondingly.
                                
                                - **Softness** *(integer) --* Softness. Selects quantizer matrix, larger values reduce high-frequency content in the encoded image.
                                
                                - **SpatialAdaptiveQuantization** *(string) --* Adjust quantization within each frame based on spatial variation of content complexity.
                                
                                - **Syntax** *(string) --* Produces a bitstream compliant with SMPTE RP-2027.
                                
                                - **Telecine** *(string) --* This field applies only if the Streams > Advanced > Framerate (framerate) field is set to 29.970. This field works with the Streams > Advanced > Preprocessors > Deinterlacer field (deinterlace_mode) and the Streams > Advanced > Interlaced Mode field (interlace_mode) to identify the scan type for the output: Progressive, Interlaced, Hard Telecine or Soft Telecine. - Hard: produces 29.97i output from 23.976 input. - Soft: produces 23.976; the player converts this output to 29.97i.
                                
                                - **TemporalAdaptiveQuantization** *(string) --* Adjust quantization within each frame based on temporal variation of content complexity.
                                
                                - **UnregisteredSeiTimecode** *(string) --* Inserts timecode for each frame as 4 bytes of an unregistered SEI message.
                            
                              - **H265Settings** *(dict) --* Settings for H265 codec
                                
                                - **AdaptiveQuantization** *(string) --* Adaptive quantization. Allows intra-frame quantizers to vary to improve visual quality.
                                
                                - **AlternateTransferFunctionSei** *(string) --* Enables Alternate Transfer Function SEI message for outputs using Hybrid Log Gamma (HLG) Electro-Optical Transfer Function (EOTF).
                                
                                - **Bitrate** *(integer) --* Average bitrate in bits/second. Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique when rounded down to the nearest multiple of 1000.
                                
                                - **CodecLevel** *(string) --* H.265 Level.
                                
                                - **CodecProfile** *(string) --* Represents the Profile and Tier, per the HEVC (H.265) specification. Selections are grouped as [Profile] / [Tier], so \"Main/High\" represents Main Profile with High Tier. 4:2:2 profiles are only available with the HEVC 4:2:2 License.
                                
                                - **DynamicSubGop** *(string) --* Choose Adaptive to improve subjective video quality for high-motion content. This will cause the service to use fewer B-frames (which infer information based on other frames) for high-motion portions of the video and more B-frames for low-motion portions. The maximum number of B-frames is limited by the value you provide for the setting B frames between reference frames (numberBFramesBetweenReferenceFrames).
                                
                                - **FlickerAdaptiveQuantization** *(string) --* Adjust quantization within each frame to reduce flicker or \'pop\' on I-frames.
                                
                                - **FramerateControl** *(string) --* If you are using the console, use the Framerate setting to specify the framerate for this output. If you want to keep the same framerate as the input video, choose Follow source. If you want to do framerate conversion, choose a framerate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your framerate as a fraction. If you are creating your transcoding job sepecification as a JSON file without the console, use FramerateControl to specify which value the service uses for the framerate for this output. Choose INITIALIZE_FROM_SOURCE if you want the service to use the framerate from the input. Choose SPECIFIED if you want the service to use the framerate you specify in the settings FramerateNumerator and FramerateDenominator.
                                
                                - **FramerateConversionAlgorithm** *(string) --* When set to INTERPOLATE, produces smoother motion during framerate conversion.
                                
                                - **FramerateDenominator** *(integer) --* Framerate denominator.
                                
                                - **FramerateNumerator** *(integer) --* Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps.
                                
                                - **GopBReference** *(string) --* If enable, use reference B frames for GOP structures that have B frames > 1.
                                
                                - **GopClosedCadence** *(integer) --* Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting.
                                
                                - **GopSize** *(float) --* GOP Length (keyframe interval) in frames or seconds. Must be greater than zero.
                                
                                - **GopSizeUnits** *(string) --* Indicates if the GOP Size in H265 is specified in frames or seconds. If seconds the system will convert the GOP Size into a frame count at run time.
                                
                                - **HrdBufferInitialFillPercentage** *(integer) --* Percentage of the buffer that should initially be filled (HRD buffer model).
                                
                                - **HrdBufferSize** *(integer) --* Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000.
                                
                                - **InterlaceMode** *(string) --* Use Interlace mode (InterlaceMode) to choose the scan line type for the output. * Top Field First (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce interlaced output with the entire output having the same field polarity (top or bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow, Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as the source. Therefore, behavior depends on the input scan type. - If the source is interlaced, the output will be interlaced with the same polarity as the source (it will follow the source). The output could therefore be a mix of \"top field first\" and \"bottom field first\". - If the source is progressive, the output will be interlaced with \"top field first\" or \"bottom field first\" polarity, depending on which of the Follow options you chose.
                                
                                - **MaxBitrate** *(integer) --* Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. Required when Rate control mode is QVBR.
                                
                                - **MinIInterval** *(integer) --* Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. This setting is only used when Scene Change Detect is enabled. Note: Maximum GOP stretch = GOP size + Min-I-interval - 1
                                
                                - **NumberBFramesBetweenReferenceFrames** *(integer) --* Number of B-frames between reference frames.
                                
                                - **NumberReferenceFrames** *(integer) --* Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding.
                                
                                - **ParControl** *(string) --* Using the API, enable ParFollowSource if you want the service to use the pixel aspect ratio from the input. Using the console, do this by choosing Follow source for Pixel aspect ratio.
                                
                                - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.
                                
                                - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.
                                
                                - **QualityTuningLevel** *(string) --* Use Quality tuning level (H265QualityTuningLevel) to specifiy whether to use fast single-pass, high-quality singlepass, or high-quality multipass video encoding.
                                
                                - **QvbrSettings** *(dict) --* Settings for quality-defined variable bitrate encoding with the H.265 codec. Required when you set Rate control mode to QVBR. Not valid when you set Rate control mode to a value other than QVBR, or when you don\'t define Rate control mode.
                                  
                                  - **MaxAverageBitrate** *(integer) --* Use this setting only when Rate control mode is QVBR and Quality tuning level is Multi-pass HQ. For Max average bitrate values suited to the complexity of your input video, the service limits the average bitrate of the video part of this output to the value you choose. That is, the total size of the video element is less than or equal to the value you set multiplied by the number of seconds of encoded output.
                                  
                                  - **QvbrQualityLevel** *(integer) --* Required when you use QVBR rate control mode. That is, when you specify qvbrSettings within h265Settings. Specify the target quality level for this output, from 1 to 10. Use higher numbers for greater quality. Level 10 results in nearly lossless compression. The quality level for most broadcast-quality transcodes is between 6 and 9.
                              
                                - **RateControlMode** *(string) --* Use this setting to specify whether this output has a variable bitrate (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR).
                                
                                - **SampleAdaptiveOffsetFilterMode** *(string) --* Specify Sample Adaptive Offset (SAO) filter strength. Adaptive mode dynamically selects best strength based on content
                                
                                - **SceneChangeDetect** *(string) --* Scene change detection (inserts I-frames on scene changes).
                                
                                - **Slices** *(integer) --* Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures.
                                
                                - **SlowPal** *(string) --* Enables Slow PAL rate conversion. 23.976fps and 24fps input is relabeled as 25fps, and audio is sped up correspondingly.
                                
                                - **SpatialAdaptiveQuantization** *(string) --* Adjust quantization within each frame based on spatial variation of content complexity.
                                
                                - **Telecine** *(string) --* This field applies only if the Streams > Advanced > Framerate (framerate) field is set to 29.970. This field works with the Streams > Advanced > Preprocessors > Deinterlacer field (deinterlace_mode) and the Streams > Advanced > Interlaced Mode field (interlace_mode) to identify the scan type for the output: Progressive, Interlaced, Hard Telecine or Soft Telecine. - Hard: produces 29.97i output from 23.976 input. - Soft: produces 23.976; the player converts this output to 29.97i.
                                
                                - **TemporalAdaptiveQuantization** *(string) --* Adjust quantization within each frame based on temporal variation of content complexity.
                                
                                - **TemporalIds** *(string) --* Enables temporal layer identifiers in the encoded bitstream. Up to 3 layers are supported depending on GOP structure: I- and P-frames form one layer, reference B-frames can form a second layer and non-reference b-frames can form a third layer. Decoders can optionally decode only the lower temporal layers to generate a lower frame rate output. For example, given a bitstream with temporal IDs and with b-frames = 1 (i.e. IbPbPb display order), a decoder could decode all the frames for full frame rate output or only the I and P frames (lowest temporal layer) for a half frame rate output.
                                
                                - **Tiles** *(string) --* Enable use of tiles, allowing horizontal as well as vertical subdivision of the encoded pictures.
                                
                                - **UnregisteredSeiTimecode** *(string) --* Inserts timecode for each frame as 4 bytes of an unregistered SEI message.
                                
                                - **WriteMp4PackagingType** *(string) --* If HVC1, output that is H.265 will be marked as HVC1 and adhere to the ISO-IECJTC1-SC29_N13798_Text_ISOIEC_FDIS_14496-15_3rd_E spec which states that parameter set NAL units will be stored in the sample headers but not in the samples directly. If HEV1, then H.265 will be marked as HEV1 and parameter set NAL units will be written into the samples.
                            
                              - **Mpeg2Settings** *(dict) --* Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the value MPEG2.
                                
                                - **AdaptiveQuantization** *(string) --* Adaptive quantization. Allows intra-frame quantizers to vary to improve visual quality.
                                
                                - **Bitrate** *(integer) --* Average bitrate in bits/second. Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique when rounded down to the nearest multiple of 1000.
                                
                                - **CodecLevel** *(string) --* Use Level (Mpeg2CodecLevel) to set the MPEG-2 level for the video output.
                                
                                - **CodecProfile** *(string) --* Use Profile (Mpeg2CodecProfile) to set the MPEG-2 profile for the video output.
                                
                                - **DynamicSubGop** *(string) --* Choose Adaptive to improve subjective video quality for high-motion content. This will cause the service to use fewer B-frames (which infer information based on other frames) for high-motion portions of the video and more B-frames for low-motion portions. The maximum number of B-frames is limited by the value you provide for the setting B frames between reference frames (numberBFramesBetweenReferenceFrames).
                                
                                - **FramerateControl** *(string) --* If you are using the console, use the Framerate setting to specify the framerate for this output. If you want to keep the same framerate as the input video, choose Follow source. If you want to do framerate conversion, choose a framerate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your framerate as a fraction. If you are creating your transcoding job sepecification as a JSON file without the console, use FramerateControl to specify which value the service uses for the framerate for this output. Choose INITIALIZE_FROM_SOURCE if you want the service to use the framerate from the input. Choose SPECIFIED if you want the service to use the framerate you specify in the settings FramerateNumerator and FramerateDenominator.
                                
                                - **FramerateConversionAlgorithm** *(string) --* When set to INTERPOLATE, produces smoother motion during framerate conversion.
                                
                                - **FramerateDenominator** *(integer) --* Framerate denominator.
                                
                                - **FramerateNumerator** *(integer) --* Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps.
                                
                                - **GopClosedCadence** *(integer) --* Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting.
                                
                                - **GopSize** *(float) --* GOP Length (keyframe interval) in frames or seconds. Must be greater than zero.
                                
                                - **GopSizeUnits** *(string) --* Indicates if the GOP Size in MPEG2 is specified in frames or seconds. If seconds the system will convert the GOP Size into a frame count at run time.
                                
                                - **HrdBufferInitialFillPercentage** *(integer) --* Percentage of the buffer that should initially be filled (HRD buffer model).
                                
                                - **HrdBufferSize** *(integer) --* Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000.
                                
                                - **InterlaceMode** *(string) --* Use Interlace mode (InterlaceMode) to choose the scan line type for the output. * Top Field First (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce interlaced output with the entire output having the same field polarity (top or bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow, Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as the source. Therefore, behavior depends on the input scan type. - If the source is interlaced, the output will be interlaced with the same polarity as the source (it will follow the source). The output could therefore be a mix of \"top field first\" and \"bottom field first\". - If the source is progressive, the output will be interlaced with \"top field first\" or \"bottom field first\" polarity, depending on which of the Follow options you chose.
                                
                                - **IntraDcPrecision** *(string) --* Use Intra DC precision (Mpeg2IntraDcPrecision) to set quantization precision for intra-block DC coefficients. If you choose the value auto, the service will automatically select the precision based on the per-frame compression ratio.
                                
                                - **MaxBitrate** *(integer) --* Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000.
                                
                                - **MinIInterval** *(integer) --* Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. This setting is only used when Scene Change Detect is enabled. Note: Maximum GOP stretch = GOP size + Min-I-interval - 1
                                
                                - **NumberBFramesBetweenReferenceFrames** *(integer) --* Number of B-frames between reference frames.
                                
                                - **ParControl** *(string) --* Using the API, enable ParFollowSource if you want the service to use the pixel aspect ratio from the input. Using the console, do this by choosing Follow source for Pixel aspect ratio.
                                
                                - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.
                                
                                - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.
                                
                                - **QualityTuningLevel** *(string) --* Use Quality tuning level (Mpeg2QualityTuningLevel) to specifiy whether to use single-pass or multipass video encoding.
                                
                                - **RateControlMode** *(string) --* Use Rate control mode (Mpeg2RateControlMode) to specifiy whether the bitrate is variable (vbr) or constant (cbr).
                                
                                - **SceneChangeDetect** *(string) --* Scene change detection (inserts I-frames on scene changes).
                                
                                - **SlowPal** *(string) --* Enables Slow PAL rate conversion. 23.976fps and 24fps input is relabeled as 25fps, and audio is sped up correspondingly.
                                
                                - **Softness** *(integer) --* Softness. Selects quantizer matrix, larger values reduce high-frequency content in the encoded image.
                                
                                - **SpatialAdaptiveQuantization** *(string) --* Adjust quantization within each frame based on spatial variation of content complexity.
                                
                                - **Syntax** *(string) --* Produces a Type D-10 compatible bitstream (SMPTE 356M-2001).
                                
                                - **Telecine** *(string) --* Only use Telecine (Mpeg2Telecine) when you set Framerate (Framerate) to 29.970. Set Telecine (Mpeg2Telecine) to Hard (hard) to produce a 29.97i output from a 23.976 input. Set it to Soft (soft) to produce 23.976 output and leave converstion to the player.
                                
                                - **TemporalAdaptiveQuantization** *(string) --* Adjust quantization within each frame based on temporal variation of content complexity.
                            
                              - **ProresSettings** *(dict) --* Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the value PRORES.
                                
                                - **CodecProfile** *(string) --* Use Profile (ProResCodecProfile) to specifiy the type of Apple ProRes codec to use for this output.
                                
                                - **FramerateControl** *(string) --* If you are using the console, use the Framerate setting to specify the framerate for this output. If you want to keep the same framerate as the input video, choose Follow source. If you want to do framerate conversion, choose a framerate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your framerate as a fraction. If you are creating your transcoding job sepecification as a JSON file without the console, use FramerateControl to specify which value the service uses for the framerate for this output. Choose INITIALIZE_FROM_SOURCE if you want the service to use the framerate from the input. Choose SPECIFIED if you want the service to use the framerate you specify in the settings FramerateNumerator and FramerateDenominator.
                                
                                - **FramerateConversionAlgorithm** *(string) --* When set to INTERPOLATE, produces smoother motion during framerate conversion.
                                
                                - **FramerateDenominator** *(integer) --* Framerate denominator.
                                
                                - **FramerateNumerator** *(integer) --* When you use the API for transcode jobs that use framerate conversion, specify the framerate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator.
                                
                                - **InterlaceMode** *(string) --* Use Interlace mode (InterlaceMode) to choose the scan line type for the output. * Top Field First (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce interlaced output with the entire output having the same field polarity (top or bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow, Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as the source. Therefore, behavior depends on the input scan type. - If the source is interlaced, the output will be interlaced with the same polarity as the source (it will follow the source). The output could therefore be a mix of \"top field first\" and \"bottom field first\". - If the source is progressive, the output will be interlaced with \"top field first\" or \"bottom field first\" polarity, depending on which of the Follow options you chose.
                                
                                - **ParControl** *(string) --* Use (ProresParControl) to specify how the service determines the pixel aspect ratio. Set to Follow source (INITIALIZE_FROM_SOURCE) to use the pixel aspect ratio from the input. To specify a different pixel aspect ratio: Using the console, choose it from the dropdown menu. Using the API, set ProresParControl to (SPECIFIED) and provide for (ParNumerator) and (ParDenominator).
                                
                                - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.
                                
                                - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.
                                
                                - **SlowPal** *(string) --* Enables Slow PAL rate conversion. 23.976fps and 24fps input is relabeled as 25fps, and audio is sped up correspondingly.
                                
                                - **Telecine** *(string) --* Only use Telecine (ProresTelecine) when you set Framerate (Framerate) to 29.970. Set Telecine (ProresTelecine) to Hard (hard) to produce a 29.97i output from a 23.976 input. Set it to Soft (soft) to produce 23.976 output and leave converstion to the player.
                            
                            - **ColorMetadata** *(string) --* Enable Insert color metadata (ColorMetadata) to include color metadata in this output. This setting is enabled by default.
                            
                            - **Crop** *(dict) --* Applies only if your input aspect ratio is different from your output aspect ratio. Use Input cropping rectangle (Crop) to specify the video area the service will include in the output. This will crop the input source, causing video pixels to be removed on encode. Do not use this setting if you have enabled Stretch to output (stretchToOutput) in your output settings.
                              
                              - **Height** *(integer) --* Height of rectangle in pixels. Specify only even numbers.
                              
                              - **Width** *(integer) --* Width of rectangle in pixels. Specify only even numbers.
                              
                              - **X** *(integer) --* The distance, in pixels, between the rectangle and the left edge of the video frame. Specify only even numbers.
                              
                              - **Y** *(integer) --* The distance, in pixels, between the rectangle and the top edge of the video frame. Specify only even numbers.
                          
                            - **DropFrameTimecode** *(string) --* Applies only to 29.97 fps outputs. When this feature is enabled, the service will use drop-frame timecode on outputs. If it is not possible to use drop-frame timecode, the system will fall back to non-drop-frame. This setting is enabled by default when Timecode insertion (TimecodeInsertion) is enabled.
                            
                            - **FixedAfd** *(integer) --* Applies only if you set AFD Signaling(AfdSignaling) to Fixed (FIXED). Use Fixed (FixedAfd) to specify a four-bit AFD value which the service will write on all frames of this video output.
                            
                            - **Height** *(integer) --* Use the Height (Height) setting to define the video resolution height for this output. Specify in pixels. If you don\'t provide a value here, the service will use the input height.
                            
                            - **Position** *(dict) --* Use Position (Position) to point to a rectangle object to define your position. This setting overrides any other aspect ratio.
                              
                              - **Height** *(integer) --* Height of rectangle in pixels. Specify only even numbers.
                              
                              - **Width** *(integer) --* Width of rectangle in pixels. Specify only even numbers.
                              
                              - **X** *(integer) --* The distance, in pixels, between the rectangle and the left edge of the video frame. Specify only even numbers.
                              
                              - **Y** *(integer) --* The distance, in pixels, between the rectangle and the top edge of the video frame. Specify only even numbers.
                          
                            - **RespondToAfd** *(string) --* Use Respond to AFD (RespondToAfd) to specify how the service changes the video itself in response to AFD values in the input. * Choose Respond to clip the input video frame according to the AFD value, input display aspect ratio, and output display aspect ratio. * Choose Passthrough to include the input AFD values. Do not choose this when AfdSignaling is set to (NONE). A preferred implementation of this workflow is to set RespondToAfd to (NONE) and set AfdSignaling to (AUTO). * Choose None to remove all input AFD values from this output.
                            
                            - **ScalingBehavior** *(string) --* Applies only if your input aspect ratio is different from your output aspect ratio. Enable Stretch to output (StretchToOutput) to have the service stretch your video image to fit. Leave this setting disabled to allow the service to letterbox your video instead. This setting overrides any positioning value you specify elsewhere in the job.
                            
                            - **Sharpness** *(integer) --* Use Sharpness (Sharpness)setting to specify the strength of anti-aliasing. This setting changes the width of the anti-alias filter kernel used for scaling. Sharpness only applies if your output resolution is different from your input resolution, and if you set Anti-alias (AntiAlias) to ENABLED. 0 is the softest setting, 100 the sharpest, and 50 recommended for most content.
                            
                            - **TimecodeInsertion** *(string) --* Applies only to H.264, H.265, MPEG2, and ProRes outputs. Only enable Timecode insertion when the input framerate is identical to the output framerate. To include timecodes in this output, set Timecode insertion (VideoTimecodeInsertion) to PIC_TIMING_SEI. To leave them out, set it to DISABLED. Default is DISABLED. When the service inserts timecodes in an output, by default, it uses any embedded timecodes from the input. If none are present, the service will set the timecode for the first output frame to zero. To change this default behavior, adjust the settings under Timecode configuration (TimecodeConfig). In the console, these settings are located under Job > Job settings > Timecode configuration. Note - Timecode source under input settings (InputTimecodeSource) does not affect the timecodes that are inserted in the output. Source under Job settings > Timecode configuration (TimecodeSource) does.
                            
                            - **VideoPreprocessors** *(dict) --* Find additional transcoding features under Preprocessors (VideoPreprocessors). Enable the features at each output individually. These features are disabled by default.
                              
                              - **ColorCorrector** *(dict) --* Enable the Color corrector (ColorCorrector) feature if necessary. Enable or disable this feature for each output individually. This setting is disabled by default.
                                
                                - **Brightness** *(integer) --* Brightness level.
                                
                                - **ColorSpaceConversion** *(string) --* Determines if colorspace conversion will be performed. If set to _None_, no conversion will be performed. If _Force 601_ or _Force 709_ are selected, conversion will be performed for inputs with differing colorspaces. An input\'s colorspace can be specified explicitly in the \"Video Selector\":#inputs-video_selector if necessary.
                                
                                - **Contrast** *(integer) --* Contrast level.
                                
                                - **Hdr10Metadata** *(dict) --* Use the HDR master display (Hdr10Metadata) settings to correct HDR metadata or to provide missing metadata. These values vary depending on the input video and must be provided by a color grader. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that these settings are not color correction. Note that if you are creating HDR outputs inside of an HLS CMAF package, to comply with the Apple specification, you must use the HVC1 for H.265 setting.
                                  
                                  - **BluePrimaryX** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                                  
                                  - **BluePrimaryY** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                                  
                                  - **GreenPrimaryX** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                                  
                                  - **GreenPrimaryY** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                                  
                                  - **MaxContentLightLevel** *(integer) --* Maximum light level among all samples in the coded video sequence, in units of candelas per square meter.
                                  
                                  - **MaxFrameAverageLightLevel** *(integer) --* Maximum average light level of any frame in the coded video sequence, in units of candelas per square meter.
                                  
                                  - **MaxLuminance** *(integer) --* Nominal maximum mastering display luminance in units of of 0.0001 candelas per square meter.
                                  
                                  - **MinLuminance** *(integer) --* Nominal minimum mastering display luminance in units of of 0.0001 candelas per square meter
                                  
                                  - **RedPrimaryX** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                                  
                                  - **RedPrimaryY** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                                  
                                  - **WhitePointX** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                                  
                                  - **WhitePointY** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                              
                                - **Hue** *(integer) --* Hue in degrees.
                                
                                - **Saturation** *(integer) --* Saturation level.
                            
                              - **Deinterlacer** *(dict) --* Use Deinterlacer (Deinterlacer) to produce smoother motion and a clearer picture.
                                
                                - **Algorithm** *(string) --* Only applies when you set Deinterlacer (DeinterlaceMode) to Deinterlace (DEINTERLACE) or Adaptive (ADAPTIVE). Motion adaptive interpolate (INTERPOLATE) produces sharper pictures, while blend (BLEND) produces smoother motion. Use (INTERPOLATE_TICKER) OR (BLEND_TICKER) if your source file includes a ticker, such as a scrolling headline at the bottom of the frame.
                                
                                - **Control** *(string) --* - When set to NORMAL (default), the deinterlacer does not convert frames that are tagged in metadata as progressive. It will only convert those that are tagged as some other type. - When set to FORCE_ALL_FRAMES, the deinterlacer converts every frame to progressive - even those that are already tagged as progressive. Turn Force mode on only if there is a good chance that the metadata has tagged frames as progressive when they are not progressive. Do not turn on otherwise; processing frames that are already progressive into progressive will probably result in lower quality video.
                                
                                - **Mode** *(string) --* Use Deinterlacer (DeinterlaceMode) to choose how the service will do deinterlacing. Default is Deinterlace. - Deinterlace converts interlaced to progressive. - Inverse telecine converts Hard Telecine 29.97i to progressive 23.976p. - Adaptive auto-detects and converts to progressive.
                            
                              - **ImageInserter** *(dict) --* Enable the Image inserter (ImageInserter) feature to include a graphic overlay on your video. Enable or disable this feature for each output individually. This setting is disabled by default.
                                
                                - **InsertableImages** *(list) --* Image to insert. Must be 32 bit windows BMP, PNG, or TGA file. Must not be larger than the output frames.
                                  
                                  - *(dict) --* Settings for Insertable Image
                                    
                                    - **Duration** *(integer) --* Use Duration (Duration) to set the time, in milliseconds, for the image to remain on the output video.
                                    
                                    - **FadeIn** *(integer) --* Use Fade in (FadeIut) to set the length, in milliseconds, of the inserted image fade in. If you don\'t specify a value for Fade in, the image will appear abruptly at the Start time.
                                    
                                    - **FadeOut** *(integer) --* Use Fade out (FadeOut) to set the length, in milliseconds, of the inserted image fade out. If you don\'t specify a value for Fade out, the image will disappear abruptly at the end of the inserted image duration.
                                    
                                    - **Height** *(integer) --* Specify the Height (Height) of the inserted image. Use a value that is less than or equal to the video resolution height. Leave this setting blank to use the native height of the image.
                                    
                                    - **ImageInserterInput** *(string) --* Use Image location (imageInserterInput) to specify the Amazon S3 location of the image to be inserted into the output. Use a 32 bit BMP, PNG, or TGA file that fits inside the video frame.
                                    
                                    - **ImageX** *(integer) --* Use Left (ImageX) to set the distance, in pixels, between the inserted image and the left edge of the frame. Required for BMP, PNG and TGA input.
                                    
                                    - **ImageY** *(integer) --* Use Top (ImageY) to set the distance, in pixels, between the inserted image and the top edge of the video frame. Required for BMP, PNG and TGA input.
                                    
                                    - **Layer** *(integer) --* Use Layer (Layer) to specify how overlapping inserted images appear. Images with higher values of layer appear on top of images with lower values of layer.
                                    
                                    - **Opacity** *(integer) --* Use Opacity (Opacity) to specify how much of the underlying video shows through the inserted image. 0 is transparent and 100 is fully opaque. Default is 50.
                                    
                                    - **StartTime** *(string) --* Use Start time (StartTime) to specify the video timecode when the image is inserted in the output. This must be in timecode (HH:MM:SS:FF or HH:MM:SS;FF) format.
                                    
                                    - **Width** *(integer) --* Specify the Width (Width) of the inserted image. Use a value that is less than or equal to the video resolution width. Leave this setting blank to use the native width of the image.
                                
                              - **NoiseReducer** *(dict) --* Enable the Noise reducer (NoiseReducer) feature to remove noise from your video output if necessary. Enable or disable this feature for each output individually. This setting is disabled by default.
                                
                                - **Filter** *(string) --* Use Noise reducer filter (NoiseReducerFilter) to select one of the following spatial image filtering functions. To use this setting, you must also enable Noise reducer (NoiseReducer). * Bilateral is an edge preserving noise reduction filter. * Mean (softest), Gaussian, Lanczos, and Sharpen (sharpest) are convolution filters. * Conserve is a min/max noise reduction filter. * Spatial is a frequency-domain filter based on JND principles.
                                
                                - **FilterSettings** *(dict) --* Settings for a noise reducer filter
                                  
                                  - **Strength** *(integer) --* Relative strength of noise reducing filter. Higher values produce stronger filtering.
                              
                                - **SpatialFilterSettings** *(dict) --* Noise reducer filter settings for spatial filter.
                                  
                                  - **PostFilterSharpenStrength** *(integer) --* Specify strength of post noise reduction sharpening filter, with 0 disabling the filter and 3 enabling it at maximum strength.
                                  
                                  - **Speed** *(integer) --* The speed of the filter, from -2 (lower speed) to 3 (higher speed), with 0 being the nominal value.
                                  
                                  - **Strength** *(integer) --* Relative strength of noise reducing filter. Higher values produce stronger filtering.
                              
                              - **TimecodeBurnin** *(dict) --* Timecode burn-in (TimecodeBurnIn)--Burns the output timecode and specified prefix into the output.
                                
                                - **FontSize** *(integer) --* Use Font Size (FontSize) to set the font size of any burned-in timecode. Valid values are 10, 16, 32, 48.
                                
                                - **Position** *(string) --* Use Position (Position) under under Timecode burn-in (TimecodeBurnIn) to specify the location the burned-in timecode on output video.
                                
                                - **Prefix** *(string) --* Use Prefix (Prefix) to place ASCII characters before any burned-in timecode. For example, a prefix of \"EZ-\" will result in the timecode \"EZ-00:00:00:00\". Provide either the characters themselves or the ASCII code equivalents. The supported range of characters is 0x20 through 0x7e. This includes letters, numbers, and all special characters represented on a standard English keyboard.
                            
                            - **Width** *(integer) --* Use Width (Width) to define the video resolution width, in pixels, for this output. If you don\'t provide a value here, the service will use the input width.
                        
                  - **TimecodeConfig** *(dict) --* Contains settings used to acquire and adjust timecode information from inputs.
                    
                    - **Anchor** *(string) --* If you use an editing platform that relies on an anchor timecode, use Anchor Timecode (Anchor) to specify a timecode that will match the input video frame to the output video frame. Use 24-hour format with frame number, (HH:MM:SS:FF) or (HH:MM:SS;FF). This setting ignores framerate conversion. System behavior for Anchor Timecode varies depending on your setting for Source (TimecodeSource). * If Source (TimecodeSource) is set to Specified Start (SPECIFIEDSTART), the first input frame is the specified value in Start Timecode (Start). Anchor Timecode (Anchor) and Start Timecode (Start) are used calculate output timecode. * If Source (TimecodeSource) is set to Start at 0 (ZEROBASED) the first frame is 00:00:00:00. * If Source (TimecodeSource) is set to Embedded (EMBEDDED), the first frame is the timecode value on the first input frame of the input.
                    
                    - **Source** *(string) --* Use Source (TimecodeSource) to set how timecodes are handled within this job. To make sure that your video, audio, captions, and markers are synchronized and that time-based features, such as image inserter, work correctly, choose the Timecode source option that matches your assets. All timecodes are in a 24-hour format with frame number (HH:MM:SS:FF). * Embedded (EMBEDDED) - Use the timecode that is in the input video. If no embedded timecode is in the source, the service will use Start at 0 (ZEROBASED) instead. * Start at 0 (ZEROBASED) - Set the timecode of the initial frame to 00:00:00:00. * Specified Start (SPECIFIEDSTART) - Set the timecode of the initial frame to a value other than zero. You use Start timecode (Start) to provide this value.
                    
                    - **Start** *(string) --* Only use when you set Source (TimecodeSource) to Specified start (SPECIFIEDSTART). Use Start timecode (Start) to specify the timecode for the initial frame. Use 24-hour format with frame number, (HH:MM:SS:FF) or (HH:MM:SS;FF).
                    
                    - **TimestampOffset** *(string) --* Only applies to outputs that support program-date-time stamp. Use Timestamp offset (TimestampOffset) to overwrite the timecode date without affecting the time and frame number. Provide the new date as a string in the format \"yyyy-mm-dd\". To use Time stamp offset, you must also enable Insert program-date-time (InsertProgramDateTime) in the output settings. For example, if the date part of your timecodes is 2002-1-25 and you want to change it to one year later, set Timestamp offset (TimestampOffset) to 2003-1-25.
                
                  - **TimedMetadataInsertion** *(dict) --* Enable Timed metadata insertion (TimedMetadataInsertion) to include ID3 tags in your job. To include timed metadata, you must enable it here, enable it in each output container, and specify tags and timecodes in ID3 insertion (Id3Insertion) objects.
                    
                    - **Id3Insertions** *(list) --* Id3Insertions contains the array of Id3Insertion instances.
                      
                      - *(dict) --* To insert ID3 tags in your output, specify two values. Use ID3 tag (Id3) to specify the base 64 encoded string and use Timecode (TimeCode) to specify the time when the tag should be inserted. To insert multiple ID3 tags in your output, create multiple instances of ID3 insertion (Id3Insertion).
                        
                        - **Id3** *(string) --* Use ID3 tag (Id3) to provide a tag value in base64-encode format.
                        
                        - **Timecode** *(string) --* Provide a Timecode (TimeCode) in HH:MM:SS:FF or HH:MM:SS;FF format.
                    
                - **Type** *(string) --* A job template can be of two types: system or custom. System or built-in job templates can\'t be modified or deleted by the user.
            
        """
        pass


class ListJobs(Paginator):
    def paginate(self, Order: str = None, Queue: str = None, Status: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediaconvert-2017-08-29/ListJobs>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Order=\'ASCENDING\'|\'DESCENDING\',
              Queue=\'string\',
              Status=\'SUBMITTED\'|\'PROGRESSING\'|\'COMPLETE\'|\'CANCELED\'|\'ERROR\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Order: string
        :param Order: When you request lists of resources, you can optionally specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.
        
        :type Queue: string
        :param Queue: Provide a queue name to get back only jobs from that queue.
        
        :type Status: string
        :param Status: A job\'s status can be SUBMITTED, PROGRESSING, COMPLETE, CANCELED, or ERROR.
        
        :type PaginationConfig: dict
        :param PaginationConfig: 
        
          A dictionary that provides parameters to control pagination.
        
          - **MaxItems** *(integer) --* 
        
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
        
          - **PageSize** *(integer) --* 
        
            The size of each page.
        
          - **StartingToken** *(string) --* 
        
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Jobs\': [
                    {
                        \'Arn\': \'string\',
                        \'BillingTagsSource\': \'QUEUE\'|\'PRESET\'|\'JOB_TEMPLATE\',
                        \'CreatedAt\': datetime(2015, 1, 1),
                        \'ErrorCode\': 123,
                        \'ErrorMessage\': \'string\',
                        \'Id\': \'string\',
                        \'JobTemplate\': \'string\',
                        \'OutputGroupDetails\': [
                            {
                                \'OutputDetails\': [
                                    {
                                        \'DurationInMs\': 123,
                                        \'VideoDetails\': {
                                            \'HeightInPx\': 123,
                                            \'WidthInPx\': 123
                                        }
                                    },
                                ]
                            },
                        ],
                        \'Queue\': \'string\',
                        \'Role\': \'string\',
                        \'Settings\': {
                            \'AdAvailOffset\': 123,
                            \'AvailBlanking\': {
                                \'AvailBlankingImage\': \'string\'
                            },
                            \'Inputs\': [
                                {
                                    \'AudioSelectorGroups\': {
                                        \'string\': {
                                            \'AudioSelectorNames\': [
                                                \'string\',
                                            ]
                                        }
                                    },
                                    \'AudioSelectors\': {
                                        \'string\': {
                                            \'CustomLanguageCode\': \'string\',
                                            \'DefaultSelection\': \'DEFAULT\'|\'NOT_DEFAULT\',
                                            \'ExternalAudioFileInput\': \'string\',
                                            \'LanguageCode\': \'ENG\'|\'SPA\'|\'FRA\'|\'DEU\'|\'GER\'|\'ZHO\'|\'ARA\'|\'HIN\'|\'JPN\'|\'RUS\'|\'POR\'|\'ITA\'|\'URD\'|\'VIE\'|\'KOR\'|\'PAN\'|\'ABK\'|\'AAR\'|\'AFR\'|\'AKA\'|\'SQI\'|\'AMH\'|\'ARG\'|\'HYE\'|\'ASM\'|\'AVA\'|\'AVE\'|\'AYM\'|\'AZE\'|\'BAM\'|\'BAK\'|\'EUS\'|\'BEL\'|\'BEN\'|\'BIH\'|\'BIS\'|\'BOS\'|\'BRE\'|\'BUL\'|\'MYA\'|\'CAT\'|\'KHM\'|\'CHA\'|\'CHE\'|\'NYA\'|\'CHU\'|\'CHV\'|\'COR\'|\'COS\'|\'CRE\'|\'HRV\'|\'CES\'|\'DAN\'|\'DIV\'|\'NLD\'|\'DZO\'|\'ENM\'|\'EPO\'|\'EST\'|\'EWE\'|\'FAO\'|\'FIJ\'|\'FIN\'|\'FRM\'|\'FUL\'|\'GLA\'|\'GLG\'|\'LUG\'|\'KAT\'|\'ELL\'|\'GRN\'|\'GUJ\'|\'HAT\'|\'HAU\'|\'HEB\'|\'HER\'|\'HMO\'|\'HUN\'|\'ISL\'|\'IDO\'|\'IBO\'|\'IND\'|\'INA\'|\'ILE\'|\'IKU\'|\'IPK\'|\'GLE\'|\'JAV\'|\'KAL\'|\'KAN\'|\'KAU\'|\'KAS\'|\'KAZ\'|\'KIK\'|\'KIN\'|\'KIR\'|\'KOM\'|\'KON\'|\'KUA\'|\'KUR\'|\'LAO\'|\'LAT\'|\'LAV\'|\'LIM\'|\'LIN\'|\'LIT\'|\'LUB\'|\'LTZ\'|\'MKD\'|\'MLG\'|\'MSA\'|\'MAL\'|\'MLT\'|\'GLV\'|\'MRI\'|\'MAR\'|\'MAH\'|\'MON\'|\'NAU\'|\'NAV\'|\'NDE\'|\'NBL\'|\'NDO\'|\'NEP\'|\'SME\'|\'NOR\'|\'NOB\'|\'NNO\'|\'OCI\'|\'OJI\'|\'ORI\'|\'ORM\'|\'OSS\'|\'PLI\'|\'FAS\'|\'POL\'|\'PUS\'|\'QUE\'|\'QAA\'|\'RON\'|\'ROH\'|\'RUN\'|\'SMO\'|\'SAG\'|\'SAN\'|\'SRD\'|\'SRB\'|\'SNA\'|\'III\'|\'SND\'|\'SIN\'|\'SLK\'|\'SLV\'|\'SOM\'|\'SOT\'|\'SUN\'|\'SWA\'|\'SSW\'|\'SWE\'|\'TGL\'|\'TAH\'|\'TGK\'|\'TAM\'|\'TAT\'|\'TEL\'|\'THA\'|\'BOD\'|\'TIR\'|\'TON\'|\'TSO\'|\'TSN\'|\'TUR\'|\'TUK\'|\'TWI\'|\'UIG\'|\'UKR\'|\'UZB\'|\'VEN\'|\'VOL\'|\'WLN\'|\'CYM\'|\'FRY\'|\'WOL\'|\'XHO\'|\'YID\'|\'YOR\'|\'ZHA\'|\'ZUL\'|\'ORJ\'|\'QPC\'|\'TNG\',
                                            \'Offset\': 123,
                                            \'Pids\': [
                                                123,
                                            ],
                                            \'ProgramSelection\': 123,
                                            \'RemixSettings\': {
                                                \'ChannelMapping\': {
                                                    \'OutputChannels\': [
                                                        {
                                                            \'InputChannels\': [
                                                                123,
                                                            ]
                                                        },
                                                    ]
                                                },
                                                \'ChannelsIn\': 123,
                                                \'ChannelsOut\': 123
                                            },
                                            \'SelectorType\': \'PID\'|\'TRACK\'|\'LANGUAGE_CODE\',
                                            \'Tracks\': [
                                                123,
                                            ]
                                        }
                                    },
                                    \'CaptionSelectors\': {
                                        \'string\': {
                                            \'CustomLanguageCode\': \'string\',
                                            \'LanguageCode\': \'ENG\'|\'SPA\'|\'FRA\'|\'DEU\'|\'GER\'|\'ZHO\'|\'ARA\'|\'HIN\'|\'JPN\'|\'RUS\'|\'POR\'|\'ITA\'|\'URD\'|\'VIE\'|\'KOR\'|\'PAN\'|\'ABK\'|\'AAR\'|\'AFR\'|\'AKA\'|\'SQI\'|\'AMH\'|\'ARG\'|\'HYE\'|\'ASM\'|\'AVA\'|\'AVE\'|\'AYM\'|\'AZE\'|\'BAM\'|\'BAK\'|\'EUS\'|\'BEL\'|\'BEN\'|\'BIH\'|\'BIS\'|\'BOS\'|\'BRE\'|\'BUL\'|\'MYA\'|\'CAT\'|\'KHM\'|\'CHA\'|\'CHE\'|\'NYA\'|\'CHU\'|\'CHV\'|\'COR\'|\'COS\'|\'CRE\'|\'HRV\'|\'CES\'|\'DAN\'|\'DIV\'|\'NLD\'|\'DZO\'|\'ENM\'|\'EPO\'|\'EST\'|\'EWE\'|\'FAO\'|\'FIJ\'|\'FIN\'|\'FRM\'|\'FUL\'|\'GLA\'|\'GLG\'|\'LUG\'|\'KAT\'|\'ELL\'|\'GRN\'|\'GUJ\'|\'HAT\'|\'HAU\'|\'HEB\'|\'HER\'|\'HMO\'|\'HUN\'|\'ISL\'|\'IDO\'|\'IBO\'|\'IND\'|\'INA\'|\'ILE\'|\'IKU\'|\'IPK\'|\'GLE\'|\'JAV\'|\'KAL\'|\'KAN\'|\'KAU\'|\'KAS\'|\'KAZ\'|\'KIK\'|\'KIN\'|\'KIR\'|\'KOM\'|\'KON\'|\'KUA\'|\'KUR\'|\'LAO\'|\'LAT\'|\'LAV\'|\'LIM\'|\'LIN\'|\'LIT\'|\'LUB\'|\'LTZ\'|\'MKD\'|\'MLG\'|\'MSA\'|\'MAL\'|\'MLT\'|\'GLV\'|\'MRI\'|\'MAR\'|\'MAH\'|\'MON\'|\'NAU\'|\'NAV\'|\'NDE\'|\'NBL\'|\'NDO\'|\'NEP\'|\'SME\'|\'NOR\'|\'NOB\'|\'NNO\'|\'OCI\'|\'OJI\'|\'ORI\'|\'ORM\'|\'OSS\'|\'PLI\'|\'FAS\'|\'POL\'|\'PUS\'|\'QUE\'|\'QAA\'|\'RON\'|\'ROH\'|\'RUN\'|\'SMO\'|\'SAG\'|\'SAN\'|\'SRD\'|\'SRB\'|\'SNA\'|\'III\'|\'SND\'|\'SIN\'|\'SLK\'|\'SLV\'|\'SOM\'|\'SOT\'|\'SUN\'|\'SWA\'|\'SSW\'|\'SWE\'|\'TGL\'|\'TAH\'|\'TGK\'|\'TAM\'|\'TAT\'|\'TEL\'|\'THA\'|\'BOD\'|\'TIR\'|\'TON\'|\'TSO\'|\'TSN\'|\'TUR\'|\'TUK\'|\'TWI\'|\'UIG\'|\'UKR\'|\'UZB\'|\'VEN\'|\'VOL\'|\'WLN\'|\'CYM\'|\'FRY\'|\'WOL\'|\'XHO\'|\'YID\'|\'YOR\'|\'ZHA\'|\'ZUL\'|\'ORJ\'|\'QPC\'|\'TNG\',
                                            \'SourceSettings\': {
                                                \'AncillarySourceSettings\': {
                                                    \'SourceAncillaryChannelNumber\': 123
                                                },
                                                \'DvbSubSourceSettings\': {
                                                    \'Pid\': 123
                                                },
                                                \'EmbeddedSourceSettings\': {
                                                    \'Convert608To708\': \'UPCONVERT\'|\'DISABLED\',
                                                    \'Source608ChannelNumber\': 123,
                                                    \'Source608TrackNumber\': 123
                                                },
                                                \'FileSourceSettings\': {
                                                    \'Convert608To708\': \'UPCONVERT\'|\'DISABLED\',
                                                    \'SourceFile\': \'string\',
                                                    \'TimeDelta\': 123
                                                },
                                                \'SourceType\': \'ANCILLARY\'|\'DVB_SUB\'|\'EMBEDDED\'|\'SCC\'|\'TTML\'|\'STL\'|\'SRT\'|\'TELETEXT\'|\'NULL_SOURCE\',
                                                \'TeletextSourceSettings\': {
                                                    \'PageNumber\': \'string\'
                                                }
                                            }
                                        }
                                    },
                                    \'DeblockFilter\': \'ENABLED\'|\'DISABLED\',
                                    \'DenoiseFilter\': \'ENABLED\'|\'DISABLED\',
                                    \'FileInput\': \'string\',
                                    \'FilterEnable\': \'AUTO\'|\'DISABLE\'|\'FORCE\',
                                    \'FilterStrength\': 123,
                                    \'InputClippings\': [
                                        {
                                            \'EndTimecode\': \'string\',
                                            \'StartTimecode\': \'string\'
                                        },
                                    ],
                                    \'ProgramNumber\': 123,
                                    \'PsiControl\': \'IGNORE_PSI\'|\'USE_PSI\',
                                    \'TimecodeSource\': \'EMBEDDED\'|\'ZEROBASED\'|\'SPECIFIEDSTART\',
                                    \'VideoSelector\': {
                                        \'ColorSpace\': \'FOLLOW\'|\'REC_601\'|\'REC_709\'|\'HDR10\'|\'HLG_2020\',
                                        \'ColorSpaceUsage\': \'FORCE\'|\'FALLBACK\',
                                        \'Hdr10Metadata\': {
                                            \'BluePrimaryX\': 123,
                                            \'BluePrimaryY\': 123,
                                            \'GreenPrimaryX\': 123,
                                            \'GreenPrimaryY\': 123,
                                            \'MaxContentLightLevel\': 123,
                                            \'MaxFrameAverageLightLevel\': 123,
                                            \'MaxLuminance\': 123,
                                            \'MinLuminance\': 123,
                                            \'RedPrimaryX\': 123,
                                            \'RedPrimaryY\': 123,
                                            \'WhitePointX\': 123,
                                            \'WhitePointY\': 123
                                        },
                                        \'Pid\': 123,
                                        \'ProgramNumber\': 123
                                    }
                                },
                            ],
                            \'NielsenConfiguration\': {
                                \'BreakoutCode\': 123,
                                \'DistributorId\': \'string\'
                            },
                            \'OutputGroups\': [
                                {
                                    \'CustomName\': \'string\',
                                    \'Name\': \'string\',
                                    \'OutputGroupSettings\': {
                                        \'CmafGroupSettings\': {
                                            \'BaseUrl\': \'string\',
                                            \'ClientCache\': \'DISABLED\'|\'ENABLED\',
                                            \'CodecSpecification\': \'RFC_6381\'|\'RFC_4281\',
                                            \'Destination\': \'string\',
                                            \'Encryption\': {
                                                \'ConstantInitializationVector\': \'string\',
                                                \'EncryptionMethod\': \'SAMPLE_AES\',
                                                \'InitializationVectorInManifest\': \'INCLUDE\'|\'EXCLUDE\',
                                                \'StaticKeyProvider\': {
                                                    \'KeyFormat\': \'string\',
                                                    \'KeyFormatVersions\': \'string\',
                                                    \'StaticKeyValue\': \'string\',
                                                    \'Url\': \'string\'
                                                },
                                                \'Type\': \'STATIC_KEY\'
                                            },
                                            \'FragmentLength\': 123,
                                            \'ManifestCompression\': \'GZIP\'|\'NONE\',
                                            \'ManifestDurationFormat\': \'FLOATING_POINT\'|\'INTEGER\',
                                            \'MinBufferTime\': 123,
                                            \'MinFinalSegmentLength\': 123.0,
                                            \'SegmentControl\': \'SINGLE_FILE\'|\'SEGMENTED_FILES\',
                                            \'SegmentLength\': 123,
                                            \'StreamInfResolution\': \'INCLUDE\'|\'EXCLUDE\',
                                            \'WriteDashManifest\': \'DISABLED\'|\'ENABLED\',
                                            \'WriteHlsManifest\': \'DISABLED\'|\'ENABLED\'
                                        },
                                        \'DashIsoGroupSettings\': {
                                            \'BaseUrl\': \'string\',
                                            \'Destination\': \'string\',
                                            \'Encryption\': {
                                                \'SpekeKeyProvider\': {
                                                    \'ResourceId\': \'string\',
                                                    \'SystemIds\': [
                                                        \'string\',
                                                    ],
                                                    \'Url\': \'string\'
                                                }
                                            },
                                            \'FragmentLength\': 123,
                                            \'HbbtvCompliance\': \'HBBTV_1_5\'|\'NONE\',
                                            \'MinBufferTime\': 123,
                                            \'SegmentControl\': \'SINGLE_FILE\'|\'SEGMENTED_FILES\',
                                            \'SegmentLength\': 123,
                                            \'WriteSegmentTimelineInRepresentation\': \'ENABLED\'|\'DISABLED\'
                                        },
                                        \'FileGroupSettings\': {
                                            \'Destination\': \'string\'
                                        },
                                        \'HlsGroupSettings\': {
                                            \'AdMarkers\': [
                                                \'ELEMENTAL\'|\'ELEMENTAL_SCTE35\',
                                            ],
                                            \'BaseUrl\': \'string\',
                                            \'CaptionLanguageMappings\': [
                                                {
                                                    \'CaptionChannel\': 123,
                                                    \'CustomLanguageCode\': \'string\',
                                                    \'LanguageCode\': \'ENG\'|\'SPA\'|\'FRA\'|\'DEU\'|\'GER\'|\'ZHO\'|\'ARA\'|\'HIN\'|\'JPN\'|\'RUS\'|\'POR\'|\'ITA\'|\'URD\'|\'VIE\'|\'KOR\'|\'PAN\'|\'ABK\'|\'AAR\'|\'AFR\'|\'AKA\'|\'SQI\'|\'AMH\'|\'ARG\'|\'HYE\'|\'ASM\'|\'AVA\'|\'AVE\'|\'AYM\'|\'AZE\'|\'BAM\'|\'BAK\'|\'EUS\'|\'BEL\'|\'BEN\'|\'BIH\'|\'BIS\'|\'BOS\'|\'BRE\'|\'BUL\'|\'MYA\'|\'CAT\'|\'KHM\'|\'CHA\'|\'CHE\'|\'NYA\'|\'CHU\'|\'CHV\'|\'COR\'|\'COS\'|\'CRE\'|\'HRV\'|\'CES\'|\'DAN\'|\'DIV\'|\'NLD\'|\'DZO\'|\'ENM\'|\'EPO\'|\'EST\'|\'EWE\'|\'FAO\'|\'FIJ\'|\'FIN\'|\'FRM\'|\'FUL\'|\'GLA\'|\'GLG\'|\'LUG\'|\'KAT\'|\'ELL\'|\'GRN\'|\'GUJ\'|\'HAT\'|\'HAU\'|\'HEB\'|\'HER\'|\'HMO\'|\'HUN\'|\'ISL\'|\'IDO\'|\'IBO\'|\'IND\'|\'INA\'|\'ILE\'|\'IKU\'|\'IPK\'|\'GLE\'|\'JAV\'|\'KAL\'|\'KAN\'|\'KAU\'|\'KAS\'|\'KAZ\'|\'KIK\'|\'KIN\'|\'KIR\'|\'KOM\'|\'KON\'|\'KUA\'|\'KUR\'|\'LAO\'|\'LAT\'|\'LAV\'|\'LIM\'|\'LIN\'|\'LIT\'|\'LUB\'|\'LTZ\'|\'MKD\'|\'MLG\'|\'MSA\'|\'MAL\'|\'MLT\'|\'GLV\'|\'MRI\'|\'MAR\'|\'MAH\'|\'MON\'|\'NAU\'|\'NAV\'|\'NDE\'|\'NBL\'|\'NDO\'|\'NEP\'|\'SME\'|\'NOR\'|\'NOB\'|\'NNO\'|\'OCI\'|\'OJI\'|\'ORI\'|\'ORM\'|\'OSS\'|\'PLI\'|\'FAS\'|\'POL\'|\'PUS\'|\'QUE\'|\'QAA\'|\'RON\'|\'ROH\'|\'RUN\'|\'SMO\'|\'SAG\'|\'SAN\'|\'SRD\'|\'SRB\'|\'SNA\'|\'III\'|\'SND\'|\'SIN\'|\'SLK\'|\'SLV\'|\'SOM\'|\'SOT\'|\'SUN\'|\'SWA\'|\'SSW\'|\'SWE\'|\'TGL\'|\'TAH\'|\'TGK\'|\'TAM\'|\'TAT\'|\'TEL\'|\'THA\'|\'BOD\'|\'TIR\'|\'TON\'|\'TSO\'|\'TSN\'|\'TUR\'|\'TUK\'|\'TWI\'|\'UIG\'|\'UKR\'|\'UZB\'|\'VEN\'|\'VOL\'|\'WLN\'|\'CYM\'|\'FRY\'|\'WOL\'|\'XHO\'|\'YID\'|\'YOR\'|\'ZHA\'|\'ZUL\'|\'ORJ\'|\'QPC\'|\'TNG\',
                                                    \'LanguageDescription\': \'string\'
                                                },
                                            ],
                                            \'CaptionLanguageSetting\': \'INSERT\'|\'OMIT\'|\'NONE\',
                                            \'ClientCache\': \'DISABLED\'|\'ENABLED\',
                                            \'CodecSpecification\': \'RFC_6381\'|\'RFC_4281\',
                                            \'Destination\': \'string\',
                                            \'DirectoryStructure\': \'SINGLE_DIRECTORY\'|\'SUBDIRECTORY_PER_STREAM\',
                                            \'Encryption\': {
                                                \'ConstantInitializationVector\': \'string\',
                                                \'EncryptionMethod\': \'AES128\'|\'SAMPLE_AES\',
                                                \'InitializationVectorInManifest\': \'INCLUDE\'|\'EXCLUDE\',
                                                \'SpekeKeyProvider\': {
                                                    \'ResourceId\': \'string\',
                                                    \'SystemIds\': [
                                                        \'string\',
                                                    ],
                                                    \'Url\': \'string\'
                                                },
                                                \'StaticKeyProvider\': {
                                                    \'KeyFormat\': \'string\',
                                                    \'KeyFormatVersions\': \'string\',
                                                    \'StaticKeyValue\': \'string\',
                                                    \'Url\': \'string\'
                                                },
                                                \'Type\': \'SPEKE\'|\'STATIC_KEY\'
                                            },
                                            \'ManifestCompression\': \'GZIP\'|\'NONE\',
                                            \'ManifestDurationFormat\': \'FLOATING_POINT\'|\'INTEGER\',
                                            \'MinFinalSegmentLength\': 123.0,
                                            \'MinSegmentLength\': 123,
                                            \'OutputSelection\': \'MANIFESTS_AND_SEGMENTS\'|\'SEGMENTS_ONLY\',
                                            \'ProgramDateTime\': \'INCLUDE\'|\'EXCLUDE\',
                                            \'ProgramDateTimePeriod\': 123,
                                            \'SegmentControl\': \'SINGLE_FILE\'|\'SEGMENTED_FILES\',
                                            \'SegmentLength\': 123,
                                            \'SegmentsPerSubdirectory\': 123,
                                            \'StreamInfResolution\': \'INCLUDE\'|\'EXCLUDE\',
                                            \'TimedMetadataId3Frame\': \'NONE\'|\'PRIV\'|\'TDRL\',
                                            \'TimedMetadataId3Period\': 123,
                                            \'TimestampDeltaMilliseconds\': 123
                                        },
                                        \'MsSmoothGroupSettings\': {
                                            \'AudioDeduplication\': \'COMBINE_DUPLICATE_STREAMS\'|\'NONE\',
                                            \'Destination\': \'string\',
                                            \'Encryption\': {
                                                \'SpekeKeyProvider\': {
                                                    \'ResourceId\': \'string\',
                                                    \'SystemIds\': [
                                                        \'string\',
                                                    ],
                                                    \'Url\': \'string\'
                                                }
                                            },
                                            \'FragmentLength\': 123,
                                            \'ManifestEncoding\': \'UTF8\'|\'UTF16\'
                                        },
                                        \'Type\': \'HLS_GROUP_SETTINGS\'|\'DASH_ISO_GROUP_SETTINGS\'|\'FILE_GROUP_SETTINGS\'|\'MS_SMOOTH_GROUP_SETTINGS\'|\'CMAF_GROUP_SETTINGS\'
                                    },
                                    \'Outputs\': [
                                        {
                                            \'AudioDescriptions\': [
                                                {
                                                    \'AudioNormalizationSettings\': {
                                                        \'Algorithm\': \'ITU_BS_1770_1\'|\'ITU_BS_1770_2\',
                                                        \'AlgorithmControl\': \'CORRECT_AUDIO\'|\'MEASURE_ONLY\',
                                                        \'CorrectionGateLevel\': 123,
                                                        \'LoudnessLogging\': \'LOG\'|\'DONT_LOG\',
                                                        \'PeakCalculation\': \'TRUE_PEAK\'|\'NONE\',
                                                        \'TargetLkfs\': 123.0
                                                    },
                                                    \'AudioSourceName\': \'string\',
                                                    \'AudioType\': 123,
                                                    \'AudioTypeControl\': \'FOLLOW_INPUT\'|\'USE_CONFIGURED\',
                                                    \'CodecSettings\': {
                                                        \'AacSettings\': {
                                                            \'AudioDescriptionBroadcasterMix\': \'BROADCASTER_MIXED_AD\'|\'NORMAL\',
                                                            \'Bitrate\': 123,
                                                            \'CodecProfile\': \'LC\'|\'HEV1\'|\'HEV2\',
                                                            \'CodingMode\': \'AD_RECEIVER_MIX\'|\'CODING_MODE_1_0\'|\'CODING_MODE_1_1\'|\'CODING_MODE_2_0\'|\'CODING_MODE_5_1\',
                                                            \'RateControlMode\': \'CBR\'|\'VBR\',
                                                            \'RawFormat\': \'LATM_LOAS\'|\'NONE\',
                                                            \'SampleRate\': 123,
                                                            \'Specification\': \'MPEG2\'|\'MPEG4\',
                                                            \'VbrQuality\': \'LOW\'|\'MEDIUM_LOW\'|\'MEDIUM_HIGH\'|\'HIGH\'
                                                        },
                                                        \'Ac3Settings\': {
                                                            \'Bitrate\': 123,
                                                            \'BitstreamMode\': \'COMPLETE_MAIN\'|\'COMMENTARY\'|\'DIALOGUE\'|\'EMERGENCY\'|\'HEARING_IMPAIRED\'|\'MUSIC_AND_EFFECTS\'|\'VISUALLY_IMPAIRED\'|\'VOICE_OVER\',
                                                            \'CodingMode\': \'CODING_MODE_1_0\'|\'CODING_MODE_1_1\'|\'CODING_MODE_2_0\'|\'CODING_MODE_3_2_LFE\',
                                                            \'Dialnorm\': 123,
                                                            \'DynamicRangeCompressionProfile\': \'FILM_STANDARD\'|\'NONE\',
                                                            \'LfeFilter\': \'ENABLED\'|\'DISABLED\',
                                                            \'MetadataControl\': \'FOLLOW_INPUT\'|\'USE_CONFIGURED\',
                                                            \'SampleRate\': 123
                                                        },
                                                        \'AiffSettings\': {
                                                            \'BitDepth\': 123,
                                                            \'Channels\': 123,
                                                            \'SampleRate\': 123
                                                        },
                                                        \'Codec\': \'AAC\'|\'MP2\'|\'WAV\'|\'AIFF\'|\'AC3\'|\'EAC3\'|\'PASSTHROUGH\',
                                                        \'Eac3Settings\': {
                                                            \'AttenuationControl\': \'ATTENUATE_3_DB\'|\'NONE\',
                                                            \'Bitrate\': 123,
                                                            \'BitstreamMode\': \'COMPLETE_MAIN\'|\'COMMENTARY\'|\'EMERGENCY\'|\'HEARING_IMPAIRED\'|\'VISUALLY_IMPAIRED\',
                                                            \'CodingMode\': \'CODING_MODE_1_0\'|\'CODING_MODE_2_0\'|\'CODING_MODE_3_2\',
                                                            \'DcFilter\': \'ENABLED\'|\'DISABLED\',
                                                            \'Dialnorm\': 123,
                                                            \'DynamicRangeCompressionLine\': \'NONE\'|\'FILM_STANDARD\'|\'FILM_LIGHT\'|\'MUSIC_STANDARD\'|\'MUSIC_LIGHT\'|\'SPEECH\',
                                                            \'DynamicRangeCompressionRf\': \'NONE\'|\'FILM_STANDARD\'|\'FILM_LIGHT\'|\'MUSIC_STANDARD\'|\'MUSIC_LIGHT\'|\'SPEECH\',
                                                            \'LfeControl\': \'LFE\'|\'NO_LFE\',
                                                            \'LfeFilter\': \'ENABLED\'|\'DISABLED\',
                                                            \'LoRoCenterMixLevel\': 123.0,
                                                            \'LoRoSurroundMixLevel\': 123.0,
                                                            \'LtRtCenterMixLevel\': 123.0,
                                                            \'LtRtSurroundMixLevel\': 123.0,
                                                            \'MetadataControl\': \'FOLLOW_INPUT\'|\'USE_CONFIGURED\',
                                                            \'PassthroughControl\': \'WHEN_POSSIBLE\'|\'NO_PASSTHROUGH\',
                                                            \'PhaseControl\': \'SHIFT_90_DEGREES\'|\'NO_SHIFT\',
                                                            \'SampleRate\': 123,
                                                            \'StereoDownmix\': \'NOT_INDICATED\'|\'LO_RO\'|\'LT_RT\'|\'DPL2\',
                                                            \'SurroundExMode\': \'NOT_INDICATED\'|\'ENABLED\'|\'DISABLED\',
                                                            \'SurroundMode\': \'NOT_INDICATED\'|\'ENABLED\'|\'DISABLED\'
                                                        },
                                                        \'Mp2Settings\': {
                                                            \'Bitrate\': 123,
                                                            \'Channels\': 123,
                                                            \'SampleRate\': 123
                                                        },
                                                        \'WavSettings\': {
                                                            \'BitDepth\': 123,
                                                            \'Channels\': 123,
                                                            \'Format\': \'RIFF\'|\'RF64\',
                                                            \'SampleRate\': 123
                                                        }
                                                    },
                                                    \'CustomLanguageCode\': \'string\',
                                                    \'LanguageCode\': \'ENG\'|\'SPA\'|\'FRA\'|\'DEU\'|\'GER\'|\'ZHO\'|\'ARA\'|\'HIN\'|\'JPN\'|\'RUS\'|\'POR\'|\'ITA\'|\'URD\'|\'VIE\'|\'KOR\'|\'PAN\'|\'ABK\'|\'AAR\'|\'AFR\'|\'AKA\'|\'SQI\'|\'AMH\'|\'ARG\'|\'HYE\'|\'ASM\'|\'AVA\'|\'AVE\'|\'AYM\'|\'AZE\'|\'BAM\'|\'BAK\'|\'EUS\'|\'BEL\'|\'BEN\'|\'BIH\'|\'BIS\'|\'BOS\'|\'BRE\'|\'BUL\'|\'MYA\'|\'CAT\'|\'KHM\'|\'CHA\'|\'CHE\'|\'NYA\'|\'CHU\'|\'CHV\'|\'COR\'|\'COS\'|\'CRE\'|\'HRV\'|\'CES\'|\'DAN\'|\'DIV\'|\'NLD\'|\'DZO\'|\'ENM\'|\'EPO\'|\'EST\'|\'EWE\'|\'FAO\'|\'FIJ\'|\'FIN\'|\'FRM\'|\'FUL\'|\'GLA\'|\'GLG\'|\'LUG\'|\'KAT\'|\'ELL\'|\'GRN\'|\'GUJ\'|\'HAT\'|\'HAU\'|\'HEB\'|\'HER\'|\'HMO\'|\'HUN\'|\'ISL\'|\'IDO\'|\'IBO\'|\'IND\'|\'INA\'|\'ILE\'|\'IKU\'|\'IPK\'|\'GLE\'|\'JAV\'|\'KAL\'|\'KAN\'|\'KAU\'|\'KAS\'|\'KAZ\'|\'KIK\'|\'KIN\'|\'KIR\'|\'KOM\'|\'KON\'|\'KUA\'|\'KUR\'|\'LAO\'|\'LAT\'|\'LAV\'|\'LIM\'|\'LIN\'|\'LIT\'|\'LUB\'|\'LTZ\'|\'MKD\'|\'MLG\'|\'MSA\'|\'MAL\'|\'MLT\'|\'GLV\'|\'MRI\'|\'MAR\'|\'MAH\'|\'MON\'|\'NAU\'|\'NAV\'|\'NDE\'|\'NBL\'|\'NDO\'|\'NEP\'|\'SME\'|\'NOR\'|\'NOB\'|\'NNO\'|\'OCI\'|\'OJI\'|\'ORI\'|\'ORM\'|\'OSS\'|\'PLI\'|\'FAS\'|\'POL\'|\'PUS\'|\'QUE\'|\'QAA\'|\'RON\'|\'ROH\'|\'RUN\'|\'SMO\'|\'SAG\'|\'SAN\'|\'SRD\'|\'SRB\'|\'SNA\'|\'III\'|\'SND\'|\'SIN\'|\'SLK\'|\'SLV\'|\'SOM\'|\'SOT\'|\'SUN\'|\'SWA\'|\'SSW\'|\'SWE\'|\'TGL\'|\'TAH\'|\'TGK\'|\'TAM\'|\'TAT\'|\'TEL\'|\'THA\'|\'BOD\'|\'TIR\'|\'TON\'|\'TSO\'|\'TSN\'|\'TUR\'|\'TUK\'|\'TWI\'|\'UIG\'|\'UKR\'|\'UZB\'|\'VEN\'|\'VOL\'|\'WLN\'|\'CYM\'|\'FRY\'|\'WOL\'|\'XHO\'|\'YID\'|\'YOR\'|\'ZHA\'|\'ZUL\'|\'ORJ\'|\'QPC\'|\'TNG\',
                                                    \'LanguageCodeControl\': \'FOLLOW_INPUT\'|\'USE_CONFIGURED\',
                                                    \'RemixSettings\': {
                                                        \'ChannelMapping\': {
                                                            \'OutputChannels\': [
                                                                {
                                                                    \'InputChannels\': [
                                                                        123,
                                                                    ]
                                                                },
                                                            ]
                                                        },
                                                        \'ChannelsIn\': 123,
                                                        \'ChannelsOut\': 123
                                                    },
                                                    \'StreamName\': \'string\'
                                                },
                                            ],
                                            \'CaptionDescriptions\': [
                                                {
                                                    \'CaptionSelectorName\': \'string\',
                                                    \'CustomLanguageCode\': \'string\',
                                                    \'DestinationSettings\': {
                                                        \'BurninDestinationSettings\': {
                                                            \'Alignment\': \'CENTERED\'|\'LEFT\',
                                                            \'BackgroundColor\': \'NONE\'|\'BLACK\'|\'WHITE\',
                                                            \'BackgroundOpacity\': 123,
                                                            \'FontColor\': \'WHITE\'|\'BLACK\'|\'YELLOW\'|\'RED\'|\'GREEN\'|\'BLUE\',
                                                            \'FontOpacity\': 123,
                                                            \'FontResolution\': 123,
                                                            \'FontSize\': 123,
                                                            \'OutlineColor\': \'BLACK\'|\'WHITE\'|\'YELLOW\'|\'RED\'|\'GREEN\'|\'BLUE\',
                                                            \'OutlineSize\': 123,
                                                            \'ShadowColor\': \'NONE\'|\'BLACK\'|\'WHITE\',
                                                            \'ShadowOpacity\': 123,
                                                            \'ShadowXOffset\': 123,
                                                            \'ShadowYOffset\': 123,
                                                            \'TeletextSpacing\': \'FIXED_GRID\'|\'PROPORTIONAL\',
                                                            \'XPosition\': 123,
                                                            \'YPosition\': 123
                                                        },
                                                        \'DestinationType\': \'BURN_IN\'|\'DVB_SUB\'|\'EMBEDDED\'|\'SCC\'|\'SRT\'|\'TELETEXT\'|\'TTML\'|\'WEBVTT\',
                                                        \'DvbSubDestinationSettings\': {
                                                            \'Alignment\': \'CENTERED\'|\'LEFT\',
                                                            \'BackgroundColor\': \'NONE\'|\'BLACK\'|\'WHITE\',
                                                            \'BackgroundOpacity\': 123,
                                                            \'FontColor\': \'WHITE\'|\'BLACK\'|\'YELLOW\'|\'RED\'|\'GREEN\'|\'BLUE\',
                                                            \'FontOpacity\': 123,
                                                            \'FontResolution\': 123,
                                                            \'FontSize\': 123,
                                                            \'OutlineColor\': \'BLACK\'|\'WHITE\'|\'YELLOW\'|\'RED\'|\'GREEN\'|\'BLUE\',
                                                            \'OutlineSize\': 123,
                                                            \'ShadowColor\': \'NONE\'|\'BLACK\'|\'WHITE\',
                                                            \'ShadowOpacity\': 123,
                                                            \'ShadowXOffset\': 123,
                                                            \'ShadowYOffset\': 123,
                                                            \'TeletextSpacing\': \'FIXED_GRID\'|\'PROPORTIONAL\',
                                                            \'XPosition\': 123,
                                                            \'YPosition\': 123
                                                        },
                                                        \'SccDestinationSettings\': {
                                                            \'Framerate\': \'FRAMERATE_23_97\'|\'FRAMERATE_24\'|\'FRAMERATE_29_97_DROPFRAME\'|\'FRAMERATE_29_97_NON_DROPFRAME\'
                                                        },
                                                        \'TeletextDestinationSettings\': {
                                                            \'PageNumber\': \'string\'
                                                        },
                                                        \'TtmlDestinationSettings\': {
                                                            \'StylePassthrough\': \'ENABLED\'|\'DISABLED\'
                                                        }
                                                    },
                                                    \'LanguageCode\': \'ENG\'|\'SPA\'|\'FRA\'|\'DEU\'|\'GER\'|\'ZHO\'|\'ARA\'|\'HIN\'|\'JPN\'|\'RUS\'|\'POR\'|\'ITA\'|\'URD\'|\'VIE\'|\'KOR\'|\'PAN\'|\'ABK\'|\'AAR\'|\'AFR\'|\'AKA\'|\'SQI\'|\'AMH\'|\'ARG\'|\'HYE\'|\'ASM\'|\'AVA\'|\'AVE\'|\'AYM\'|\'AZE\'|\'BAM\'|\'BAK\'|\'EUS\'|\'BEL\'|\'BEN\'|\'BIH\'|\'BIS\'|\'BOS\'|\'BRE\'|\'BUL\'|\'MYA\'|\'CAT\'|\'KHM\'|\'CHA\'|\'CHE\'|\'NYA\'|\'CHU\'|\'CHV\'|\'COR\'|\'COS\'|\'CRE\'|\'HRV\'|\'CES\'|\'DAN\'|\'DIV\'|\'NLD\'|\'DZO\'|\'ENM\'|\'EPO\'|\'EST\'|\'EWE\'|\'FAO\'|\'FIJ\'|\'FIN\'|\'FRM\'|\'FUL\'|\'GLA\'|\'GLG\'|\'LUG\'|\'KAT\'|\'ELL\'|\'GRN\'|\'GUJ\'|\'HAT\'|\'HAU\'|\'HEB\'|\'HER\'|\'HMO\'|\'HUN\'|\'ISL\'|\'IDO\'|\'IBO\'|\'IND\'|\'INA\'|\'ILE\'|\'IKU\'|\'IPK\'|\'GLE\'|\'JAV\'|\'KAL\'|\'KAN\'|\'KAU\'|\'KAS\'|\'KAZ\'|\'KIK\'|\'KIN\'|\'KIR\'|\'KOM\'|\'KON\'|\'KUA\'|\'KUR\'|\'LAO\'|\'LAT\'|\'LAV\'|\'LIM\'|\'LIN\'|\'LIT\'|\'LUB\'|\'LTZ\'|\'MKD\'|\'MLG\'|\'MSA\'|\'MAL\'|\'MLT\'|\'GLV\'|\'MRI\'|\'MAR\'|\'MAH\'|\'MON\'|\'NAU\'|\'NAV\'|\'NDE\'|\'NBL\'|\'NDO\'|\'NEP\'|\'SME\'|\'NOR\'|\'NOB\'|\'NNO\'|\'OCI\'|\'OJI\'|\'ORI\'|\'ORM\'|\'OSS\'|\'PLI\'|\'FAS\'|\'POL\'|\'PUS\'|\'QUE\'|\'QAA\'|\'RON\'|\'ROH\'|\'RUN\'|\'SMO\'|\'SAG\'|\'SAN\'|\'SRD\'|\'SRB\'|\'SNA\'|\'III\'|\'SND\'|\'SIN\'|\'SLK\'|\'SLV\'|\'SOM\'|\'SOT\'|\'SUN\'|\'SWA\'|\'SSW\'|\'SWE\'|\'TGL\'|\'TAH\'|\'TGK\'|\'TAM\'|\'TAT\'|\'TEL\'|\'THA\'|\'BOD\'|\'TIR\'|\'TON\'|\'TSO\'|\'TSN\'|\'TUR\'|\'TUK\'|\'TWI\'|\'UIG\'|\'UKR\'|\'UZB\'|\'VEN\'|\'VOL\'|\'WLN\'|\'CYM\'|\'FRY\'|\'WOL\'|\'XHO\'|\'YID\'|\'YOR\'|\'ZHA\'|\'ZUL\'|\'ORJ\'|\'QPC\'|\'TNG\',
                                                    \'LanguageDescription\': \'string\'
                                                },
                                            ],
                                            \'ContainerSettings\': {
                                                \'Container\': \'F4V\'|\'ISMV\'|\'M2TS\'|\'M3U8\'|\'CMFC\'|\'MOV\'|\'MP4\'|\'MPD\'|\'MXF\'|\'RAW\',
                                                \'F4vSettings\': {
                                                    \'MoovPlacement\': \'PROGRESSIVE_DOWNLOAD\'|\'NORMAL\'
                                                },
                                                \'M2tsSettings\': {
                                                    \'AudioBufferModel\': \'DVB\'|\'ATSC\',
                                                    \'AudioFramesPerPes\': 123,
                                                    \'AudioPids\': [
                                                        123,
                                                    ],
                                                    \'Bitrate\': 123,
                                                    \'BufferModel\': \'MULTIPLEX\'|\'NONE\',
                                                    \'DvbNitSettings\': {
                                                        \'NetworkId\': 123,
                                                        \'NetworkName\': \'string\',
                                                        \'NitInterval\': 123
                                                    },
                                                    \'DvbSdtSettings\': {
                                                        \'OutputSdt\': \'SDT_FOLLOW\'|\'SDT_FOLLOW_IF_PRESENT\'|\'SDT_MANUAL\'|\'SDT_NONE\',
                                                        \'SdtInterval\': 123,
                                                        \'ServiceName\': \'string\',
                                                        \'ServiceProviderName\': \'string\'
                                                    },
                                                    \'DvbSubPids\': [
                                                        123,
                                                    ],
                                                    \'DvbTdtSettings\': {
                                                        \'TdtInterval\': 123
                                                    },
                                                    \'DvbTeletextPid\': 123,
                                                    \'EbpAudioInterval\': \'VIDEO_AND_FIXED_INTERVALS\'|\'VIDEO_INTERVAL\',
                                                    \'EbpPlacement\': \'VIDEO_AND_AUDIO_PIDS\'|\'VIDEO_PID\',
                                                    \'EsRateInPes\': \'INCLUDE\'|\'EXCLUDE\',
                                                    \'FragmentTime\': 123.0,
                                                    \'MaxPcrInterval\': 123,
                                                    \'MinEbpInterval\': 123,
                                                    \'NielsenId3\': \'INSERT\'|\'NONE\',
                                                    \'NullPacketBitrate\': 123.0,
                                                    \'PatInterval\': 123,
                                                    \'PcrControl\': \'PCR_EVERY_PES_PACKET\'|\'CONFIGURED_PCR_PERIOD\',
                                                    \'PcrPid\': 123,
                                                    \'PmtInterval\': 123,
                                                    \'PmtPid\': 123,
                                                    \'PrivateMetadataPid\': 123,
                                                    \'ProgramNumber\': 123,
                                                    \'RateMode\': \'VBR\'|\'CBR\',
                                                    \'Scte35Pid\': 123,
                                                    \'Scte35Source\': \'PASSTHROUGH\'|\'NONE\',
                                                    \'SegmentationMarkers\': \'NONE\'|\'RAI_SEGSTART\'|\'RAI_ADAPT\'|\'PSI_SEGSTART\'|\'EBP\'|\'EBP_LEGACY\',
                                                    \'SegmentationStyle\': \'MAINTAIN_CADENCE\'|\'RESET_CADENCE\',
                                                    \'SegmentationTime\': 123.0,
                                                    \'TimedMetadataPid\': 123,
                                                    \'TransportStreamId\': 123,
                                                    \'VideoPid\': 123
                                                },
                                                \'M3u8Settings\': {
                                                    \'AudioFramesPerPes\': 123,
                                                    \'AudioPids\': [
                                                        123,
                                                    ],
                                                    \'NielsenId3\': \'INSERT\'|\'NONE\',
                                                    \'PatInterval\': 123,
                                                    \'PcrControl\': \'PCR_EVERY_PES_PACKET\'|\'CONFIGURED_PCR_PERIOD\',
                                                    \'PcrPid\': 123,
                                                    \'PmtInterval\': 123,
                                                    \'PmtPid\': 123,
                                                    \'PrivateMetadataPid\': 123,
                                                    \'ProgramNumber\': 123,
                                                    \'Scte35Pid\': 123,
                                                    \'Scte35Source\': \'PASSTHROUGH\'|\'NONE\',
                                                    \'TimedMetadata\': \'PASSTHROUGH\'|\'NONE\',
                                                    \'TimedMetadataPid\': 123,
                                                    \'TransportStreamId\': 123,
                                                    \'VideoPid\': 123
                                                },
                                                \'MovSettings\': {
                                                    \'ClapAtom\': \'INCLUDE\'|\'EXCLUDE\',
                                                    \'CslgAtom\': \'INCLUDE\'|\'EXCLUDE\',
                                                    \'Mpeg2FourCCControl\': \'XDCAM\'|\'MPEG\',
                                                    \'PaddingControl\': \'OMNEON\'|\'NONE\',
                                                    \'Reference\': \'SELF_CONTAINED\'|\'EXTERNAL\'
                                                },
                                                \'Mp4Settings\': {
                                                    \'CslgAtom\': \'INCLUDE\'|\'EXCLUDE\',
                                                    \'FreeSpaceBox\': \'INCLUDE\'|\'EXCLUDE\',
                                                    \'MoovPlacement\': \'PROGRESSIVE_DOWNLOAD\'|\'NORMAL\',
                                                    \'Mp4MajorBrand\': \'string\'
                                                }
                                            },
                                            \'Extension\': \'string\',
                                            \'NameModifier\': \'string\',
                                            \'OutputSettings\': {
                                                \'HlsSettings\': {
                                                    \'AudioGroupId\': \'string\',
                                                    \'AudioRenditionSets\': \'string\',
                                                    \'AudioTrackType\': \'ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT\'|\'ALTERNATE_AUDIO_AUTO_SELECT\'|\'ALTERNATE_AUDIO_NOT_AUTO_SELECT\'|\'AUDIO_ONLY_VARIANT_STREAM\',
                                                    \'IFrameOnlyManifest\': \'INCLUDE\'|\'EXCLUDE\',
                                                    \'SegmentModifier\': \'string\'
                                                }
                                            },
                                            \'Preset\': \'string\',
                                            \'VideoDescription\': {
                                                \'AfdSignaling\': \'NONE\'|\'AUTO\'|\'FIXED\',
                                                \'AntiAlias\': \'DISABLED\'|\'ENABLED\',
                                                \'CodecSettings\': {
                                                    \'Codec\': \'FRAME_CAPTURE\'|\'H_264\'|\'H_265\'|\'MPEG2\'|\'PRORES\',
                                                    \'FrameCaptureSettings\': {
                                                        \'FramerateDenominator\': 123,
                                                        \'FramerateNumerator\': 123,
                                                        \'MaxCaptures\': 123,
                                                        \'Quality\': 123
                                                    },
                                                    \'H264Settings\': {
                                                        \'AdaptiveQuantization\': \'OFF\'|\'LOW\'|\'MEDIUM\'|\'HIGH\'|\'HIGHER\'|\'MAX\',
                                                        \'Bitrate\': 123,
                                                        \'CodecLevel\': \'AUTO\'|\'LEVEL_1\'|\'LEVEL_1_1\'|\'LEVEL_1_2\'|\'LEVEL_1_3\'|\'LEVEL_2\'|\'LEVEL_2_1\'|\'LEVEL_2_2\'|\'LEVEL_3\'|\'LEVEL_3_1\'|\'LEVEL_3_2\'|\'LEVEL_4\'|\'LEVEL_4_1\'|\'LEVEL_4_2\'|\'LEVEL_5\'|\'LEVEL_5_1\'|\'LEVEL_5_2\',
                                                        \'CodecProfile\': \'BASELINE\'|\'HIGH\'|\'HIGH_10BIT\'|\'HIGH_422\'|\'HIGH_422_10BIT\'|\'MAIN\',
                                                        \'DynamicSubGop\': \'ADAPTIVE\'|\'STATIC\',
                                                        \'EntropyEncoding\': \'CABAC\'|\'CAVLC\',
                                                        \'FieldEncoding\': \'PAFF\'|\'FORCE_FIELD\',
                                                        \'FlickerAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\',
                                                        \'FramerateControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                                        \'FramerateConversionAlgorithm\': \'DUPLICATE_DROP\'|\'INTERPOLATE\',
                                                        \'FramerateDenominator\': 123,
                                                        \'FramerateNumerator\': 123,
                                                        \'GopBReference\': \'DISABLED\'|\'ENABLED\',
                                                        \'GopClosedCadence\': 123,
                                                        \'GopSize\': 123.0,
                                                        \'GopSizeUnits\': \'FRAMES\'|\'SECONDS\',
                                                        \'HrdBufferInitialFillPercentage\': 123,
                                                        \'HrdBufferSize\': 123,
                                                        \'InterlaceMode\': \'PROGRESSIVE\'|\'TOP_FIELD\'|\'BOTTOM_FIELD\'|\'FOLLOW_TOP_FIELD\'|\'FOLLOW_BOTTOM_FIELD\',
                                                        \'MaxBitrate\': 123,
                                                        \'MinIInterval\': 123,
                                                        \'NumberBFramesBetweenReferenceFrames\': 123,
                                                        \'NumberReferenceFrames\': 123,
                                                        \'ParControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                                        \'ParDenominator\': 123,
                                                        \'ParNumerator\': 123,
                                                        \'QualityTuningLevel\': \'SINGLE_PASS\'|\'SINGLE_PASS_HQ\'|\'MULTI_PASS_HQ\',
                                                        \'QvbrSettings\': {
                                                            \'MaxAverageBitrate\': 123,
                                                            \'QvbrQualityLevel\': 123
                                                        },
                                                        \'RateControlMode\': \'VBR\'|\'CBR\'|\'QVBR\',
                                                        \'RepeatPps\': \'DISABLED\'|\'ENABLED\',
                                                        \'SceneChangeDetect\': \'DISABLED\'|\'ENABLED\',
                                                        \'Slices\': 123,
                                                        \'SlowPal\': \'DISABLED\'|\'ENABLED\',
                                                        \'Softness\': 123,
                                                        \'SpatialAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\',
                                                        \'Syntax\': \'DEFAULT\'|\'RP2027\',
                                                        \'Telecine\': \'NONE\'|\'SOFT\'|\'HARD\',
                                                        \'TemporalAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\',
                                                        \'UnregisteredSeiTimecode\': \'DISABLED\'|\'ENABLED\'
                                                    },
                                                    \'H265Settings\': {
                                                        \'AdaptiveQuantization\': \'OFF\'|\'LOW\'|\'MEDIUM\'|\'HIGH\'|\'HIGHER\'|\'MAX\',
                                                        \'AlternateTransferFunctionSei\': \'DISABLED\'|\'ENABLED\',
                                                        \'Bitrate\': 123,
                                                        \'CodecLevel\': \'AUTO\'|\'LEVEL_1\'|\'LEVEL_2\'|\'LEVEL_2_1\'|\'LEVEL_3\'|\'LEVEL_3_1\'|\'LEVEL_4\'|\'LEVEL_4_1\'|\'LEVEL_5\'|\'LEVEL_5_1\'|\'LEVEL_5_2\'|\'LEVEL_6\'|\'LEVEL_6_1\'|\'LEVEL_6_2\',
                                                        \'CodecProfile\': \'MAIN_MAIN\'|\'MAIN_HIGH\'|\'MAIN10_MAIN\'|\'MAIN10_HIGH\'|\'MAIN_422_8BIT_MAIN\'|\'MAIN_422_8BIT_HIGH\'|\'MAIN_422_10BIT_MAIN\'|\'MAIN_422_10BIT_HIGH\',
                                                        \'DynamicSubGop\': \'ADAPTIVE\'|\'STATIC\',
                                                        \'FlickerAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\',
                                                        \'FramerateControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                                        \'FramerateConversionAlgorithm\': \'DUPLICATE_DROP\'|\'INTERPOLATE\',
                                                        \'FramerateDenominator\': 123,
                                                        \'FramerateNumerator\': 123,
                                                        \'GopBReference\': \'DISABLED\'|\'ENABLED\',
                                                        \'GopClosedCadence\': 123,
                                                        \'GopSize\': 123.0,
                                                        \'GopSizeUnits\': \'FRAMES\'|\'SECONDS\',
                                                        \'HrdBufferInitialFillPercentage\': 123,
                                                        \'HrdBufferSize\': 123,
                                                        \'InterlaceMode\': \'PROGRESSIVE\'|\'TOP_FIELD\'|\'BOTTOM_FIELD\'|\'FOLLOW_TOP_FIELD\'|\'FOLLOW_BOTTOM_FIELD\',
                                                        \'MaxBitrate\': 123,
                                                        \'MinIInterval\': 123,
                                                        \'NumberBFramesBetweenReferenceFrames\': 123,
                                                        \'NumberReferenceFrames\': 123,
                                                        \'ParControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                                        \'ParDenominator\': 123,
                                                        \'ParNumerator\': 123,
                                                        \'QualityTuningLevel\': \'SINGLE_PASS\'|\'SINGLE_PASS_HQ\'|\'MULTI_PASS_HQ\',
                                                        \'QvbrSettings\': {
                                                            \'MaxAverageBitrate\': 123,
                                                            \'QvbrQualityLevel\': 123
                                                        },
                                                        \'RateControlMode\': \'VBR\'|\'CBR\'|\'QVBR\',
                                                        \'SampleAdaptiveOffsetFilterMode\': \'DEFAULT\'|\'ADAPTIVE\'|\'OFF\',
                                                        \'SceneChangeDetect\': \'DISABLED\'|\'ENABLED\',
                                                        \'Slices\': 123,
                                                        \'SlowPal\': \'DISABLED\'|\'ENABLED\',
                                                        \'SpatialAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\',
                                                        \'Telecine\': \'NONE\'|\'SOFT\'|\'HARD\',
                                                        \'TemporalAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\',
                                                        \'TemporalIds\': \'DISABLED\'|\'ENABLED\',
                                                        \'Tiles\': \'DISABLED\'|\'ENABLED\',
                                                        \'UnregisteredSeiTimecode\': \'DISABLED\'|\'ENABLED\',
                                                        \'WriteMp4PackagingType\': \'HVC1\'|\'HEV1\'
                                                    },
                                                    \'Mpeg2Settings\': {
                                                        \'AdaptiveQuantization\': \'OFF\'|\'LOW\'|\'MEDIUM\'|\'HIGH\',
                                                        \'Bitrate\': 123,
                                                        \'CodecLevel\': \'AUTO\'|\'LOW\'|\'MAIN\'|\'HIGH1440\'|\'HIGH\',
                                                        \'CodecProfile\': \'MAIN\'|\'PROFILE_422\',
                                                        \'DynamicSubGop\': \'ADAPTIVE\'|\'STATIC\',
                                                        \'FramerateControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                                        \'FramerateConversionAlgorithm\': \'DUPLICATE_DROP\'|\'INTERPOLATE\',
                                                        \'FramerateDenominator\': 123,
                                                        \'FramerateNumerator\': 123,
                                                        \'GopClosedCadence\': 123,
                                                        \'GopSize\': 123.0,
                                                        \'GopSizeUnits\': \'FRAMES\'|\'SECONDS\',
                                                        \'HrdBufferInitialFillPercentage\': 123,
                                                        \'HrdBufferSize\': 123,
                                                        \'InterlaceMode\': \'PROGRESSIVE\'|\'TOP_FIELD\'|\'BOTTOM_FIELD\'|\'FOLLOW_TOP_FIELD\'|\'FOLLOW_BOTTOM_FIELD\',
                                                        \'IntraDcPrecision\': \'AUTO\'|\'INTRA_DC_PRECISION_8\'|\'INTRA_DC_PRECISION_9\'|\'INTRA_DC_PRECISION_10\'|\'INTRA_DC_PRECISION_11\',
                                                        \'MaxBitrate\': 123,
                                                        \'MinIInterval\': 123,
                                                        \'NumberBFramesBetweenReferenceFrames\': 123,
                                                        \'ParControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                                        \'ParDenominator\': 123,
                                                        \'ParNumerator\': 123,
                                                        \'QualityTuningLevel\': \'SINGLE_PASS\'|\'MULTI_PASS\',
                                                        \'RateControlMode\': \'VBR\'|\'CBR\',
                                                        \'SceneChangeDetect\': \'DISABLED\'|\'ENABLED\',
                                                        \'SlowPal\': \'DISABLED\'|\'ENABLED\',
                                                        \'Softness\': 123,
                                                        \'SpatialAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\',
                                                        \'Syntax\': \'DEFAULT\'|\'D_10\',
                                                        \'Telecine\': \'NONE\'|\'SOFT\'|\'HARD\',
                                                        \'TemporalAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\'
                                                    },
                                                    \'ProresSettings\': {
                                                        \'CodecProfile\': \'APPLE_PRORES_422\'|\'APPLE_PRORES_422_HQ\'|\'APPLE_PRORES_422_LT\'|\'APPLE_PRORES_422_PROXY\',
                                                        \'FramerateControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                                        \'FramerateConversionAlgorithm\': \'DUPLICATE_DROP\'|\'INTERPOLATE\',
                                                        \'FramerateDenominator\': 123,
                                                        \'FramerateNumerator\': 123,
                                                        \'InterlaceMode\': \'PROGRESSIVE\'|\'TOP_FIELD\'|\'BOTTOM_FIELD\'|\'FOLLOW_TOP_FIELD\'|\'FOLLOW_BOTTOM_FIELD\',
                                                        \'ParControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                                        \'ParDenominator\': 123,
                                                        \'ParNumerator\': 123,
                                                        \'SlowPal\': \'DISABLED\'|\'ENABLED\',
                                                        \'Telecine\': \'NONE\'|\'HARD\'
                                                    }
                                                },
                                                \'ColorMetadata\': \'IGNORE\'|\'INSERT\',
                                                \'Crop\': {
                                                    \'Height\': 123,
                                                    \'Width\': 123,
                                                    \'X\': 123,
                                                    \'Y\': 123
                                                },
                                                \'DropFrameTimecode\': \'DISABLED\'|\'ENABLED\',
                                                \'FixedAfd\': 123,
                                                \'Height\': 123,
                                                \'Position\': {
                                                    \'Height\': 123,
                                                    \'Width\': 123,
                                                    \'X\': 123,
                                                    \'Y\': 123
                                                },
                                                \'RespondToAfd\': \'NONE\'|\'RESPOND\'|\'PASSTHROUGH\',
                                                \'ScalingBehavior\': \'DEFAULT\'|\'STRETCH_TO_OUTPUT\',
                                                \'Sharpness\': 123,
                                                \'TimecodeInsertion\': \'DISABLED\'|\'PIC_TIMING_SEI\',
                                                \'VideoPreprocessors\': {
                                                    \'ColorCorrector\': {
                                                        \'Brightness\': 123,
                                                        \'ColorSpaceConversion\': \'NONE\'|\'FORCE_601\'|\'FORCE_709\'|\'FORCE_HDR10\'|\'FORCE_HLG_2020\',
                                                        \'Contrast\': 123,
                                                        \'Hdr10Metadata\': {
                                                            \'BluePrimaryX\': 123,
                                                            \'BluePrimaryY\': 123,
                                                            \'GreenPrimaryX\': 123,
                                                            \'GreenPrimaryY\': 123,
                                                            \'MaxContentLightLevel\': 123,
                                                            \'MaxFrameAverageLightLevel\': 123,
                                                            \'MaxLuminance\': 123,
                                                            \'MinLuminance\': 123,
                                                            \'RedPrimaryX\': 123,
                                                            \'RedPrimaryY\': 123,
                                                            \'WhitePointX\': 123,
                                                            \'WhitePointY\': 123
                                                        },
                                                        \'Hue\': 123,
                                                        \'Saturation\': 123
                                                    },
                                                    \'Deinterlacer\': {
                                                        \'Algorithm\': \'INTERPOLATE\'|\'INTERPOLATE_TICKER\'|\'BLEND\'|\'BLEND_TICKER\',
                                                        \'Control\': \'FORCE_ALL_FRAMES\'|\'NORMAL\',
                                                        \'Mode\': \'DEINTERLACE\'|\'INVERSE_TELECINE\'|\'ADAPTIVE\'
                                                    },
                                                    \'ImageInserter\': {
                                                        \'InsertableImages\': [
                                                            {
                                                                \'Duration\': 123,
                                                                \'FadeIn\': 123,
                                                                \'FadeOut\': 123,
                                                                \'Height\': 123,
                                                                \'ImageInserterInput\': \'string\',
                                                                \'ImageX\': 123,
                                                                \'ImageY\': 123,
                                                                \'Layer\': 123,
                                                                \'Opacity\': 123,
                                                                \'StartTime\': \'string\',
                                                                \'Width\': 123
                                                            },
                                                        ]
                                                    },
                                                    \'NoiseReducer\': {
                                                        \'Filter\': \'BILATERAL\'|\'MEAN\'|\'GAUSSIAN\'|\'LANCZOS\'|\'SHARPEN\'|\'CONSERVE\'|\'SPATIAL\',
                                                        \'FilterSettings\': {
                                                            \'Strength\': 123
                                                        },
                                                        \'SpatialFilterSettings\': {
                                                            \'PostFilterSharpenStrength\': 123,
                                                            \'Speed\': 123,
                                                            \'Strength\': 123
                                                        }
                                                    },
                                                    \'TimecodeBurnin\': {
                                                        \'FontSize\': 123,
                                                        \'Position\': \'TOP_CENTER\'|\'TOP_LEFT\'|\'TOP_RIGHT\'|\'MIDDLE_LEFT\'|\'MIDDLE_CENTER\'|\'MIDDLE_RIGHT\'|\'BOTTOM_LEFT\'|\'BOTTOM_CENTER\'|\'BOTTOM_RIGHT\',
                                                        \'Prefix\': \'string\'
                                                    }
                                                },
                                                \'Width\': 123
                                            }
                                        },
                                    ]
                                },
                            ],
                            \'TimecodeConfig\': {
                                \'Anchor\': \'string\',
                                \'Source\': \'EMBEDDED\'|\'ZEROBASED\'|\'SPECIFIEDSTART\',
                                \'Start\': \'string\',
                                \'TimestampOffset\': \'string\'
                            },
                            \'TimedMetadataInsertion\': {
                                \'Id3Insertions\': [
                                    {
                                        \'Id3\': \'string\',
                                        \'Timecode\': \'string\'
                                    },
                                ]
                            }
                        },
                        \'Status\': \'SUBMITTED\'|\'PROGRESSING\'|\'COMPLETE\'|\'CANCELED\'|\'ERROR\',
                        \'Timing\': {
                            \'FinishTime\': datetime(2015, 1, 1),
                            \'StartTime\': datetime(2015, 1, 1),
                            \'SubmitTime\': datetime(2015, 1, 1)
                        },
                        \'UserMetadata\': {
                            \'string\': \'string\'
                        }
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Jobs** *(list) --* List of jobs
              
              - *(dict) --* Each job converts an input file into an output file or files. For more information, see the User Guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html
                
                - **Arn** *(string) --* An identifier for this resource that is unique within all of AWS.
                
                - **BillingTagsSource** *(string) --* Optional. Choose a tag type that AWS Billing and Cost Management will use to sort your AWS Elemental MediaConvert costs on any billing report that you set up. Any transcoding outputs that don\'t have an associated tag will appear in your billing report unsorted. If you don\'t choose a valid value for this field, your job outputs will appear on the billing report unsorted.
                
                - **CreatedAt** *(datetime) --* The time, in Unix epoch format in seconds, when the job got created.
                
                - **ErrorCode** *(integer) --* Error code for the job
                
                - **ErrorMessage** *(string) --* Error message of Job
                
                - **Id** *(string) --* A portion of the job\'s ARN, unique within your AWS Elemental MediaConvert resources
                
                - **JobTemplate** *(string) --* The job template that the job is created from, if it is created from a job template.
                
                - **OutputGroupDetails** *(list) --* List of output group details
                  
                  - *(dict) --* Contains details about the output groups specified in the job settings.
                    
                    - **OutputDetails** *(list) --* Details about the output
                      
                      - *(dict) --* Details regarding output
                        
                        - **DurationInMs** *(integer) --* Duration in milliseconds
                        
                        - **VideoDetails** *(dict) --* Contains details about the output\'s video stream
                          
                          - **HeightInPx** *(integer) --* Height in pixels for the output
                          
                          - **WidthInPx** *(integer) --* Width in pixels for the output
                      
                - **Queue** *(string) --* Optional. When you create a job, you can specify a queue to send it to. If you don\'t specify, the job will go to the default queue. For more about queues, see the User Guide topic at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html
                
                - **Role** *(string) --* The IAM role you use for creating this job. For details about permissions, see the User Guide topic at the User Guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html
                
                - **Settings** *(dict) --* JobSettings contains all the transcode settings for a job.
                  
                  - **AdAvailOffset** *(integer) --* When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time.
                  
                  - **AvailBlanking** *(dict) --* Settings for ad avail blanking. Video can be blanked or overlaid with an image, and audio muted during SCTE-35 triggered ad avails.
                    
                    - **AvailBlankingImage** *(string) --* Blanking image to be used. Leave empty for solid black. Only bmp and png images are supported.
                
                  - **Inputs** *(list) --* Use Inputs (inputs) to define source file used in the transcode job. There can be multiple inputs add in a job. These inputs will be concantenated together to create the output.
                    
                    - *(dict) --* Specifies media input
                      
                      - **AudioSelectorGroups** *(dict) --* Specifies set of audio selectors within an input to combine. An input may have multiple audio selector groups. See \"Audio Selector Group\":#inputs-audio_selector_group for more information.
                        
                        - *(string) --* 
                          
                          - *(dict) --* Group of Audio Selectors
                            
                            - **AudioSelectorNames** *(list) --* Name of an Audio Selector within the same input to include in the group. Audio selector names are standardized, based on their order within the input (e.g., \"Audio Selector 1\"). The audio selector name parameter can be repeated to add any number of audio selectors to the group.
                              
                              - *(string) --* 
                          
                      - **AudioSelectors** *(dict) --* Use Audio selectors (AudioSelectors) to specify a track or set of tracks from the input that you will use in your outputs. You can use mutiple Audio selectors per input.
                        
                        - *(string) --* 
                          
                          - *(dict) --* Selector for Audio
                            
                            - **CustomLanguageCode** *(string) --* Selects a specific language code from within an audio source, using the ISO 639-2 or ISO 639-3 three-letter language code
                            
                            - **DefaultSelection** *(string) --* Enable this setting on one audio selector to set it as the default for the job. The service uses this default for outputs where it can\'t find the specified input audio. If you don\'t set a default, those outputs have no audio.
                            
                            - **ExternalAudioFileInput** *(string) --* Specifies audio data from an external file source.
                            
                            - **LanguageCode** *(string) --* Selects a specific language code from within an audio source.
                            
                            - **Offset** *(integer) --* Specifies a time delta in milliseconds to offset the audio from the input video.
                            
                            - **Pids** *(list) --* Selects a specific PID from within an audio source (e.g. 257 selects PID 0x101).
                              
                              - *(integer) --* 
                          
                            - **ProgramSelection** *(integer) --* Use this setting for input streams that contain Dolby E, to have the service extract specific program data from the track. To select multiple programs, create multiple selectors with the same Track and different Program numbers. In the console, this setting is visible when you set Selector type to Track. Choose the program number from the dropdown list. If you are sending a JSON file, provide the program ID, which is part of the audio metadata. If your input file has incorrect metadata, you can choose All channels instead of a program number to have the service ignore the program IDs and include all the programs in the track.
                            
                            - **RemixSettings** *(dict) --* Use these settings to reorder the audio channels of one input to match those of another input. This allows you to combine the two files into a single output, one after the other.
                              
                              - **ChannelMapping** *(dict) --* Channel mapping (ChannelMapping) contains the group of fields that hold the remixing value for each channel. Units are in dB. Acceptable values are within the range from -60 (mute) through 6. A setting of 0 passes the input channel unchanged to the output channel (no attenuation or amplification).
                                
                                - **OutputChannels** *(list) --* List of output channels
                                  
                                  - *(dict) --* OutputChannel mapping settings.
                                    
                                    - **InputChannels** *(list) --* List of input channels
                                      
                                      - *(integer) --* 
                                  
                              - **ChannelsIn** *(integer) --* Specify the number of audio channels from your input that you want to use in your output. With remixing, you might combine or split the data in these channels, so the number of channels in your final output might be different.
                              
                              - **ChannelsOut** *(integer) --* Specify the number of channels in this output after remixing. Valid values: 1, 2, 4, 6, 8
                          
                            - **SelectorType** *(string) --* Specifies the type of the audio selector.
                            
                            - **Tracks** *(list) --* Identify a track from the input audio to include in this selector by entering the track index number. To include several tracks in a single audio selector, specify multiple tracks as follows. Using the console, enter a comma-separated list. For examle, type \"1,2,3\" to include tracks 1 through 3. Specifying directly in your JSON job file, provide the track numbers in an array. For example, \"tracks\": [1,2,3].
                              
                              - *(integer) --* 
                          
                      - **CaptionSelectors** *(dict) --* Use Captions selectors (CaptionSelectors) to specify the captions data from the input that you will use in your outputs. You can use mutiple captions selectors per input.
                        
                        - *(string) --* 
                          
                          - *(dict) --* Set up captions in your outputs by first selecting them from your input here.
                            
                            - **CustomLanguageCode** *(string) --* The specific language to extract from source, using the ISO 639-2 or ISO 639-3 three-letter language code. If input is SCTE-27, complete this field and/or PID to select the caption language to extract. If input is DVB-Sub and output is Burn-in or SMPTE-TT, complete this field and/or PID to select the caption language to extract. If input is DVB-Sub that is being passed through, omit this field (and PID field); there is no way to extract a specific language with pass-through captions.
                            
                            - **LanguageCode** *(string) --* The specific language to extract from source. If input is SCTE-27, complete this field and/or PID to select the caption language to extract. If input is DVB-Sub and output is Burn-in or SMPTE-TT, complete this field and/or PID to select the caption language to extract. If input is DVB-Sub that is being passed through, omit this field (and PID field); there is no way to extract a specific language with pass-through captions.
                            
                            - **SourceSettings** *(dict) --* Source settings (SourceSettings) contains the group of settings for captions in the input.
                              
                              - **AncillarySourceSettings** *(dict) --* Settings for ancillary captions source.
                                
                                - **SourceAncillaryChannelNumber** *(integer) --* Specifies the 608 channel number in the ancillary data track from which to extract captions. Unused for passthrough.
                            
                              - **DvbSubSourceSettings** *(dict) --* DVB Sub Source Settings
                                
                                - **Pid** *(integer) --* When using DVB-Sub with Burn-In or SMPTE-TT, use this PID for the source content. Unused for DVB-Sub passthrough. All DVB-Sub content is passed through, regardless of selectors.
                            
                              - **EmbeddedSourceSettings** *(dict) --* Settings for embedded captions Source
                                
                                - **Convert608To708** *(string) --* When set to UPCONVERT, 608 data is both passed through via the \"608 compatibility bytes\" fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded.
                                
                                - **Source608ChannelNumber** *(integer) --* Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough.
                                
                                - **Source608TrackNumber** *(integer) --* Specifies the video track index used for extracting captions. The system only supports one input video track, so this should always be set to \'1\'.
                            
                              - **FileSourceSettings** *(dict) --* Settings for File-based Captions in Source
                                
                                - **Convert608To708** *(string) --* If set to UPCONVERT, 608 caption data is both passed through via the \"608 compatibility bytes\" fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded.
                                
                                - **SourceFile** *(string) --* External caption file used for loading captions. Accepted file extensions are \'scc\', \'ttml\', \'dfxp\', \'stl\', \'srt\', and \'smi\'.
                                
                                - **TimeDelta** *(integer) --* Specifies a time delta in seconds to offset the captions from the source file.
                            
                              - **SourceType** *(string) --* Use Source (SourceType) to identify the format of your input captions. The service cannot auto-detect caption format.
                              
                              - **TeletextSourceSettings** *(dict) --* Settings specific to Teletext caption sources, including Page number.
                                
                                - **PageNumber** *(string) --* Use Page Number (PageNumber) to specify the three-digit hexadecimal page number that will be used for Teletext captions. Do not use this setting if you are passing through teletext from the input source to output.
                            
                      - **DeblockFilter** *(string) --* Enable Deblock (InputDeblockFilter) to produce smoother motion in the output. Default is disabled. Only manaully controllable for MPEG2 and uncompressed video inputs.
                      
                      - **DenoiseFilter** *(string) --* Enable Denoise (InputDenoiseFilter) to filter noise from the input. Default is disabled. Only applicable to MPEG2, H.264, H.265, and uncompressed video inputs.
                      
                      - **FileInput** *(string) --* Use Input (fileInput) to define the source file used in the transcode job. There can be multiple inputs in a job. These inputs are concantenated, in the order they are specified in the job, to create the output.
                      
                      - **FilterEnable** *(string) --* Use Filter enable (InputFilterEnable) to specify how the transcoding service applies the denoise and deblock filters. You must also enable the filters separately, with Denoise (InputDenoiseFilter) and Deblock (InputDeblockFilter). * Auto - The transcoding service determines whether to apply filtering, depending on input type and quality. * Disable - The input is not filtered. This is true even if you use the API to enable them in (InputDeblockFilter) and (InputDeblockFilter). * Force - The in put is filtered regardless of input type.
                      
                      - **FilterStrength** *(integer) --* Use Filter strength (FilterStrength) to adjust the magnitude the input filter settings (Deblock and Denoise). The range is -5 to 5. Default is 0.
                      
                      - **InputClippings** *(list) --* (InputClippings) contains sets of start and end times that together specify a portion of the input to be used in the outputs. If you provide only a start time, the clip will be the entire input from that point to the end. If you provide only an end time, it will be the entire input up to that point. When you specify more than one input clip, the transcoding service creates the job outputs by stringing the clips together in the order you specify them.
                        
                        - *(dict) --* To transcode only portions of your input (clips), include one Input clipping (one instance of InputClipping in the JSON job file) for each input clip. All input clips you specify will be included in every output of the job.
                          
                          - **EndTimecode** *(string) --* Set End timecode (EndTimecode) to the end of the portion of the input you are clipping. The frame corresponding to the End timecode value is included in the clip. Start timecode or End timecode may be left blank, but not both. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When choosing this value, take into account your setting for timecode source under input settings (InputTimecodeSource). For example, if you have embedded timecodes that start at 01:00:00:00 and you want your clip to end six minutes into the video, use 01:06:00:00.
                          
                          - **StartTimecode** *(string) --* Set Start timecode (StartTimecode) to the beginning of the portion of the input you are clipping. The frame corresponding to the Start timecode value is included in the clip. Start timecode or End timecode may be left blank, but not both. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When choosing this value, take into account your setting for Input timecode source. For example, if you have embedded timecodes that start at 01:00:00:00 and you want your clip to begin five minutes into the video, use 01:05:00:00.
                      
                      - **ProgramNumber** *(integer) --* Use Program (programNumber) to select a specific program from within a multi-program transport stream. Note that Quad 4K is not currently supported. Default is the first program within the transport stream. If the program you specify doesn\'t exist, the transcoding service will use this default.
                      
                      - **PsiControl** *(string) --* Set PSI control (InputPsiControl) for transport stream inputs to specify which data the demux process to scans. * Ignore PSI - Scan all PIDs for audio and video. * Use PSI - Scan only PSI data.
                      
                      - **TimecodeSource** *(string) --* Timecode source under input settings (InputTimecodeSource) only affects the behavior of features that apply to a single input at a time, such as input clipping and synchronizing some captions formats. Use this setting to specify whether the service counts frames by timecodes embedded in the video (EMBEDDED) or by starting the first frame at zero (ZEROBASED). In both cases, the timecode format is HH:MM:SS:FF or HH:MM:SS;FF, where FF is the frame number. Only set this to EMBEDDED if your source video has embedded timecodes.
                      
                      - **VideoSelector** *(dict) --* Selector for video.
                        
                        - **ColorSpace** *(string) --* If your input video has accurate color space metadata, or if you don\'t know about color space, leave this set to the default value FOLLOW. The service will automatically detect your input color space. If your input video has metadata indicating the wrong color space, or if your input video is missing color space metadata that should be there, specify the accurate color space here. If you choose HDR10, you can also correct inaccurate color space coefficients, using the HDR master display information controls. You must also set Color space usage (ColorSpaceUsage) to FORCE for the service to use these values.
                        
                        - **ColorSpaceUsage** *(string) --* There are two sources for color metadata, the input file and the job configuration (in the Color space and HDR master display informaiton settings). The Color space usage setting controls which takes precedence. FORCE: The system will use color metadata supplied by user, if any. If the user does not supply color metadata, the system will use data from the source. FALLBACK: The system will use color metadata from the source. If source has no color metadata, the system will use user-supplied color metadata values if available.
                        
                        - **Hdr10Metadata** *(dict) --* Use the HDR master display (Hdr10Metadata) settings to correct HDR metadata or to provide missing metadata. These values vary depending on the input video and must be provided by a color grader. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that these settings are not color correction. Note that if you are creating HDR outputs inside of an HLS CMAF package, to comply with the Apple specification, you must use the HVC1 for H.265 setting.
                          
                          - **BluePrimaryX** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                          
                          - **BluePrimaryY** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                          
                          - **GreenPrimaryX** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                          
                          - **GreenPrimaryY** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                          
                          - **MaxContentLightLevel** *(integer) --* Maximum light level among all samples in the coded video sequence, in units of candelas per square meter.
                          
                          - **MaxFrameAverageLightLevel** *(integer) --* Maximum average light level of any frame in the coded video sequence, in units of candelas per square meter.
                          
                          - **MaxLuminance** *(integer) --* Nominal maximum mastering display luminance in units of of 0.0001 candelas per square meter.
                          
                          - **MinLuminance** *(integer) --* Nominal minimum mastering display luminance in units of of 0.0001 candelas per square meter
                          
                          - **RedPrimaryX** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                          
                          - **RedPrimaryY** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                          
                          - **WhitePointX** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                          
                          - **WhitePointY** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                      
                        - **Pid** *(integer) --* Use PID (Pid) to select specific video data from an input file. Specify this value as an integer; the system automatically converts it to the hexidecimal value. For example, 257 selects PID 0x101. A PID, or packet identifier, is an identifier for a set of data in an MPEG-2 transport stream container.
                        
                        - **ProgramNumber** *(integer) --* Selects a specific program from within a multi-program transport stream. Note that Quad 4K is not currently supported.
                    
                  - **NielsenConfiguration** *(dict) --* Settings for Nielsen Configuration
                    
                    - **BreakoutCode** *(integer) --* Use Nielsen Configuration (NielsenConfiguration) to set the Nielsen measurement system breakout code. Supported values are 0, 3, 7, and 9.
                    
                    - **DistributorId** *(string) --* Use Distributor ID (DistributorID) to specify the distributor ID that is assigned to your organization by Neilsen.
                
                  - **OutputGroups** *(list) --* (OutputGroups) contains one group of settings for each set of outputs that share a common package type. All unpackaged files (MPEG-4, MPEG-2 TS, Quicktime, MXF, and no container) are grouped in a single output group as well. Required in (OutputGroups) is a group of settings that apply to the whole group. This required object depends on the value you set for (Type) under (OutputGroups)>(OutputGroupSettings). Type, settings object pairs are as follows. * FILE_GROUP_SETTINGS, FileGroupSettings * HLS_GROUP_SETTINGS, HlsGroupSettings * DASH_ISO_GROUP_SETTINGS, DashIsoGroupSettings * MS_SMOOTH_GROUP_SETTINGS, MsSmoothGroupSettings * CMAF_GROUP_SETTINGS, CmafGroupSettings
                    
                    - *(dict) --* Group of outputs
                      
                      - **CustomName** *(string) --* Use Custom Group Name (CustomName) to specify a name for the output group. This value is displayed on the console and can make your job settings JSON more human-readable. It does not affect your outputs. Use up to twelve characters that are either letters, numbers, spaces, or underscores.
                      
                      - **Name** *(string) --* Name of the output group
                      
                      - **OutputGroupSettings** *(dict) --* Output Group settings, including type
                        
                        - **CmafGroupSettings** *(dict) --* Required when you set (Type) under (OutputGroups)>(OutputGroupSettings) to CMAF_GROUP_SETTINGS. Each output in a CMAF Output Group may only contain a single video, audio, or caption output.
                          
                          - **BaseUrl** *(string) --* A partial URI prefix that will be put in the manifest file at the top level BaseURL element. Can be used if streams are delivered from a different URL than the manifest file.
                          
                          - **ClientCache** *(string) --* When set to ENABLED, sets #EXT-X-ALLOW-CACHE:no tag, which prevents client from saving media segments for later replay.
                          
                          - **CodecSpecification** *(string) --* Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation.
                          
                          - **Destination** *(string) --* Use Destination (Destination) to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file.
                          
                          - **Encryption** *(dict) --* DRM settings.
                            
                            - **ConstantInitializationVector** *(string) --* This is a 128-bit, 16-byte hex value represented by a 32-character text string. If this parameter is not set then the Initialization Vector will follow the segment number by default.
                            
                            - **EncryptionMethod** *(string) --* Encrypts the segments with the given encryption scheme. Leave blank to disable. Selecting \'Disabled\' in the web interface also disables encryption.
                            
                            - **InitializationVectorInManifest** *(string) --* The Initialization Vector is a 128-bit number used in conjunction with the key for encrypting blocks. If set to INCLUDE, Initialization Vector is listed in the manifest. Otherwise Initialization Vector is not in the manifest.
                            
                            - **StaticKeyProvider** *(dict) --* Settings for use with a SPEKE key provider.
                              
                              - **KeyFormat** *(string) --* Relates to DRM implementation. Sets the value of the KEYFORMAT attribute. Must be \'identity\' or a reverse DNS string. May be omitted to indicate an implicit value of \'identity\'.
                              
                              - **KeyFormatVersions** *(string) --* Relates to DRM implementation. Either a single positive integer version value or a slash delimited list of version values (1/2/3).
                              
                              - **StaticKeyValue** *(string) --* Relates to DRM implementation. Use a 32-character hexidecimal string to specify Key Value (StaticKeyValue).
                              
                              - **Url** *(string) --* Relates to DRM implementation. The location of the license server used for protecting content.
                          
                            - **Type** *(string) --* Indicates which type of key provider is used for encryption.
                        
                          - **FragmentLength** *(integer) --* Length of fragments to generate (in seconds). Fragment length must be compatible with GOP size and Framerate. Note that fragments will end on the next keyframe after this number of seconds, so actual fragment length may be longer. When Emit Single File is checked, the fragmentation is internal to a single output file and it does not cause the creation of many output files as in other output types.
                          
                          - **ManifestCompression** *(string) --* When set to GZIP, compresses HLS playlist.
                          
                          - **ManifestDurationFormat** *(string) --* Indicates whether the output manifest should use floating point values for segment duration.
                          
                          - **MinBufferTime** *(integer) --* Minimum time of initially buffered media that is needed to ensure smooth playout.
                          
                          - **MinFinalSegmentLength** *(float) --* Keep this setting at the default value of 0, unless you are troubleshooting a problem with how devices play back the end of your video asset. If you know that player devices are hanging on the final segment of your video because the length of your final segment is too short, use this setting to specify a minimum final segment length, in seconds. Choose a value that is greater than or equal to 1 and less than your segment length. When you specify a value for this setting, the encoder will combine any final segment that is shorter than the length that you specify with the previous segment. For example, your segment length is 3 seconds and your final segment is .5 seconds without a minimum final segment length; when you set the minimum final segment length to 1, your final segment is 3.5 seconds.
                          
                          - **SegmentControl** *(string) --* When set to SINGLE_FILE, a single output file is generated, which is internally segmented using the Fragment Length and Segment Length. When set to SEGMENTED_FILES, separate segment files will be created.
                          
                          - **SegmentLength** *(integer) --* Use this setting to specify the length, in seconds, of each individual CMAF segment. This value applies to the whole package; that is, to every output in the output group. Note that segments end on the first keyframe after this number of seconds, so the actual segment length might be slightly longer. If you set Segment control (CmafSegmentControl) to single file, the service puts the content of each output in a single file that has metadata that marks these segments. If you set it to segmented files, the service creates multiple files for each output, each with the content of one segment.
                          
                          - **StreamInfResolution** *(string) --* Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest.
                          
                          - **WriteDashManifest** *(string) --* When set to ENABLED, a DASH MPD manifest will be generated for this output.
                          
                          - **WriteHlsManifest** *(string) --* When set to ENABLED, an Apple HLS manifest will be generated for this output.
                      
                        - **DashIsoGroupSettings** *(dict) --* Required when you set (Type) under (OutputGroups)>(OutputGroupSettings) to DASH_ISO_GROUP_SETTINGS.
                          
                          - **BaseUrl** *(string) --* A partial URI prefix that will be put in the manifest (.mpd) file at the top level BaseURL element. Can be used if streams are delivered from a different URL than the manifest file.
                          
                          - **Destination** *(string) --* Use Destination (Destination) to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file.
                          
                          - **Encryption** *(dict) --* DRM settings.
                            
                            - **SpekeKeyProvider** *(dict) --* Settings for use with a SPEKE key provider
                              
                              - **ResourceId** *(string) --* The SPEKE-compliant server uses Resource ID (ResourceId) to identify content.
                              
                              - **SystemIds** *(list) --* Relates to SPEKE implementation. DRM system identifiers. DASH output groups support a max of two system ids. Other group types support one system id.
                                
                                - *(string) --* 
                            
                              - **Url** *(string) --* Use URL (Url) to specify the SPEKE-compliant server that will provide keys for content.
                          
                          - **FragmentLength** *(integer) --* Length of fragments to generate (in seconds). Fragment length must be compatible with GOP size and Framerate. Note that fragments will end on the next keyframe after this number of seconds, so actual fragment length may be longer. When Emit Single File is checked, the fragmentation is internal to a single output file and it does not cause the creation of many output files as in other output types.
                          
                          - **HbbtvCompliance** *(string) --* Supports HbbTV specification as indicated
                          
                          - **MinBufferTime** *(integer) --* Minimum time of initially buffered media that is needed to ensure smooth playout.
                          
                          - **SegmentControl** *(string) --* When set to SINGLE_FILE, a single output file is generated, which is internally segmented using the Fragment Length and Segment Length. When set to SEGMENTED_FILES, separate segment files will be created.
                          
                          - **SegmentLength** *(integer) --* Length of mpd segments to create (in seconds). Note that segments will end on the next keyframe after this number of seconds, so actual segment length may be longer. When Emit Single File is checked, the segmentation is internal to a single output file and it does not cause the creation of many output files as in other output types.
                          
                          - **WriteSegmentTimelineInRepresentation** *(string) --* When ENABLED, segment durations are indicated in the manifest using SegmentTimeline and SegmentTimeline will be promoted down into Representation from AdaptationSet.
                      
                        - **FileGroupSettings** *(dict) --* Required when you set (Type) under (OutputGroups)>(OutputGroupSettings) to FILE_GROUP_SETTINGS.
                          
                          - **Destination** *(string) --* Use Destination (Destination) to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file.
                      
                        - **HlsGroupSettings** *(dict) --* Required when you set (Type) under (OutputGroups)>(OutputGroupSettings) to HLS_GROUP_SETTINGS.
                          
                          - **AdMarkers** *(list) --* Choose one or more ad marker types to pass SCTE35 signals through to this group of Apple HLS outputs.
                            
                            - *(string) --* 
                        
                          - **BaseUrl** *(string) --* A partial URI prefix that will be prepended to each output in the media .m3u8 file. Can be used if base manifest is delivered from a different URL than the main .m3u8 file.
                          
                          - **CaptionLanguageMappings** *(list) --* Language to be used on Caption outputs
                            
                            - *(dict) --* Caption Language Mapping
                              
                              - **CaptionChannel** *(integer) --* Caption channel.
                              
                              - **CustomLanguageCode** *(string) --* Specify the language for this caption channel, using the ISO 639-2 or ISO 639-3 three-letter language code
                              
                              - **LanguageCode** *(string) --* Specify the language, using the ISO 639-2 three-letter code listed at https://www.loc.gov/standards/iso639-2/php/code_list.php.
                              
                              - **LanguageDescription** *(string) --* Caption language description.
                          
                          - **CaptionLanguageSetting** *(string) --* Applies only to 608 Embedded output captions. Insert: Include CLOSED-CAPTIONS lines in the manifest. Specify at least one language in the CC1 Language Code field. One CLOSED-CAPTION line is added for each Language Code you specify. Make sure to specify the languages in the order in which they appear in the original source (if the source is embedded format) or the order of the caption selectors (if the source is other than embedded). Otherwise, languages in the manifest will not match up properly with the output captions. None: Include CLOSED-CAPTIONS=NONE line in the manifest. Omit: Omit any CLOSED-CAPTIONS line from the manifest.
                          
                          - **ClientCache** *(string) --* When set to ENABLED, sets #EXT-X-ALLOW-CACHE:no tag, which prevents client from saving media segments for later replay.
                          
                          - **CodecSpecification** *(string) --* Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation.
                          
                          - **Destination** *(string) --* Use Destination (Destination) to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file.
                          
                          - **DirectoryStructure** *(string) --* Indicates whether segments should be placed in subdirectories.
                          
                          - **Encryption** *(dict) --* DRM settings.
                            
                            - **ConstantInitializationVector** *(string) --* This is a 128-bit, 16-byte hex value represented by a 32-character text string. If this parameter is not set then the Initialization Vector will follow the segment number by default.
                            
                            - **EncryptionMethod** *(string) --* Encrypts the segments with the given encryption scheme. Leave blank to disable. Selecting \'Disabled\' in the web interface also disables encryption.
                            
                            - **InitializationVectorInManifest** *(string) --* The Initialization Vector is a 128-bit number used in conjunction with the key for encrypting blocks. If set to INCLUDE, Initialization Vector is listed in the manifest. Otherwise Initialization Vector is not in the manifest.
                            
                            - **SpekeKeyProvider** *(dict) --* Settings for use with a SPEKE key provider
                              
                              - **ResourceId** *(string) --* The SPEKE-compliant server uses Resource ID (ResourceId) to identify content.
                              
                              - **SystemIds** *(list) --* Relates to SPEKE implementation. DRM system identifiers. DASH output groups support a max of two system ids. Other group types support one system id.
                                
                                - *(string) --* 
                            
                              - **Url** *(string) --* Use URL (Url) to specify the SPEKE-compliant server that will provide keys for content.
                          
                            - **StaticKeyProvider** *(dict) --* Settings for use with a SPEKE key provider.
                              
                              - **KeyFormat** *(string) --* Relates to DRM implementation. Sets the value of the KEYFORMAT attribute. Must be \'identity\' or a reverse DNS string. May be omitted to indicate an implicit value of \'identity\'.
                              
                              - **KeyFormatVersions** *(string) --* Relates to DRM implementation. Either a single positive integer version value or a slash delimited list of version values (1/2/3).
                              
                              - **StaticKeyValue** *(string) --* Relates to DRM implementation. Use a 32-character hexidecimal string to specify Key Value (StaticKeyValue).
                              
                              - **Url** *(string) --* Relates to DRM implementation. The location of the license server used for protecting content.
                          
                            - **Type** *(string) --* Indicates which type of key provider is used for encryption.
                        
                          - **ManifestCompression** *(string) --* When set to GZIP, compresses HLS playlist.
                          
                          - **ManifestDurationFormat** *(string) --* Indicates whether the output manifest should use floating point values for segment duration.
                          
                          - **MinFinalSegmentLength** *(float) --* Keep this setting at the default value of 0, unless you are troubleshooting a problem with how devices play back the end of your video asset. If you know that player devices are hanging on the final segment of your video because the length of your final segment is too short, use this setting to specify a minimum final segment length, in seconds. Choose a value that is greater than or equal to 1 and less than your segment length. When you specify a value for this setting, the encoder will combine any final segment that is shorter than the length that you specify with the previous segment. For example, your segment length is 3 seconds and your final segment is .5 seconds without a minimum final segment length; when you set the minimum final segment length to 1, your final segment is 3.5 seconds.
                          
                          - **MinSegmentLength** *(integer) --* When set, Minimum Segment Size is enforced by looking ahead and back within the specified range for a nearby avail and extending the segment size if needed.
                          
                          - **OutputSelection** *(string) --* Indicates whether the .m3u8 manifest file should be generated for this HLS output group.
                          
                          - **ProgramDateTime** *(string) --* Includes or excludes EXT-X-PROGRAM-DATE-TIME tag in .m3u8 manifest files. The value is calculated as follows: either the program date and time are initialized using the input timecode source, or the time is initialized using the input timecode source and the date is initialized using the timestamp_offset.
                          
                          - **ProgramDateTimePeriod** *(integer) --* Period of insertion of EXT-X-PROGRAM-DATE-TIME entry, in seconds.
                          
                          - **SegmentControl** *(string) --* When set to SINGLE_FILE, emits program as a single media resource (.ts) file, uses #EXT-X-BYTERANGE tags to index segment for playback.
                          
                          - **SegmentLength** *(integer) --* Length of MPEG-2 Transport Stream segments to create (in seconds). Note that segments will end on the next keyframe after this number of seconds, so actual segment length may be longer.
                          
                          - **SegmentsPerSubdirectory** *(integer) --* Number of segments to write to a subdirectory before starting a new one. directoryStructure must be SINGLE_DIRECTORY for this setting to have an effect.
                          
                          - **StreamInfResolution** *(string) --* Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest.
                          
                          - **TimedMetadataId3Frame** *(string) --* Indicates ID3 frame that has the timecode.
                          
                          - **TimedMetadataId3Period** *(integer) --* Timed Metadata interval in seconds.
                          
                          - **TimestampDeltaMilliseconds** *(integer) --* Provides an extra millisecond delta offset to fine tune the timestamps.
                      
                        - **MsSmoothGroupSettings** *(dict) --* Required when you set (Type) under (OutputGroups)>(OutputGroupSettings) to MS_SMOOTH_GROUP_SETTINGS.
                          
                          - **AudioDeduplication** *(string) --* COMBINE_DUPLICATE_STREAMS combines identical audio encoding settings across a Microsoft Smooth output group into a single audio stream.
                          
                          - **Destination** *(string) --* Use Destination (Destination) to specify the S3 output location and the output filename base. Destination accepts format identifiers. If you do not specify the base filename in the URI, the service will use the filename of the input file. If your job has multiple inputs, the service uses the filename of the first input file.
                          
                          - **Encryption** *(dict) --* If you are using DRM, set DRM System (MsSmoothEncryptionSettings) to specify the value SpekeKeyProvider.
                            
                            - **SpekeKeyProvider** *(dict) --* Settings for use with a SPEKE key provider
                              
                              - **ResourceId** *(string) --* The SPEKE-compliant server uses Resource ID (ResourceId) to identify content.
                              
                              - **SystemIds** *(list) --* Relates to SPEKE implementation. DRM system identifiers. DASH output groups support a max of two system ids. Other group types support one system id.
                                
                                - *(string) --* 
                            
                              - **Url** *(string) --* Use URL (Url) to specify the SPEKE-compliant server that will provide keys for content.
                          
                          - **FragmentLength** *(integer) --* Use Fragment length (FragmentLength) to specify the mp4 fragment sizes in seconds. Fragment length must be compatible with GOP size and framerate.
                          
                          - **ManifestEncoding** *(string) --* Use Manifest encoding (MsSmoothManifestEncoding) to specify the encoding format for the server and client manifest. Valid options are utf8 and utf16.
                      
                        - **Type** *(string) --* Type of output group (File group, Apple HLS, DASH ISO, Microsoft Smooth Streaming, CMAF)
                    
                      - **Outputs** *(list) --* This object holds groups of encoding settings, one group of settings per output.
                        
                        - *(dict) --* An output object describes the settings for a single output file or stream in an output group.
                          
                          - **AudioDescriptions** *(list) --* (AudioDescriptions) contains groups of audio encoding settings organized by audio codec. Include one instance of (AudioDescriptions) per output. (AudioDescriptions) can contain multiple groups of encoding settings.
                            
                            - *(dict) --* Description of audio output
                              
                              - **AudioNormalizationSettings** *(dict) --* Advanced audio normalization settings.
                                
                                - **Algorithm** *(string) --* Audio normalization algorithm to use. 1770-1 conforms to the CALM Act specification, 1770-2 conforms to the EBU R-128 specification.
                                
                                - **AlgorithmControl** *(string) --* When enabled the output audio is corrected using the chosen algorithm. If disabled, the audio will be measured but not adjusted.
                                
                                - **CorrectionGateLevel** *(integer) --* Content measuring above this level will be corrected to the target level. Content measuring below this level will not be corrected. Gating only applies when not using real_time_correction.
                                
                                - **LoudnessLogging** *(string) --* If set to LOG, log each output\'s audio track loudness to a CSV file.
                                
                                - **PeakCalculation** *(string) --* If set to TRUE_PEAK, calculate and log the TruePeak for each output\'s audio track loudness.
                                
                                - **TargetLkfs** *(float) --* Target LKFS(loudness) to adjust volume to. If no value is entered, a default value will be used according to the chosen algorithm. The CALM Act (1770-1) recommends a target of -24 LKFS. The EBU R-128 specification (1770-2) recommends a target of -23 LKFS.
                            
                              - **AudioSourceName** *(string) --* Specifies which audio data to use from each input. In the simplest case, specify an \"Audio Selector\":#inputs-audio_selector by name based on its order within each input. For example if you specify \"Audio Selector 3\", then the third audio selector will be used from each input. If an input does not have an \"Audio Selector 3\", then the audio selector marked as \"default\" in that input will be used. If there is no audio selector marked as \"default\", silence will be inserted for the duration of that input. Alternatively, an \"Audio Selector Group\":#inputs-audio_selector_group name may be specified, with similar default/silence behavior. If no audio_source_name is specified, then \"Audio Selector 1\" will be chosen automatically.
                              
                              - **AudioType** *(integer) --* Applies only if Follow Input Audio Type is unchecked (false). A number between 0 and 255. The following are defined in ISO-IEC 13818-1: 0 = Undefined, 1 = Clean Effects, 2 = Hearing Impaired, 3 = Visually Impaired Commentary, 4-255 = Reserved.
                              
                              - **AudioTypeControl** *(string) --* When set to FOLLOW_INPUT, if the input contains an ISO 639 audio_type, then that value is passed through to the output. If the input contains no ISO 639 audio_type, the value in Audio Type is included in the output. Otherwise the value in Audio Type is included in the output. Note that this field and audioType are both ignored if audioDescriptionBroadcasterMix is set to BROADCASTER_MIXED_AD.
                              
                              - **CodecSettings** *(dict) --* Audio codec settings (CodecSettings) under (AudioDescriptions) contains the group of settings related to audio encoding. The settings in this group vary depending on the value you choose for Audio codec (Codec). For each codec enum you choose, define the corresponding settings object. The following lists the codec enum, settings object pairs. * AAC, AacSettings * MP2, Mp2Settings * WAV, WavSettings * AIFF, AiffSettings * AC3, Ac3Settings * EAC3, Eac3Settings
                                
                                - **AacSettings** *(dict) --* Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the value AAC. The service accepts one of two mutually exclusive groups of AAC settings--VBR and CBR. To select one of these modes, set the value of Bitrate control mode (rateControlMode) to \"VBR\" or \"CBR\". In VBR mode, you control the audio quality with the setting VBR quality (vbrQuality). In CBR mode, you use the setting Bitrate (bitrate). Defaults and valid values depend on the rate control mode.
                                  
                                  - **AudioDescriptionBroadcasterMix** *(string) --* Choose BROADCASTER_MIXED_AD when the input contains pre-mixed main audio + audio description (AD) as a stereo pair. The value for AudioType will be set to 3, which signals to downstream systems that this stream contains \"broadcaster mixed AD\". Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. When you choose BROADCASTER_MIXED_AD, the encoder ignores any values you provide in AudioType and FollowInputAudioType. Choose NORMAL when the input does not contain pre-mixed audio + audio description (AD). In this case, the encoder will use any values you provide for AudioType and FollowInputAudioType.
                                  
                                  - **Bitrate** *(integer) --* Average bitrate in bits/second. Defaults and valid values depend on rate control mode and profile.
                                  
                                  - **CodecProfile** *(string) --* AAC Profile.
                                  
                                  - **CodingMode** *(string) --* Mono (Audio Description), Mono, Stereo, or 5.1 channel layout. Valid values depend on rate control mode and profile. \"1.0 - Audio Description (Receiver Mix)\" setting receives a stereo description plus control track and emits a mono AAC encode of the description track, with control data emitted in the PES header as per ETSI TS 101 154 Annex E.
                                  
                                  - **RateControlMode** *(string) --* Rate Control Mode.
                                  
                                  - **RawFormat** *(string) --* Enables LATM/LOAS AAC output. Note that if you use LATM/LOAS AAC in an output, you must choose \"No container\" for the output container.
                                  
                                  - **SampleRate** *(integer) --* Sample rate in Hz. Valid values depend on rate control mode and profile.
                                  
                                  - **Specification** *(string) --* Use MPEG-2 AAC instead of MPEG-4 AAC audio for raw or MPEG-2 Transport Stream containers.
                                  
                                  - **VbrQuality** *(string) --* VBR Quality Level - Only used if rate_control_mode is VBR.
                              
                                - **Ac3Settings** *(dict) --* Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the value AC3.
                                  
                                  - **Bitrate** *(integer) --* Average bitrate in bits/second. Valid bitrates depend on the coding mode.
                                  
                                  - **BitstreamMode** *(string) --* Specifies the \"Bitstream Mode\" (bsmod) for the emitted AC-3 stream. See ATSC A/52-2012 for background on these values.
                                  
                                  - **CodingMode** *(string) --* Dolby Digital coding mode. Determines number of channels.
                                  
                                  - **Dialnorm** *(integer) --* Sets the dialnorm for the output. If blank and input audio is Dolby Digital, dialnorm will be passed through.
                                  
                                  - **DynamicRangeCompressionProfile** *(string) --* If set to FILM_STANDARD, adds dynamic range compression signaling to the output bitstream as defined in the Dolby Digital specification.
                                  
                                  - **LfeFilter** *(string) --* Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3_2_LFE coding mode.
                                  
                                  - **MetadataControl** *(string) --* When set to FOLLOW_INPUT, encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.
                                  
                                  - **SampleRate** *(integer) --* Sample rate in hz. Sample rate is always 48000.
                              
                                - **AiffSettings** *(dict) --* Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the value AIFF.
                                  
                                  - **BitDepth** *(integer) --* Specify Bit depth (BitDepth), in bits per sample, to choose the encoding quality for this audio track.
                                  
                                  - **Channels** *(integer) --* Set Channels to specify the number of channels in this output audio track. Choosing Mono in the console will give you 1 output channel; choosing Stereo will give you 2. In the API, valid values are 1 and 2.
                                  
                                  - **SampleRate** *(integer) --* Sample rate in hz.
                              
                                - **Codec** *(string) --* Type of Audio codec.
                                
                                - **Eac3Settings** *(dict) --* Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the value EAC3.
                                  
                                  - **AttenuationControl** *(string) --* If set to ATTENUATE_3_DB, applies a 3 dB attenuation to the surround channels. Only used for 3/2 coding mode.
                                  
                                  - **Bitrate** *(integer) --* Average bitrate in bits/second. Valid bitrates depend on the coding mode.
                                  
                                  - **BitstreamMode** *(string) --* Specifies the \"Bitstream Mode\" (bsmod) for the emitted E-AC-3 stream. See ATSC A/52-2012 (Annex E) for background on these values.
                                  
                                  - **CodingMode** *(string) --* Dolby Digital Plus coding mode. Determines number of channels.
                                  
                                  - **DcFilter** *(string) --* Activates a DC highpass filter for all input channels.
                                  
                                  - **Dialnorm** *(integer) --* Sets the dialnorm for the output. If blank and input audio is Dolby Digital Plus, dialnorm will be passed through.
                                  
                                  - **DynamicRangeCompressionLine** *(string) --* Enables Dynamic Range Compression that restricts the absolute peak level for a signal.
                                  
                                  - **DynamicRangeCompressionRf** *(string) --* Enables Heavy Dynamic Range Compression, ensures that the instantaneous signal peaks do not exceed specified levels.
                                  
                                  - **LfeControl** *(string) --* When encoding 3/2 audio, controls whether the LFE channel is enabled
                                  
                                  - **LfeFilter** *(string) --* Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3_2_LFE coding mode.
                                  
                                  - **LoRoCenterMixLevel** *(float) --* Left only/Right only center mix level. Only used for 3/2 coding mode. Valid values: 3.0, 1.5, 0.0, -1.5 -3.0 -4.5 -6.0 -60
                                  
                                  - **LoRoSurroundMixLevel** *(float) --* Left only/Right only surround mix level. Only used for 3/2 coding mode. Valid values: -1.5 -3.0 -4.5 -6.0 -60
                                  
                                  - **LtRtCenterMixLevel** *(float) --* Left total/Right total center mix level. Only used for 3/2 coding mode. Valid values: 3.0, 1.5, 0.0, -1.5 -3.0 -4.5 -6.0 -60
                                  
                                  - **LtRtSurroundMixLevel** *(float) --* Left total/Right total surround mix level. Only used for 3/2 coding mode. Valid values: -1.5 -3.0 -4.5 -6.0 -60
                                  
                                  - **MetadataControl** *(string) --* When set to FOLLOW_INPUT, encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.
                                  
                                  - **PassthroughControl** *(string) --* When set to WHEN_POSSIBLE, input DD+ audio will be passed through if it is present on the input. this detection is dynamic over the life of the transcode. Inputs that alternate between DD+ and non-DD+ content will have a consistent DD+ output as the system alternates between passthrough and encoding.
                                  
                                  - **PhaseControl** *(string) --* Controls the amount of phase-shift applied to the surround channels. Only used for 3/2 coding mode.
                                  
                                  - **SampleRate** *(integer) --* Sample rate in hz. Sample rate is always 48000.
                                  
                                  - **StereoDownmix** *(string) --* Stereo downmix preference. Only used for 3/2 coding mode.
                                  
                                  - **SurroundExMode** *(string) --* When encoding 3/2 audio, sets whether an extra center back surround channel is matrix encoded into the left and right surround channels.
                                  
                                  - **SurroundMode** *(string) --* When encoding 2/0 audio, sets whether Dolby Surround is matrix encoded into the two channels.
                              
                                - **Mp2Settings** *(dict) --* Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the value MP2.
                                  
                                  - **Bitrate** *(integer) --* Average bitrate in bits/second.
                                  
                                  - **Channels** *(integer) --* Set Channels to specify the number of channels in this output audio track. Choosing Mono in the console will give you 1 output channel; choosing Stereo will give you 2. In the API, valid values are 1 and 2.
                                  
                                  - **SampleRate** *(integer) --* Sample rate in hz.
                              
                                - **WavSettings** *(dict) --* Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the value WAV.
                                  
                                  - **BitDepth** *(integer) --* Specify Bit depth (BitDepth), in bits per sample, to choose the encoding quality for this audio track.
                                  
                                  - **Channels** *(integer) --* Set Channels to specify the number of channels in this output audio track. With WAV, valid values 1, 2, 4, and 8. In the console, these values are Mono, Stereo, 4-Channel, and 8-Channel, respectively.
                                  
                                  - **Format** *(string) --* The service defaults to using RIFF for WAV outputs. If your output audio is likely to exceed 4 GB in file size, or if you otherwise need the extended support of the RF64 format, set your output WAV file format to RF64.
                                  
                                  - **SampleRate** *(integer) --* Sample rate in Hz.
                              
                              - **CustomLanguageCode** *(string) --* Specify the language for this audio output track, using the ISO 639-2 or ISO 639-3 three-letter language code. The language specified will be used when \'Follow Input Language Code\' is not selected or when \'Follow Input Language Code\' is selected but there is no ISO 639 language code specified by the input.
                              
                              - **LanguageCode** *(string) --* Indicates the language of the audio output track. The ISO 639 language specified in the \'Language Code\' drop down will be used when \'Follow Input Language Code\' is not selected or when \'Follow Input Language Code\' is selected but there is no ISO 639 language code specified by the input.
                              
                              - **LanguageCodeControl** *(string) --* Choosing FOLLOW_INPUT will cause the ISO 639 language code of the output to follow the ISO 639 language code of the input. The language specified for languageCode\' will be used when USE_CONFIGURED is selected or when FOLLOW_INPUT is selected but there is no ISO 639 language code specified by the input.
                              
                              - **RemixSettings** *(dict) --* Advanced audio remixing settings.
                                
                                - **ChannelMapping** *(dict) --* Channel mapping (ChannelMapping) contains the group of fields that hold the remixing value for each channel. Units are in dB. Acceptable values are within the range from -60 (mute) through 6. A setting of 0 passes the input channel unchanged to the output channel (no attenuation or amplification).
                                  
                                  - **OutputChannels** *(list) --* List of output channels
                                    
                                    - *(dict) --* OutputChannel mapping settings.
                                      
                                      - **InputChannels** *(list) --* List of input channels
                                        
                                        - *(integer) --* 
                                    
                                - **ChannelsIn** *(integer) --* Specify the number of audio channels from your input that you want to use in your output. With remixing, you might combine or split the data in these channels, so the number of channels in your final output might be different.
                                
                                - **ChannelsOut** *(integer) --* Specify the number of channels in this output after remixing. Valid values: 1, 2, 4, 6, 8
                            
                              - **StreamName** *(string) --* Used for MS Smooth and Apple HLS outputs. Indicates the name displayed by the player (eg. English, or Director Commentary). Alphanumeric characters, spaces, and underscore are legal.
                          
                          - **CaptionDescriptions** *(list) --* (CaptionDescriptions) contains groups of captions settings. For each output that has captions, include one instance of (CaptionDescriptions). (CaptionDescriptions) can contain multiple groups of captions settings.
                            
                            - *(dict) --* Description of Caption output
                              
                              - **CaptionSelectorName** *(string) --* Specifies which \"Caption Selector\":#inputs-caption_selector to use from each input when generating captions. The name should be of the format \"Caption Selector \", which denotes that the Nth Caption Selector will be used from each input.
                              
                              - **CustomLanguageCode** *(string) --* Indicates the language of the caption output track, using the ISO 639-2 or ISO 639-3 three-letter language code
                              
                              - **DestinationSettings** *(dict) --* Specific settings required by destination type. Note that burnin_destination_settings are not available if the source of the caption data is Embedded or Teletext.
                                
                                - **BurninDestinationSettings** *(dict) --* Burn-In Destination Settings.
                                  
                                  - **Alignment** *(string) --* If no explicit x_position or y_position is provided, setting alignment to centered will place the captions at the bottom center of the output. Similarly, setting a left alignment will align captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **BackgroundColor** *(string) --* Specifies the color of the rectangle behind the captions. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **BackgroundOpacity** *(integer) --* Specifies the opacity of the background rectangle. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
                                  
                                  - **FontColor** *(string) --* Specifies the color of the burned-in captions. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **FontOpacity** *(integer) --* Specifies the opacity of the burned-in captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **FontResolution** *(integer) --* Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **FontSize** *(integer) --* A positive integer indicates the exact font size in points. Set to 0 for automatic font size selection. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **OutlineColor** *(string) --* Specifies font outline color. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **OutlineSize** *(integer) --* Specifies font outline size in pixels. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **ShadowColor** *(string) --* Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **ShadowOpacity** *(integer) --* Specifies the opacity of the shadow. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
                                  
                                  - **ShadowXOffset** *(integer) --* Specifies the horizontal offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **ShadowYOffset** *(integer) --* Specifies the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **TeletextSpacing** *(string) --* Only applies to jobs with input captions in Teletext or STL formats. Specify whether the spacing between letters in your captions is set by the captions grid or varies depending on letter width. Choose fixed grid to conform to the spacing specified in the captions file more accurately. Choose proportional to make the text easier to read if the captions are closed caption.
                                  
                                  - **XPosition** *(integer) --* Specifies the horizontal position of the caption relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit x_position is provided, the horizontal caption position will be determined by the alignment parameter. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **YPosition** *(integer) --* Specifies the vertical position of the caption relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit y_position is provided, the caption will be positioned towards the bottom of the output. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                              
                                - **DestinationType** *(string) --* Type of Caption output, including Burn-In, Embedded, SCC, SRT, TTML, WebVTT, DVB-Sub, Teletext.
                                
                                - **DvbSubDestinationSettings** *(dict) --* DVB-Sub Destination Settings
                                  
                                  - **Alignment** *(string) --* If no explicit x_position or y_position is provided, setting alignment to centered will place the captions at the bottom center of the output. Similarly, setting a left alignment will align captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **BackgroundColor** *(string) --* Specifies the color of the rectangle behind the captions. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **BackgroundOpacity** *(integer) --* Specifies the opacity of the background rectangle. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
                                  
                                  - **FontColor** *(string) --* Specifies the color of the burned-in captions. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **FontOpacity** *(integer) --* Specifies the opacity of the burned-in captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **FontResolution** *(integer) --* Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **FontSize** *(integer) --* A positive integer indicates the exact font size in points. Set to 0 for automatic font size selection. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **OutlineColor** *(string) --* Specifies font outline color. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **OutlineSize** *(integer) --* Specifies font outline size in pixels. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **ShadowColor** *(string) --* Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **ShadowOpacity** *(integer) --* Specifies the opacity of the shadow. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
                                  
                                  - **ShadowXOffset** *(integer) --* Specifies the horizontal offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **ShadowYOffset** *(integer) --* Specifies the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **TeletextSpacing** *(string) --* Only applies to jobs with input captions in Teletext or STL formats. Specify whether the spacing between letters in your captions is set by the captions grid or varies depending on letter width. Choose fixed grid to conform to the spacing specified in the captions file more accurately. Choose proportional to make the text easier to read if the captions are closed caption.
                                  
                                  - **XPosition** *(integer) --* Specifies the horizontal position of the caption relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit x_position is provided, the horizontal caption position will be determined by the alignment parameter. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                                  
                                  - **YPosition** *(integer) --* Specifies the vertical position of the caption relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit y_position is provided, the caption will be positioned towards the bottom of the output. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                              
                                - **SccDestinationSettings** *(dict) --* Settings for SCC caption output.
                                  
                                  - **Framerate** *(string) --* Set Framerate (SccDestinationFramerate) to make sure that the captions and the video are synchronized in the output. Specify a framerate that matches the framerate of the associated video. If the video framerate is 29.97, choose 29.97 dropframe (FRAMERATE_29_97_DROPFRAME) only if the video has video_insertion=true and drop_frame_timecode=true; otherwise, choose 29.97 non-dropframe (FRAMERATE_29_97_NON_DROPFRAME).
                              
                                - **TeletextDestinationSettings** *(dict) --* Settings for Teletext caption output
                                  
                                  - **PageNumber** *(string) --* Set pageNumber to the Teletext page number for the destination captions for this output. This value must be a three-digit hexadecimal string; strings ending in -FF are invalid. If you are passing through the entire set of Teletext data, do not use this field.
                              
                                - **TtmlDestinationSettings** *(dict) --* Settings specific to TTML caption outputs, including Pass style information (TtmlStylePassthrough).
                                  
                                  - **StylePassthrough** *(string) --* Pass through style and position information from a TTML-like input source (TTML, SMPTE-TT, CFF-TT) to the CFF-TT output or TTML output.
                              
                              - **LanguageCode** *(string) --* Indicates the language of the caption output track.
                              
                              - **LanguageDescription** *(string) --* Human readable information to indicate captions available for players (eg. English, or Spanish). Alphanumeric characters, spaces, and underscore are legal.
                          
                          - **ContainerSettings** *(dict) --* Container specific settings.
                            
                            - **Container** *(string) --* Container for this output. Some containers require a container settings object. If not specified, the default object will be created.
                            
                            - **F4vSettings** *(dict) --* Settings for F4v container
                              
                              - **MoovPlacement** *(string) --* If set to PROGRESSIVE_DOWNLOAD, the MOOV atom is relocated to the beginning of the archive as required for progressive downloading. Otherwise it is placed normally at the end.
                          
                            - **M2tsSettings** *(dict) --* Settings for M2TS Container.
                              
                              - **AudioBufferModel** *(string) --* Selects between the DVB and ATSC buffer models for Dolby Digital audio.
                              
                              - **AudioFramesPerPes** *(integer) --* The number of audio frames to insert for each PES packet.
                              
                              - **AudioPids** *(list) --* Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation.
                                
                                - *(integer) --* 
                            
                              - **Bitrate** *(integer) --* The output bitrate of the transport stream in bits per second. Setting to 0 lets the muxer automatically determine the appropriate bitrate. Other common values are 3750000, 7500000, and 15000000.
                              
                              - **BufferModel** *(string) --* Controls what buffer model to use for accurate interleaving. If set to MULTIPLEX, use multiplex buffer model. If set to NONE, this can lead to lower latency, but low-memory devices may not be able to play back the stream without interruptions.
                              
                              - **DvbNitSettings** *(dict) --* Inserts DVB Network Information Table (NIT) at the specified table repetition interval.
                                
                                - **NetworkId** *(integer) --* The numeric value placed in the Network Information Table (NIT).
                                
                                - **NetworkName** *(string) --* The network name text placed in the network_name_descriptor inside the Network Information Table. Maximum length is 256 characters.
                                
                                - **NitInterval** *(integer) --* The number of milliseconds between instances of this table in the output transport stream.
                            
                              - **DvbSdtSettings** *(dict) --* Inserts DVB Service Description Table (NIT) at the specified table repetition interval.
                                
                                - **OutputSdt** *(string) --* Selects method of inserting SDT information into output stream. \"Follow input SDT\" copies SDT information from input stream to output stream. \"Follow input SDT if present\" copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. Enter \"SDT Manually\" means user will enter the SDT information. \"No SDT\" means output stream will not contain SDT information.
                                
                                - **SdtInterval** *(integer) --* The number of milliseconds between instances of this table in the output transport stream.
                                
                                - **ServiceName** *(string) --* The service name placed in the service_descriptor in the Service Description Table. Maximum length is 256 characters.
                                
                                - **ServiceProviderName** *(string) --* The service provider name placed in the service_descriptor in the Service Description Table. Maximum length is 256 characters.
                            
                              - **DvbSubPids** *(list) --* Packet Identifier (PID) for input source DVB Subtitle data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation.
                                
                                - *(integer) --* 
                            
                              - **DvbTdtSettings** *(dict) --* Inserts DVB Time and Date Table (TDT) at the specified table repetition interval.
                                
                                - **TdtInterval** *(integer) --* The number of milliseconds between instances of this table in the output transport stream.
                            
                              - **DvbTeletextPid** *(integer) --* Packet Identifier (PID) for input source DVB Teletext data to this output.
                              
                              - **EbpAudioInterval** *(string) --* When set to VIDEO_AND_FIXED_INTERVALS, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. When set to VIDEO_INTERVAL, these additional markers will not be inserted. Only applicable when EBP segmentation markers are is selected (segmentationMarkers is EBP or EBP_LEGACY).
                              
                              - **EbpPlacement** *(string) --* Selects which PIDs to place EBP markers on. They can either be placed only on the video PID, or on both the video PID and all audio PIDs. Only applicable when EBP segmentation markers are is selected (segmentationMarkers is EBP or EBP_LEGACY).
                              
                              - **EsRateInPes** *(string) --* Controls whether to include the ES Rate field in the PES header.
                              
                              - **FragmentTime** *(float) --* The length in seconds of each fragment. Only used with EBP markers.
                              
                              - **MaxPcrInterval** *(integer) --* Maximum time in milliseconds between Program Clock References (PCRs) inserted into the transport stream.
                              
                              - **MinEbpInterval** *(integer) --* When set, enforces that Encoder Boundary Points do not come within the specified time interval of each other by looking ahead at input video. If another EBP is going to come in within the specified time interval, the current EBP is not emitted, and the segment is \"stretched\" to the next marker. The lookahead value does not add latency to the system. The Live Event must be configured elsewhere to create sufficient latency to make the lookahead accurate.
                              
                              - **NielsenId3** *(string) --* If INSERT, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.
                              
                              - **NullPacketBitrate** *(float) --* Value in bits per second of extra null packets to insert into the transport stream. This can be used if a downstream encryption system requires periodic null packets.
                              
                              - **PatInterval** *(integer) --* The number of milliseconds between instances of this table in the output transport stream.
                              
                              - **PcrControl** *(string) --* When set to PCR_EVERY_PES_PACKET, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This is effective only when the PCR PID is the same as the video or audio elementary stream.
                              
                              - **PcrPid** *(integer) --* Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID.
                              
                              - **PmtInterval** *(integer) --* The number of milliseconds between instances of this table in the output transport stream.
                              
                              - **PmtPid** *(integer) --* Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream.
                              
                              - **PrivateMetadataPid** *(integer) --* Packet Identifier (PID) of the private metadata stream in the transport stream.
                              
                              - **ProgramNumber** *(integer) --* The value of the program number field in the Program Map Table.
                              
                              - **RateMode** *(string) --* When set to CBR, inserts null packets into transport stream to fill specified bitrate. When set to VBR, the bitrate setting acts as the maximum bitrate, but the output will not be padded up to that bitrate.
                              
                              - **Scte35Pid** *(integer) --* Packet Identifier (PID) of the SCTE-35 stream in the transport stream.
                              
                              - **Scte35Source** *(string) --* Enables SCTE-35 passthrough (scte35Source) to pass any SCTE-35 signals from input to output.
                              
                              - **SegmentationMarkers** *(string) --* Inserts segmentation markers at each segmentation_time period. rai_segstart sets the Random Access Indicator bit in the adaptation field. rai_adapt sets the RAI bit and adds the current timecode in the private data bytes. psi_segstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebp_legacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format.
                              
                              - **SegmentationStyle** *(string) --* The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of \"reset_cadence\" is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of of $segmentation_time seconds. When a segmentation style of \"maintain_cadence\" is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentation_time seconds. Note that EBP lookahead is a slight exception to this rule.
                              
                              - **SegmentationTime** *(float) --* The length in seconds of each segment. Required unless markers is set to _none_.
                              
                              - **TimedMetadataPid** *(integer) --* Packet Identifier (PID) of the timed metadata stream in the transport stream.
                              
                              - **TransportStreamId** *(integer) --* The value of the transport stream ID field in the Program Map Table.
                              
                              - **VideoPid** *(integer) --* Packet Identifier (PID) of the elementary video stream in the transport stream.
                          
                            - **M3u8Settings** *(dict) --* Settings for TS segments in HLS
                              
                              - **AudioFramesPerPes** *(integer) --* The number of audio frames to insert for each PES packet.
                              
                              - **AudioPids** *(list) --* Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation.
                                
                                - *(integer) --* 
                            
                              - **NielsenId3** *(string) --* If INSERT, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.
                              
                              - **PatInterval** *(integer) --* The number of milliseconds between instances of this table in the output transport stream.
                              
                              - **PcrControl** *(string) --* When set to PCR_EVERY_PES_PACKET a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.
                              
                              - **PcrPid** *(integer) --* Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID.
                              
                              - **PmtInterval** *(integer) --* The number of milliseconds between instances of this table in the output transport stream.
                              
                              - **PmtPid** *(integer) --* Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream.
                              
                              - **PrivateMetadataPid** *(integer) --* Packet Identifier (PID) of the private metadata stream in the transport stream.
                              
                              - **ProgramNumber** *(integer) --* The value of the program number field in the Program Map Table.
                              
                              - **Scte35Pid** *(integer) --* Packet Identifier (PID) of the SCTE-35 stream in the transport stream.
                              
                              - **Scte35Source** *(string) --* Enables SCTE-35 passthrough (scte35Source) to pass any SCTE-35 signals from input to output.
                              
                              - **TimedMetadata** *(string) --* Applies only to HLS outputs. Use this setting to specify whether the service inserts the ID3 timed metadata from the input in this output.
                              
                              - **TimedMetadataPid** *(integer) --* Packet Identifier (PID) of the timed metadata stream in the transport stream.
                              
                              - **TransportStreamId** *(integer) --* The value of the transport stream ID field in the Program Map Table.
                              
                              - **VideoPid** *(integer) --* Packet Identifier (PID) of the elementary video stream in the transport stream.
                          
                            - **MovSettings** *(dict) --* Settings for MOV Container.
                              
                              - **ClapAtom** *(string) --* When enabled, include \'clap\' atom if appropriate for the video output settings.
                              
                              - **CslgAtom** *(string) --* When enabled, file composition times will start at zero, composition times in the \'ctts\' (composition time to sample) box for B-frames will be negative, and a \'cslg\' (composition shift least greatest) box will be included per 14496-1 amendment 1. This improves compatibility with Apple players and tools.
                              
                              - **Mpeg2FourCCControl** *(string) --* When set to XDCAM, writes MPEG2 video streams into the QuickTime file using XDCAM fourcc codes. This increases compatibility with Apple editors and players, but may decrease compatibility with other players. Only applicable when the video codec is MPEG2.
                              
                              - **PaddingControl** *(string) --* If set to OMNEON, inserts Omneon-compatible padding
                              
                              - **Reference** *(string) --* A value of \'external\' creates separate media files and the wrapper file (.mov) contains references to these media files. A value of \'self_contained\' creates only a wrapper (.mov) file and this file contains all of the media.
                          
                            - **Mp4Settings** *(dict) --* Settings for MP4 Container
                              
                              - **CslgAtom** *(string) --* When enabled, file composition times will start at zero, composition times in the \'ctts\' (composition time to sample) box for B-frames will be negative, and a \'cslg\' (composition shift least greatest) box will be included per 14496-1 amendment 1. This improves compatibility with Apple players and tools.
                              
                              - **FreeSpaceBox** *(string) --* Inserts a free-space box immediately after the moov box.
                              
                              - **MoovPlacement** *(string) --* If set to PROGRESSIVE_DOWNLOAD, the MOOV atom is relocated to the beginning of the archive as required for progressive downloading. Otherwise it is placed normally at the end.
                              
                              - **Mp4MajorBrand** *(string) --* Overrides the \"Major Brand\" field in the output file. Usually not necessary to specify.
                          
                          - **Extension** *(string) --* Use Extension (Extension) to specify the file extension for outputs in File output groups. If you do not specify a value, the service will use default extensions by container type as follows * MPEG-2 transport stream, m2ts * Quicktime, mov * MXF container, mxf * MPEG-4 container, mp4 * No Container, the service will use codec extensions (e.g. AAC, H265, H265, AC3)
                          
                          - **NameModifier** *(string) --* Use Name modifier (NameModifier) to have the service add a string to the end of each output filename. You specify the base filename as part of your destination URI. When you create multiple outputs in the same output group, Name modifier (NameModifier) is required. Name modifier also accepts format identifiers. For DASH ISO outputs, if you use the format identifiers $Number$ or $Time$ in one output, you must use them in the same way in all outputs of the output group.
                          
                          - **OutputSettings** *(dict) --* Specific settings for this type of output.
                            
                            - **HlsSettings** *(dict) --* Settings for HLS output groups
                              
                              - **AudioGroupId** *(string) --* Specifies the group to which the audio Rendition belongs.
                              
                              - **AudioRenditionSets** *(string) --* List all the audio groups that are used with the video output stream. Input all the audio GROUP-IDs that are associated to the video, separate by \',\'.
                              
                              - **AudioTrackType** *(string) --* Four types of audio-only tracks are supported: Audio-Only Variant Stream The client can play back this audio-only stream instead of video in low-bandwidth scenarios. Represented as an EXT-X-STREAM-INF in the HLS manifest. Alternate Audio, Auto Select, Default Alternate rendition that the client should try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=YES, AUTOSELECT=YES Alternate Audio, Auto Select, Not Default Alternate rendition that the client may try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=YES Alternate Audio, not Auto Select Alternate rendition that the client will not try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=NO
                              
                              - **IFrameOnlyManifest** *(string) --* When set to INCLUDE, writes I-Frame Only Manifest in addition to the HLS manifest
                              
                              - **SegmentModifier** *(string) --* String concatenated to end of segment filenames. Accepts \"Format Identifiers\":#format_identifier_parameters.
                          
                          - **Preset** *(string) --* Use Preset (Preset) to specifiy a preset for your transcoding settings. Provide the system or custom preset name. You can specify either Preset (Preset) or Container settings (ContainerSettings), but not both.
                          
                          - **VideoDescription** *(dict) --* (VideoDescription) contains a group of video encoding settings. The specific video settings depend on the video codec you choose when you specify a value for Video codec (codec). Include one instance of (VideoDescription) per output.
                            
                            - **AfdSignaling** *(string) --* This setting only applies to H.264 and MPEG2 outputs. Use Insert AFD signaling (AfdSignaling) to specify whether the service includes AFD values in the output video data and what those values are. * Choose None to remove all AFD values from this output. * Choose Fixed to ignore input AFD values and instead encode the value specified in the job. * Choose Auto to calculate output AFD values based on the input AFD scaler data.
                            
                            - **AntiAlias** *(string) --* Enable Anti-alias (AntiAlias) to enhance sharp edges in video output when your input resolution is much larger than your output resolution. Default is enabled.
                            
                            - **CodecSettings** *(dict) --* Video codec settings, (CodecSettings) under (VideoDescription), contains the group of settings related to video encoding. The settings in this group vary depending on the value you choose for Video codec (Codec). For each codec enum you choose, define the corresponding settings object. The following lists the codec enum, settings object pairs. * H_264, H264Settings * H_265, H265Settings * MPEG2, Mpeg2Settings * PRORES, ProresSettings * FRAME_CAPTURE, FrameCaptureSettings
                              
                              - **Codec** *(string) --* Type of video codec
                              
                              - **FrameCaptureSettings** *(dict) --* Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the value FRAME_CAPTURE.
                                
                                - **FramerateDenominator** *(integer) --* Frame capture will encode the first frame of the output stream, then one frame every framerateDenominator/framerateNumerator seconds. For example, settings of framerateNumerator = 1 and framerateDenominator = 3 (a rate of 1/3 frame per second) will capture the first frame, then 1 frame every 3s. Files will be named as filename.n.jpg where n is the 0-based sequence number of each Capture.
                                
                                - **FramerateNumerator** *(integer) --* Frame capture will encode the first frame of the output stream, then one frame every framerateDenominator/framerateNumerator seconds. For example, settings of framerateNumerator = 1 and framerateDenominator = 3 (a rate of 1/3 frame per second) will capture the first frame, then 1 frame every 3s. Files will be named as filename.NNNNNNN.jpg where N is the 0-based frame sequence number zero padded to 7 decimal places.
                                
                                - **MaxCaptures** *(integer) --* Maximum number of captures (encoded jpg output files).
                                
                                - **Quality** *(integer) --* JPEG Quality - a higher value equals higher quality.
                            
                              - **H264Settings** *(dict) --* Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the value H_264.
                                
                                - **AdaptiveQuantization** *(string) --* Adaptive quantization. Allows intra-frame quantizers to vary to improve visual quality.
                                
                                - **Bitrate** *(integer) --* Average bitrate in bits/second. Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique when rounded down to the nearest multiple of 1000.
                                
                                - **CodecLevel** *(string) --* H.264 Level.
                                
                                - **CodecProfile** *(string) --* H.264 Profile. High 4:2:2 and 10-bit profiles are only available with the AVC-I License.
                                
                                - **DynamicSubGop** *(string) --* Choose Adaptive to improve subjective video quality for high-motion content. This will cause the service to use fewer B-frames (which infer information based on other frames) for high-motion portions of the video and more B-frames for low-motion portions. The maximum number of B-frames is limited by the value you provide for the setting B frames between reference frames (numberBFramesBetweenReferenceFrames).
                                
                                - **EntropyEncoding** *(string) --* Entropy encoding mode. Use CABAC (must be in Main or High profile) or CAVLC.
                                
                                - **FieldEncoding** *(string) --* Choosing FORCE_FIELD disables PAFF encoding for interlaced outputs.
                                
                                - **FlickerAdaptiveQuantization** *(string) --* Adjust quantization within each frame to reduce flicker or \'pop\' on I-frames.
                                
                                - **FramerateControl** *(string) --* If you are using the console, use the Framerate setting to specify the framerate for this output. If you want to keep the same framerate as the input video, choose Follow source. If you want to do framerate conversion, choose a framerate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your framerate as a fraction. If you are creating your transcoding job specification as a JSON file without the console, use FramerateControl to specify which value the service uses for the framerate for this output. Choose INITIALIZE_FROM_SOURCE if you want the service to use the framerate from the input. Choose SPECIFIED if you want the service to use the framerate you specify in the settings FramerateNumerator and FramerateDenominator.
                                
                                - **FramerateConversionAlgorithm** *(string) --* When set to INTERPOLATE, produces smoother motion during framerate conversion.
                                
                                - **FramerateDenominator** *(integer) --* When you use the API for transcode jobs that use framerate conversion, specify the framerate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use framerate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.
                                
                                - **FramerateNumerator** *(integer) --* Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps.
                                
                                - **GopBReference** *(string) --* If enable, use reference B frames for GOP structures that have B frames > 1.
                                
                                - **GopClosedCadence** *(integer) --* Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting.
                                
                                - **GopSize** *(float) --* GOP Length (keyframe interval) in frames or seconds. Must be greater than zero.
                                
                                - **GopSizeUnits** *(string) --* Indicates if the GOP Size in H264 is specified in frames or seconds. If seconds the system will convert the GOP Size into a frame count at run time.
                                
                                - **HrdBufferInitialFillPercentage** *(integer) --* Percentage of the buffer that should initially be filled (HRD buffer model).
                                
                                - **HrdBufferSize** *(integer) --* Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000.
                                
                                - **InterlaceMode** *(string) --* Use Interlace mode (InterlaceMode) to choose the scan line type for the output. * Top Field First (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce interlaced output with the entire output having the same field polarity (top or bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow, Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as the source. Therefore, behavior depends on the input scan type, as follows. - If the source is interlaced, the output will be interlaced with the same polarity as the source (it will follow the source). The output could therefore be a mix of \"top field first\" and \"bottom field first\". - If the source is progressive, the output will be interlaced with \"top field first\" or \"bottom field first\" polarity, depending on which of the Follow options you chose.
                                
                                - **MaxBitrate** *(integer) --* Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. Required when Rate control mode is QVBR.
                                
                                - **MinIInterval** *(integer) --* Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. This setting is only used when Scene Change Detect is enabled. Note: Maximum GOP stretch = GOP size + Min-I-interval - 1
                                
                                - **NumberBFramesBetweenReferenceFrames** *(integer) --* Number of B-frames between reference frames.
                                
                                - **NumberReferenceFrames** *(integer) --* Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding.
                                
                                - **ParControl** *(string) --* Using the API, enable ParFollowSource if you want the service to use the pixel aspect ratio from the input. Using the console, do this by choosing Follow source for Pixel aspect ratio.
                                
                                - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.
                                
                                - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.
                                
                                - **QualityTuningLevel** *(string) --* Use Quality tuning level (H264QualityTuningLevel) to specifiy whether to use fast single-pass, high-quality singlepass, or high-quality multipass video encoding.
                                
                                - **QvbrSettings** *(dict) --* Settings for quality-defined variable bitrate encoding with the H.264 codec. Required when you set Rate control mode to QVBR. Not valid when you set Rate control mode to a value other than QVBR, or when you don\'t define Rate control mode.
                                  
                                  - **MaxAverageBitrate** *(integer) --* Use this setting only when Rate control mode is QVBR and Quality tuning level is Multi-pass HQ. For Max average bitrate values suited to the complexity of your input video, the service limits the average bitrate of the video part of this output to the value you choose. That is, the total size of the video element is less than or equal to the value you set multiplied by the number of seconds of encoded output.
                                  
                                  - **QvbrQualityLevel** *(integer) --* Required when you use QVBR rate control mode. That is, when you specify qvbrSettings within h264Settings. Specify the target quality level for this output, from 1 to 10. Use higher numbers for greater quality. Level 10 results in nearly lossless compression. The quality level for most broadcast-quality transcodes is between 6 and 9.
                              
                                - **RateControlMode** *(string) --* Use this setting to specify whether this output has a variable bitrate (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR).
                                
                                - **RepeatPps** *(string) --* Places a PPS header on each encoded picture, even if repeated.
                                
                                - **SceneChangeDetect** *(string) --* Scene change detection (inserts I-frames on scene changes).
                                
                                - **Slices** *(integer) --* Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures.
                                
                                - **SlowPal** *(string) --* Enables Slow PAL rate conversion. 23.976fps and 24fps input is relabeled as 25fps, and audio is sped up correspondingly.
                                
                                - **Softness** *(integer) --* Softness. Selects quantizer matrix, larger values reduce high-frequency content in the encoded image.
                                
                                - **SpatialAdaptiveQuantization** *(string) --* Adjust quantization within each frame based on spatial variation of content complexity.
                                
                                - **Syntax** *(string) --* Produces a bitstream compliant with SMPTE RP-2027.
                                
                                - **Telecine** *(string) --* This field applies only if the Streams > Advanced > Framerate (framerate) field is set to 29.970. This field works with the Streams > Advanced > Preprocessors > Deinterlacer field (deinterlace_mode) and the Streams > Advanced > Interlaced Mode field (interlace_mode) to identify the scan type for the output: Progressive, Interlaced, Hard Telecine or Soft Telecine. - Hard: produces 29.97i output from 23.976 input. - Soft: produces 23.976; the player converts this output to 29.97i.
                                
                                - **TemporalAdaptiveQuantization** *(string) --* Adjust quantization within each frame based on temporal variation of content complexity.
                                
                                - **UnregisteredSeiTimecode** *(string) --* Inserts timecode for each frame as 4 bytes of an unregistered SEI message.
                            
                              - **H265Settings** *(dict) --* Settings for H265 codec
                                
                                - **AdaptiveQuantization** *(string) --* Adaptive quantization. Allows intra-frame quantizers to vary to improve visual quality.
                                
                                - **AlternateTransferFunctionSei** *(string) --* Enables Alternate Transfer Function SEI message for outputs using Hybrid Log Gamma (HLG) Electro-Optical Transfer Function (EOTF).
                                
                                - **Bitrate** *(integer) --* Average bitrate in bits/second. Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique when rounded down to the nearest multiple of 1000.
                                
                                - **CodecLevel** *(string) --* H.265 Level.
                                
                                - **CodecProfile** *(string) --* Represents the Profile and Tier, per the HEVC (H.265) specification. Selections are grouped as [Profile] / [Tier], so \"Main/High\" represents Main Profile with High Tier. 4:2:2 profiles are only available with the HEVC 4:2:2 License.
                                
                                - **DynamicSubGop** *(string) --* Choose Adaptive to improve subjective video quality for high-motion content. This will cause the service to use fewer B-frames (which infer information based on other frames) for high-motion portions of the video and more B-frames for low-motion portions. The maximum number of B-frames is limited by the value you provide for the setting B frames between reference frames (numberBFramesBetweenReferenceFrames).
                                
                                - **FlickerAdaptiveQuantization** *(string) --* Adjust quantization within each frame to reduce flicker or \'pop\' on I-frames.
                                
                                - **FramerateControl** *(string) --* If you are using the console, use the Framerate setting to specify the framerate for this output. If you want to keep the same framerate as the input video, choose Follow source. If you want to do framerate conversion, choose a framerate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your framerate as a fraction. If you are creating your transcoding job sepecification as a JSON file without the console, use FramerateControl to specify which value the service uses for the framerate for this output. Choose INITIALIZE_FROM_SOURCE if you want the service to use the framerate from the input. Choose SPECIFIED if you want the service to use the framerate you specify in the settings FramerateNumerator and FramerateDenominator.
                                
                                - **FramerateConversionAlgorithm** *(string) --* When set to INTERPOLATE, produces smoother motion during framerate conversion.
                                
                                - **FramerateDenominator** *(integer) --* Framerate denominator.
                                
                                - **FramerateNumerator** *(integer) --* Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps.
                                
                                - **GopBReference** *(string) --* If enable, use reference B frames for GOP structures that have B frames > 1.
                                
                                - **GopClosedCadence** *(integer) --* Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting.
                                
                                - **GopSize** *(float) --* GOP Length (keyframe interval) in frames or seconds. Must be greater than zero.
                                
                                - **GopSizeUnits** *(string) --* Indicates if the GOP Size in H265 is specified in frames or seconds. If seconds the system will convert the GOP Size into a frame count at run time.
                                
                                - **HrdBufferInitialFillPercentage** *(integer) --* Percentage of the buffer that should initially be filled (HRD buffer model).
                                
                                - **HrdBufferSize** *(integer) --* Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000.
                                
                                - **InterlaceMode** *(string) --* Use Interlace mode (InterlaceMode) to choose the scan line type for the output. * Top Field First (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce interlaced output with the entire output having the same field polarity (top or bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow, Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as the source. Therefore, behavior depends on the input scan type. - If the source is interlaced, the output will be interlaced with the same polarity as the source (it will follow the source). The output could therefore be a mix of \"top field first\" and \"bottom field first\". - If the source is progressive, the output will be interlaced with \"top field first\" or \"bottom field first\" polarity, depending on which of the Follow options you chose.
                                
                                - **MaxBitrate** *(integer) --* Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. Required when Rate control mode is QVBR.
                                
                                - **MinIInterval** *(integer) --* Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. This setting is only used when Scene Change Detect is enabled. Note: Maximum GOP stretch = GOP size + Min-I-interval - 1
                                
                                - **NumberBFramesBetweenReferenceFrames** *(integer) --* Number of B-frames between reference frames.
                                
                                - **NumberReferenceFrames** *(integer) --* Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding.
                                
                                - **ParControl** *(string) --* Using the API, enable ParFollowSource if you want the service to use the pixel aspect ratio from the input. Using the console, do this by choosing Follow source for Pixel aspect ratio.
                                
                                - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.
                                
                                - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.
                                
                                - **QualityTuningLevel** *(string) --* Use Quality tuning level (H265QualityTuningLevel) to specifiy whether to use fast single-pass, high-quality singlepass, or high-quality multipass video encoding.
                                
                                - **QvbrSettings** *(dict) --* Settings for quality-defined variable bitrate encoding with the H.265 codec. Required when you set Rate control mode to QVBR. Not valid when you set Rate control mode to a value other than QVBR, or when you don\'t define Rate control mode.
                                  
                                  - **MaxAverageBitrate** *(integer) --* Use this setting only when Rate control mode is QVBR and Quality tuning level is Multi-pass HQ. For Max average bitrate values suited to the complexity of your input video, the service limits the average bitrate of the video part of this output to the value you choose. That is, the total size of the video element is less than or equal to the value you set multiplied by the number of seconds of encoded output.
                                  
                                  - **QvbrQualityLevel** *(integer) --* Required when you use QVBR rate control mode. That is, when you specify qvbrSettings within h265Settings. Specify the target quality level for this output, from 1 to 10. Use higher numbers for greater quality. Level 10 results in nearly lossless compression. The quality level for most broadcast-quality transcodes is between 6 and 9.
                              
                                - **RateControlMode** *(string) --* Use this setting to specify whether this output has a variable bitrate (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR).
                                
                                - **SampleAdaptiveOffsetFilterMode** *(string) --* Specify Sample Adaptive Offset (SAO) filter strength. Adaptive mode dynamically selects best strength based on content
                                
                                - **SceneChangeDetect** *(string) --* Scene change detection (inserts I-frames on scene changes).
                                
                                - **Slices** *(integer) --* Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures.
                                
                                - **SlowPal** *(string) --* Enables Slow PAL rate conversion. 23.976fps and 24fps input is relabeled as 25fps, and audio is sped up correspondingly.
                                
                                - **SpatialAdaptiveQuantization** *(string) --* Adjust quantization within each frame based on spatial variation of content complexity.
                                
                                - **Telecine** *(string) --* This field applies only if the Streams > Advanced > Framerate (framerate) field is set to 29.970. This field works with the Streams > Advanced > Preprocessors > Deinterlacer field (deinterlace_mode) and the Streams > Advanced > Interlaced Mode field (interlace_mode) to identify the scan type for the output: Progressive, Interlaced, Hard Telecine or Soft Telecine. - Hard: produces 29.97i output from 23.976 input. - Soft: produces 23.976; the player converts this output to 29.97i.
                                
                                - **TemporalAdaptiveQuantization** *(string) --* Adjust quantization within each frame based on temporal variation of content complexity.
                                
                                - **TemporalIds** *(string) --* Enables temporal layer identifiers in the encoded bitstream. Up to 3 layers are supported depending on GOP structure: I- and P-frames form one layer, reference B-frames can form a second layer and non-reference b-frames can form a third layer. Decoders can optionally decode only the lower temporal layers to generate a lower frame rate output. For example, given a bitstream with temporal IDs and with b-frames = 1 (i.e. IbPbPb display order), a decoder could decode all the frames for full frame rate output or only the I and P frames (lowest temporal layer) for a half frame rate output.
                                
                                - **Tiles** *(string) --* Enable use of tiles, allowing horizontal as well as vertical subdivision of the encoded pictures.
                                
                                - **UnregisteredSeiTimecode** *(string) --* Inserts timecode for each frame as 4 bytes of an unregistered SEI message.
                                
                                - **WriteMp4PackagingType** *(string) --* If HVC1, output that is H.265 will be marked as HVC1 and adhere to the ISO-IECJTC1-SC29_N13798_Text_ISOIEC_FDIS_14496-15_3rd_E spec which states that parameter set NAL units will be stored in the sample headers but not in the samples directly. If HEV1, then H.265 will be marked as HEV1 and parameter set NAL units will be written into the samples.
                            
                              - **Mpeg2Settings** *(dict) --* Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the value MPEG2.
                                
                                - **AdaptiveQuantization** *(string) --* Adaptive quantization. Allows intra-frame quantizers to vary to improve visual quality.
                                
                                - **Bitrate** *(integer) --* Average bitrate in bits/second. Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique when rounded down to the nearest multiple of 1000.
                                
                                - **CodecLevel** *(string) --* Use Level (Mpeg2CodecLevel) to set the MPEG-2 level for the video output.
                                
                                - **CodecProfile** *(string) --* Use Profile (Mpeg2CodecProfile) to set the MPEG-2 profile for the video output.
                                
                                - **DynamicSubGop** *(string) --* Choose Adaptive to improve subjective video quality for high-motion content. This will cause the service to use fewer B-frames (which infer information based on other frames) for high-motion portions of the video and more B-frames for low-motion portions. The maximum number of B-frames is limited by the value you provide for the setting B frames between reference frames (numberBFramesBetweenReferenceFrames).
                                
                                - **FramerateControl** *(string) --* If you are using the console, use the Framerate setting to specify the framerate for this output. If you want to keep the same framerate as the input video, choose Follow source. If you want to do framerate conversion, choose a framerate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your framerate as a fraction. If you are creating your transcoding job sepecification as a JSON file without the console, use FramerateControl to specify which value the service uses for the framerate for this output. Choose INITIALIZE_FROM_SOURCE if you want the service to use the framerate from the input. Choose SPECIFIED if you want the service to use the framerate you specify in the settings FramerateNumerator and FramerateDenominator.
                                
                                - **FramerateConversionAlgorithm** *(string) --* When set to INTERPOLATE, produces smoother motion during framerate conversion.
                                
                                - **FramerateDenominator** *(integer) --* Framerate denominator.
                                
                                - **FramerateNumerator** *(integer) --* Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps.
                                
                                - **GopClosedCadence** *(integer) --* Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting.
                                
                                - **GopSize** *(float) --* GOP Length (keyframe interval) in frames or seconds. Must be greater than zero.
                                
                                - **GopSizeUnits** *(string) --* Indicates if the GOP Size in MPEG2 is specified in frames or seconds. If seconds the system will convert the GOP Size into a frame count at run time.
                                
                                - **HrdBufferInitialFillPercentage** *(integer) --* Percentage of the buffer that should initially be filled (HRD buffer model).
                                
                                - **HrdBufferSize** *(integer) --* Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000.
                                
                                - **InterlaceMode** *(string) --* Use Interlace mode (InterlaceMode) to choose the scan line type for the output. * Top Field First (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce interlaced output with the entire output having the same field polarity (top or bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow, Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as the source. Therefore, behavior depends on the input scan type. - If the source is interlaced, the output will be interlaced with the same polarity as the source (it will follow the source). The output could therefore be a mix of \"top field first\" and \"bottom field first\". - If the source is progressive, the output will be interlaced with \"top field first\" or \"bottom field first\" polarity, depending on which of the Follow options you chose.
                                
                                - **IntraDcPrecision** *(string) --* Use Intra DC precision (Mpeg2IntraDcPrecision) to set quantization precision for intra-block DC coefficients. If you choose the value auto, the service will automatically select the precision based on the per-frame compression ratio.
                                
                                - **MaxBitrate** *(integer) --* Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000.
                                
                                - **MinIInterval** *(integer) --* Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. This setting is only used when Scene Change Detect is enabled. Note: Maximum GOP stretch = GOP size + Min-I-interval - 1
                                
                                - **NumberBFramesBetweenReferenceFrames** *(integer) --* Number of B-frames between reference frames.
                                
                                - **ParControl** *(string) --* Using the API, enable ParFollowSource if you want the service to use the pixel aspect ratio from the input. Using the console, do this by choosing Follow source for Pixel aspect ratio.
                                
                                - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.
                                
                                - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.
                                
                                - **QualityTuningLevel** *(string) --* Use Quality tuning level (Mpeg2QualityTuningLevel) to specifiy whether to use single-pass or multipass video encoding.
                                
                                - **RateControlMode** *(string) --* Use Rate control mode (Mpeg2RateControlMode) to specifiy whether the bitrate is variable (vbr) or constant (cbr).
                                
                                - **SceneChangeDetect** *(string) --* Scene change detection (inserts I-frames on scene changes).
                                
                                - **SlowPal** *(string) --* Enables Slow PAL rate conversion. 23.976fps and 24fps input is relabeled as 25fps, and audio is sped up correspondingly.
                                
                                - **Softness** *(integer) --* Softness. Selects quantizer matrix, larger values reduce high-frequency content in the encoded image.
                                
                                - **SpatialAdaptiveQuantization** *(string) --* Adjust quantization within each frame based on spatial variation of content complexity.
                                
                                - **Syntax** *(string) --* Produces a Type D-10 compatible bitstream (SMPTE 356M-2001).
                                
                                - **Telecine** *(string) --* Only use Telecine (Mpeg2Telecine) when you set Framerate (Framerate) to 29.970. Set Telecine (Mpeg2Telecine) to Hard (hard) to produce a 29.97i output from a 23.976 input. Set it to Soft (soft) to produce 23.976 output and leave converstion to the player.
                                
                                - **TemporalAdaptiveQuantization** *(string) --* Adjust quantization within each frame based on temporal variation of content complexity.
                            
                              - **ProresSettings** *(dict) --* Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the value PRORES.
                                
                                - **CodecProfile** *(string) --* Use Profile (ProResCodecProfile) to specifiy the type of Apple ProRes codec to use for this output.
                                
                                - **FramerateControl** *(string) --* If you are using the console, use the Framerate setting to specify the framerate for this output. If you want to keep the same framerate as the input video, choose Follow source. If you want to do framerate conversion, choose a framerate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your framerate as a fraction. If you are creating your transcoding job sepecification as a JSON file without the console, use FramerateControl to specify which value the service uses for the framerate for this output. Choose INITIALIZE_FROM_SOURCE if you want the service to use the framerate from the input. Choose SPECIFIED if you want the service to use the framerate you specify in the settings FramerateNumerator and FramerateDenominator.
                                
                                - **FramerateConversionAlgorithm** *(string) --* When set to INTERPOLATE, produces smoother motion during framerate conversion.
                                
                                - **FramerateDenominator** *(integer) --* Framerate denominator.
                                
                                - **FramerateNumerator** *(integer) --* When you use the API for transcode jobs that use framerate conversion, specify the framerate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator.
                                
                                - **InterlaceMode** *(string) --* Use Interlace mode (InterlaceMode) to choose the scan line type for the output. * Top Field First (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce interlaced output with the entire output having the same field polarity (top or bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow, Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as the source. Therefore, behavior depends on the input scan type. - If the source is interlaced, the output will be interlaced with the same polarity as the source (it will follow the source). The output could therefore be a mix of \"top field first\" and \"bottom field first\". - If the source is progressive, the output will be interlaced with \"top field first\" or \"bottom field first\" polarity, depending on which of the Follow options you chose.
                                
                                - **ParControl** *(string) --* Use (ProresParControl) to specify how the service determines the pixel aspect ratio. Set to Follow source (INITIALIZE_FROM_SOURCE) to use the pixel aspect ratio from the input. To specify a different pixel aspect ratio: Using the console, choose it from the dropdown menu. Using the API, set ProresParControl to (SPECIFIED) and provide for (ParNumerator) and (ParDenominator).
                                
                                - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.
                                
                                - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.
                                
                                - **SlowPal** *(string) --* Enables Slow PAL rate conversion. 23.976fps and 24fps input is relabeled as 25fps, and audio is sped up correspondingly.
                                
                                - **Telecine** *(string) --* Only use Telecine (ProresTelecine) when you set Framerate (Framerate) to 29.970. Set Telecine (ProresTelecine) to Hard (hard) to produce a 29.97i output from a 23.976 input. Set it to Soft (soft) to produce 23.976 output and leave converstion to the player.
                            
                            - **ColorMetadata** *(string) --* Enable Insert color metadata (ColorMetadata) to include color metadata in this output. This setting is enabled by default.
                            
                            - **Crop** *(dict) --* Applies only if your input aspect ratio is different from your output aspect ratio. Use Input cropping rectangle (Crop) to specify the video area the service will include in the output. This will crop the input source, causing video pixels to be removed on encode. Do not use this setting if you have enabled Stretch to output (stretchToOutput) in your output settings.
                              
                              - **Height** *(integer) --* Height of rectangle in pixels. Specify only even numbers.
                              
                              - **Width** *(integer) --* Width of rectangle in pixels. Specify only even numbers.
                              
                              - **X** *(integer) --* The distance, in pixels, between the rectangle and the left edge of the video frame. Specify only even numbers.
                              
                              - **Y** *(integer) --* The distance, in pixels, between the rectangle and the top edge of the video frame. Specify only even numbers.
                          
                            - **DropFrameTimecode** *(string) --* Applies only to 29.97 fps outputs. When this feature is enabled, the service will use drop-frame timecode on outputs. If it is not possible to use drop-frame timecode, the system will fall back to non-drop-frame. This setting is enabled by default when Timecode insertion (TimecodeInsertion) is enabled.
                            
                            - **FixedAfd** *(integer) --* Applies only if you set AFD Signaling(AfdSignaling) to Fixed (FIXED). Use Fixed (FixedAfd) to specify a four-bit AFD value which the service will write on all frames of this video output.
                            
                            - **Height** *(integer) --* Use the Height (Height) setting to define the video resolution height for this output. Specify in pixels. If you don\'t provide a value here, the service will use the input height.
                            
                            - **Position** *(dict) --* Use Position (Position) to point to a rectangle object to define your position. This setting overrides any other aspect ratio.
                              
                              - **Height** *(integer) --* Height of rectangle in pixels. Specify only even numbers.
                              
                              - **Width** *(integer) --* Width of rectangle in pixels. Specify only even numbers.
                              
                              - **X** *(integer) --* The distance, in pixels, between the rectangle and the left edge of the video frame. Specify only even numbers.
                              
                              - **Y** *(integer) --* The distance, in pixels, between the rectangle and the top edge of the video frame. Specify only even numbers.
                          
                            - **RespondToAfd** *(string) --* Use Respond to AFD (RespondToAfd) to specify how the service changes the video itself in response to AFD values in the input. * Choose Respond to clip the input video frame according to the AFD value, input display aspect ratio, and output display aspect ratio. * Choose Passthrough to include the input AFD values. Do not choose this when AfdSignaling is set to (NONE). A preferred implementation of this workflow is to set RespondToAfd to (NONE) and set AfdSignaling to (AUTO). * Choose None to remove all input AFD values from this output.
                            
                            - **ScalingBehavior** *(string) --* Applies only if your input aspect ratio is different from your output aspect ratio. Enable Stretch to output (StretchToOutput) to have the service stretch your video image to fit. Leave this setting disabled to allow the service to letterbox your video instead. This setting overrides any positioning value you specify elsewhere in the job.
                            
                            - **Sharpness** *(integer) --* Use Sharpness (Sharpness)setting to specify the strength of anti-aliasing. This setting changes the width of the anti-alias filter kernel used for scaling. Sharpness only applies if your output resolution is different from your input resolution, and if you set Anti-alias (AntiAlias) to ENABLED. 0 is the softest setting, 100 the sharpest, and 50 recommended for most content.
                            
                            - **TimecodeInsertion** *(string) --* Applies only to H.264, H.265, MPEG2, and ProRes outputs. Only enable Timecode insertion when the input framerate is identical to the output framerate. To include timecodes in this output, set Timecode insertion (VideoTimecodeInsertion) to PIC_TIMING_SEI. To leave them out, set it to DISABLED. Default is DISABLED. When the service inserts timecodes in an output, by default, it uses any embedded timecodes from the input. If none are present, the service will set the timecode for the first output frame to zero. To change this default behavior, adjust the settings under Timecode configuration (TimecodeConfig). In the console, these settings are located under Job > Job settings > Timecode configuration. Note - Timecode source under input settings (InputTimecodeSource) does not affect the timecodes that are inserted in the output. Source under Job settings > Timecode configuration (TimecodeSource) does.
                            
                            - **VideoPreprocessors** *(dict) --* Find additional transcoding features under Preprocessors (VideoPreprocessors). Enable the features at each output individually. These features are disabled by default.
                              
                              - **ColorCorrector** *(dict) --* Enable the Color corrector (ColorCorrector) feature if necessary. Enable or disable this feature for each output individually. This setting is disabled by default.
                                
                                - **Brightness** *(integer) --* Brightness level.
                                
                                - **ColorSpaceConversion** *(string) --* Determines if colorspace conversion will be performed. If set to _None_, no conversion will be performed. If _Force 601_ or _Force 709_ are selected, conversion will be performed for inputs with differing colorspaces. An input\'s colorspace can be specified explicitly in the \"Video Selector\":#inputs-video_selector if necessary.
                                
                                - **Contrast** *(integer) --* Contrast level.
                                
                                - **Hdr10Metadata** *(dict) --* Use the HDR master display (Hdr10Metadata) settings to correct HDR metadata or to provide missing metadata. These values vary depending on the input video and must be provided by a color grader. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that these settings are not color correction. Note that if you are creating HDR outputs inside of an HLS CMAF package, to comply with the Apple specification, you must use the HVC1 for H.265 setting.
                                  
                                  - **BluePrimaryX** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                                  
                                  - **BluePrimaryY** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                                  
                                  - **GreenPrimaryX** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                                  
                                  - **GreenPrimaryY** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                                  
                                  - **MaxContentLightLevel** *(integer) --* Maximum light level among all samples in the coded video sequence, in units of candelas per square meter.
                                  
                                  - **MaxFrameAverageLightLevel** *(integer) --* Maximum average light level of any frame in the coded video sequence, in units of candelas per square meter.
                                  
                                  - **MaxLuminance** *(integer) --* Nominal maximum mastering display luminance in units of of 0.0001 candelas per square meter.
                                  
                                  - **MinLuminance** *(integer) --* Nominal minimum mastering display luminance in units of of 0.0001 candelas per square meter
                                  
                                  - **RedPrimaryX** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                                  
                                  - **RedPrimaryY** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                                  
                                  - **WhitePointX** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                                  
                                  - **WhitePointY** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                              
                                - **Hue** *(integer) --* Hue in degrees.
                                
                                - **Saturation** *(integer) --* Saturation level.
                            
                              - **Deinterlacer** *(dict) --* Use Deinterlacer (Deinterlacer) to produce smoother motion and a clearer picture.
                                
                                - **Algorithm** *(string) --* Only applies when you set Deinterlacer (DeinterlaceMode) to Deinterlace (DEINTERLACE) or Adaptive (ADAPTIVE). Motion adaptive interpolate (INTERPOLATE) produces sharper pictures, while blend (BLEND) produces smoother motion. Use (INTERPOLATE_TICKER) OR (BLEND_TICKER) if your source file includes a ticker, such as a scrolling headline at the bottom of the frame.
                                
                                - **Control** *(string) --* - When set to NORMAL (default), the deinterlacer does not convert frames that are tagged in metadata as progressive. It will only convert those that are tagged as some other type. - When set to FORCE_ALL_FRAMES, the deinterlacer converts every frame to progressive - even those that are already tagged as progressive. Turn Force mode on only if there is a good chance that the metadata has tagged frames as progressive when they are not progressive. Do not turn on otherwise; processing frames that are already progressive into progressive will probably result in lower quality video.
                                
                                - **Mode** *(string) --* Use Deinterlacer (DeinterlaceMode) to choose how the service will do deinterlacing. Default is Deinterlace. - Deinterlace converts interlaced to progressive. - Inverse telecine converts Hard Telecine 29.97i to progressive 23.976p. - Adaptive auto-detects and converts to progressive.
                            
                              - **ImageInserter** *(dict) --* Enable the Image inserter (ImageInserter) feature to include a graphic overlay on your video. Enable or disable this feature for each output individually. This setting is disabled by default.
                                
                                - **InsertableImages** *(list) --* Image to insert. Must be 32 bit windows BMP, PNG, or TGA file. Must not be larger than the output frames.
                                  
                                  - *(dict) --* Settings for Insertable Image
                                    
                                    - **Duration** *(integer) --* Use Duration (Duration) to set the time, in milliseconds, for the image to remain on the output video.
                                    
                                    - **FadeIn** *(integer) --* Use Fade in (FadeIut) to set the length, in milliseconds, of the inserted image fade in. If you don\'t specify a value for Fade in, the image will appear abruptly at the Start time.
                                    
                                    - **FadeOut** *(integer) --* Use Fade out (FadeOut) to set the length, in milliseconds, of the inserted image fade out. If you don\'t specify a value for Fade out, the image will disappear abruptly at the end of the inserted image duration.
                                    
                                    - **Height** *(integer) --* Specify the Height (Height) of the inserted image. Use a value that is less than or equal to the video resolution height. Leave this setting blank to use the native height of the image.
                                    
                                    - **ImageInserterInput** *(string) --* Use Image location (imageInserterInput) to specify the Amazon S3 location of the image to be inserted into the output. Use a 32 bit BMP, PNG, or TGA file that fits inside the video frame.
                                    
                                    - **ImageX** *(integer) --* Use Left (ImageX) to set the distance, in pixels, between the inserted image and the left edge of the frame. Required for BMP, PNG and TGA input.
                                    
                                    - **ImageY** *(integer) --* Use Top (ImageY) to set the distance, in pixels, between the inserted image and the top edge of the video frame. Required for BMP, PNG and TGA input.
                                    
                                    - **Layer** *(integer) --* Use Layer (Layer) to specify how overlapping inserted images appear. Images with higher values of layer appear on top of images with lower values of layer.
                                    
                                    - **Opacity** *(integer) --* Use Opacity (Opacity) to specify how much of the underlying video shows through the inserted image. 0 is transparent and 100 is fully opaque. Default is 50.
                                    
                                    - **StartTime** *(string) --* Use Start time (StartTime) to specify the video timecode when the image is inserted in the output. This must be in timecode (HH:MM:SS:FF or HH:MM:SS;FF) format.
                                    
                                    - **Width** *(integer) --* Specify the Width (Width) of the inserted image. Use a value that is less than or equal to the video resolution width. Leave this setting blank to use the native width of the image.
                                
                              - **NoiseReducer** *(dict) --* Enable the Noise reducer (NoiseReducer) feature to remove noise from your video output if necessary. Enable or disable this feature for each output individually. This setting is disabled by default.
                                
                                - **Filter** *(string) --* Use Noise reducer filter (NoiseReducerFilter) to select one of the following spatial image filtering functions. To use this setting, you must also enable Noise reducer (NoiseReducer). * Bilateral is an edge preserving noise reduction filter. * Mean (softest), Gaussian, Lanczos, and Sharpen (sharpest) are convolution filters. * Conserve is a min/max noise reduction filter. * Spatial is a frequency-domain filter based on JND principles.
                                
                                - **FilterSettings** *(dict) --* Settings for a noise reducer filter
                                  
                                  - **Strength** *(integer) --* Relative strength of noise reducing filter. Higher values produce stronger filtering.
                              
                                - **SpatialFilterSettings** *(dict) --* Noise reducer filter settings for spatial filter.
                                  
                                  - **PostFilterSharpenStrength** *(integer) --* Specify strength of post noise reduction sharpening filter, with 0 disabling the filter and 3 enabling it at maximum strength.
                                  
                                  - **Speed** *(integer) --* The speed of the filter, from -2 (lower speed) to 3 (higher speed), with 0 being the nominal value.
                                  
                                  - **Strength** *(integer) --* Relative strength of noise reducing filter. Higher values produce stronger filtering.
                              
                              - **TimecodeBurnin** *(dict) --* Timecode burn-in (TimecodeBurnIn)--Burns the output timecode and specified prefix into the output.
                                
                                - **FontSize** *(integer) --* Use Font Size (FontSize) to set the font size of any burned-in timecode. Valid values are 10, 16, 32, 48.
                                
                                - **Position** *(string) --* Use Position (Position) under under Timecode burn-in (TimecodeBurnIn) to specify the location the burned-in timecode on output video.
                                
                                - **Prefix** *(string) --* Use Prefix (Prefix) to place ASCII characters before any burned-in timecode. For example, a prefix of \"EZ-\" will result in the timecode \"EZ-00:00:00:00\". Provide either the characters themselves or the ASCII code equivalents. The supported range of characters is 0x20 through 0x7e. This includes letters, numbers, and all special characters represented on a standard English keyboard.
                            
                            - **Width** *(integer) --* Use Width (Width) to define the video resolution width, in pixels, for this output. If you don\'t provide a value here, the service will use the input width.
                        
                  - **TimecodeConfig** *(dict) --* Contains settings used to acquire and adjust timecode information from inputs.
                    
                    - **Anchor** *(string) --* If you use an editing platform that relies on an anchor timecode, use Anchor Timecode (Anchor) to specify a timecode that will match the input video frame to the output video frame. Use 24-hour format with frame number, (HH:MM:SS:FF) or (HH:MM:SS;FF). This setting ignores framerate conversion. System behavior for Anchor Timecode varies depending on your setting for Source (TimecodeSource). * If Source (TimecodeSource) is set to Specified Start (SPECIFIEDSTART), the first input frame is the specified value in Start Timecode (Start). Anchor Timecode (Anchor) and Start Timecode (Start) are used calculate output timecode. * If Source (TimecodeSource) is set to Start at 0 (ZEROBASED) the first frame is 00:00:00:00. * If Source (TimecodeSource) is set to Embedded (EMBEDDED), the first frame is the timecode value on the first input frame of the input.
                    
                    - **Source** *(string) --* Use Source (TimecodeSource) to set how timecodes are handled within this job. To make sure that your video, audio, captions, and markers are synchronized and that time-based features, such as image inserter, work correctly, choose the Timecode source option that matches your assets. All timecodes are in a 24-hour format with frame number (HH:MM:SS:FF). * Embedded (EMBEDDED) - Use the timecode that is in the input video. If no embedded timecode is in the source, the service will use Start at 0 (ZEROBASED) instead. * Start at 0 (ZEROBASED) - Set the timecode of the initial frame to 00:00:00:00. * Specified Start (SPECIFIEDSTART) - Set the timecode of the initial frame to a value other than zero. You use Start timecode (Start) to provide this value.
                    
                    - **Start** *(string) --* Only use when you set Source (TimecodeSource) to Specified start (SPECIFIEDSTART). Use Start timecode (Start) to specify the timecode for the initial frame. Use 24-hour format with frame number, (HH:MM:SS:FF) or (HH:MM:SS;FF).
                    
                    - **TimestampOffset** *(string) --* Only applies to outputs that support program-date-time stamp. Use Timestamp offset (TimestampOffset) to overwrite the timecode date without affecting the time and frame number. Provide the new date as a string in the format \"yyyy-mm-dd\". To use Time stamp offset, you must also enable Insert program-date-time (InsertProgramDateTime) in the output settings. For example, if the date part of your timecodes is 2002-1-25 and you want to change it to one year later, set Timestamp offset (TimestampOffset) to 2003-1-25.
                
                  - **TimedMetadataInsertion** *(dict) --* Enable Timed metadata insertion (TimedMetadataInsertion) to include ID3 tags in your job. To include timed metadata, you must enable it here, enable it in each output container, and specify tags and timecodes in ID3 insertion (Id3Insertion) objects.
                    
                    - **Id3Insertions** *(list) --* Id3Insertions contains the array of Id3Insertion instances.
                      
                      - *(dict) --* To insert ID3 tags in your output, specify two values. Use ID3 tag (Id3) to specify the base 64 encoded string and use Timecode (TimeCode) to specify the time when the tag should be inserted. To insert multiple ID3 tags in your output, create multiple instances of ID3 insertion (Id3Insertion).
                        
                        - **Id3** *(string) --* Use ID3 tag (Id3) to provide a tag value in base64-encode format.
                        
                        - **Timecode** *(string) --* Provide a Timecode (TimeCode) in HH:MM:SS:FF or HH:MM:SS;FF format.
                    
                - **Status** *(string) --* A job\'s status can be SUBMITTED, PROGRESSING, COMPLETE, CANCELED, or ERROR.
                
                - **Timing** *(dict) --* Information about when jobs are submitted, started, and finished is specified in Unix epoch format in seconds.
                  
                  - **FinishTime** *(datetime) --* The time, in Unix epoch format, that the transcoding job finished
                  
                  - **StartTime** *(datetime) --* The time, in Unix epoch format, that transcoding for the job began.
                  
                  - **SubmitTime** *(datetime) --* The time, in Unix epoch format, that you submitted the job.
              
                - **UserMetadata** *(dict) --* User-defined metadata that you want to associate with an MediaConvert job. You specify metadata in key/value pairs.
                  
                  - *(string) --* 
                    
                    - *(string) --* 
              
        """
        pass


class ListPresets(Paginator):
    def paginate(self, Category: str = None, ListBy: str = None, Order: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediaconvert-2017-08-29/ListPresets>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Category=\'string\',
              ListBy=\'NAME\'|\'CREATION_DATE\'|\'SYSTEM\',
              Order=\'ASCENDING\'|\'DESCENDING\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Category: string
        :param Category: Optionally, specify a preset category to limit responses to only presets from that category.
        
        :type ListBy: string
        :param ListBy: Optional. When you request a list of presets, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don\'t specify, the service will list them by name.
        
        :type Order: string
        :param Order: When you request lists of resources, you can optionally specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.
        
        :type PaginationConfig: dict
        :param PaginationConfig: 
        
          A dictionary that provides parameters to control pagination.
        
          - **MaxItems** *(integer) --* 
        
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
        
          - **PageSize** *(integer) --* 
        
            The size of each page.
        
          - **StartingToken** *(string) --* 
        
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Presets\': [
                    {
                        \'Arn\': \'string\',
                        \'Category\': \'string\',
                        \'CreatedAt\': datetime(2015, 1, 1),
                        \'Description\': \'string\',
                        \'LastUpdated\': datetime(2015, 1, 1),
                        \'Name\': \'string\',
                        \'Settings\': {
                            \'AudioDescriptions\': [
                                {
                                    \'AudioNormalizationSettings\': {
                                        \'Algorithm\': \'ITU_BS_1770_1\'|\'ITU_BS_1770_2\',
                                        \'AlgorithmControl\': \'CORRECT_AUDIO\'|\'MEASURE_ONLY\',
                                        \'CorrectionGateLevel\': 123,
                                        \'LoudnessLogging\': \'LOG\'|\'DONT_LOG\',
                                        \'PeakCalculation\': \'TRUE_PEAK\'|\'NONE\',
                                        \'TargetLkfs\': 123.0
                                    },
                                    \'AudioSourceName\': \'string\',
                                    \'AudioType\': 123,
                                    \'AudioTypeControl\': \'FOLLOW_INPUT\'|\'USE_CONFIGURED\',
                                    \'CodecSettings\': {
                                        \'AacSettings\': {
                                            \'AudioDescriptionBroadcasterMix\': \'BROADCASTER_MIXED_AD\'|\'NORMAL\',
                                            \'Bitrate\': 123,
                                            \'CodecProfile\': \'LC\'|\'HEV1\'|\'HEV2\',
                                            \'CodingMode\': \'AD_RECEIVER_MIX\'|\'CODING_MODE_1_0\'|\'CODING_MODE_1_1\'|\'CODING_MODE_2_0\'|\'CODING_MODE_5_1\',
                                            \'RateControlMode\': \'CBR\'|\'VBR\',
                                            \'RawFormat\': \'LATM_LOAS\'|\'NONE\',
                                            \'SampleRate\': 123,
                                            \'Specification\': \'MPEG2\'|\'MPEG4\',
                                            \'VbrQuality\': \'LOW\'|\'MEDIUM_LOW\'|\'MEDIUM_HIGH\'|\'HIGH\'
                                        },
                                        \'Ac3Settings\': {
                                            \'Bitrate\': 123,
                                            \'BitstreamMode\': \'COMPLETE_MAIN\'|\'COMMENTARY\'|\'DIALOGUE\'|\'EMERGENCY\'|\'HEARING_IMPAIRED\'|\'MUSIC_AND_EFFECTS\'|\'VISUALLY_IMPAIRED\'|\'VOICE_OVER\',
                                            \'CodingMode\': \'CODING_MODE_1_0\'|\'CODING_MODE_1_1\'|\'CODING_MODE_2_0\'|\'CODING_MODE_3_2_LFE\',
                                            \'Dialnorm\': 123,
                                            \'DynamicRangeCompressionProfile\': \'FILM_STANDARD\'|\'NONE\',
                                            \'LfeFilter\': \'ENABLED\'|\'DISABLED\',
                                            \'MetadataControl\': \'FOLLOW_INPUT\'|\'USE_CONFIGURED\',
                                            \'SampleRate\': 123
                                        },
                                        \'AiffSettings\': {
                                            \'BitDepth\': 123,
                                            \'Channels\': 123,
                                            \'SampleRate\': 123
                                        },
                                        \'Codec\': \'AAC\'|\'MP2\'|\'WAV\'|\'AIFF\'|\'AC3\'|\'EAC3\'|\'PASSTHROUGH\',
                                        \'Eac3Settings\': {
                                            \'AttenuationControl\': \'ATTENUATE_3_DB\'|\'NONE\',
                                            \'Bitrate\': 123,
                                            \'BitstreamMode\': \'COMPLETE_MAIN\'|\'COMMENTARY\'|\'EMERGENCY\'|\'HEARING_IMPAIRED\'|\'VISUALLY_IMPAIRED\',
                                            \'CodingMode\': \'CODING_MODE_1_0\'|\'CODING_MODE_2_0\'|\'CODING_MODE_3_2\',
                                            \'DcFilter\': \'ENABLED\'|\'DISABLED\',
                                            \'Dialnorm\': 123,
                                            \'DynamicRangeCompressionLine\': \'NONE\'|\'FILM_STANDARD\'|\'FILM_LIGHT\'|\'MUSIC_STANDARD\'|\'MUSIC_LIGHT\'|\'SPEECH\',
                                            \'DynamicRangeCompressionRf\': \'NONE\'|\'FILM_STANDARD\'|\'FILM_LIGHT\'|\'MUSIC_STANDARD\'|\'MUSIC_LIGHT\'|\'SPEECH\',
                                            \'LfeControl\': \'LFE\'|\'NO_LFE\',
                                            \'LfeFilter\': \'ENABLED\'|\'DISABLED\',
                                            \'LoRoCenterMixLevel\': 123.0,
                                            \'LoRoSurroundMixLevel\': 123.0,
                                            \'LtRtCenterMixLevel\': 123.0,
                                            \'LtRtSurroundMixLevel\': 123.0,
                                            \'MetadataControl\': \'FOLLOW_INPUT\'|\'USE_CONFIGURED\',
                                            \'PassthroughControl\': \'WHEN_POSSIBLE\'|\'NO_PASSTHROUGH\',
                                            \'PhaseControl\': \'SHIFT_90_DEGREES\'|\'NO_SHIFT\',
                                            \'SampleRate\': 123,
                                            \'StereoDownmix\': \'NOT_INDICATED\'|\'LO_RO\'|\'LT_RT\'|\'DPL2\',
                                            \'SurroundExMode\': \'NOT_INDICATED\'|\'ENABLED\'|\'DISABLED\',
                                            \'SurroundMode\': \'NOT_INDICATED\'|\'ENABLED\'|\'DISABLED\'
                                        },
                                        \'Mp2Settings\': {
                                            \'Bitrate\': 123,
                                            \'Channels\': 123,
                                            \'SampleRate\': 123
                                        },
                                        \'WavSettings\': {
                                            \'BitDepth\': 123,
                                            \'Channels\': 123,
                                            \'Format\': \'RIFF\'|\'RF64\',
                                            \'SampleRate\': 123
                                        }
                                    },
                                    \'CustomLanguageCode\': \'string\',
                                    \'LanguageCode\': \'ENG\'|\'SPA\'|\'FRA\'|\'DEU\'|\'GER\'|\'ZHO\'|\'ARA\'|\'HIN\'|\'JPN\'|\'RUS\'|\'POR\'|\'ITA\'|\'URD\'|\'VIE\'|\'KOR\'|\'PAN\'|\'ABK\'|\'AAR\'|\'AFR\'|\'AKA\'|\'SQI\'|\'AMH\'|\'ARG\'|\'HYE\'|\'ASM\'|\'AVA\'|\'AVE\'|\'AYM\'|\'AZE\'|\'BAM\'|\'BAK\'|\'EUS\'|\'BEL\'|\'BEN\'|\'BIH\'|\'BIS\'|\'BOS\'|\'BRE\'|\'BUL\'|\'MYA\'|\'CAT\'|\'KHM\'|\'CHA\'|\'CHE\'|\'NYA\'|\'CHU\'|\'CHV\'|\'COR\'|\'COS\'|\'CRE\'|\'HRV\'|\'CES\'|\'DAN\'|\'DIV\'|\'NLD\'|\'DZO\'|\'ENM\'|\'EPO\'|\'EST\'|\'EWE\'|\'FAO\'|\'FIJ\'|\'FIN\'|\'FRM\'|\'FUL\'|\'GLA\'|\'GLG\'|\'LUG\'|\'KAT\'|\'ELL\'|\'GRN\'|\'GUJ\'|\'HAT\'|\'HAU\'|\'HEB\'|\'HER\'|\'HMO\'|\'HUN\'|\'ISL\'|\'IDO\'|\'IBO\'|\'IND\'|\'INA\'|\'ILE\'|\'IKU\'|\'IPK\'|\'GLE\'|\'JAV\'|\'KAL\'|\'KAN\'|\'KAU\'|\'KAS\'|\'KAZ\'|\'KIK\'|\'KIN\'|\'KIR\'|\'KOM\'|\'KON\'|\'KUA\'|\'KUR\'|\'LAO\'|\'LAT\'|\'LAV\'|\'LIM\'|\'LIN\'|\'LIT\'|\'LUB\'|\'LTZ\'|\'MKD\'|\'MLG\'|\'MSA\'|\'MAL\'|\'MLT\'|\'GLV\'|\'MRI\'|\'MAR\'|\'MAH\'|\'MON\'|\'NAU\'|\'NAV\'|\'NDE\'|\'NBL\'|\'NDO\'|\'NEP\'|\'SME\'|\'NOR\'|\'NOB\'|\'NNO\'|\'OCI\'|\'OJI\'|\'ORI\'|\'ORM\'|\'OSS\'|\'PLI\'|\'FAS\'|\'POL\'|\'PUS\'|\'QUE\'|\'QAA\'|\'RON\'|\'ROH\'|\'RUN\'|\'SMO\'|\'SAG\'|\'SAN\'|\'SRD\'|\'SRB\'|\'SNA\'|\'III\'|\'SND\'|\'SIN\'|\'SLK\'|\'SLV\'|\'SOM\'|\'SOT\'|\'SUN\'|\'SWA\'|\'SSW\'|\'SWE\'|\'TGL\'|\'TAH\'|\'TGK\'|\'TAM\'|\'TAT\'|\'TEL\'|\'THA\'|\'BOD\'|\'TIR\'|\'TON\'|\'TSO\'|\'TSN\'|\'TUR\'|\'TUK\'|\'TWI\'|\'UIG\'|\'UKR\'|\'UZB\'|\'VEN\'|\'VOL\'|\'WLN\'|\'CYM\'|\'FRY\'|\'WOL\'|\'XHO\'|\'YID\'|\'YOR\'|\'ZHA\'|\'ZUL\'|\'ORJ\'|\'QPC\'|\'TNG\',
                                    \'LanguageCodeControl\': \'FOLLOW_INPUT\'|\'USE_CONFIGURED\',
                                    \'RemixSettings\': {
                                        \'ChannelMapping\': {
                                            \'OutputChannels\': [
                                                {
                                                    \'InputChannels\': [
                                                        123,
                                                    ]
                                                },
                                            ]
                                        },
                                        \'ChannelsIn\': 123,
                                        \'ChannelsOut\': 123
                                    },
                                    \'StreamName\': \'string\'
                                },
                            ],
                            \'CaptionDescriptions\': [
                                {
                                    \'CustomLanguageCode\': \'string\',
                                    \'DestinationSettings\': {
                                        \'BurninDestinationSettings\': {
                                            \'Alignment\': \'CENTERED\'|\'LEFT\',
                                            \'BackgroundColor\': \'NONE\'|\'BLACK\'|\'WHITE\',
                                            \'BackgroundOpacity\': 123,
                                            \'FontColor\': \'WHITE\'|\'BLACK\'|\'YELLOW\'|\'RED\'|\'GREEN\'|\'BLUE\',
                                            \'FontOpacity\': 123,
                                            \'FontResolution\': 123,
                                            \'FontSize\': 123,
                                            \'OutlineColor\': \'BLACK\'|\'WHITE\'|\'YELLOW\'|\'RED\'|\'GREEN\'|\'BLUE\',
                                            \'OutlineSize\': 123,
                                            \'ShadowColor\': \'NONE\'|\'BLACK\'|\'WHITE\',
                                            \'ShadowOpacity\': 123,
                                            \'ShadowXOffset\': 123,
                                            \'ShadowYOffset\': 123,
                                            \'TeletextSpacing\': \'FIXED_GRID\'|\'PROPORTIONAL\',
                                            \'XPosition\': 123,
                                            \'YPosition\': 123
                                        },
                                        \'DestinationType\': \'BURN_IN\'|\'DVB_SUB\'|\'EMBEDDED\'|\'SCC\'|\'SRT\'|\'TELETEXT\'|\'TTML\'|\'WEBVTT\',
                                        \'DvbSubDestinationSettings\': {
                                            \'Alignment\': \'CENTERED\'|\'LEFT\',
                                            \'BackgroundColor\': \'NONE\'|\'BLACK\'|\'WHITE\',
                                            \'BackgroundOpacity\': 123,
                                            \'FontColor\': \'WHITE\'|\'BLACK\'|\'YELLOW\'|\'RED\'|\'GREEN\'|\'BLUE\',
                                            \'FontOpacity\': 123,
                                            \'FontResolution\': 123,
                                            \'FontSize\': 123,
                                            \'OutlineColor\': \'BLACK\'|\'WHITE\'|\'YELLOW\'|\'RED\'|\'GREEN\'|\'BLUE\',
                                            \'OutlineSize\': 123,
                                            \'ShadowColor\': \'NONE\'|\'BLACK\'|\'WHITE\',
                                            \'ShadowOpacity\': 123,
                                            \'ShadowXOffset\': 123,
                                            \'ShadowYOffset\': 123,
                                            \'TeletextSpacing\': \'FIXED_GRID\'|\'PROPORTIONAL\',
                                            \'XPosition\': 123,
                                            \'YPosition\': 123
                                        },
                                        \'SccDestinationSettings\': {
                                            \'Framerate\': \'FRAMERATE_23_97\'|\'FRAMERATE_24\'|\'FRAMERATE_29_97_DROPFRAME\'|\'FRAMERATE_29_97_NON_DROPFRAME\'
                                        },
                                        \'TeletextDestinationSettings\': {
                                            \'PageNumber\': \'string\'
                                        },
                                        \'TtmlDestinationSettings\': {
                                            \'StylePassthrough\': \'ENABLED\'|\'DISABLED\'
                                        }
                                    },
                                    \'LanguageCode\': \'ENG\'|\'SPA\'|\'FRA\'|\'DEU\'|\'GER\'|\'ZHO\'|\'ARA\'|\'HIN\'|\'JPN\'|\'RUS\'|\'POR\'|\'ITA\'|\'URD\'|\'VIE\'|\'KOR\'|\'PAN\'|\'ABK\'|\'AAR\'|\'AFR\'|\'AKA\'|\'SQI\'|\'AMH\'|\'ARG\'|\'HYE\'|\'ASM\'|\'AVA\'|\'AVE\'|\'AYM\'|\'AZE\'|\'BAM\'|\'BAK\'|\'EUS\'|\'BEL\'|\'BEN\'|\'BIH\'|\'BIS\'|\'BOS\'|\'BRE\'|\'BUL\'|\'MYA\'|\'CAT\'|\'KHM\'|\'CHA\'|\'CHE\'|\'NYA\'|\'CHU\'|\'CHV\'|\'COR\'|\'COS\'|\'CRE\'|\'HRV\'|\'CES\'|\'DAN\'|\'DIV\'|\'NLD\'|\'DZO\'|\'ENM\'|\'EPO\'|\'EST\'|\'EWE\'|\'FAO\'|\'FIJ\'|\'FIN\'|\'FRM\'|\'FUL\'|\'GLA\'|\'GLG\'|\'LUG\'|\'KAT\'|\'ELL\'|\'GRN\'|\'GUJ\'|\'HAT\'|\'HAU\'|\'HEB\'|\'HER\'|\'HMO\'|\'HUN\'|\'ISL\'|\'IDO\'|\'IBO\'|\'IND\'|\'INA\'|\'ILE\'|\'IKU\'|\'IPK\'|\'GLE\'|\'JAV\'|\'KAL\'|\'KAN\'|\'KAU\'|\'KAS\'|\'KAZ\'|\'KIK\'|\'KIN\'|\'KIR\'|\'KOM\'|\'KON\'|\'KUA\'|\'KUR\'|\'LAO\'|\'LAT\'|\'LAV\'|\'LIM\'|\'LIN\'|\'LIT\'|\'LUB\'|\'LTZ\'|\'MKD\'|\'MLG\'|\'MSA\'|\'MAL\'|\'MLT\'|\'GLV\'|\'MRI\'|\'MAR\'|\'MAH\'|\'MON\'|\'NAU\'|\'NAV\'|\'NDE\'|\'NBL\'|\'NDO\'|\'NEP\'|\'SME\'|\'NOR\'|\'NOB\'|\'NNO\'|\'OCI\'|\'OJI\'|\'ORI\'|\'ORM\'|\'OSS\'|\'PLI\'|\'FAS\'|\'POL\'|\'PUS\'|\'QUE\'|\'QAA\'|\'RON\'|\'ROH\'|\'RUN\'|\'SMO\'|\'SAG\'|\'SAN\'|\'SRD\'|\'SRB\'|\'SNA\'|\'III\'|\'SND\'|\'SIN\'|\'SLK\'|\'SLV\'|\'SOM\'|\'SOT\'|\'SUN\'|\'SWA\'|\'SSW\'|\'SWE\'|\'TGL\'|\'TAH\'|\'TGK\'|\'TAM\'|\'TAT\'|\'TEL\'|\'THA\'|\'BOD\'|\'TIR\'|\'TON\'|\'TSO\'|\'TSN\'|\'TUR\'|\'TUK\'|\'TWI\'|\'UIG\'|\'UKR\'|\'UZB\'|\'VEN\'|\'VOL\'|\'WLN\'|\'CYM\'|\'FRY\'|\'WOL\'|\'XHO\'|\'YID\'|\'YOR\'|\'ZHA\'|\'ZUL\'|\'ORJ\'|\'QPC\'|\'TNG\',
                                    \'LanguageDescription\': \'string\'
                                },
                            ],
                            \'ContainerSettings\': {
                                \'Container\': \'F4V\'|\'ISMV\'|\'M2TS\'|\'M3U8\'|\'CMFC\'|\'MOV\'|\'MP4\'|\'MPD\'|\'MXF\'|\'RAW\',
                                \'F4vSettings\': {
                                    \'MoovPlacement\': \'PROGRESSIVE_DOWNLOAD\'|\'NORMAL\'
                                },
                                \'M2tsSettings\': {
                                    \'AudioBufferModel\': \'DVB\'|\'ATSC\',
                                    \'AudioFramesPerPes\': 123,
                                    \'AudioPids\': [
                                        123,
                                    ],
                                    \'Bitrate\': 123,
                                    \'BufferModel\': \'MULTIPLEX\'|\'NONE\',
                                    \'DvbNitSettings\': {
                                        \'NetworkId\': 123,
                                        \'NetworkName\': \'string\',
                                        \'NitInterval\': 123
                                    },
                                    \'DvbSdtSettings\': {
                                        \'OutputSdt\': \'SDT_FOLLOW\'|\'SDT_FOLLOW_IF_PRESENT\'|\'SDT_MANUAL\'|\'SDT_NONE\',
                                        \'SdtInterval\': 123,
                                        \'ServiceName\': \'string\',
                                        \'ServiceProviderName\': \'string\'
                                    },
                                    \'DvbSubPids\': [
                                        123,
                                    ],
                                    \'DvbTdtSettings\': {
                                        \'TdtInterval\': 123
                                    },
                                    \'DvbTeletextPid\': 123,
                                    \'EbpAudioInterval\': \'VIDEO_AND_FIXED_INTERVALS\'|\'VIDEO_INTERVAL\',
                                    \'EbpPlacement\': \'VIDEO_AND_AUDIO_PIDS\'|\'VIDEO_PID\',
                                    \'EsRateInPes\': \'INCLUDE\'|\'EXCLUDE\',
                                    \'FragmentTime\': 123.0,
                                    \'MaxPcrInterval\': 123,
                                    \'MinEbpInterval\': 123,
                                    \'NielsenId3\': \'INSERT\'|\'NONE\',
                                    \'NullPacketBitrate\': 123.0,
                                    \'PatInterval\': 123,
                                    \'PcrControl\': \'PCR_EVERY_PES_PACKET\'|\'CONFIGURED_PCR_PERIOD\',
                                    \'PcrPid\': 123,
                                    \'PmtInterval\': 123,
                                    \'PmtPid\': 123,
                                    \'PrivateMetadataPid\': 123,
                                    \'ProgramNumber\': 123,
                                    \'RateMode\': \'VBR\'|\'CBR\',
                                    \'Scte35Pid\': 123,
                                    \'Scte35Source\': \'PASSTHROUGH\'|\'NONE\',
                                    \'SegmentationMarkers\': \'NONE\'|\'RAI_SEGSTART\'|\'RAI_ADAPT\'|\'PSI_SEGSTART\'|\'EBP\'|\'EBP_LEGACY\',
                                    \'SegmentationStyle\': \'MAINTAIN_CADENCE\'|\'RESET_CADENCE\',
                                    \'SegmentationTime\': 123.0,
                                    \'TimedMetadataPid\': 123,
                                    \'TransportStreamId\': 123,
                                    \'VideoPid\': 123
                                },
                                \'M3u8Settings\': {
                                    \'AudioFramesPerPes\': 123,
                                    \'AudioPids\': [
                                        123,
                                    ],
                                    \'NielsenId3\': \'INSERT\'|\'NONE\',
                                    \'PatInterval\': 123,
                                    \'PcrControl\': \'PCR_EVERY_PES_PACKET\'|\'CONFIGURED_PCR_PERIOD\',
                                    \'PcrPid\': 123,
                                    \'PmtInterval\': 123,
                                    \'PmtPid\': 123,
                                    \'PrivateMetadataPid\': 123,
                                    \'ProgramNumber\': 123,
                                    \'Scte35Pid\': 123,
                                    \'Scte35Source\': \'PASSTHROUGH\'|\'NONE\',
                                    \'TimedMetadata\': \'PASSTHROUGH\'|\'NONE\',
                                    \'TimedMetadataPid\': 123,
                                    \'TransportStreamId\': 123,
                                    \'VideoPid\': 123
                                },
                                \'MovSettings\': {
                                    \'ClapAtom\': \'INCLUDE\'|\'EXCLUDE\',
                                    \'CslgAtom\': \'INCLUDE\'|\'EXCLUDE\',
                                    \'Mpeg2FourCCControl\': \'XDCAM\'|\'MPEG\',
                                    \'PaddingControl\': \'OMNEON\'|\'NONE\',
                                    \'Reference\': \'SELF_CONTAINED\'|\'EXTERNAL\'
                                },
                                \'Mp4Settings\': {
                                    \'CslgAtom\': \'INCLUDE\'|\'EXCLUDE\',
                                    \'FreeSpaceBox\': \'INCLUDE\'|\'EXCLUDE\',
                                    \'MoovPlacement\': \'PROGRESSIVE_DOWNLOAD\'|\'NORMAL\',
                                    \'Mp4MajorBrand\': \'string\'
                                }
                            },
                            \'VideoDescription\': {
                                \'AfdSignaling\': \'NONE\'|\'AUTO\'|\'FIXED\',
                                \'AntiAlias\': \'DISABLED\'|\'ENABLED\',
                                \'CodecSettings\': {
                                    \'Codec\': \'FRAME_CAPTURE\'|\'H_264\'|\'H_265\'|\'MPEG2\'|\'PRORES\',
                                    \'FrameCaptureSettings\': {
                                        \'FramerateDenominator\': 123,
                                        \'FramerateNumerator\': 123,
                                        \'MaxCaptures\': 123,
                                        \'Quality\': 123
                                    },
                                    \'H264Settings\': {
                                        \'AdaptiveQuantization\': \'OFF\'|\'LOW\'|\'MEDIUM\'|\'HIGH\'|\'HIGHER\'|\'MAX\',
                                        \'Bitrate\': 123,
                                        \'CodecLevel\': \'AUTO\'|\'LEVEL_1\'|\'LEVEL_1_1\'|\'LEVEL_1_2\'|\'LEVEL_1_3\'|\'LEVEL_2\'|\'LEVEL_2_1\'|\'LEVEL_2_2\'|\'LEVEL_3\'|\'LEVEL_3_1\'|\'LEVEL_3_2\'|\'LEVEL_4\'|\'LEVEL_4_1\'|\'LEVEL_4_2\'|\'LEVEL_5\'|\'LEVEL_5_1\'|\'LEVEL_5_2\',
                                        \'CodecProfile\': \'BASELINE\'|\'HIGH\'|\'HIGH_10BIT\'|\'HIGH_422\'|\'HIGH_422_10BIT\'|\'MAIN\',
                                        \'DynamicSubGop\': \'ADAPTIVE\'|\'STATIC\',
                                        \'EntropyEncoding\': \'CABAC\'|\'CAVLC\',
                                        \'FieldEncoding\': \'PAFF\'|\'FORCE_FIELD\',
                                        \'FlickerAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\',
                                        \'FramerateControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                        \'FramerateConversionAlgorithm\': \'DUPLICATE_DROP\'|\'INTERPOLATE\',
                                        \'FramerateDenominator\': 123,
                                        \'FramerateNumerator\': 123,
                                        \'GopBReference\': \'DISABLED\'|\'ENABLED\',
                                        \'GopClosedCadence\': 123,
                                        \'GopSize\': 123.0,
                                        \'GopSizeUnits\': \'FRAMES\'|\'SECONDS\',
                                        \'HrdBufferInitialFillPercentage\': 123,
                                        \'HrdBufferSize\': 123,
                                        \'InterlaceMode\': \'PROGRESSIVE\'|\'TOP_FIELD\'|\'BOTTOM_FIELD\'|\'FOLLOW_TOP_FIELD\'|\'FOLLOW_BOTTOM_FIELD\',
                                        \'MaxBitrate\': 123,
                                        \'MinIInterval\': 123,
                                        \'NumberBFramesBetweenReferenceFrames\': 123,
                                        \'NumberReferenceFrames\': 123,
                                        \'ParControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                        \'ParDenominator\': 123,
                                        \'ParNumerator\': 123,
                                        \'QualityTuningLevel\': \'SINGLE_PASS\'|\'SINGLE_PASS_HQ\'|\'MULTI_PASS_HQ\',
                                        \'QvbrSettings\': {
                                            \'MaxAverageBitrate\': 123,
                                            \'QvbrQualityLevel\': 123
                                        },
                                        \'RateControlMode\': \'VBR\'|\'CBR\'|\'QVBR\',
                                        \'RepeatPps\': \'DISABLED\'|\'ENABLED\',
                                        \'SceneChangeDetect\': \'DISABLED\'|\'ENABLED\',
                                        \'Slices\': 123,
                                        \'SlowPal\': \'DISABLED\'|\'ENABLED\',
                                        \'Softness\': 123,
                                        \'SpatialAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\',
                                        \'Syntax\': \'DEFAULT\'|\'RP2027\',
                                        \'Telecine\': \'NONE\'|\'SOFT\'|\'HARD\',
                                        \'TemporalAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\',
                                        \'UnregisteredSeiTimecode\': \'DISABLED\'|\'ENABLED\'
                                    },
                                    \'H265Settings\': {
                                        \'AdaptiveQuantization\': \'OFF\'|\'LOW\'|\'MEDIUM\'|\'HIGH\'|\'HIGHER\'|\'MAX\',
                                        \'AlternateTransferFunctionSei\': \'DISABLED\'|\'ENABLED\',
                                        \'Bitrate\': 123,
                                        \'CodecLevel\': \'AUTO\'|\'LEVEL_1\'|\'LEVEL_2\'|\'LEVEL_2_1\'|\'LEVEL_3\'|\'LEVEL_3_1\'|\'LEVEL_4\'|\'LEVEL_4_1\'|\'LEVEL_5\'|\'LEVEL_5_1\'|\'LEVEL_5_2\'|\'LEVEL_6\'|\'LEVEL_6_1\'|\'LEVEL_6_2\',
                                        \'CodecProfile\': \'MAIN_MAIN\'|\'MAIN_HIGH\'|\'MAIN10_MAIN\'|\'MAIN10_HIGH\'|\'MAIN_422_8BIT_MAIN\'|\'MAIN_422_8BIT_HIGH\'|\'MAIN_422_10BIT_MAIN\'|\'MAIN_422_10BIT_HIGH\',
                                        \'DynamicSubGop\': \'ADAPTIVE\'|\'STATIC\',
                                        \'FlickerAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\',
                                        \'FramerateControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                        \'FramerateConversionAlgorithm\': \'DUPLICATE_DROP\'|\'INTERPOLATE\',
                                        \'FramerateDenominator\': 123,
                                        \'FramerateNumerator\': 123,
                                        \'GopBReference\': \'DISABLED\'|\'ENABLED\',
                                        \'GopClosedCadence\': 123,
                                        \'GopSize\': 123.0,
                                        \'GopSizeUnits\': \'FRAMES\'|\'SECONDS\',
                                        \'HrdBufferInitialFillPercentage\': 123,
                                        \'HrdBufferSize\': 123,
                                        \'InterlaceMode\': \'PROGRESSIVE\'|\'TOP_FIELD\'|\'BOTTOM_FIELD\'|\'FOLLOW_TOP_FIELD\'|\'FOLLOW_BOTTOM_FIELD\',
                                        \'MaxBitrate\': 123,
                                        \'MinIInterval\': 123,
                                        \'NumberBFramesBetweenReferenceFrames\': 123,
                                        \'NumberReferenceFrames\': 123,
                                        \'ParControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                        \'ParDenominator\': 123,
                                        \'ParNumerator\': 123,
                                        \'QualityTuningLevel\': \'SINGLE_PASS\'|\'SINGLE_PASS_HQ\'|\'MULTI_PASS_HQ\',
                                        \'QvbrSettings\': {
                                            \'MaxAverageBitrate\': 123,
                                            \'QvbrQualityLevel\': 123
                                        },
                                        \'RateControlMode\': \'VBR\'|\'CBR\'|\'QVBR\',
                                        \'SampleAdaptiveOffsetFilterMode\': \'DEFAULT\'|\'ADAPTIVE\'|\'OFF\',
                                        \'SceneChangeDetect\': \'DISABLED\'|\'ENABLED\',
                                        \'Slices\': 123,
                                        \'SlowPal\': \'DISABLED\'|\'ENABLED\',
                                        \'SpatialAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\',
                                        \'Telecine\': \'NONE\'|\'SOFT\'|\'HARD\',
                                        \'TemporalAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\',
                                        \'TemporalIds\': \'DISABLED\'|\'ENABLED\',
                                        \'Tiles\': \'DISABLED\'|\'ENABLED\',
                                        \'UnregisteredSeiTimecode\': \'DISABLED\'|\'ENABLED\',
                                        \'WriteMp4PackagingType\': \'HVC1\'|\'HEV1\'
                                    },
                                    \'Mpeg2Settings\': {
                                        \'AdaptiveQuantization\': \'OFF\'|\'LOW\'|\'MEDIUM\'|\'HIGH\',
                                        \'Bitrate\': 123,
                                        \'CodecLevel\': \'AUTO\'|\'LOW\'|\'MAIN\'|\'HIGH1440\'|\'HIGH\',
                                        \'CodecProfile\': \'MAIN\'|\'PROFILE_422\',
                                        \'DynamicSubGop\': \'ADAPTIVE\'|\'STATIC\',
                                        \'FramerateControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                        \'FramerateConversionAlgorithm\': \'DUPLICATE_DROP\'|\'INTERPOLATE\',
                                        \'FramerateDenominator\': 123,
                                        \'FramerateNumerator\': 123,
                                        \'GopClosedCadence\': 123,
                                        \'GopSize\': 123.0,
                                        \'GopSizeUnits\': \'FRAMES\'|\'SECONDS\',
                                        \'HrdBufferInitialFillPercentage\': 123,
                                        \'HrdBufferSize\': 123,
                                        \'InterlaceMode\': \'PROGRESSIVE\'|\'TOP_FIELD\'|\'BOTTOM_FIELD\'|\'FOLLOW_TOP_FIELD\'|\'FOLLOW_BOTTOM_FIELD\',
                                        \'IntraDcPrecision\': \'AUTO\'|\'INTRA_DC_PRECISION_8\'|\'INTRA_DC_PRECISION_9\'|\'INTRA_DC_PRECISION_10\'|\'INTRA_DC_PRECISION_11\',
                                        \'MaxBitrate\': 123,
                                        \'MinIInterval\': 123,
                                        \'NumberBFramesBetweenReferenceFrames\': 123,
                                        \'ParControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                        \'ParDenominator\': 123,
                                        \'ParNumerator\': 123,
                                        \'QualityTuningLevel\': \'SINGLE_PASS\'|\'MULTI_PASS\',
                                        \'RateControlMode\': \'VBR\'|\'CBR\',
                                        \'SceneChangeDetect\': \'DISABLED\'|\'ENABLED\',
                                        \'SlowPal\': \'DISABLED\'|\'ENABLED\',
                                        \'Softness\': 123,
                                        \'SpatialAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\',
                                        \'Syntax\': \'DEFAULT\'|\'D_10\',
                                        \'Telecine\': \'NONE\'|\'SOFT\'|\'HARD\',
                                        \'TemporalAdaptiveQuantization\': \'DISABLED\'|\'ENABLED\'
                                    },
                                    \'ProresSettings\': {
                                        \'CodecProfile\': \'APPLE_PRORES_422\'|\'APPLE_PRORES_422_HQ\'|\'APPLE_PRORES_422_LT\'|\'APPLE_PRORES_422_PROXY\',
                                        \'FramerateControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                        \'FramerateConversionAlgorithm\': \'DUPLICATE_DROP\'|\'INTERPOLATE\',
                                        \'FramerateDenominator\': 123,
                                        \'FramerateNumerator\': 123,
                                        \'InterlaceMode\': \'PROGRESSIVE\'|\'TOP_FIELD\'|\'BOTTOM_FIELD\'|\'FOLLOW_TOP_FIELD\'|\'FOLLOW_BOTTOM_FIELD\',
                                        \'ParControl\': \'INITIALIZE_FROM_SOURCE\'|\'SPECIFIED\',
                                        \'ParDenominator\': 123,
                                        \'ParNumerator\': 123,
                                        \'SlowPal\': \'DISABLED\'|\'ENABLED\',
                                        \'Telecine\': \'NONE\'|\'HARD\'
                                    }
                                },
                                \'ColorMetadata\': \'IGNORE\'|\'INSERT\',
                                \'Crop\': {
                                    \'Height\': 123,
                                    \'Width\': 123,
                                    \'X\': 123,
                                    \'Y\': 123
                                },
                                \'DropFrameTimecode\': \'DISABLED\'|\'ENABLED\',
                                \'FixedAfd\': 123,
                                \'Height\': 123,
                                \'Position\': {
                                    \'Height\': 123,
                                    \'Width\': 123,
                                    \'X\': 123,
                                    \'Y\': 123
                                },
                                \'RespondToAfd\': \'NONE\'|\'RESPOND\'|\'PASSTHROUGH\',
                                \'ScalingBehavior\': \'DEFAULT\'|\'STRETCH_TO_OUTPUT\',
                                \'Sharpness\': 123,
                                \'TimecodeInsertion\': \'DISABLED\'|\'PIC_TIMING_SEI\',
                                \'VideoPreprocessors\': {
                                    \'ColorCorrector\': {
                                        \'Brightness\': 123,
                                        \'ColorSpaceConversion\': \'NONE\'|\'FORCE_601\'|\'FORCE_709\'|\'FORCE_HDR10\'|\'FORCE_HLG_2020\',
                                        \'Contrast\': 123,
                                        \'Hdr10Metadata\': {
                                            \'BluePrimaryX\': 123,
                                            \'BluePrimaryY\': 123,
                                            \'GreenPrimaryX\': 123,
                                            \'GreenPrimaryY\': 123,
                                            \'MaxContentLightLevel\': 123,
                                            \'MaxFrameAverageLightLevel\': 123,
                                            \'MaxLuminance\': 123,
                                            \'MinLuminance\': 123,
                                            \'RedPrimaryX\': 123,
                                            \'RedPrimaryY\': 123,
                                            \'WhitePointX\': 123,
                                            \'WhitePointY\': 123
                                        },
                                        \'Hue\': 123,
                                        \'Saturation\': 123
                                    },
                                    \'Deinterlacer\': {
                                        \'Algorithm\': \'INTERPOLATE\'|\'INTERPOLATE_TICKER\'|\'BLEND\'|\'BLEND_TICKER\',
                                        \'Control\': \'FORCE_ALL_FRAMES\'|\'NORMAL\',
                                        \'Mode\': \'DEINTERLACE\'|\'INVERSE_TELECINE\'|\'ADAPTIVE\'
                                    },
                                    \'ImageInserter\': {
                                        \'InsertableImages\': [
                                            {
                                                \'Duration\': 123,
                                                \'FadeIn\': 123,
                                                \'FadeOut\': 123,
                                                \'Height\': 123,
                                                \'ImageInserterInput\': \'string\',
                                                \'ImageX\': 123,
                                                \'ImageY\': 123,
                                                \'Layer\': 123,
                                                \'Opacity\': 123,
                                                \'StartTime\': \'string\',
                                                \'Width\': 123
                                            },
                                        ]
                                    },
                                    \'NoiseReducer\': {
                                        \'Filter\': \'BILATERAL\'|\'MEAN\'|\'GAUSSIAN\'|\'LANCZOS\'|\'SHARPEN\'|\'CONSERVE\'|\'SPATIAL\',
                                        \'FilterSettings\': {
                                            \'Strength\': 123
                                        },
                                        \'SpatialFilterSettings\': {
                                            \'PostFilterSharpenStrength\': 123,
                                            \'Speed\': 123,
                                            \'Strength\': 123
                                        }
                                    },
                                    \'TimecodeBurnin\': {
                                        \'FontSize\': 123,
                                        \'Position\': \'TOP_CENTER\'|\'TOP_LEFT\'|\'TOP_RIGHT\'|\'MIDDLE_LEFT\'|\'MIDDLE_CENTER\'|\'MIDDLE_RIGHT\'|\'BOTTOM_LEFT\'|\'BOTTOM_CENTER\'|\'BOTTOM_RIGHT\',
                                        \'Prefix\': \'string\'
                                    }
                                },
                                \'Width\': 123
                            }
                        },
                        \'Type\': \'SYSTEM\'|\'CUSTOM\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Presets** *(list) --* List of presets
              
              - *(dict) --* A preset is a collection of preconfigured media conversion settings that you want MediaConvert to apply to the output during the conversion process.
                
                - **Arn** *(string) --* An identifier for this resource that is unique within all of AWS.
                
                - **Category** *(string) --* An optional category you create to organize your presets.
                
                - **CreatedAt** *(datetime) --* The timestamp in epoch seconds for preset creation.
                
                - **Description** *(string) --* An optional description you create for each preset.
                
                - **LastUpdated** *(datetime) --* The timestamp in epoch seconds when the preset was last updated.
                
                - **Name** *(string) --* A name you create for each preset. Each name must be unique within your account.
                
                - **Settings** *(dict) --* Settings for preset
                  
                  - **AudioDescriptions** *(list) --* (AudioDescriptions) contains groups of audio encoding settings organized by audio codec. Include one instance of (AudioDescriptions) per output. (AudioDescriptions) can contain multiple groups of encoding settings.
                    
                    - *(dict) --* Description of audio output
                      
                      - **AudioNormalizationSettings** *(dict) --* Advanced audio normalization settings.
                        
                        - **Algorithm** *(string) --* Audio normalization algorithm to use. 1770-1 conforms to the CALM Act specification, 1770-2 conforms to the EBU R-128 specification.
                        
                        - **AlgorithmControl** *(string) --* When enabled the output audio is corrected using the chosen algorithm. If disabled, the audio will be measured but not adjusted.
                        
                        - **CorrectionGateLevel** *(integer) --* Content measuring above this level will be corrected to the target level. Content measuring below this level will not be corrected. Gating only applies when not using real_time_correction.
                        
                        - **LoudnessLogging** *(string) --* If set to LOG, log each output\'s audio track loudness to a CSV file.
                        
                        - **PeakCalculation** *(string) --* If set to TRUE_PEAK, calculate and log the TruePeak for each output\'s audio track loudness.
                        
                        - **TargetLkfs** *(float) --* Target LKFS(loudness) to adjust volume to. If no value is entered, a default value will be used according to the chosen algorithm. The CALM Act (1770-1) recommends a target of -24 LKFS. The EBU R-128 specification (1770-2) recommends a target of -23 LKFS.
                    
                      - **AudioSourceName** *(string) --* Specifies which audio data to use from each input. In the simplest case, specify an \"Audio Selector\":#inputs-audio_selector by name based on its order within each input. For example if you specify \"Audio Selector 3\", then the third audio selector will be used from each input. If an input does not have an \"Audio Selector 3\", then the audio selector marked as \"default\" in that input will be used. If there is no audio selector marked as \"default\", silence will be inserted for the duration of that input. Alternatively, an \"Audio Selector Group\":#inputs-audio_selector_group name may be specified, with similar default/silence behavior. If no audio_source_name is specified, then \"Audio Selector 1\" will be chosen automatically.
                      
                      - **AudioType** *(integer) --* Applies only if Follow Input Audio Type is unchecked (false). A number between 0 and 255. The following are defined in ISO-IEC 13818-1: 0 = Undefined, 1 = Clean Effects, 2 = Hearing Impaired, 3 = Visually Impaired Commentary, 4-255 = Reserved.
                      
                      - **AudioTypeControl** *(string) --* When set to FOLLOW_INPUT, if the input contains an ISO 639 audio_type, then that value is passed through to the output. If the input contains no ISO 639 audio_type, the value in Audio Type is included in the output. Otherwise the value in Audio Type is included in the output. Note that this field and audioType are both ignored if audioDescriptionBroadcasterMix is set to BROADCASTER_MIXED_AD.
                      
                      - **CodecSettings** *(dict) --* Audio codec settings (CodecSettings) under (AudioDescriptions) contains the group of settings related to audio encoding. The settings in this group vary depending on the value you choose for Audio codec (Codec). For each codec enum you choose, define the corresponding settings object. The following lists the codec enum, settings object pairs. * AAC, AacSettings * MP2, Mp2Settings * WAV, WavSettings * AIFF, AiffSettings * AC3, Ac3Settings * EAC3, Eac3Settings
                        
                        - **AacSettings** *(dict) --* Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the value AAC. The service accepts one of two mutually exclusive groups of AAC settings--VBR and CBR. To select one of these modes, set the value of Bitrate control mode (rateControlMode) to \"VBR\" or \"CBR\". In VBR mode, you control the audio quality with the setting VBR quality (vbrQuality). In CBR mode, you use the setting Bitrate (bitrate). Defaults and valid values depend on the rate control mode.
                          
                          - **AudioDescriptionBroadcasterMix** *(string) --* Choose BROADCASTER_MIXED_AD when the input contains pre-mixed main audio + audio description (AD) as a stereo pair. The value for AudioType will be set to 3, which signals to downstream systems that this stream contains \"broadcaster mixed AD\". Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. When you choose BROADCASTER_MIXED_AD, the encoder ignores any values you provide in AudioType and FollowInputAudioType. Choose NORMAL when the input does not contain pre-mixed audio + audio description (AD). In this case, the encoder will use any values you provide for AudioType and FollowInputAudioType.
                          
                          - **Bitrate** *(integer) --* Average bitrate in bits/second. Defaults and valid values depend on rate control mode and profile.
                          
                          - **CodecProfile** *(string) --* AAC Profile.
                          
                          - **CodingMode** *(string) --* Mono (Audio Description), Mono, Stereo, or 5.1 channel layout. Valid values depend on rate control mode and profile. \"1.0 - Audio Description (Receiver Mix)\" setting receives a stereo description plus control track and emits a mono AAC encode of the description track, with control data emitted in the PES header as per ETSI TS 101 154 Annex E.
                          
                          - **RateControlMode** *(string) --* Rate Control Mode.
                          
                          - **RawFormat** *(string) --* Enables LATM/LOAS AAC output. Note that if you use LATM/LOAS AAC in an output, you must choose \"No container\" for the output container.
                          
                          - **SampleRate** *(integer) --* Sample rate in Hz. Valid values depend on rate control mode and profile.
                          
                          - **Specification** *(string) --* Use MPEG-2 AAC instead of MPEG-4 AAC audio for raw or MPEG-2 Transport Stream containers.
                          
                          - **VbrQuality** *(string) --* VBR Quality Level - Only used if rate_control_mode is VBR.
                      
                        - **Ac3Settings** *(dict) --* Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the value AC3.
                          
                          - **Bitrate** *(integer) --* Average bitrate in bits/second. Valid bitrates depend on the coding mode.
                          
                          - **BitstreamMode** *(string) --* Specifies the \"Bitstream Mode\" (bsmod) for the emitted AC-3 stream. See ATSC A/52-2012 for background on these values.
                          
                          - **CodingMode** *(string) --* Dolby Digital coding mode. Determines number of channels.
                          
                          - **Dialnorm** *(integer) --* Sets the dialnorm for the output. If blank and input audio is Dolby Digital, dialnorm will be passed through.
                          
                          - **DynamicRangeCompressionProfile** *(string) --* If set to FILM_STANDARD, adds dynamic range compression signaling to the output bitstream as defined in the Dolby Digital specification.
                          
                          - **LfeFilter** *(string) --* Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3_2_LFE coding mode.
                          
                          - **MetadataControl** *(string) --* When set to FOLLOW_INPUT, encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.
                          
                          - **SampleRate** *(integer) --* Sample rate in hz. Sample rate is always 48000.
                      
                        - **AiffSettings** *(dict) --* Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the value AIFF.
                          
                          - **BitDepth** *(integer) --* Specify Bit depth (BitDepth), in bits per sample, to choose the encoding quality for this audio track.
                          
                          - **Channels** *(integer) --* Set Channels to specify the number of channels in this output audio track. Choosing Mono in the console will give you 1 output channel; choosing Stereo will give you 2. In the API, valid values are 1 and 2.
                          
                          - **SampleRate** *(integer) --* Sample rate in hz.
                      
                        - **Codec** *(string) --* Type of Audio codec.
                        
                        - **Eac3Settings** *(dict) --* Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the value EAC3.
                          
                          - **AttenuationControl** *(string) --* If set to ATTENUATE_3_DB, applies a 3 dB attenuation to the surround channels. Only used for 3/2 coding mode.
                          
                          - **Bitrate** *(integer) --* Average bitrate in bits/second. Valid bitrates depend on the coding mode.
                          
                          - **BitstreamMode** *(string) --* Specifies the \"Bitstream Mode\" (bsmod) for the emitted E-AC-3 stream. See ATSC A/52-2012 (Annex E) for background on these values.
                          
                          - **CodingMode** *(string) --* Dolby Digital Plus coding mode. Determines number of channels.
                          
                          - **DcFilter** *(string) --* Activates a DC highpass filter for all input channels.
                          
                          - **Dialnorm** *(integer) --* Sets the dialnorm for the output. If blank and input audio is Dolby Digital Plus, dialnorm will be passed through.
                          
                          - **DynamicRangeCompressionLine** *(string) --* Enables Dynamic Range Compression that restricts the absolute peak level for a signal.
                          
                          - **DynamicRangeCompressionRf** *(string) --* Enables Heavy Dynamic Range Compression, ensures that the instantaneous signal peaks do not exceed specified levels.
                          
                          - **LfeControl** *(string) --* When encoding 3/2 audio, controls whether the LFE channel is enabled
                          
                          - **LfeFilter** *(string) --* Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with 3_2_LFE coding mode.
                          
                          - **LoRoCenterMixLevel** *(float) --* Left only/Right only center mix level. Only used for 3/2 coding mode. Valid values: 3.0, 1.5, 0.0, -1.5 -3.0 -4.5 -6.0 -60
                          
                          - **LoRoSurroundMixLevel** *(float) --* Left only/Right only surround mix level. Only used for 3/2 coding mode. Valid values: -1.5 -3.0 -4.5 -6.0 -60
                          
                          - **LtRtCenterMixLevel** *(float) --* Left total/Right total center mix level. Only used for 3/2 coding mode. Valid values: 3.0, 1.5, 0.0, -1.5 -3.0 -4.5 -6.0 -60
                          
                          - **LtRtSurroundMixLevel** *(float) --* Left total/Right total surround mix level. Only used for 3/2 coding mode. Valid values: -1.5 -3.0 -4.5 -6.0 -60
                          
                          - **MetadataControl** *(string) --* When set to FOLLOW_INPUT, encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.
                          
                          - **PassthroughControl** *(string) --* When set to WHEN_POSSIBLE, input DD+ audio will be passed through if it is present on the input. this detection is dynamic over the life of the transcode. Inputs that alternate between DD+ and non-DD+ content will have a consistent DD+ output as the system alternates between passthrough and encoding.
                          
                          - **PhaseControl** *(string) --* Controls the amount of phase-shift applied to the surround channels. Only used for 3/2 coding mode.
                          
                          - **SampleRate** *(integer) --* Sample rate in hz. Sample rate is always 48000.
                          
                          - **StereoDownmix** *(string) --* Stereo downmix preference. Only used for 3/2 coding mode.
                          
                          - **SurroundExMode** *(string) --* When encoding 3/2 audio, sets whether an extra center back surround channel is matrix encoded into the left and right surround channels.
                          
                          - **SurroundMode** *(string) --* When encoding 2/0 audio, sets whether Dolby Surround is matrix encoded into the two channels.
                      
                        - **Mp2Settings** *(dict) --* Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the value MP2.
                          
                          - **Bitrate** *(integer) --* Average bitrate in bits/second.
                          
                          - **Channels** *(integer) --* Set Channels to specify the number of channels in this output audio track. Choosing Mono in the console will give you 1 output channel; choosing Stereo will give you 2. In the API, valid values are 1 and 2.
                          
                          - **SampleRate** *(integer) --* Sample rate in hz.
                      
                        - **WavSettings** *(dict) --* Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the value WAV.
                          
                          - **BitDepth** *(integer) --* Specify Bit depth (BitDepth), in bits per sample, to choose the encoding quality for this audio track.
                          
                          - **Channels** *(integer) --* Set Channels to specify the number of channels in this output audio track. With WAV, valid values 1, 2, 4, and 8. In the console, these values are Mono, Stereo, 4-Channel, and 8-Channel, respectively.
                          
                          - **Format** *(string) --* The service defaults to using RIFF for WAV outputs. If your output audio is likely to exceed 4 GB in file size, or if you otherwise need the extended support of the RF64 format, set your output WAV file format to RF64.
                          
                          - **SampleRate** *(integer) --* Sample rate in Hz.
                      
                      - **CustomLanguageCode** *(string) --* Specify the language for this audio output track, using the ISO 639-2 or ISO 639-3 three-letter language code. The language specified will be used when \'Follow Input Language Code\' is not selected or when \'Follow Input Language Code\' is selected but there is no ISO 639 language code specified by the input.
                      
                      - **LanguageCode** *(string) --* Indicates the language of the audio output track. The ISO 639 language specified in the \'Language Code\' drop down will be used when \'Follow Input Language Code\' is not selected or when \'Follow Input Language Code\' is selected but there is no ISO 639 language code specified by the input.
                      
                      - **LanguageCodeControl** *(string) --* Choosing FOLLOW_INPUT will cause the ISO 639 language code of the output to follow the ISO 639 language code of the input. The language specified for languageCode\' will be used when USE_CONFIGURED is selected or when FOLLOW_INPUT is selected but there is no ISO 639 language code specified by the input.
                      
                      - **RemixSettings** *(dict) --* Advanced audio remixing settings.
                        
                        - **ChannelMapping** *(dict) --* Channel mapping (ChannelMapping) contains the group of fields that hold the remixing value for each channel. Units are in dB. Acceptable values are within the range from -60 (mute) through 6. A setting of 0 passes the input channel unchanged to the output channel (no attenuation or amplification).
                          
                          - **OutputChannels** *(list) --* List of output channels
                            
                            - *(dict) --* OutputChannel mapping settings.
                              
                              - **InputChannels** *(list) --* List of input channels
                                
                                - *(integer) --* 
                            
                        - **ChannelsIn** *(integer) --* Specify the number of audio channels from your input that you want to use in your output. With remixing, you might combine or split the data in these channels, so the number of channels in your final output might be different.
                        
                        - **ChannelsOut** *(integer) --* Specify the number of channels in this output after remixing. Valid values: 1, 2, 4, 6, 8
                    
                      - **StreamName** *(string) --* Used for MS Smooth and Apple HLS outputs. Indicates the name displayed by the player (eg. English, or Director Commentary). Alphanumeric characters, spaces, and underscore are legal.
                  
                  - **CaptionDescriptions** *(list) --* Caption settings for this preset. There can be multiple caption settings in a single output.
                    
                    - *(dict) --* Caption Description for preset
                      
                      - **CustomLanguageCode** *(string) --* Indicates the language of the caption output track, using the ISO 639-2 or ISO 639-3 three-letter language code
                      
                      - **DestinationSettings** *(dict) --* Specific settings required by destination type. Note that burnin_destination_settings are not available if the source of the caption data is Embedded or Teletext.
                        
                        - **BurninDestinationSettings** *(dict) --* Burn-In Destination Settings.
                          
                          - **Alignment** *(string) --* If no explicit x_position or y_position is provided, setting alignment to centered will place the captions at the bottom center of the output. Similarly, setting a left alignment will align captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                          
                          - **BackgroundColor** *(string) --* Specifies the color of the rectangle behind the captions. All burn-in and DVB-Sub font settings must match.
                          
                          - **BackgroundOpacity** *(integer) --* Specifies the opacity of the background rectangle. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
                          
                          - **FontColor** *(string) --* Specifies the color of the burned-in captions. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                          
                          - **FontOpacity** *(integer) --* Specifies the opacity of the burned-in captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font settings must match.
                          
                          - **FontResolution** *(integer) --* Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and DVB-Sub font settings must match.
                          
                          - **FontSize** *(integer) --* A positive integer indicates the exact font size in points. Set to 0 for automatic font size selection. All burn-in and DVB-Sub font settings must match.
                          
                          - **OutlineColor** *(string) --* Specifies font outline color. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                          
                          - **OutlineSize** *(integer) --* Specifies font outline size in pixels. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                          
                          - **ShadowColor** *(string) --* Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub font settings must match.
                          
                          - **ShadowOpacity** *(integer) --* Specifies the opacity of the shadow. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
                          
                          - **ShadowXOffset** *(integer) --* Specifies the horizontal offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings must match.
                          
                          - **ShadowYOffset** *(integer) --* Specifies the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. All burn-in and DVB-Sub font settings must match.
                          
                          - **TeletextSpacing** *(string) --* Only applies to jobs with input captions in Teletext or STL formats. Specify whether the spacing between letters in your captions is set by the captions grid or varies depending on letter width. Choose fixed grid to conform to the spacing specified in the captions file more accurately. Choose proportional to make the text easier to read if the captions are closed caption.
                          
                          - **XPosition** *(integer) --* Specifies the horizontal position of the caption relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit x_position is provided, the horizontal caption position will be determined by the alignment parameter. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                          
                          - **YPosition** *(integer) --* Specifies the vertical position of the caption relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit y_position is provided, the caption will be positioned towards the bottom of the output. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                      
                        - **DestinationType** *(string) --* Type of Caption output, including Burn-In, Embedded, SCC, SRT, TTML, WebVTT, DVB-Sub, Teletext.
                        
                        - **DvbSubDestinationSettings** *(dict) --* DVB-Sub Destination Settings
                          
                          - **Alignment** *(string) --* If no explicit x_position or y_position is provided, setting alignment to centered will place the captions at the bottom center of the output. Similarly, setting a left alignment will align captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                          
                          - **BackgroundColor** *(string) --* Specifies the color of the rectangle behind the captions. All burn-in and DVB-Sub font settings must match.
                          
                          - **BackgroundOpacity** *(integer) --* Specifies the opacity of the background rectangle. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
                          
                          - **FontColor** *(string) --* Specifies the color of the burned-in captions. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                          
                          - **FontOpacity** *(integer) --* Specifies the opacity of the burned-in captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font settings must match.
                          
                          - **FontResolution** *(integer) --* Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and DVB-Sub font settings must match.
                          
                          - **FontSize** *(integer) --* A positive integer indicates the exact font size in points. Set to 0 for automatic font size selection. All burn-in and DVB-Sub font settings must match.
                          
                          - **OutlineColor** *(string) --* Specifies font outline color. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                          
                          - **OutlineSize** *(integer) --* Specifies font outline size in pixels. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                          
                          - **ShadowColor** *(string) --* Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub font settings must match.
                          
                          - **ShadowOpacity** *(integer) --* Specifies the opacity of the shadow. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
                          
                          - **ShadowXOffset** *(integer) --* Specifies the horizontal offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings must match.
                          
                          - **ShadowYOffset** *(integer) --* Specifies the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. All burn-in and DVB-Sub font settings must match.
                          
                          - **TeletextSpacing** *(string) --* Only applies to jobs with input captions in Teletext or STL formats. Specify whether the spacing between letters in your captions is set by the captions grid or varies depending on letter width. Choose fixed grid to conform to the spacing specified in the captions file more accurately. Choose proportional to make the text easier to read if the captions are closed caption.
                          
                          - **XPosition** *(integer) --* Specifies the horizontal position of the caption relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit x_position is provided, the horizontal caption position will be determined by the alignment parameter. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                          
                          - **YPosition** *(integer) --* Specifies the vertical position of the caption relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit y_position is provided, the caption will be positioned towards the bottom of the output. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
                      
                        - **SccDestinationSettings** *(dict) --* Settings for SCC caption output.
                          
                          - **Framerate** *(string) --* Set Framerate (SccDestinationFramerate) to make sure that the captions and the video are synchronized in the output. Specify a framerate that matches the framerate of the associated video. If the video framerate is 29.97, choose 29.97 dropframe (FRAMERATE_29_97_DROPFRAME) only if the video has video_insertion=true and drop_frame_timecode=true; otherwise, choose 29.97 non-dropframe (FRAMERATE_29_97_NON_DROPFRAME).
                      
                        - **TeletextDestinationSettings** *(dict) --* Settings for Teletext caption output
                          
                          - **PageNumber** *(string) --* Set pageNumber to the Teletext page number for the destination captions for this output. This value must be a three-digit hexadecimal string; strings ending in -FF are invalid. If you are passing through the entire set of Teletext data, do not use this field.
                      
                        - **TtmlDestinationSettings** *(dict) --* Settings specific to TTML caption outputs, including Pass style information (TtmlStylePassthrough).
                          
                          - **StylePassthrough** *(string) --* Pass through style and position information from a TTML-like input source (TTML, SMPTE-TT, CFF-TT) to the CFF-TT output or TTML output.
                      
                      - **LanguageCode** *(string) --* Indicates the language of the caption output track.
                      
                      - **LanguageDescription** *(string) --* Human readable information to indicate captions available for players (eg. English, or Spanish). Alphanumeric characters, spaces, and underscore are legal.
                  
                  - **ContainerSettings** *(dict) --* Container specific settings.
                    
                    - **Container** *(string) --* Container for this output. Some containers require a container settings object. If not specified, the default object will be created.
                    
                    - **F4vSettings** *(dict) --* Settings for F4v container
                      
                      - **MoovPlacement** *(string) --* If set to PROGRESSIVE_DOWNLOAD, the MOOV atom is relocated to the beginning of the archive as required for progressive downloading. Otherwise it is placed normally at the end.
                  
                    - **M2tsSettings** *(dict) --* Settings for M2TS Container.
                      
                      - **AudioBufferModel** *(string) --* Selects between the DVB and ATSC buffer models for Dolby Digital audio.
                      
                      - **AudioFramesPerPes** *(integer) --* The number of audio frames to insert for each PES packet.
                      
                      - **AudioPids** *(list) --* Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation.
                        
                        - *(integer) --* 
                    
                      - **Bitrate** *(integer) --* The output bitrate of the transport stream in bits per second. Setting to 0 lets the muxer automatically determine the appropriate bitrate. Other common values are 3750000, 7500000, and 15000000.
                      
                      - **BufferModel** *(string) --* Controls what buffer model to use for accurate interleaving. If set to MULTIPLEX, use multiplex buffer model. If set to NONE, this can lead to lower latency, but low-memory devices may not be able to play back the stream without interruptions.
                      
                      - **DvbNitSettings** *(dict) --* Inserts DVB Network Information Table (NIT) at the specified table repetition interval.
                        
                        - **NetworkId** *(integer) --* The numeric value placed in the Network Information Table (NIT).
                        
                        - **NetworkName** *(string) --* The network name text placed in the network_name_descriptor inside the Network Information Table. Maximum length is 256 characters.
                        
                        - **NitInterval** *(integer) --* The number of milliseconds between instances of this table in the output transport stream.
                    
                      - **DvbSdtSettings** *(dict) --* Inserts DVB Service Description Table (NIT) at the specified table repetition interval.
                        
                        - **OutputSdt** *(string) --* Selects method of inserting SDT information into output stream. \"Follow input SDT\" copies SDT information from input stream to output stream. \"Follow input SDT if present\" copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. Enter \"SDT Manually\" means user will enter the SDT information. \"No SDT\" means output stream will not contain SDT information.
                        
                        - **SdtInterval** *(integer) --* The number of milliseconds between instances of this table in the output transport stream.
                        
                        - **ServiceName** *(string) --* The service name placed in the service_descriptor in the Service Description Table. Maximum length is 256 characters.
                        
                        - **ServiceProviderName** *(string) --* The service provider name placed in the service_descriptor in the Service Description Table. Maximum length is 256 characters.
                    
                      - **DvbSubPids** *(list) --* Packet Identifier (PID) for input source DVB Subtitle data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation.
                        
                        - *(integer) --* 
                    
                      - **DvbTdtSettings** *(dict) --* Inserts DVB Time and Date Table (TDT) at the specified table repetition interval.
                        
                        - **TdtInterval** *(integer) --* The number of milliseconds between instances of this table in the output transport stream.
                    
                      - **DvbTeletextPid** *(integer) --* Packet Identifier (PID) for input source DVB Teletext data to this output.
                      
                      - **EbpAudioInterval** *(string) --* When set to VIDEO_AND_FIXED_INTERVALS, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. When set to VIDEO_INTERVAL, these additional markers will not be inserted. Only applicable when EBP segmentation markers are is selected (segmentationMarkers is EBP or EBP_LEGACY).
                      
                      - **EbpPlacement** *(string) --* Selects which PIDs to place EBP markers on. They can either be placed only on the video PID, or on both the video PID and all audio PIDs. Only applicable when EBP segmentation markers are is selected (segmentationMarkers is EBP or EBP_LEGACY).
                      
                      - **EsRateInPes** *(string) --* Controls whether to include the ES Rate field in the PES header.
                      
                      - **FragmentTime** *(float) --* The length in seconds of each fragment. Only used with EBP markers.
                      
                      - **MaxPcrInterval** *(integer) --* Maximum time in milliseconds between Program Clock References (PCRs) inserted into the transport stream.
                      
                      - **MinEbpInterval** *(integer) --* When set, enforces that Encoder Boundary Points do not come within the specified time interval of each other by looking ahead at input video. If another EBP is going to come in within the specified time interval, the current EBP is not emitted, and the segment is \"stretched\" to the next marker. The lookahead value does not add latency to the system. The Live Event must be configured elsewhere to create sufficient latency to make the lookahead accurate.
                      
                      - **NielsenId3** *(string) --* If INSERT, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.
                      
                      - **NullPacketBitrate** *(float) --* Value in bits per second of extra null packets to insert into the transport stream. This can be used if a downstream encryption system requires periodic null packets.
                      
                      - **PatInterval** *(integer) --* The number of milliseconds between instances of this table in the output transport stream.
                      
                      - **PcrControl** *(string) --* When set to PCR_EVERY_PES_PACKET, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This is effective only when the PCR PID is the same as the video or audio elementary stream.
                      
                      - **PcrPid** *(integer) --* Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID.
                      
                      - **PmtInterval** *(integer) --* The number of milliseconds between instances of this table in the output transport stream.
                      
                      - **PmtPid** *(integer) --* Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream.
                      
                      - **PrivateMetadataPid** *(integer) --* Packet Identifier (PID) of the private metadata stream in the transport stream.
                      
                      - **ProgramNumber** *(integer) --* The value of the program number field in the Program Map Table.
                      
                      - **RateMode** *(string) --* When set to CBR, inserts null packets into transport stream to fill specified bitrate. When set to VBR, the bitrate setting acts as the maximum bitrate, but the output will not be padded up to that bitrate.
                      
                      - **Scte35Pid** *(integer) --* Packet Identifier (PID) of the SCTE-35 stream in the transport stream.
                      
                      - **Scte35Source** *(string) --* Enables SCTE-35 passthrough (scte35Source) to pass any SCTE-35 signals from input to output.
                      
                      - **SegmentationMarkers** *(string) --* Inserts segmentation markers at each segmentation_time period. rai_segstart sets the Random Access Indicator bit in the adaptation field. rai_adapt sets the RAI bit and adds the current timecode in the private data bytes. psi_segstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebp_legacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format.
                      
                      - **SegmentationStyle** *(string) --* The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of \"reset_cadence\" is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of of $segmentation_time seconds. When a segmentation style of \"maintain_cadence\" is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentation_time seconds. Note that EBP lookahead is a slight exception to this rule.
                      
                      - **SegmentationTime** *(float) --* The length in seconds of each segment. Required unless markers is set to _none_.
                      
                      - **TimedMetadataPid** *(integer) --* Packet Identifier (PID) of the timed metadata stream in the transport stream.
                      
                      - **TransportStreamId** *(integer) --* The value of the transport stream ID field in the Program Map Table.
                      
                      - **VideoPid** *(integer) --* Packet Identifier (PID) of the elementary video stream in the transport stream.
                  
                    - **M3u8Settings** *(dict) --* Settings for TS segments in HLS
                      
                      - **AudioFramesPerPes** *(integer) --* The number of audio frames to insert for each PES packet.
                      
                      - **AudioPids** *(list) --* Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation.
                        
                        - *(integer) --* 
                    
                      - **NielsenId3** *(string) --* If INSERT, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.
                      
                      - **PatInterval** *(integer) --* The number of milliseconds between instances of this table in the output transport stream.
                      
                      - **PcrControl** *(string) --* When set to PCR_EVERY_PES_PACKET a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.
                      
                      - **PcrPid** *(integer) --* Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID.
                      
                      - **PmtInterval** *(integer) --* The number of milliseconds between instances of this table in the output transport stream.
                      
                      - **PmtPid** *(integer) --* Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream.
                      
                      - **PrivateMetadataPid** *(integer) --* Packet Identifier (PID) of the private metadata stream in the transport stream.
                      
                      - **ProgramNumber** *(integer) --* The value of the program number field in the Program Map Table.
                      
                      - **Scte35Pid** *(integer) --* Packet Identifier (PID) of the SCTE-35 stream in the transport stream.
                      
                      - **Scte35Source** *(string) --* Enables SCTE-35 passthrough (scte35Source) to pass any SCTE-35 signals from input to output.
                      
                      - **TimedMetadata** *(string) --* Applies only to HLS outputs. Use this setting to specify whether the service inserts the ID3 timed metadata from the input in this output.
                      
                      - **TimedMetadataPid** *(integer) --* Packet Identifier (PID) of the timed metadata stream in the transport stream.
                      
                      - **TransportStreamId** *(integer) --* The value of the transport stream ID field in the Program Map Table.
                      
                      - **VideoPid** *(integer) --* Packet Identifier (PID) of the elementary video stream in the transport stream.
                  
                    - **MovSettings** *(dict) --* Settings for MOV Container.
                      
                      - **ClapAtom** *(string) --* When enabled, include \'clap\' atom if appropriate for the video output settings.
                      
                      - **CslgAtom** *(string) --* When enabled, file composition times will start at zero, composition times in the \'ctts\' (composition time to sample) box for B-frames will be negative, and a \'cslg\' (composition shift least greatest) box will be included per 14496-1 amendment 1. This improves compatibility with Apple players and tools.
                      
                      - **Mpeg2FourCCControl** *(string) --* When set to XDCAM, writes MPEG2 video streams into the QuickTime file using XDCAM fourcc codes. This increases compatibility with Apple editors and players, but may decrease compatibility with other players. Only applicable when the video codec is MPEG2.
                      
                      - **PaddingControl** *(string) --* If set to OMNEON, inserts Omneon-compatible padding
                      
                      - **Reference** *(string) --* A value of \'external\' creates separate media files and the wrapper file (.mov) contains references to these media files. A value of \'self_contained\' creates only a wrapper (.mov) file and this file contains all of the media.
                  
                    - **Mp4Settings** *(dict) --* Settings for MP4 Container
                      
                      - **CslgAtom** *(string) --* When enabled, file composition times will start at zero, composition times in the \'ctts\' (composition time to sample) box for B-frames will be negative, and a \'cslg\' (composition shift least greatest) box will be included per 14496-1 amendment 1. This improves compatibility with Apple players and tools.
                      
                      - **FreeSpaceBox** *(string) --* Inserts a free-space box immediately after the moov box.
                      
                      - **MoovPlacement** *(string) --* If set to PROGRESSIVE_DOWNLOAD, the MOOV atom is relocated to the beginning of the archive as required for progressive downloading. Otherwise it is placed normally at the end.
                      
                      - **Mp4MajorBrand** *(string) --* Overrides the \"Major Brand\" field in the output file. Usually not necessary to specify.
                  
                  - **VideoDescription** *(dict) --* (VideoDescription) contains a group of video encoding settings. The specific video settings depend on the video codec you choose when you specify a value for Video codec (codec). Include one instance of (VideoDescription) per output.
                    
                    - **AfdSignaling** *(string) --* This setting only applies to H.264 and MPEG2 outputs. Use Insert AFD signaling (AfdSignaling) to specify whether the service includes AFD values in the output video data and what those values are. * Choose None to remove all AFD values from this output. * Choose Fixed to ignore input AFD values and instead encode the value specified in the job. * Choose Auto to calculate output AFD values based on the input AFD scaler data.
                    
                    - **AntiAlias** *(string) --* Enable Anti-alias (AntiAlias) to enhance sharp edges in video output when your input resolution is much larger than your output resolution. Default is enabled.
                    
                    - **CodecSettings** *(dict) --* Video codec settings, (CodecSettings) under (VideoDescription), contains the group of settings related to video encoding. The settings in this group vary depending on the value you choose for Video codec (Codec). For each codec enum you choose, define the corresponding settings object. The following lists the codec enum, settings object pairs. * H_264, H264Settings * H_265, H265Settings * MPEG2, Mpeg2Settings * PRORES, ProresSettings * FRAME_CAPTURE, FrameCaptureSettings
                      
                      - **Codec** *(string) --* Type of video codec
                      
                      - **FrameCaptureSettings** *(dict) --* Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the value FRAME_CAPTURE.
                        
                        - **FramerateDenominator** *(integer) --* Frame capture will encode the first frame of the output stream, then one frame every framerateDenominator/framerateNumerator seconds. For example, settings of framerateNumerator = 1 and framerateDenominator = 3 (a rate of 1/3 frame per second) will capture the first frame, then 1 frame every 3s. Files will be named as filename.n.jpg where n is the 0-based sequence number of each Capture.
                        
                        - **FramerateNumerator** *(integer) --* Frame capture will encode the first frame of the output stream, then one frame every framerateDenominator/framerateNumerator seconds. For example, settings of framerateNumerator = 1 and framerateDenominator = 3 (a rate of 1/3 frame per second) will capture the first frame, then 1 frame every 3s. Files will be named as filename.NNNNNNN.jpg where N is the 0-based frame sequence number zero padded to 7 decimal places.
                        
                        - **MaxCaptures** *(integer) --* Maximum number of captures (encoded jpg output files).
                        
                        - **Quality** *(integer) --* JPEG Quality - a higher value equals higher quality.
                    
                      - **H264Settings** *(dict) --* Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the value H_264.
                        
                        - **AdaptiveQuantization** *(string) --* Adaptive quantization. Allows intra-frame quantizers to vary to improve visual quality.
                        
                        - **Bitrate** *(integer) --* Average bitrate in bits/second. Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique when rounded down to the nearest multiple of 1000.
                        
                        - **CodecLevel** *(string) --* H.264 Level.
                        
                        - **CodecProfile** *(string) --* H.264 Profile. High 4:2:2 and 10-bit profiles are only available with the AVC-I License.
                        
                        - **DynamicSubGop** *(string) --* Choose Adaptive to improve subjective video quality for high-motion content. This will cause the service to use fewer B-frames (which infer information based on other frames) for high-motion portions of the video and more B-frames for low-motion portions. The maximum number of B-frames is limited by the value you provide for the setting B frames between reference frames (numberBFramesBetweenReferenceFrames).
                        
                        - **EntropyEncoding** *(string) --* Entropy encoding mode. Use CABAC (must be in Main or High profile) or CAVLC.
                        
                        - **FieldEncoding** *(string) --* Choosing FORCE_FIELD disables PAFF encoding for interlaced outputs.
                        
                        - **FlickerAdaptiveQuantization** *(string) --* Adjust quantization within each frame to reduce flicker or \'pop\' on I-frames.
                        
                        - **FramerateControl** *(string) --* If you are using the console, use the Framerate setting to specify the framerate for this output. If you want to keep the same framerate as the input video, choose Follow source. If you want to do framerate conversion, choose a framerate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your framerate as a fraction. If you are creating your transcoding job specification as a JSON file without the console, use FramerateControl to specify which value the service uses for the framerate for this output. Choose INITIALIZE_FROM_SOURCE if you want the service to use the framerate from the input. Choose SPECIFIED if you want the service to use the framerate you specify in the settings FramerateNumerator and FramerateDenominator.
                        
                        - **FramerateConversionAlgorithm** *(string) --* When set to INTERPOLATE, produces smoother motion during framerate conversion.
                        
                        - **FramerateDenominator** *(integer) --* When you use the API for transcode jobs that use framerate conversion, specify the framerate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateDenominator to specify the denominator of this fraction. In this example, use 1001 for the value of FramerateDenominator. When you use the console for transcode jobs that use framerate conversion, provide the value as a decimal number for Framerate. In this example, specify 23.976.
                        
                        - **FramerateNumerator** *(integer) --* Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps.
                        
                        - **GopBReference** *(string) --* If enable, use reference B frames for GOP structures that have B frames > 1.
                        
                        - **GopClosedCadence** *(integer) --* Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting.
                        
                        - **GopSize** *(float) --* GOP Length (keyframe interval) in frames or seconds. Must be greater than zero.
                        
                        - **GopSizeUnits** *(string) --* Indicates if the GOP Size in H264 is specified in frames or seconds. If seconds the system will convert the GOP Size into a frame count at run time.
                        
                        - **HrdBufferInitialFillPercentage** *(integer) --* Percentage of the buffer that should initially be filled (HRD buffer model).
                        
                        - **HrdBufferSize** *(integer) --* Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000.
                        
                        - **InterlaceMode** *(string) --* Use Interlace mode (InterlaceMode) to choose the scan line type for the output. * Top Field First (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce interlaced output with the entire output having the same field polarity (top or bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow, Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as the source. Therefore, behavior depends on the input scan type, as follows. - If the source is interlaced, the output will be interlaced with the same polarity as the source (it will follow the source). The output could therefore be a mix of \"top field first\" and \"bottom field first\". - If the source is progressive, the output will be interlaced with \"top field first\" or \"bottom field first\" polarity, depending on which of the Follow options you chose.
                        
                        - **MaxBitrate** *(integer) --* Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. Required when Rate control mode is QVBR.
                        
                        - **MinIInterval** *(integer) --* Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. This setting is only used when Scene Change Detect is enabled. Note: Maximum GOP stretch = GOP size + Min-I-interval - 1
                        
                        - **NumberBFramesBetweenReferenceFrames** *(integer) --* Number of B-frames between reference frames.
                        
                        - **NumberReferenceFrames** *(integer) --* Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding.
                        
                        - **ParControl** *(string) --* Using the API, enable ParFollowSource if you want the service to use the pixel aspect ratio from the input. Using the console, do this by choosing Follow source for Pixel aspect ratio.
                        
                        - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.
                        
                        - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.
                        
                        - **QualityTuningLevel** *(string) --* Use Quality tuning level (H264QualityTuningLevel) to specifiy whether to use fast single-pass, high-quality singlepass, or high-quality multipass video encoding.
                        
                        - **QvbrSettings** *(dict) --* Settings for quality-defined variable bitrate encoding with the H.264 codec. Required when you set Rate control mode to QVBR. Not valid when you set Rate control mode to a value other than QVBR, or when you don\'t define Rate control mode.
                          
                          - **MaxAverageBitrate** *(integer) --* Use this setting only when Rate control mode is QVBR and Quality tuning level is Multi-pass HQ. For Max average bitrate values suited to the complexity of your input video, the service limits the average bitrate of the video part of this output to the value you choose. That is, the total size of the video element is less than or equal to the value you set multiplied by the number of seconds of encoded output.
                          
                          - **QvbrQualityLevel** *(integer) --* Required when you use QVBR rate control mode. That is, when you specify qvbrSettings within h264Settings. Specify the target quality level for this output, from 1 to 10. Use higher numbers for greater quality. Level 10 results in nearly lossless compression. The quality level for most broadcast-quality transcodes is between 6 and 9.
                      
                        - **RateControlMode** *(string) --* Use this setting to specify whether this output has a variable bitrate (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR).
                        
                        - **RepeatPps** *(string) --* Places a PPS header on each encoded picture, even if repeated.
                        
                        - **SceneChangeDetect** *(string) --* Scene change detection (inserts I-frames on scene changes).
                        
                        - **Slices** *(integer) --* Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures.
                        
                        - **SlowPal** *(string) --* Enables Slow PAL rate conversion. 23.976fps and 24fps input is relabeled as 25fps, and audio is sped up correspondingly.
                        
                        - **Softness** *(integer) --* Softness. Selects quantizer matrix, larger values reduce high-frequency content in the encoded image.
                        
                        - **SpatialAdaptiveQuantization** *(string) --* Adjust quantization within each frame based on spatial variation of content complexity.
                        
                        - **Syntax** *(string) --* Produces a bitstream compliant with SMPTE RP-2027.
                        
                        - **Telecine** *(string) --* This field applies only if the Streams > Advanced > Framerate (framerate) field is set to 29.970. This field works with the Streams > Advanced > Preprocessors > Deinterlacer field (deinterlace_mode) and the Streams > Advanced > Interlaced Mode field (interlace_mode) to identify the scan type for the output: Progressive, Interlaced, Hard Telecine or Soft Telecine. - Hard: produces 29.97i output from 23.976 input. - Soft: produces 23.976; the player converts this output to 29.97i.
                        
                        - **TemporalAdaptiveQuantization** *(string) --* Adjust quantization within each frame based on temporal variation of content complexity.
                        
                        - **UnregisteredSeiTimecode** *(string) --* Inserts timecode for each frame as 4 bytes of an unregistered SEI message.
                    
                      - **H265Settings** *(dict) --* Settings for H265 codec
                        
                        - **AdaptiveQuantization** *(string) --* Adaptive quantization. Allows intra-frame quantizers to vary to improve visual quality.
                        
                        - **AlternateTransferFunctionSei** *(string) --* Enables Alternate Transfer Function SEI message for outputs using Hybrid Log Gamma (HLG) Electro-Optical Transfer Function (EOTF).
                        
                        - **Bitrate** *(integer) --* Average bitrate in bits/second. Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique when rounded down to the nearest multiple of 1000.
                        
                        - **CodecLevel** *(string) --* H.265 Level.
                        
                        - **CodecProfile** *(string) --* Represents the Profile and Tier, per the HEVC (H.265) specification. Selections are grouped as [Profile] / [Tier], so \"Main/High\" represents Main Profile with High Tier. 4:2:2 profiles are only available with the HEVC 4:2:2 License.
                        
                        - **DynamicSubGop** *(string) --* Choose Adaptive to improve subjective video quality for high-motion content. This will cause the service to use fewer B-frames (which infer information based on other frames) for high-motion portions of the video and more B-frames for low-motion portions. The maximum number of B-frames is limited by the value you provide for the setting B frames between reference frames (numberBFramesBetweenReferenceFrames).
                        
                        - **FlickerAdaptiveQuantization** *(string) --* Adjust quantization within each frame to reduce flicker or \'pop\' on I-frames.
                        
                        - **FramerateControl** *(string) --* If you are using the console, use the Framerate setting to specify the framerate for this output. If you want to keep the same framerate as the input video, choose Follow source. If you want to do framerate conversion, choose a framerate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your framerate as a fraction. If you are creating your transcoding job sepecification as a JSON file without the console, use FramerateControl to specify which value the service uses for the framerate for this output. Choose INITIALIZE_FROM_SOURCE if you want the service to use the framerate from the input. Choose SPECIFIED if you want the service to use the framerate you specify in the settings FramerateNumerator and FramerateDenominator.
                        
                        - **FramerateConversionAlgorithm** *(string) --* When set to INTERPOLATE, produces smoother motion during framerate conversion.
                        
                        - **FramerateDenominator** *(integer) --* Framerate denominator.
                        
                        - **FramerateNumerator** *(integer) --* Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps.
                        
                        - **GopBReference** *(string) --* If enable, use reference B frames for GOP structures that have B frames > 1.
                        
                        - **GopClosedCadence** *(integer) --* Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting.
                        
                        - **GopSize** *(float) --* GOP Length (keyframe interval) in frames or seconds. Must be greater than zero.
                        
                        - **GopSizeUnits** *(string) --* Indicates if the GOP Size in H265 is specified in frames or seconds. If seconds the system will convert the GOP Size into a frame count at run time.
                        
                        - **HrdBufferInitialFillPercentage** *(integer) --* Percentage of the buffer that should initially be filled (HRD buffer model).
                        
                        - **HrdBufferSize** *(integer) --* Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000.
                        
                        - **InterlaceMode** *(string) --* Use Interlace mode (InterlaceMode) to choose the scan line type for the output. * Top Field First (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce interlaced output with the entire output having the same field polarity (top or bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow, Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as the source. Therefore, behavior depends on the input scan type. - If the source is interlaced, the output will be interlaced with the same polarity as the source (it will follow the source). The output could therefore be a mix of \"top field first\" and \"bottom field first\". - If the source is progressive, the output will be interlaced with \"top field first\" or \"bottom field first\" polarity, depending on which of the Follow options you chose.
                        
                        - **MaxBitrate** *(integer) --* Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000. Required when Rate control mode is QVBR.
                        
                        - **MinIInterval** *(integer) --* Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. This setting is only used when Scene Change Detect is enabled. Note: Maximum GOP stretch = GOP size + Min-I-interval - 1
                        
                        - **NumberBFramesBetweenReferenceFrames** *(integer) --* Number of B-frames between reference frames.
                        
                        - **NumberReferenceFrames** *(integer) --* Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding.
                        
                        - **ParControl** *(string) --* Using the API, enable ParFollowSource if you want the service to use the pixel aspect ratio from the input. Using the console, do this by choosing Follow source for Pixel aspect ratio.
                        
                        - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.
                        
                        - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.
                        
                        - **QualityTuningLevel** *(string) --* Use Quality tuning level (H265QualityTuningLevel) to specifiy whether to use fast single-pass, high-quality singlepass, or high-quality multipass video encoding.
                        
                        - **QvbrSettings** *(dict) --* Settings for quality-defined variable bitrate encoding with the H.265 codec. Required when you set Rate control mode to QVBR. Not valid when you set Rate control mode to a value other than QVBR, or when you don\'t define Rate control mode.
                          
                          - **MaxAverageBitrate** *(integer) --* Use this setting only when Rate control mode is QVBR and Quality tuning level is Multi-pass HQ. For Max average bitrate values suited to the complexity of your input video, the service limits the average bitrate of the video part of this output to the value you choose. That is, the total size of the video element is less than or equal to the value you set multiplied by the number of seconds of encoded output.
                          
                          - **QvbrQualityLevel** *(integer) --* Required when you use QVBR rate control mode. That is, when you specify qvbrSettings within h265Settings. Specify the target quality level for this output, from 1 to 10. Use higher numbers for greater quality. Level 10 results in nearly lossless compression. The quality level for most broadcast-quality transcodes is between 6 and 9.
                      
                        - **RateControlMode** *(string) --* Use this setting to specify whether this output has a variable bitrate (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR).
                        
                        - **SampleAdaptiveOffsetFilterMode** *(string) --* Specify Sample Adaptive Offset (SAO) filter strength. Adaptive mode dynamically selects best strength based on content
                        
                        - **SceneChangeDetect** *(string) --* Scene change detection (inserts I-frames on scene changes).
                        
                        - **Slices** *(integer) --* Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures.
                        
                        - **SlowPal** *(string) --* Enables Slow PAL rate conversion. 23.976fps and 24fps input is relabeled as 25fps, and audio is sped up correspondingly.
                        
                        - **SpatialAdaptiveQuantization** *(string) --* Adjust quantization within each frame based on spatial variation of content complexity.
                        
                        - **Telecine** *(string) --* This field applies only if the Streams > Advanced > Framerate (framerate) field is set to 29.970. This field works with the Streams > Advanced > Preprocessors > Deinterlacer field (deinterlace_mode) and the Streams > Advanced > Interlaced Mode field (interlace_mode) to identify the scan type for the output: Progressive, Interlaced, Hard Telecine or Soft Telecine. - Hard: produces 29.97i output from 23.976 input. - Soft: produces 23.976; the player converts this output to 29.97i.
                        
                        - **TemporalAdaptiveQuantization** *(string) --* Adjust quantization within each frame based on temporal variation of content complexity.
                        
                        - **TemporalIds** *(string) --* Enables temporal layer identifiers in the encoded bitstream. Up to 3 layers are supported depending on GOP structure: I- and P-frames form one layer, reference B-frames can form a second layer and non-reference b-frames can form a third layer. Decoders can optionally decode only the lower temporal layers to generate a lower frame rate output. For example, given a bitstream with temporal IDs and with b-frames = 1 (i.e. IbPbPb display order), a decoder could decode all the frames for full frame rate output or only the I and P frames (lowest temporal layer) for a half frame rate output.
                        
                        - **Tiles** *(string) --* Enable use of tiles, allowing horizontal as well as vertical subdivision of the encoded pictures.
                        
                        - **UnregisteredSeiTimecode** *(string) --* Inserts timecode for each frame as 4 bytes of an unregistered SEI message.
                        
                        - **WriteMp4PackagingType** *(string) --* If HVC1, output that is H.265 will be marked as HVC1 and adhere to the ISO-IECJTC1-SC29_N13798_Text_ISOIEC_FDIS_14496-15_3rd_E spec which states that parameter set NAL units will be stored in the sample headers but not in the samples directly. If HEV1, then H.265 will be marked as HEV1 and parameter set NAL units will be written into the samples.
                    
                      - **Mpeg2Settings** *(dict) --* Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the value MPEG2.
                        
                        - **AdaptiveQuantization** *(string) --* Adaptive quantization. Allows intra-frame quantizers to vary to improve visual quality.
                        
                        - **Bitrate** *(integer) --* Average bitrate in bits/second. Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique when rounded down to the nearest multiple of 1000.
                        
                        - **CodecLevel** *(string) --* Use Level (Mpeg2CodecLevel) to set the MPEG-2 level for the video output.
                        
                        - **CodecProfile** *(string) --* Use Profile (Mpeg2CodecProfile) to set the MPEG-2 profile for the video output.
                        
                        - **DynamicSubGop** *(string) --* Choose Adaptive to improve subjective video quality for high-motion content. This will cause the service to use fewer B-frames (which infer information based on other frames) for high-motion portions of the video and more B-frames for low-motion portions. The maximum number of B-frames is limited by the value you provide for the setting B frames between reference frames (numberBFramesBetweenReferenceFrames).
                        
                        - **FramerateControl** *(string) --* If you are using the console, use the Framerate setting to specify the framerate for this output. If you want to keep the same framerate as the input video, choose Follow source. If you want to do framerate conversion, choose a framerate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your framerate as a fraction. If you are creating your transcoding job sepecification as a JSON file without the console, use FramerateControl to specify which value the service uses for the framerate for this output. Choose INITIALIZE_FROM_SOURCE if you want the service to use the framerate from the input. Choose SPECIFIED if you want the service to use the framerate you specify in the settings FramerateNumerator and FramerateDenominator.
                        
                        - **FramerateConversionAlgorithm** *(string) --* When set to INTERPOLATE, produces smoother motion during framerate conversion.
                        
                        - **FramerateDenominator** *(integer) --* Framerate denominator.
                        
                        - **FramerateNumerator** *(integer) --* Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps.
                        
                        - **GopClosedCadence** *(integer) --* Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting.
                        
                        - **GopSize** *(float) --* GOP Length (keyframe interval) in frames or seconds. Must be greater than zero.
                        
                        - **GopSizeUnits** *(string) --* Indicates if the GOP Size in MPEG2 is specified in frames or seconds. If seconds the system will convert the GOP Size into a frame count at run time.
                        
                        - **HrdBufferInitialFillPercentage** *(integer) --* Percentage of the buffer that should initially be filled (HRD buffer model).
                        
                        - **HrdBufferSize** *(integer) --* Size of buffer (HRD buffer model) in bits. For example, enter five megabits as 5000000.
                        
                        - **InterlaceMode** *(string) --* Use Interlace mode (InterlaceMode) to choose the scan line type for the output. * Top Field First (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce interlaced output with the entire output having the same field polarity (top or bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow, Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as the source. Therefore, behavior depends on the input scan type. - If the source is interlaced, the output will be interlaced with the same polarity as the source (it will follow the source). The output could therefore be a mix of \"top field first\" and \"bottom field first\". - If the source is progressive, the output will be interlaced with \"top field first\" or \"bottom field first\" polarity, depending on which of the Follow options you chose.
                        
                        - **IntraDcPrecision** *(string) --* Use Intra DC precision (Mpeg2IntraDcPrecision) to set quantization precision for intra-block DC coefficients. If you choose the value auto, the service will automatically select the precision based on the per-frame compression ratio.
                        
                        - **MaxBitrate** *(integer) --* Maximum bitrate in bits/second. For example, enter five megabits per second as 5000000.
                        
                        - **MinIInterval** *(integer) --* Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. This setting is only used when Scene Change Detect is enabled. Note: Maximum GOP stretch = GOP size + Min-I-interval - 1
                        
                        - **NumberBFramesBetweenReferenceFrames** *(integer) --* Number of B-frames between reference frames.
                        
                        - **ParControl** *(string) --* Using the API, enable ParFollowSource if you want the service to use the pixel aspect ratio from the input. Using the console, do this by choosing Follow source for Pixel aspect ratio.
                        
                        - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.
                        
                        - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.
                        
                        - **QualityTuningLevel** *(string) --* Use Quality tuning level (Mpeg2QualityTuningLevel) to specifiy whether to use single-pass or multipass video encoding.
                        
                        - **RateControlMode** *(string) --* Use Rate control mode (Mpeg2RateControlMode) to specifiy whether the bitrate is variable (vbr) or constant (cbr).
                        
                        - **SceneChangeDetect** *(string) --* Scene change detection (inserts I-frames on scene changes).
                        
                        - **SlowPal** *(string) --* Enables Slow PAL rate conversion. 23.976fps and 24fps input is relabeled as 25fps, and audio is sped up correspondingly.
                        
                        - **Softness** *(integer) --* Softness. Selects quantizer matrix, larger values reduce high-frequency content in the encoded image.
                        
                        - **SpatialAdaptiveQuantization** *(string) --* Adjust quantization within each frame based on spatial variation of content complexity.
                        
                        - **Syntax** *(string) --* Produces a Type D-10 compatible bitstream (SMPTE 356M-2001).
                        
                        - **Telecine** *(string) --* Only use Telecine (Mpeg2Telecine) when you set Framerate (Framerate) to 29.970. Set Telecine (Mpeg2Telecine) to Hard (hard) to produce a 29.97i output from a 23.976 input. Set it to Soft (soft) to produce 23.976 output and leave converstion to the player.
                        
                        - **TemporalAdaptiveQuantization** *(string) --* Adjust quantization within each frame based on temporal variation of content complexity.
                    
                      - **ProresSettings** *(dict) --* Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the value PRORES.
                        
                        - **CodecProfile** *(string) --* Use Profile (ProResCodecProfile) to specifiy the type of Apple ProRes codec to use for this output.
                        
                        - **FramerateControl** *(string) --* If you are using the console, use the Framerate setting to specify the framerate for this output. If you want to keep the same framerate as the input video, choose Follow source. If you want to do framerate conversion, choose a framerate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your framerate as a fraction. If you are creating your transcoding job sepecification as a JSON file without the console, use FramerateControl to specify which value the service uses for the framerate for this output. Choose INITIALIZE_FROM_SOURCE if you want the service to use the framerate from the input. Choose SPECIFIED if you want the service to use the framerate you specify in the settings FramerateNumerator and FramerateDenominator.
                        
                        - **FramerateConversionAlgorithm** *(string) --* When set to INTERPOLATE, produces smoother motion during framerate conversion.
                        
                        - **FramerateDenominator** *(integer) --* Framerate denominator.
                        
                        - **FramerateNumerator** *(integer) --* When you use the API for transcode jobs that use framerate conversion, specify the framerate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use FramerateNumerator to specify the numerator of this fraction. In this example, use 24000 for the value of FramerateNumerator.
                        
                        - **InterlaceMode** *(string) --* Use Interlace mode (InterlaceMode) to choose the scan line type for the output. * Top Field First (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce interlaced output with the entire output having the same field polarity (top or bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow, Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as the source. Therefore, behavior depends on the input scan type. - If the source is interlaced, the output will be interlaced with the same polarity as the source (it will follow the source). The output could therefore be a mix of \"top field first\" and \"bottom field first\". - If the source is progressive, the output will be interlaced with \"top field first\" or \"bottom field first\" polarity, depending on which of the Follow options you chose.
                        
                        - **ParControl** *(string) --* Use (ProresParControl) to specify how the service determines the pixel aspect ratio. Set to Follow source (INITIALIZE_FROM_SOURCE) to use the pixel aspect ratio from the input. To specify a different pixel aspect ratio: Using the console, choose it from the dropdown menu. Using the API, set ProresParControl to (SPECIFIED) and provide for (ParNumerator) and (ParDenominator).
                        
                        - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.
                        
                        - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.
                        
                        - **SlowPal** *(string) --* Enables Slow PAL rate conversion. 23.976fps and 24fps input is relabeled as 25fps, and audio is sped up correspondingly.
                        
                        - **Telecine** *(string) --* Only use Telecine (ProresTelecine) when you set Framerate (Framerate) to 29.970. Set Telecine (ProresTelecine) to Hard (hard) to produce a 29.97i output from a 23.976 input. Set it to Soft (soft) to produce 23.976 output and leave converstion to the player.
                    
                    - **ColorMetadata** *(string) --* Enable Insert color metadata (ColorMetadata) to include color metadata in this output. This setting is enabled by default.
                    
                    - **Crop** *(dict) --* Applies only if your input aspect ratio is different from your output aspect ratio. Use Input cropping rectangle (Crop) to specify the video area the service will include in the output. This will crop the input source, causing video pixels to be removed on encode. Do not use this setting if you have enabled Stretch to output (stretchToOutput) in your output settings.
                      
                      - **Height** *(integer) --* Height of rectangle in pixels. Specify only even numbers.
                      
                      - **Width** *(integer) --* Width of rectangle in pixels. Specify only even numbers.
                      
                      - **X** *(integer) --* The distance, in pixels, between the rectangle and the left edge of the video frame. Specify only even numbers.
                      
                      - **Y** *(integer) --* The distance, in pixels, between the rectangle and the top edge of the video frame. Specify only even numbers.
                  
                    - **DropFrameTimecode** *(string) --* Applies only to 29.97 fps outputs. When this feature is enabled, the service will use drop-frame timecode on outputs. If it is not possible to use drop-frame timecode, the system will fall back to non-drop-frame. This setting is enabled by default when Timecode insertion (TimecodeInsertion) is enabled.
                    
                    - **FixedAfd** *(integer) --* Applies only if you set AFD Signaling(AfdSignaling) to Fixed (FIXED). Use Fixed (FixedAfd) to specify a four-bit AFD value which the service will write on all frames of this video output.
                    
                    - **Height** *(integer) --* Use the Height (Height) setting to define the video resolution height for this output. Specify in pixels. If you don\'t provide a value here, the service will use the input height.
                    
                    - **Position** *(dict) --* Use Position (Position) to point to a rectangle object to define your position. This setting overrides any other aspect ratio.
                      
                      - **Height** *(integer) --* Height of rectangle in pixels. Specify only even numbers.
                      
                      - **Width** *(integer) --* Width of rectangle in pixels. Specify only even numbers.
                      
                      - **X** *(integer) --* The distance, in pixels, between the rectangle and the left edge of the video frame. Specify only even numbers.
                      
                      - **Y** *(integer) --* The distance, in pixels, between the rectangle and the top edge of the video frame. Specify only even numbers.
                  
                    - **RespondToAfd** *(string) --* Use Respond to AFD (RespondToAfd) to specify how the service changes the video itself in response to AFD values in the input. * Choose Respond to clip the input video frame according to the AFD value, input display aspect ratio, and output display aspect ratio. * Choose Passthrough to include the input AFD values. Do not choose this when AfdSignaling is set to (NONE). A preferred implementation of this workflow is to set RespondToAfd to (NONE) and set AfdSignaling to (AUTO). * Choose None to remove all input AFD values from this output.
                    
                    - **ScalingBehavior** *(string) --* Applies only if your input aspect ratio is different from your output aspect ratio. Enable Stretch to output (StretchToOutput) to have the service stretch your video image to fit. Leave this setting disabled to allow the service to letterbox your video instead. This setting overrides any positioning value you specify elsewhere in the job.
                    
                    - **Sharpness** *(integer) --* Use Sharpness (Sharpness)setting to specify the strength of anti-aliasing. This setting changes the width of the anti-alias filter kernel used for scaling. Sharpness only applies if your output resolution is different from your input resolution, and if you set Anti-alias (AntiAlias) to ENABLED. 0 is the softest setting, 100 the sharpest, and 50 recommended for most content.
                    
                    - **TimecodeInsertion** *(string) --* Applies only to H.264, H.265, MPEG2, and ProRes outputs. Only enable Timecode insertion when the input framerate is identical to the output framerate. To include timecodes in this output, set Timecode insertion (VideoTimecodeInsertion) to PIC_TIMING_SEI. To leave them out, set it to DISABLED. Default is DISABLED. When the service inserts timecodes in an output, by default, it uses any embedded timecodes from the input. If none are present, the service will set the timecode for the first output frame to zero. To change this default behavior, adjust the settings under Timecode configuration (TimecodeConfig). In the console, these settings are located under Job > Job settings > Timecode configuration. Note - Timecode source under input settings (InputTimecodeSource) does not affect the timecodes that are inserted in the output. Source under Job settings > Timecode configuration (TimecodeSource) does.
                    
                    - **VideoPreprocessors** *(dict) --* Find additional transcoding features under Preprocessors (VideoPreprocessors). Enable the features at each output individually. These features are disabled by default.
                      
                      - **ColorCorrector** *(dict) --* Enable the Color corrector (ColorCorrector) feature if necessary. Enable or disable this feature for each output individually. This setting is disabled by default.
                        
                        - **Brightness** *(integer) --* Brightness level.
                        
                        - **ColorSpaceConversion** *(string) --* Determines if colorspace conversion will be performed. If set to _None_, no conversion will be performed. If _Force 601_ or _Force 709_ are selected, conversion will be performed for inputs with differing colorspaces. An input\'s colorspace can be specified explicitly in the \"Video Selector\":#inputs-video_selector if necessary.
                        
                        - **Contrast** *(integer) --* Contrast level.
                        
                        - **Hdr10Metadata** *(dict) --* Use the HDR master display (Hdr10Metadata) settings to correct HDR metadata or to provide missing metadata. These values vary depending on the input video and must be provided by a color grader. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that these settings are not color correction. Note that if you are creating HDR outputs inside of an HLS CMAF package, to comply with the Apple specification, you must use the HVC1 for H.265 setting.
                          
                          - **BluePrimaryX** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                          
                          - **BluePrimaryY** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                          
                          - **GreenPrimaryX** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                          
                          - **GreenPrimaryY** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                          
                          - **MaxContentLightLevel** *(integer) --* Maximum light level among all samples in the coded video sequence, in units of candelas per square meter.
                          
                          - **MaxFrameAverageLightLevel** *(integer) --* Maximum average light level of any frame in the coded video sequence, in units of candelas per square meter.
                          
                          - **MaxLuminance** *(integer) --* Nominal maximum mastering display luminance in units of of 0.0001 candelas per square meter.
                          
                          - **MinLuminance** *(integer) --* Nominal minimum mastering display luminance in units of of 0.0001 candelas per square meter
                          
                          - **RedPrimaryX** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                          
                          - **RedPrimaryY** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                          
                          - **WhitePointX** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                          
                          - **WhitePointY** *(integer) --* HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction.
                      
                        - **Hue** *(integer) --* Hue in degrees.
                        
                        - **Saturation** *(integer) --* Saturation level.
                    
                      - **Deinterlacer** *(dict) --* Use Deinterlacer (Deinterlacer) to produce smoother motion and a clearer picture.
                        
                        - **Algorithm** *(string) --* Only applies when you set Deinterlacer (DeinterlaceMode) to Deinterlace (DEINTERLACE) or Adaptive (ADAPTIVE). Motion adaptive interpolate (INTERPOLATE) produces sharper pictures, while blend (BLEND) produces smoother motion. Use (INTERPOLATE_TICKER) OR (BLEND_TICKER) if your source file includes a ticker, such as a scrolling headline at the bottom of the frame.
                        
                        - **Control** *(string) --* - When set to NORMAL (default), the deinterlacer does not convert frames that are tagged in metadata as progressive. It will only convert those that are tagged as some other type. - When set to FORCE_ALL_FRAMES, the deinterlacer converts every frame to progressive - even those that are already tagged as progressive. Turn Force mode on only if there is a good chance that the metadata has tagged frames as progressive when they are not progressive. Do not turn on otherwise; processing frames that are already progressive into progressive will probably result in lower quality video.
                        
                        - **Mode** *(string) --* Use Deinterlacer (DeinterlaceMode) to choose how the service will do deinterlacing. Default is Deinterlace. - Deinterlace converts interlaced to progressive. - Inverse telecine converts Hard Telecine 29.97i to progressive 23.976p. - Adaptive auto-detects and converts to progressive.
                    
                      - **ImageInserter** *(dict) --* Enable the Image inserter (ImageInserter) feature to include a graphic overlay on your video. Enable or disable this feature for each output individually. This setting is disabled by default.
                        
                        - **InsertableImages** *(list) --* Image to insert. Must be 32 bit windows BMP, PNG, or TGA file. Must not be larger than the output frames.
                          
                          - *(dict) --* Settings for Insertable Image
                            
                            - **Duration** *(integer) --* Use Duration (Duration) to set the time, in milliseconds, for the image to remain on the output video.
                            
                            - **FadeIn** *(integer) --* Use Fade in (FadeIut) to set the length, in milliseconds, of the inserted image fade in. If you don\'t specify a value for Fade in, the image will appear abruptly at the Start time.
                            
                            - **FadeOut** *(integer) --* Use Fade out (FadeOut) to set the length, in milliseconds, of the inserted image fade out. If you don\'t specify a value for Fade out, the image will disappear abruptly at the end of the inserted image duration.
                            
                            - **Height** *(integer) --* Specify the Height (Height) of the inserted image. Use a value that is less than or equal to the video resolution height. Leave this setting blank to use the native height of the image.
                            
                            - **ImageInserterInput** *(string) --* Use Image location (imageInserterInput) to specify the Amazon S3 location of the image to be inserted into the output. Use a 32 bit BMP, PNG, or TGA file that fits inside the video frame.
                            
                            - **ImageX** *(integer) --* Use Left (ImageX) to set the distance, in pixels, between the inserted image and the left edge of the frame. Required for BMP, PNG and TGA input.
                            
                            - **ImageY** *(integer) --* Use Top (ImageY) to set the distance, in pixels, between the inserted image and the top edge of the video frame. Required for BMP, PNG and TGA input.
                            
                            - **Layer** *(integer) --* Use Layer (Layer) to specify how overlapping inserted images appear. Images with higher values of layer appear on top of images with lower values of layer.
                            
                            - **Opacity** *(integer) --* Use Opacity (Opacity) to specify how much of the underlying video shows through the inserted image. 0 is transparent and 100 is fully opaque. Default is 50.
                            
                            - **StartTime** *(string) --* Use Start time (StartTime) to specify the video timecode when the image is inserted in the output. This must be in timecode (HH:MM:SS:FF or HH:MM:SS;FF) format.
                            
                            - **Width** *(integer) --* Specify the Width (Width) of the inserted image. Use a value that is less than or equal to the video resolution width. Leave this setting blank to use the native width of the image.
                        
                      - **NoiseReducer** *(dict) --* Enable the Noise reducer (NoiseReducer) feature to remove noise from your video output if necessary. Enable or disable this feature for each output individually. This setting is disabled by default.
                        
                        - **Filter** *(string) --* Use Noise reducer filter (NoiseReducerFilter) to select one of the following spatial image filtering functions. To use this setting, you must also enable Noise reducer (NoiseReducer). * Bilateral is an edge preserving noise reduction filter. * Mean (softest), Gaussian, Lanczos, and Sharpen (sharpest) are convolution filters. * Conserve is a min/max noise reduction filter. * Spatial is a frequency-domain filter based on JND principles.
                        
                        - **FilterSettings** *(dict) --* Settings for a noise reducer filter
                          
                          - **Strength** *(integer) --* Relative strength of noise reducing filter. Higher values produce stronger filtering.
                      
                        - **SpatialFilterSettings** *(dict) --* Noise reducer filter settings for spatial filter.
                          
                          - **PostFilterSharpenStrength** *(integer) --* Specify strength of post noise reduction sharpening filter, with 0 disabling the filter and 3 enabling it at maximum strength.
                          
                          - **Speed** *(integer) --* The speed of the filter, from -2 (lower speed) to 3 (higher speed), with 0 being the nominal value.
                          
                          - **Strength** *(integer) --* Relative strength of noise reducing filter. Higher values produce stronger filtering.
                      
                      - **TimecodeBurnin** *(dict) --* Timecode burn-in (TimecodeBurnIn)--Burns the output timecode and specified prefix into the output.
                        
                        - **FontSize** *(integer) --* Use Font Size (FontSize) to set the font size of any burned-in timecode. Valid values are 10, 16, 32, 48.
                        
                        - **Position** *(string) --* Use Position (Position) under under Timecode burn-in (TimecodeBurnIn) to specify the location the burned-in timecode on output video.
                        
                        - **Prefix** *(string) --* Use Prefix (Prefix) to place ASCII characters before any burned-in timecode. For example, a prefix of \"EZ-\" will result in the timecode \"EZ-00:00:00:00\". Provide either the characters themselves or the ASCII code equivalents. The supported range of characters is 0x20 through 0x7e. This includes letters, numbers, and all special characters represented on a standard English keyboard.
                    
                    - **Width** *(integer) --* Use Width (Width) to define the video resolution width, in pixels, for this output. If you don\'t provide a value here, the service will use the input width.
                
                - **Type** *(string) --* A preset can be of two types: system or custom. System or built-in preset can\'t be modified or deleted by the user.
            
        """
        pass


class ListQueues(Paginator):
    def paginate(self, ListBy: str = None, Order: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mediaconvert-2017-08-29/ListQueues>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              ListBy=\'NAME\'|\'CREATION_DATE\',
              Order=\'ASCENDING\'|\'DESCENDING\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type ListBy: string
        :param ListBy: Optional. When you request a list of queues, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don\'t specify, the service will list them by creation date.
        
        :type Order: string
        :param Order: When you request lists of resources, you can optionally specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.
        
        :type PaginationConfig: dict
        :param PaginationConfig: 
        
          A dictionary that provides parameters to control pagination.
        
          - **MaxItems** *(integer) --* 
        
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
        
          - **PageSize** *(integer) --* 
        
            The size of each page.
        
          - **StartingToken** *(string) --* 
        
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Queues\': [
                    {
                        \'Arn\': \'string\',
                        \'CreatedAt\': datetime(2015, 1, 1),
                        \'Description\': \'string\',
                        \'LastUpdated\': datetime(2015, 1, 1),
                        \'Name\': \'string\',
                        \'PricingPlan\': \'ON_DEMAND\'|\'RESERVED\',
                        \'ProgressingJobsCount\': 123,
                        \'ReservationPlan\': {
                            \'Commitment\': \'ONE_YEAR\',
                            \'ExpiresAt\': datetime(2015, 1, 1),
                            \'PurchasedAt\': datetime(2015, 1, 1),
                            \'RenewalType\': \'AUTO_RENEW\'|\'EXPIRE\',
                            \'ReservedSlots\': 123,
                            \'Status\': \'ACTIVE\'|\'EXPIRED\'
                        },
                        \'Status\': \'ACTIVE\'|\'PAUSED\',
                        \'SubmittedJobsCount\': 123,
                        \'Type\': \'SYSTEM\'|\'CUSTOM\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Queues** *(list) --* List of queues.
              
              - *(dict) --* You can use queues to manage the resources that are available to your AWS account for running multiple transcoding jobs at the same time. If you don\'t specify a queue, the service sends all jobs through the default queue. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/about-resource-allocation-and-job-prioritization.html.
                
                - **Arn** *(string) --* An identifier for this resource that is unique within all of AWS.
                
                - **CreatedAt** *(datetime) --* The time stamp in epoch seconds for queue creation.
                
                - **Description** *(string) --* An optional description that you create for each queue.
                
                - **LastUpdated** *(datetime) --* The time stamp in epoch seconds when the queue was last updated.
                
                - **Name** *(string) --* A name that you create for each queue. Each name must be unique within your account.
                
                - **PricingPlan** *(string) --* Specifies whether the pricing plan for the queue is On-demand or Reserved. The pricing plan for the queue determines whether you pay On-demand or Reserved pricing for the transcoding jobs that you run through the queue. For Reserved queue pricing, you must set up a contract. You can create a Reserved queue contract through the AWS Elemental MediaConvert console.
                
                - **ProgressingJobsCount** *(integer) --* The estimated number of jobs with a PROGRESSING status.
                
                - **ReservationPlan** *(dict) --* Details about the pricing plan for your reserved queue. Required for reserved queues and not applicable to on-demand queues.
                  
                  - **Commitment** *(string) --* The length of time that you commit to when you set up a pricing plan contract for a reserved queue.
                  
                  - **ExpiresAt** *(datetime) --* The time stamp, in epoch seconds, for when the pricing plan for this reserved queue expires.
                  
                  - **PurchasedAt** *(datetime) --* The time stamp in epoch seconds when the reserved queue\'s reservation plan was created.
                  
                  - **RenewalType** *(string) --* Specifies whether the pricing plan contract for your reserved queue automatically renews (AUTO_RENEW) or expires (EXPIRE) at the end of the contract period.
                  
                  - **ReservedSlots** *(integer) --* Specifies the number of reserved transcode slots (RTSs) for this queue. The number of RTS determines how many jobs the queue can process in parallel; each RTS can process one job at a time. To increase this number, create a replacement contract through the AWS Elemental MediaConvert console.
                  
                  - **Status** *(string) --* Specifies whether the pricing plan for your reserved queue is ACTIVE or EXPIRED.
              
                - **Status** *(string) --* Queues can be ACTIVE or PAUSED. If you pause a queue, the service won\'t begin processing jobs in that queue. Jobs that are running when you pause the queue continue to run until they finish or result in an error.
                
                - **SubmittedJobsCount** *(integer) --* The estimated number of jobs with a SUBMITTED status.
                
                - **Type** *(string) --* Specifies whether this queue is system or custom. System queues are built in. You can\'t modify or delete system queues. You can create and modify custom queues.
            
        """
        pass
