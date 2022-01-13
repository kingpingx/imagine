from distutils.command.upload import upload
from typing_extensions import Required
from unicodedata import name
from django import forms
from django.forms import ModelForm
from .models import *
from django.utils.safestring import mark_safe

CHOICES= [
    ('male', 'Male'),
    ('female', 'Female'),
    ('rather not to say', 'Rather not to say'),
    ]

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 100%; margin-bottom: 10px; font-family: Roboto; font-size: 20px;'}))
    password = forms.CharField(label='Password',max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 100%; margin-bottom: 10px; font-family: Roboto; font-size: 20px'}))

class RegisterForm(forms.Form):
    firstname = forms.CharField(label='Firstname', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'width: 100%; margin-bottom: 10px;'}))
    lastname = forms.CharField(label='Lastname', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'width: 100%; margin-bottom: 10px;'}))
    email = forms.CharField(label='Email', max_length=30, widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width: 100%; margin-bottom: 10px;'}))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'placeholder': 'Address', 'style': 'width: 100%; margin-bottom: 10px;'}))
    ph_number = forms.IntegerField(label='Contact Number',widget=forms.TextInput(attrs={'placeholder': 'Contact number', 'style': 'width: 100%; margin-bottom: 10px;'}))
    username = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 100%; margin-bottom: 10px;'}))
    password = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 100%; margin-bottom: 10px;'}))
    cnfpassword = forms.CharField(label='Cnfpassword', max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'style': 'width: 100%; margin-bottom: 10px;'}))
    gender = forms.CharField( max_length=20, required=False)

class ProfileForm(forms.Form):
# class ProfileForm(ModelForm):
    # class Meta:
    #     model = User_profile
    #     fields = ['first_name', 'last_name', 'address', 'ph_number', 'gender', 'image']
    firstname = forms.CharField(label='Firstname', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'width: 100%; margin-bottom: 10px;'}), required=False)
    lastname = forms.CharField(label='Lastname', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'width: 100%; margin-bottom: 10px;'}), required=False)
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'placeholder': 'Address', 'style': 'width: 100%; margin-bottom: 10px;'}), required=False)
    ph_number = forms.IntegerField(label='Contact Number',widget=forms.TextInput(attrs={'placeholder': 'Contact number', 'style': 'width: 100%; margin-bottom: 10px;'}), required=False)
    gender = forms.CharField(label='Gender', widget=forms.Select(choices=CHOICES))
    img = forms.FileField(required = False)