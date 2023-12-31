from django.forms import ModelForm
from .models import Task

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput, TextInput




class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'email', 'password1', 'password2']



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))


    