
from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    password.widget.attrs['class']='form-control'
    class Meta:
        model = User
        fields = {'username' , 'email' , 'password'}
        widgets = {
            'username' : forms.TextInput(attrs = {'placeholder': 'Username', 'class':'form-control'}),
            'email'    : forms.TextInput(attrs = {'placeholder': 'E-Mail', 'class':'form-control'}),
            'password' : forms.PasswordInput(attrs = {'placeholder': 'Password', 'class':'form-control'}),
        }


class UserExtra(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = {'profile_pic'}




        


