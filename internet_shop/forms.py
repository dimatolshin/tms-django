from django import forms
from django.contrib.auth.models import User


class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    email = forms.EmailField(label='Email', max_length=100)
    first_name = forms.CharField(label='First_name', max_length=20)
    last_name = forms.CharField(label='Last_name', max_length=20)
