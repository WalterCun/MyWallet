from django.test import TestCase

# Create your tests here.
from django.urls import path
from .views import add_transaction, list_transactions

urlpatterns = [
    path("", list_transactions, name="list-transactions"),
    path("add/", add_transaction, name="add-transaction"),
]
