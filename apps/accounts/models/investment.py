#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""  """
from django.db import models

from apps.accounts.models.account import Account
from apps.accounts.models.asset_type import AssetType


class Investment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="investments")
    asset_type = models.ForeignKey(AssetType, on_delete=models.PROTECT)
    asset_name = models.CharField(max_length=100)  # Ej: Bitcoin, Tesla, ETF Vanguard
    quantity = models.DecimalField(max_digits=15, decimal_places=8)
    purchase_price = models.DecimalField(max_digits=15, decimal_places=2)
    purchase_date = models.DateField()
    current_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)  # Se puede actualizar

    def __str__(self):
        return f"{self.asset_name} - {self.quantity} ({self.account.currency.code})"
