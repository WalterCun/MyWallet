from django.db.models import (
    Model,
    ForeignKey,
    CASCADE,
    DecimalField,
    CharField,
    TextField,
    DateTimeField,
)
from apps.accounts.models.account import Account

class Transaction(Model):
    TRANSACTION_TYPES = [
        ("income", "Ingreso"),
        ("expense", "Gasto"),
        ("transfer", "Transferencia"),
    ]

    account = ForeignKey(Account, on_delete=CASCADE, related_name="transactions")
    amount = DecimalField(max_digits=15, decimal_places=2)
    transaction_type = CharField(max_length=10, choices=TRANSACTION_TYPES)
    description = TextField(blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_transaction_type_display()} - {self.amount} ({self.account.name})"
