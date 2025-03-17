from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Sum
from apps.transactions.models import Transaction
from apps.accounts.models.account import Account

@login_required(login_url="profile/login/")
def dashboard(request):
    # Get user's accounts and their balances
    accounts = Account.objects.filter(user=request.user)
    total_balance = accounts.aggregate(total=Sum('balance'))['total'] or 0

    # Get recent transactions
    recent_transactions = Transaction.objects.filter(
        account__user=request.user
    ).order_by('-created_at')[:5]

    # Calculate income and expenses for the current month
    income = Transaction.objects.filter(
        account__user=request.user,
        transaction_type='income'
    ).aggregate(total=Sum('amount'))['total'] or 0

    expenses = Transaction.objects.filter(
        account__user=request.user,
        transaction_type='expense'
    ).aggregate(total=Sum('amount'))['total'] or 0

    context = {
        'total_balance': total_balance,
        'accounts': accounts,
        'recent_transactions': recent_transactions,
        'total_income': income,
        'total_expenses': expenses,
    }
    return render(request, "dashboard/dashboard.html", context)
