from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from .validators import validate_email_syntax


class EmailBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        if validate_email_syntax(username):
            user_model = get_user_model()
            try:
                user_model = user_model.objects.get(email=username)
            except user_model.DoesNotExist:
                return None
            else:
                if user_model.check_password(password):
                    return user_model
        return None
