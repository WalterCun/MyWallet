#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""  """
from django.db.models import Model
from django.db.models.fields import CharField


class AssetType(Model):
    name = CharField(max_length=50, unique=True)  # Ej: Acciones, Criptomonedas, Fondos Mutuos

    def __str__(self):
        return self.name
