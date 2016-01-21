from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from time import time
from datetime import date
from datetime import datetime

# Create your models here.

class UserDetail(models.Model):
	my_bank_account = models.IntegerField(default=0)
	my_cash_account = models.IntegerField(default=0)
	user = models.ForeignKey(User)
	alias = models.CharField(max_length=100)
	address_line1 = models.CharField(max_length=200,null=False)
	address_line2 = models.CharField(max_length=200,null=True)
	contact_no = models.IntegerField(null=False)
	contact_no1 = models.IntegerField(null=True)
	city = models.CharField(max_length=50,null=False)
	state = models.CharField(max_length=50,null=False)
	country = models.CharField(max_length=100,null=False)
	pin_code = models.IntegerField(null=False)

class Account(models.Model):
	accounttype= models.ForeignKey('AccountType')
	group = models.ForeignKey('Group')

class AccountType(models.Model):
	real_account = models.IntegerField(default=0)
	personal_account = models.IntegerField(default=0)
	nominal_account = models.IntegerField(default=0)

class AccountingYear(models.Model):
	user = models.ForeignKey(User)
	start_date = models.DateField()
	end_date = models.DateField()
	company = models.ForeignKey('Company',null=True)
	duration = models.IntegerField()

class SelfMadeAccount(models.Model):
	account_name = models.CharField(max_length=100)
	opening_balance = models.IntegerField()

class TransactionType(models.Model):
	RECIEPT = 0
	PAYMENT = 1
	SALE = 2
	CONTRA = 3
	JOURNAL = 4

	PAYMENTCHOICES = ((RECIEPT, "Reciept"), (PAYMENT, "Payment"), (SALE, 'Sale'), (CONTRA, 'Contra'),(JOURNAL,'Journal'))
	
   	optionType = models.IntegerField(choices=PAYMENTCHOICES)

class Company(models.Model):
	company_name = models.CharField(max_length=100)

class Group(models.Model):
	BANK_ACCOUNT = 0
	BANK_OCC_AC = 1
	BRANCH_OR_DIVISION = 2
	CAPITAL_ACCOUNT = 3
	CASH_IN_HAND = 4
	CURRENT_ASSETS = 5
	CURRENT_LIABILITY = 6
	DEPOSITES_ASSETS = 7 
	DIRECT_EXPENSE = 8
	DIRECT_INCOME = 9
	DUTY_AND_TAX = 10
	EXPENSE_DIRECT = 11
	EXPENSE_INDIRECT = 12
	FIXED_ASSETS = 13
	INCOME_DIRECT = 14
	INCOME_INDIRECT = 15 
	INDIRECT_EXPENSE = 16
	INDIRECT_INCOME = 17
	INVESTMENT = 18
	LOAN_AND_ADVANCE_ASSETS = 19
	LOAN_LIABILITY = 20
	MISC_EXPENSE_ASSETS = 21
	PROVISION = 22
	PURCAHSE_ACCOUNT = 23
	RESERVE_AND_SURPLUS = 24
	RETAINED_EARNING = 25
	SALES_ACCOUNTS = 26
	SECURED_LOANS = 27
	STOCK_IN_HAND = 28


	ACCOUNTCHOICES = ((BANK_ACCOUNT, "Bank Account"),(BANK_OCC_AC, "Bank OCC A/C"),(BRANCH_OR_DIVISION, "Branch/Division"), 
		(CAPITAL_ACCOUNT, "Capital Account"),(CASH_IN_HAND,"Cash in Hand"),(CURRENT_ASSETS,"Current Assets"),(CURRENT_LIABILITY,"Current Liabilities"),
		(DEPOSITES_ASSETS,"Deposites (Assets)"),(DIRECT_EXPENSE,"Direct Expense"),(DIRECT_INCOME,"Direct Income"),
		(DUTY_AND_TAX,"Duty & Tax"),(EXPENSE_DIRECT,"Expense (Direct)"),(EXPENSE_INDIRECT,"Expense (Indirect"),
		(FIXED_ASSETS,"fixed Assets"),(INCOME_DIRECT,"Income (Direct)"),(INCOME_INDIRECT,"Income (Indirect)"),
		(INDIRECT_EXPENSE,"Indirect Expense"),(INDIRECT_INCOME,"Indirect Income"),(INVESTMENT,"Investments"),
		(LOAN_AND_ADVANCE_ASSETS,"Loan & Advance Assets"),(LOAN_LIABILITY,"Loan Liability"),(MISC_EXPENSE_ASSETS,"Misc.Expense Assets"),
		(PROVISION,"Provision"),(PURCAHSE_ACCOUNT,"Purchase Account"),(RESERVE_AND_SURPLUS,"Reserve & Surplus"),
		(RETAINED_EARNING,"Retained Earning"),(SALES_ACCOUNTS,"Sales Accounts"),(SECURED_LOANS,"Secured Loans"),
		(STOCK_IN_HAND,"Stock in Hand"))

	optionType=models.IntegerField(choices=ACCOUNTCHOICES)