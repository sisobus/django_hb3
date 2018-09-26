from django.apps import AppConfig
from django.contrib.auth import get_user_model 


class AuthorizationConfig(AppConfig):
	name = 'authorization'

	def ready(self):
		def get_absolute_url(self):
			return "/accounts/{}".format(self.id)
		UserModel = get_user_model()
		UserModel.add_to_class('get_absolute_url', get_absolute_url)
