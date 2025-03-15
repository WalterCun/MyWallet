#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""  """
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from ..profiles.models import User, Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "gender"]

class UserLoginForm(AuthenticationForm):
    pass  # Usa la autenticación de Django por defecto

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar", "phone"]

class PasswordChangeForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("new_password") != cleaned_data.get("confirm_password"):
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data
