#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""  """

from django.urls import path
from ..views.index import LandingView

app_name = "landing"
urlpatterns = [
    path("", LandingView.as_view(), name="landing"),
]