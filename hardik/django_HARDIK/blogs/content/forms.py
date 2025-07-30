from django import forms
from .models import Author,contents
from django.contrib.auth.models import User

class authorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name","email"]
        widgets = {
            "name" : forms.TextInput(attrs={"required": "true"}),
            "email": forms.EmailInput(attrs={"required": "true"})
        }

class contentForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        empty_label="Select Author",
        queryset=Author.objects.all(),
        widget=forms.Select(attrs={"required": "false"})
    )
    class Meta:
        model = contents
        fields = ['title','content','image','author']
        widgets = {
            "title" : forms.TextInput(attrs={"required": "true","style":"width:60%; resize: vertical;"}),
            "content" : forms.Textarea(attrs={"required": "true"}),
        }

class userForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']
        widget = {
            "username" : forms.TextInput(),
            "email" : forms.EmailInput(),
            "password" : forms.PasswordInput()
        }
        help_texts = {
            "username": None,
        }

class loginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"required": "true"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"required": "true"})
    )
        