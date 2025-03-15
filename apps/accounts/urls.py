from django.urls import path
from .views import filter_account_types, list_accounts

urlpatterns = [
    path("", list_accounts, name="list-accounts"),
    path("filter-account-types/", filter_account_types, name="filter-account-types"),
]
