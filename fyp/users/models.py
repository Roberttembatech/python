from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=128)

    def __str__(self):
        return self.user.get_full_name()
