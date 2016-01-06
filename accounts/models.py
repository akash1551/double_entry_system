from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from time import time

# Create your models here.

class Address(models.Model):
	user = models.ForeignKey(User)
	address = models.CharField(max_length=200,null=False)
	city = models.CharField(max_length=50,null=False)
	state = models.CharField(max_length=50,null=False)
	pin_code = models.IntegerField(null=True)
	contact_no = models.IntegerField(null=True)

class Accounts(models.Model):
	accounttype= models.ForeignKey('AccountType')
	debit = models.IntegerField()
	credit = models.IntegerField()
	opening_balance = models.IntegerField()
	trial_balance = models.IntegerField()
	current_balance = models.IntegerField()

class AccountType(models.Model):
	real_account = models.IntegerField()
	personal_account = models.IntegerField()
	nominal_account = models.IntegerField()

class AccountingYear(models.Model):
	start_date = models.DateField()
	end_date = models.DateField()
	company = models.ForeignKey('Company')

class TransactionType(models.Model):
	"""transactiontype = ChoiceField(reciept = models.IntegerField()
									payment = models.IntegerField()
									sale = models.IntegerField()
									contra = models.IntegerField()
									journal = models.IntegerField())"""
	RECIEPT = 0
	PAYMENT = 1
	SALE = 2
	CONTRA = 3
	JOURNAL = 4

	PAYMENTCHOICES = ((RECIEPT, "Reciept"), (PAYMENT, "Payment"), (SALE, 'Sale'), (CONTRA, 'Contra'),(JOURNAL,'Journal'))
	
   	optionType = models.IntegerField(choices=PAYMENTCHOICES)

class Company(models.Model):
	company_name = models.CharField(max_length=100)
