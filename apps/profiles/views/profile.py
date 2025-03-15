#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""  """
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages

from ..forms import ProfileUpdateForm, PasswordChangeForm


@login_required
def update_profile(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, "profile/update.html", {"form": form})


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            user = request.user
            if user.check_password(form.cleaned_data["current_password"]):
                user.set_password(form.cleaned_data["new_password"])
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Contraseña cambiada correctamente.")
                return redirect("profile")
            else:
                messages.error(request, "Contraseña actual incorrecta.")
    else:
        form = PasswordChangeForm()
    return render(request, "profile/change_password.html", {"form": form})
