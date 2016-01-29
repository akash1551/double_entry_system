# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-28 11:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AccountingYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('optionType', models.IntegerField(choices=[(0, 'Real Account'), (1, 'Personal Account'), (2, 'Nominal Account')])),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DebtorAndCreditor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('debtor_name', models.CharField(max_length=100, null=True)),
                ('creditor_name', models.CharField(max_length=100, null=True)),
                ('debit_amount', models.IntegerField(null=True)),
                ('credit_amount', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optionType', models.IntegerField(choices=[(0, 'Bank Account'), (1, 'Bank OCC A/C'), (2, 'Branch/Division'), (3, 'Capital Account'), (4, 'Cash in Hand'), (5, 'Current Assets'), (6, 'Current Liabilities'), (7, 'Deposites (Assets)'), (8, 'Direct Expense'), (9, 'Direct Income'), (10, 'Duty & Tax'), (11, 'Expense (Direct)'), (12, 'Expense (Indirect'), (13, 'fixed Assets'), (14, 'Income (Direct)'), (15, 'Income (Indirect)'), (16, 'Indirect Expense'), (17, 'Indirect Income'), (18, 'Investments'), (19, 'Loan & Advance Assets'), (20, 'Loan Liability'), (21, 'Misc.Expense Assets'), (22, 'Provision'), (23, 'Purchase Account'), (24, 'Reserve & Surplus'), (25, 'Retained Earning'), (26, 'Sales Accounts'), (27, 'Secured Loans'), (28, 'Stock in Hand')])),
            ],
        ),
        migrations.CreateModel(
            name='SelfMadeAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('opening_balance', models.IntegerField()),
                ('account_name', models.CharField(max_length=100)),
                ('account', models.ManyToManyField(related_name='DebtorAndCreditor_account', to='accounts.DebtorAndCreditor')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optionType', models.IntegerField(choices=[(0, 'Reciept'), (1, 'Payment'), (2, 'Sale'), (3, 'Contra'), (4, 'Journal'), (5, 'Purchase'), (6, 'Debit Note'), (7, 'Crdit Note'), (8, 'Memo')])),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('my_bank_account', models.IntegerField(default=0)),
                ('my_cash_account', models.IntegerField(default=0)),
                ('alias', models.CharField(max_length=100)),
                ('address_line1', models.CharField(max_length=200)),
                ('address_line2', models.CharField(max_length=200, null=True)),
                ('contact_no', models.IntegerField()),
                ('contact_no1', models.IntegerField(null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=100)),
                ('pin_code', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='accountingyear',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Company'),
        ),
        migrations.AddField(
            model_name='accountingyear',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='account',
            name='account',
            field=models.ManyToManyField(to='accounts.DebtorAndCreditor'),
        ),
        migrations.AddField(
            model_name='account',
            name='accounttype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.AccountType'),
        ),
        migrations.AddField(
            model_name='account',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Group'),
        ),
    ]
