from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from my_app.models import Blog


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=150)
    password2 = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"

