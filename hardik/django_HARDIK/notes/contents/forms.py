from django import forms
from django.contrib.auth.models import User

from .models import note


class registerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']
        widget = {
            "username" : forms.TextInput(),
            "email" : forms.EmailInput(),
            "password" : forms.PasswordInput()
        }

        help_texts = {
            "username": None
        }

class loginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget= forms.TextInput(attrs={"required":"true"})
        )
    password = forms.CharField(
        widget= forms.PasswordInput(attrs={"required":"true"})
    )

