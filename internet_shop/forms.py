from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms

from internet_shop.models import Profile

User = get_user_model()


# TODO use ModelForm
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", 'last_name', "email")





class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", 'last_name', "email", "password1", "password2",)

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()
        Profile.objects.create(user=user)
        if commit:
            user.save()
        return user
