from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import AccountType, Account


def filter_account_types(request):
    category_id = request.GET.get("category")
    types = AccountType.objects.filter(category_id=category_id).values("id", "name")
    return JsonResponse(list(types), safe=False)

def list_accounts(request):
    accounts = Account.objects.filter(user=request.user, archived=False)
    return render(request, "accounts/list.html", {"accounts": accounts})