from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm '
                                                                                                          'Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {

            'username': forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
        }


