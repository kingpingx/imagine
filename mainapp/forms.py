from django import forms
from django.utils.safestring import mark_safe


class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'max-width: 300px;',}))
    password = forms.CharField(label='Password',max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'max-width: 300px;'}))

class RegisterForm(forms.Form):
    firstname = forms.CharField(label='Firstname', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lastname = forms.CharField(label='Lastname', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.CharField(label='Email', max_length=30, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    ph_number = forms.IntegerField(label='Contact Number',widget=forms.TextInput(attrs={'placeholder': 'Contact number'}))
    username = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    cnfpassword = forms.CharField(label='Cnfpassword', max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    gender = forms.CharField( max_length=20, required=False)