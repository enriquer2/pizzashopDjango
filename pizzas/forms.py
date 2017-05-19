# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import ModelForm
from pizzas.models import Pizza, Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from profiles.models import User


class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'score')

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=254, required=True, help_text='Required.')
    name = forms.CharField(max_length=100, required=True, help_text='Required.')
    phone = forms.CharField(max_length=30, required=False, help_text='Optional.')
    city = forms.CharField(max_length=100, required=False, help_text='Optional.')
    birthday = forms.DateField(required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'name', 'phone', 'city','birthday', 'email', 'password1', 'password2' )
