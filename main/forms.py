from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class preguntas(forms.Form):
    pregunta = forms.CharField(label = "Tu Pregunta",max_length=300)

class CustomUserCreationForm(UserCreationForm):
    pass