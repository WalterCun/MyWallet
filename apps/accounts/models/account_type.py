#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""  """
from django.db.models import Model, CharField, ForeignKey, SET_NULL

from apps.accounts.models.account_category import AccountCategory


class AccountType(Model):
    name = CharField(max_length=50, unique=True)  # Ej: Ahorro, Corriente, Cripto, Bolsa
    category = ForeignKey(
        AccountCategory, on_delete=SET_NULL, null=True, blank=True,
        related_name="account_types"
    )  # Si es NULL, aplica a todas las categorías

    def __str__(self):
        return f"{self.name} ({self.category.name if self.category else 'Todas'})"
