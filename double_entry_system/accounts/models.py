from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from time import time
from datetime import date
from datetime import datetime
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

class UserDetail(models.Model):
	created_at = models.DateTimeField(auto_now_add=True,null=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.TextField()
	user = models.ForeignKey(User,null=True)
	alias = models.CharField(max_length=100)
	address_line1 = models.CharField(max_length=200,null=False)
	address_line2 = models.CharField(max_length=200,null=True)
	contact_no = models.IntegerField(null=True)
	contact_no1 = models.IntegerField(null=True)
	city = models.CharField(max_length=50,null=False)
	state = models.CharField(max_length=50,null=False)
	country = models.CharField(max_length=100,null=False)
	pin_code = models.IntegerField(null=False)
	account = models.ManyToManyField('Account')
	bank_account = models.ForeignKey('Account',related_name='bank_account')
	cash_account = models.ForeignKey('Account',related_name='cash_account')

	def __unicode__(self):
		return self.first_name

class Account(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	account_name = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100,null=True)
	last_name = models.CharField(max_length=100,null=True)
	alias = models.CharField(max_length=100)
	address_line1 = models.CharField(max_length=200,null=False)
	address_line2 = models.CharField(max_length=200,null=True)
	contact_no = models.IntegerField(null=False)
	contact_no1 = models.IntegerField(null=True)
	email = models.TextField()
	city = models.CharField(max_length=50,null=False)
	state = models.CharField(max_length=50,null=False)
	country = models.CharField(max_length=100,null=False)
	pin_code = models.IntegerField(null=False)
	current_balance = models.IntegerField(default=0,null=True)
	opening_balance = models.IntegerField(null=True)
	accounttype= models.ForeignKey('AccountType',null=True)
	group = models.ForeignKey('Group',null=True)

	def __unicode__(self):
		return self.account_name

class Transaction(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	transaction_date = models.DateTimeField()
	transactiontype = models.ForeignKey('TransactionType')
	transaction_record = models.ManyToManyField('TransactionRecord')
	description = models.TextField()
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.description

class TransactionRecord (models.Model):
	amount = models.IntegerField(null=True,default=0)
	is_debit = models.BooleanField() # Debit=True, Credit=False
	account = models.ForeignKey('Account')

class Company(models.Model):
	company_name = models.CharField(max_length=100)
	company_account = models.ForeignKey('Account',null=True)

	def __unicode__(self):
		return self.company_name

class AccountingYear(models.Model):
	created_at = models.DateTimeField(auto_now_add=True,null=True)
	user = models.ForeignKey(User,null=True)
	start_date = models.DateField(null=True)
	end_date = models.DateField(null=True)
	duration = models.IntegerField()
	transaction = models.ManyToManyField('Transaction')

	def __unicode__(self):
		return str(self.user.username)
class AccountType(models.Model):
	created_at = models.DateTimeField(auto_now_add=True,null=True)

	REAL_ACCOUNT = 0
	PERSONAL_ACCOUNT = 1
	NOMINAL_ACCOUNT = 2

	ACCOUNTCHOICES = ((REAL_ACCOUNT,"Real Account"),(PERSONAL_ACCOUNT,"Personal Account"),(NOMINAL_ACCOUNT,"Nominal Account"))
	optionType = models.IntegerField(choices=ACCOUNTCHOICES)

	def __unicode__(self):
		return str(self.optionType)


class TransactionType(models.Model):
	RECIEPT = 0
	PAYMENT = 1
	SALE = 2
	CONTRA = 3
	JOURNAL = 4
	PURCHASE = 5
	DEBIT_NOTE = 6
	CREDIT_NOTE = 7
	MEMO = 8

	PAYMENTCHOICES = ((RECIEPT, "Reciept"), (PAYMENT, "Payment"), (SALE, 'Sale'), (CONTRA, 'Contra'),(JOURNAL,'Journal'),
	(PURCHASE,"Purchase"),(DEBIT_NOTE,"Debit Note"),(CREDIT_NOTE,"Crdit Note"),(MEMO,"Memo"))
	
   	optionType = models.IntegerField(choices=PAYMENTCHOICES)

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

	optionType=models.IntegerField(choices=ACCOUNTCHOICES,null=True)

	group_name = models.CharField(max_length=50,null=True)