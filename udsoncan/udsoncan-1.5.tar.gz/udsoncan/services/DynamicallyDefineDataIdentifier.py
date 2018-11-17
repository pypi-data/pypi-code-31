from . import *
from udsoncan.Response import Response
from udsoncan.exceptions import *

class DynamicallyDefineDataIdentifier(BaseService):
	_sid = 0x2C

	supported_negative_response = [	 Response.Code.SubFunctionNotSupported,
							Response.Code.IncorrectMessageLegthOrInvalidFormat,
							Response.Code.ConditionsNotCorrect,
							Response.Code.RequestOutOfRange,
							Response.Code.SecurityAccessDenied
							]

	@classmethod
	def make_request(cls):
		raise NotImplementedError('Service is not implemented')

	@classmethod
	def interpret_response(cls, response):
		raise NotImplementedError('Service is not implemented')

	class ResponseData(BaseResponseData):	
		def __init__(self):
			super().__init__(DynamicallyDefineDataIdentifier)