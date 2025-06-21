from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User 
import re

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match(r'^\+?\d{10,15}$', username):
            raise forms.ValidationError('Введите корректный номер телефона.')
        return username    


    