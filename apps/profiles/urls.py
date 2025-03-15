#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""  """
from django.urls import path
from .views import register, user_login, user_logout, update_profile, change_password

urlpatterns = [
    # path("register/", register, name="register"),
    # path("login/", user_login, name="login"),
    # path("logout/", user_logout, name="logout"),
    path("profile/", update_profile, name="profile"),
    # path("change-password/", change_password, name="change_password"),
]
