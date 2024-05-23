from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class Trainer_form(ModelForm):
    class Meta:
        model = Trainer
        fields = "__all__"
        exclude = ["user"]


class PokemonForm(ModelForm):
    class Meta:
        model = Pokemon
        fields = ('num', 'name', 'pokemon_type', 'description', 'evolutions', 'pokemon_pic')

        widgets = {
            'num' : forms.TextInput(attrs={'class': 'form-control'}), 
            'name' : forms.TextInput(attrs={'class': 'form-control'}), 
            'pokemon_type' : forms.SelectMultiple(attrs={'class': 'form-control'}), 
            'description' : forms.Textarea(attrs={'class': 'form-control'}), 
            'evolutions' : forms.Textarea(attrs={'class': 'form-control'}), 
            'pokemon_pic' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }