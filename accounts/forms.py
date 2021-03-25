from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput())
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    age = forms.IntegerField(required=True, widget=forms.NumberInput(),
    help_text='age must be from 18 and above')
    gender = forms.CharField(max_length=6, required=True, widget=forms.TextInput(), help_text='female only')

    class Meta:
        model = User
        fields = ('full_name', 'username', 'email', 'age', 'gender', 'password1', 'password2')
    