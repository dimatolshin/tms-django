from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django import forms

User = get_user_model()


# TODO use ModelForm
class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    email = forms.EmailField(label='Email', max_length=100)
    first_name = forms.CharField(label='First_name', max_length=20)
    last_name = forms.CharField(label='Last_name', max_length=20)


# class UserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username","first_name",'last_name', "email", "password1", "password2",)

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['email']
        user.email = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        if commit:
            user.save()
        return user
