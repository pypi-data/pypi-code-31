"""Auto-generated file, do not edit by hand. SK metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SK = PhoneMetadata(id='SK', country_code=421, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-689]\\d{8}|[2-59]\\d{6}|[2-5]\\d{5}', possible_length=(6, 7, 9)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2(?:16|[2-9]\\d{3})|[3-5][1-8]\\d{3})\\d{4}|(?:2|[3-5][1-8])1[67]\\d{3}|[3-5][1-8]16\\d\\d', example_number='221234567', possible_length=(6, 7, 9)),
    mobile=PhoneNumberDesc(national_number_pattern='9(?:0(?:[1-8]\\d|9[1-9])|(?:1[0-24-9]|[45]\\d)\\d)\\d{5}', example_number='912123456', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{6}', example_number='800123456', possible_length=(9,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='9(?:00|[78]\\d)\\d{6}', example_number='900123456', possible_length=(9,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='8[5-9]\\d{7}', example_number='850123456', possible_length=(9,)),
    voip=PhoneNumberDesc(national_number_pattern='6(?:02|5[0-4]|9[0-6])\\d{6}', example_number='690123456', possible_length=(9,)),
    pager=PhoneNumberDesc(national_number_pattern='9090\\d{3}', example_number='9090123', possible_length=(7,)),
    uan=PhoneNumberDesc(national_number_pattern='96\\d{7}', example_number='961234567', possible_length=(9,)),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='(?:(?:602|8(?:00|[5-9]\\d))\\d{3}|9(?:0(?:0\\d{3}|90)|[78]\\d{4}))\\d{3}', possible_length=(7, 9)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d)(\\d{2})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['21'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2,3})', format='\\1 \\2 \\3', leading_digits_pattern=['[3-5][1-8]1', '[3-5][1-8]1[67]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{4})(\\d{3})', format='\\1 \\2', leading_digits_pattern=['909', '9090'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d)(\\d{3})(\\d{3})(\\d{2})', format='\\1/\\2 \\3 \\4', leading_digits_pattern=['2'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{2})(\\d{2})', format='\\1/\\2 \\3 \\4', leading_digits_pattern=['[3-5]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['[689]'], national_prefix_formatting_rule='0\\1')],
    mobile_number_portable_region=True)
