from django.shortcuts import render, redirect
from .forms import TransactionForm
from .models import Transaction


def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard:home")  # Redirigir a donde se necesite
    else:
        form = TransactionForm()

    return render(request, "transactions/add_transaction.html", {"form": form})

def list_transactions(request):
    transactions = Transaction.objects.filter(account__user=request.user)
    return render(request, "transactions/list.html", {"transactions": transactions})