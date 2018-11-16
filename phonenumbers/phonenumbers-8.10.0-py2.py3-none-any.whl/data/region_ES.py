"""Auto-generated file, do not edit by hand. ES metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ES = PhoneMetadata(id='ES', country_code=34, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:51|[6-9]\\d)\\d{7}', possible_length=(9,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:8(?:[1356]\\d|[28][0-8]|[47][1-9])\\d{4}|9(?:(?:(?:[135]\\d|[28][0-8]|4[1-9])\\d\\d|7(?:[124-9]\\d\\d|3(?:[0-8]\\d|9[1-9])))\\d\\d|6(?:[0-8]\\d{4}|9(?:0(?:[0-57-9]\\d\\d|6(?:0[0-8]|1[1-9]|[2-9]\\d))|[1-9]\\d{3}))))\\d\\d', example_number='810123456', possible_length=(9,)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:(?:6\\d|7[1-48])\\d{5}|9(?:6906(?:09|10)|7390\\d\\d))\\d\\d', example_number='612345678', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='[89]00\\d{6}', example_number='800123456', possible_length=(9,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='80[367]\\d{6}', example_number='803123456', possible_length=(9,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='90[12]\\d{6}', example_number='901123456', possible_length=(9,)),
    personal_number=PhoneNumberDesc(national_number_pattern='70\\d{7}', example_number='701234567', possible_length=(9,)),
    uan=PhoneNumberDesc(national_number_pattern='51\\d{7}', example_number='511234567', possible_length=(9,)),
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['[89]00']),
        NumberFormat(pattern='(\\d{3})(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['[568]|7[0-48]|9(?:0[12]|[1-8])'])],
    mobile_number_portable_region=True)
