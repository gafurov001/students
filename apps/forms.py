from django import forms
from django.contrib.auth.forms import BaseUserCreationForm
from django.contrib.auth.hashers import make_password
from django.forms import ModelForm, CharField

from apps.models import User


class CreateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'phone_number', 'user_id', 'group', 'date_of_birth', 'gender', 'image',
                  "type", 'username', 'email', 'password']

    def clean_password(self):
        return make_password(self.cleaned_data.get('password'))


class CustomCreateUserForm(ModelForm):
    confirm_password = CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            return ''
        return make_password(password)

    # def is_valid(self):
    #     return super().is_valid()
    #
    # def form_invalid(self):
    #     return ''
