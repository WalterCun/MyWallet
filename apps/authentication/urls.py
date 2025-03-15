#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""  """
from django.urls import path
from .views import auth_view

app_name = "authentication"

urlpatterns = [
    path("", auth_view, name="auth"),  # /auth/
]
