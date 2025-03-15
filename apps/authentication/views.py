from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

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
