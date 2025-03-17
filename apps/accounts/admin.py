from django.contrib import admin
from .models import Account, AccountCategory, AccountType, Currency, Color

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'account_type', 'initial_balance', 'currency', 'archived')
    list_filter = ('account_type', 'currency', 'archived')
    search_fields = ('name', 'account_number')

admin.site.register(AccountCategory)
admin.site.register(AccountType)
admin.site.register(Currency)
admin.site.register(Color)
