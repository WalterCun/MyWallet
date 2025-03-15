#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""  """
from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=10, unique=True)  # Ej: USD, EUR, BTC
    symbol = models.CharField(max_length=5)  # Ej: $, €, ฿

    def __str__(self):
        return f"{self.name} ({self.code})"
