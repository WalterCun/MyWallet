from django.urls import path
from ..views.pages import BlogView

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
]