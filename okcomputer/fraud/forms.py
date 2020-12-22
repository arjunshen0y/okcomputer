from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo,Transaction

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = {'username' , 'email' , 'password'}
        widgets = {
            'username' : forms.TextInput(attrs = {'placeholder': 'Username'}),
            'email'    : forms.TextInput(attrs = {'placeholder': 'E-Mail'}),
            'password' : forms.PasswordInput(attrs = {'placeholder': 'Password'}),
        }


class UserExtra(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = {'profile_pic'}
        

'''
class Transaction_Details(forms.ModelForm):
    class Meta():
        model = Transaction
<<<<<<< Updated upstream
        exclude = ['cat']'''
=======
        exclude = ['cat']
>>>>>>> Stashed changes
    