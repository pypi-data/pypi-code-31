from django.conf import settings
import django
if django.VERSION >= (1, 10):
	from django.utils.deprecation import MiddlewareMixin as BaseMiddleware
else:
	BaseMiddleware = object

SKINS = ('skin-blue', 'skin-black', 'skin-red', 'skin-yellow', 'skin-purple', 'skin-green', 'skin-blue-light',
		 'skin-black-light', 'skin-red-light', 'skin-yellow-light', 'skin-purple-light', 'skin-green-light')


class ClassicUserAccountsMiddleWare(BaseMiddleware):
	def process_request(self, request):
		try:
			if hasattr(settings, 'SITE_NAME'):
				request.site_name = settings.SITE_NAME
			if request.user.is_authenticated and hasattr(settings, 'ROLE_BASED_SKIN'):
				my_skin = ''
				skins = settings.ROLE_BASED_SKIN
				for skin in skins:
					roles = request.user.groups.filter(name=skin["role"]).first()
					if roles:
						my_skin = skin["skin_name"]
						break
				print(my_skin)
				request.skin = my_skin

		except:
			request.site_name = ''
