#8 create this imports

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username' , 'email', 'password1', 'password2']  # 10 go create a html file copying from create_entry code