from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Account, AccountType, AccountCategory, Currency, Color

User = get_user_model()

class AccountModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.category = AccountCategory.objects.create(name='Test Category')
        self.account_type = AccountType.objects.create(name='Test Type')
        self.currency = Currency.objects.create(name='US Dollar', code='USD', symbol='$')
        self.color = Color.objects.create(name='Blue', hex='#0000FF')
        
    def test_account_creation(self):
        account = Account.objects.create(
            user=self.user,
            category=self.category,
            name='Test Account',
            account_type=self.account_type,
            initial_balance=1000.00,
            currency=self.currency,
            color=self.color
        )
        self.assertEqual(account.name, 'Test Account')
        self.assertEqual(account.initial_balance, 1000.00)
        self.assertFalse(account.archived)
