from django.contrib.auth.models import UserManager as orig

class UserManager(orig):

  def filter(self, *args, **kwargs):
    pass
