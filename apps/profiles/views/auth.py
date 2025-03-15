#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""  """
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def deactivate_account(request):
    """Desactiva la cuenta del usuario sin eliminarla"""
    request.user.profile.is_active = False
    request.user.profile.save()
    messages.success(request, "Tu cuenta ha sido desactivada.")
    return redirect("dashboard")

@login_required
def delete_account(request):
    """Marca la cuenta como eliminada en lugar de borrarla físicamente"""
    request.user.is_deleted = True
    request.user.save()
    messages.success(request, "Tu cuenta ha sido eliminada.")
    return redirect("home")

def auth_view(request):
    """
    Vista unificada para Login y Registro.
    """
    login_form = AuthenticationForm()
    register_form = UserCreationForm()

    if request.method == "POST":
        # ¿Vino del botón de login o de registro?
        if "login_submit" in request.POST:
            login_form = AuthenticationForm(data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                if user:
                    login(request, user)
                    return redirect("home")  # O a donde quieras redirigir
                else:
                    messages.error(request, "Credenciales inválidas.")
        elif "register_submit" in request.POST:
            register_form = UserCreationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                # Autenticar y loguear automáticamente
                username = register_form.cleaned_data.get("username")
                password = register_form.cleaned_data.get("password1")
                user_auth = authenticate(username=username, password=password)
                if user_auth:
                    login(request, user_auth)
                    return redirect("home")
                else:
                    messages.warning(request, "Registro exitoso, pero no se pudo iniciar sesión.")

    context = {
        "login_form": login_form,
        "register_form": register_form,
    }
    return render(request, "auth/flip_auth.html", context)