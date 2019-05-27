from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import UserProfile

class UserRegisterForm(UserCreationForm):
    qualification=forms.CharField()

    class Meta:
        model=User
        fields = [ 'username', 'password1', 'password2', 'first_name','last_name', 'email', 'qualification', ]
