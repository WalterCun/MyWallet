#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""  """
from django.contrib.auth import get_user_model
from django.db.models import Model, DecimalField, ForeignKey, CharField, CASCADE, PROTECT, BooleanField, DateTimeField

from apps.accounts.models.account_category import AccountCategory
from apps.accounts.models.account_type import AccountType
from apps.accounts.models.currency import Currency
from apps.accounts.models.color import Color

User = get_user_model()


class Account(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name="accounts")
    category = ForeignKey(AccountCategory, null=True, on_delete=PROTECT)  # Flujo de la cuenta
    name = CharField(max_length=100)
    account_number = CharField(max_length=50, blank=True, null=True)
    account_type = ForeignKey(AccountType, on_delete=PROTECT)
    initial_balance = DecimalField(max_digits=15, decimal_places=2)
    currency = ForeignKey(Currency, on_delete=PROTECT)
    color = ForeignKey(Color, on_delete=PROTECT)

    exclude_from_stats = BooleanField(default=False)
    archived = BooleanField(default=False)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        category_name = self.category.name if self.category else "No Category"
        return f"{self.name} - {self.currency.code} ({category_name})"
