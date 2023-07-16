from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from django.contrib.auth.models import User

class CustomValidators():
    def validate_alphanumeric(value):
        valid_characters = list('abcdefghijklmnopqrstuvwxyz')
        valid_characters += list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        valid_characters += list('1234567890')
        
        if not set(value) < set(valid_characters):
            raise ValidationError('You shoud use only alphanumeric characters', code='invalid')
    
    def validate_no_match_username(value):
        if User.objects.filter(username = value).exists():
            raise ValidationError('Username has been already taken', code='invalid')

        

class UserNameField(forms.CharField):
    default_validators = [CustomValidators.validate_alphanumeric, validators.MaxLengthValidator, validators.MinLengthValidator, CustomValidators.validate_no_match_username]

class PassWordField(forms.CharField):
    default_validators = [CustomValidators.validate_alphanumeric, validators.MaxLengthValidator, validators.MinLengthValidator]

class SignUpForm(forms.Form):
    username = UserNameField(label="Username", max_length=32, min_length=6)
    password = PassWordField(label="Password", max_length=32, min_length=6, widget=forms.PasswordInput)
    repeat_password = PassWordField(label="Repeat password", max_length=32, min_length=6, widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')
        
        if password and repeat_password:
            if password != repeat_password:
                error = ValidationError('Passwords do not match')
                self.add_error('repeat_password', error)