from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# costumising the UserCreationForm form and adding 2 extra value
#first_name and last_name
class CreateUserForm(UserCreationForm):
    first_name  = forms.CharField(max_length = 60)
    last_name   = forms.CharField(max_length = 60)
    class Meta:
        model   = User
        fields  = [
        'username','first_name','last_name','email','password1','password2',
        ]