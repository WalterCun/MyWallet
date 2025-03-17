#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""  """

from django.urls import path, include
from ..views.index import LandingView

app_name = "landing"
urlpatterns = [
    path("", LandingView.as_view(), name="landing"),
    path("blog/", include("apps.landing.urls.blog")),
    path("roadmap/", include("apps.landing.urls.roadmap")),
    path("suggestions/", include("apps.landing.urls.suggestions")),
    path("support/", include("apps.landing.urls.support")),
]