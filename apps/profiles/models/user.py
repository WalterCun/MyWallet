#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""User model extending Django's AbstractUser with additional fields for the MyWallet application."""
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    GENDER_CHOICES = [
        ("M", "Masculino"),
        ("F", "Femenino"),
    ]

    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)  # Indica si el usuario ha solicitado la eliminación

    # Agregar related_name personalizado para evitar conflictos
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Nombre único
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Nombre único
        blank=True
    )

    def __str__(self):
        return self.username
