from django.db import models

class Bank(models.Model):
    bank_name = models.CharField(max_length=100)
    date_created = models.DateField(name="Creation Date",auto_now_add=True)
    bank_ID = models.AutoField(primary_key=True)

class Account(models.Model):
    account_number = models.CharField(max_length=20)
    bank_ID = models.ForeignKey(Bank)
    bank_ID.db_column = "bank_ID"
    account_ID = models.AutoField(primary_key=True)

class ExpenseType(models.Model):
    expense_ID = models.AutoField(primary_key=True)
    expense_description = models.CharField(max_length=50)
    date_created = models.DateField(name="Creation Date",auto_now_add=True)

class IncomeType(models.Model):
    income_ID = models.AutoField(primary_key=True)
    income_description = models.CharField(max_length=50)
    date_created = models.DateField(name="Creation Date",auto_now_add=True)

class Currency(models.Model):
    currency_ID = models.AutoField(primary_key=True)
    currency_abv = models.CharField(max_length=10)
    currency_description = models.CharField(max_length=60)
    date_created = models.DateField(name="Creation Date",auto_now_add=True)

class AccountBalance(models.Model):
    account_ID = models.ForeignKey(Account)
    account_ID.db_column = "account_ID"
    expense_ID = models.ForeignKey(ExpenseType)
    expense_ID.db_column = "expense_ID"
    income_ID = models.ForeignKey(IncomeType)
    income_ID.db_column = "income_ID"
    currency_ID = models.ForeignKey(Currency)
    currency_ID.db_column = "currency_ID"
    balance_ID = models.AutoField(primary_key=True)
    balance_value = models.DecimalField(max_digits=18, decimal_places=2)
    date_transaction = models.DateField(name="Date of Transaction", auto_now_add=True)

