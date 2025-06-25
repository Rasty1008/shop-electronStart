import re
from django import forms


class PhoneValidationMixin:
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match(r'^\+?\d{10,15}$', username):
            raise forms.ValidationError('Введите корректный номер телефона.')
        return username