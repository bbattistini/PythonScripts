# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_number', models.CharField(max_length=20)),
                ('account_ID', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccountBalance',
            fields=[
                ('balance_ID', models.AutoField(serialize=False, primary_key=True)),
                ('balance_value', models.DecimalField(max_digits=18, decimal_places=2)),
                ('Date of Transaction', models.DateField(auto_now_add=True)),
                ('account_ID', models.ForeignKey(to='keitaroFinances.Account', db_column=b'account_ID')),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('bank_name', models.CharField(max_length=100)),
                ('Creation Date', models.DateField(auto_now_add=True)),
                ('bank_ID', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('currency_ID', models.AutoField(serialize=False, primary_key=True)),
                ('currency_abv', models.CharField(max_length=10)),
                ('currency_description', models.CharField(max_length=60)),
                ('Creation Date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseType',
            fields=[
                ('expense_ID', models.AutoField(serialize=False, primary_key=True)),
                ('expense_description', models.CharField(max_length=50)),
                ('Creation Date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='IncomeType',
            fields=[
                ('income_ID', models.AutoField(serialize=False, primary_key=True)),
                ('income_description', models.CharField(max_length=50)),
                ('Creation Date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='currency_ID',
            field=models.ForeignKey(to='keitaroFinances.Currency', db_column=b'currency_ID'),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='expense_ID',
            field=models.ForeignKey(to='keitaroFinances.ExpenseType', db_column=b'expense_ID'),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='income_ID',
            field=models.ForeignKey(to='keitaroFinances.IncomeType', db_column=b'income_ID'),
        ),
        migrations.AddField(
            model_name='account',
            name='bank_ID',
            field=models.ForeignKey(to='keitaroFinances.Bank', db_column=b'bank_ID'),
        ),
    ]
