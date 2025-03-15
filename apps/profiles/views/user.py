#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""  """
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from ..forms import UserRegisterForm, UserLoginForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = UserRegisterForm()
    return render(request, "profile/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = UserLoginForm()
    return render(request, "profile/login.html", {"form": form})

@login_required
def user_logout(request):
    logout(request)
    return redirect("home")

