"""Auto-generated file, do not edit by hand. CX metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CX = PhoneMetadata(id='CX', country_code=61, international_prefix='001[14-689]|14(?:1[14]|34|4[17]|[56]6|7[47]|88)0011',
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{5,9}|(?:[48]\\d\\d|550)\\d{6}', possible_length=(6, 7, 8, 9, 10), possible_length_local_only=(8,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='8(?:51(?:0(?:01|30|59)|117)|91(?:00[6-9]|1(?:[28]1|49|78)|2(?:09|63)|3(?:12|26|75)|4(?:56|97)|64\\d|7(?:0[01]|1[0-2])|958))\\d{3}', example_number='891641234', possible_length=(9,), possible_length_local_only=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='4(?:[0-3]\\d|4[047-9]|5[0-25-9]|6[6-9]|7[02-9]|8[0-2457-9]|9[017-9])\\d{6}', example_number='412345678', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='180(?:0\\d{3}|2)\\d{3}', example_number='1800123456', possible_length=(7, 10)),
    premium_rate=PhoneNumberDesc(national_number_pattern='190[0-26]\\d{6}', example_number='1900123456', possible_length=(10,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='13(?:00\\d{3}|45[0-4])\\d{3}|13\\d{4}', example_number='1300123456', possible_length=(6, 8, 10)),
    voip=PhoneNumberDesc(national_number_pattern='(?:14(?:5\\d|71)|550\\d)\\d{5}', example_number='550123456', possible_length=(9,)),
    preferred_international_prefix='0011',
    national_prefix='0',
    national_prefix_for_parsing='0')
