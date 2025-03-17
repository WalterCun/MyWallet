from django.urls import path
from ..views.pages import SuggestionsView

urlpatterns = [
    path('', SuggestionsView.as_view(), name='suggestions'),
]