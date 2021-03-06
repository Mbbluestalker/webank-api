from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin



class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """creates and saves a new user"""
        if not email:
            raise ValueError("User must have an Email")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """creates and saves a new superuser"""
        if password is None:
            raise TypeError("Password should not been None")
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    username = models.CharField(max_length=255, null=True, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    otp = models.CharField(max_length=10, null=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.username)

ACCOUNT_TYPE = (
    ('SAVINGS', 'savings'),
    ('CURRENT', "current"),
)


class Accounts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='user', related_name='account')
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    account_no = models.IntegerField(unique=True)
    account_type = models.CharField(max_length=40, choices=ACCOUNT_TYPE)
    account_balance = models.FloatField(default=[0])
    
    def __str__(self):
        return str(self.account_no)


DEPOSIT = 'Deposit'
WITHDRAWAL = 'Withdrawal'

TRANSACTION_TYPE_CHOICES = (
    (DEPOSIT, 'Deposit'),
    (WITHDRAWAL, 'Withdrawal'),
)

class Transaction(models.Model):
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE, default='1234567890', related_name='transaction')
    amount = models.DecimalField(decimal_places=2,max_digits=12)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    transaction_type = models.CharField(max_length= 20, choices=TRANSACTION_TYPE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.transaction_type)

    class Meta:
        ordering = ['timestamp']

class Report(models.Model):
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    report_name = models.CharField(max_length=50)
    report_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.report_name)
