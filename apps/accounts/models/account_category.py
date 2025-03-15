#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""  """
from django.db.models.base import Model
from django.db.models.fields import CharField


class AccountCategory(Model):
    name = CharField(max_length=50, unique=True)  # Ej: Bancaria, Inversión, Importada, Manual

    def __str__(self):
        return self.name
