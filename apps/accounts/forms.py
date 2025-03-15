#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""  """
from django import forms
from .models import Account, AccountType

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["category", "account_type", "name", "account_number", "initial_balance", "currency", "color"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "category" in self.data:
            try:
                category_id = int(self.data.get("category"))
                self.fields["account_type"].queryset = AccountType.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass  # No se seleccionó categoría todavía
        else:
            self.fields["account_type"].queryset = AccountType.objects.none()
