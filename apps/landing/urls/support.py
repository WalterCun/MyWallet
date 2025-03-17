from django.urls import path
from ..views.support import SupportView

urlpatterns = [
    path('', SupportView.as_view(), name='support'),
]