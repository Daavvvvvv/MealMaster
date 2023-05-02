from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class idForm(forms.Form):
    idDieta = forms.CharField(label='De que dieta desea ver las comidas', max_length=100,empty_value="hola")
    

class CustomUserCreationForm(UserCreationForm):
    pass