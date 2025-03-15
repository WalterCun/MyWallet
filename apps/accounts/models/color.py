#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""  """
from django.db.models import Model, CharField


class Color(Model):
    name = CharField(max_length=50, unique=True)  # Ej: Rojo, Azul, Verde
    hex_code = CharField(max_length=7, unique=True)  # Ej: #FF0000

    def __str__(self):
        return self.name
