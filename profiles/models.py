from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(User):
    class Meta:
        proxy = True

    def display_name(self):
        return '{}_{}_{}'.format(self.username, self.first_name, self.last_name)
