from django.shortcuts import render, redirect
from .forms import TransactionForm
from .models import Transaction
from django.contrib import messages

@login_required
def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Transaction added successfully.")
            return redirect("authentication:auth")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = TransactionForm()

    return render(request, "transactions/add_transaction.html", {"form": form})
    
@login_required
def list_transactions(request):
    transactions = Transaction.objects.filter(account__user=request.user)
    return render(request, "transactions/list.html", {"transactions": transactions})