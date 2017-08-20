from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class LoginBackend(ModelBackend):
	def authenticate(self, username=None, password=None, **kwargs):
		try:
			if "@" not in username:
				user=User.objects.get(username=username)
			else:
				user=User.objects.get(email=username)
		except user.DoesNotExist:
			return None
		else:
			if getattr(user, 'is_active', False) and user.check_password(password):
				return user
		return None