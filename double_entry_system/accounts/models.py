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

class Account(models.Model):
	account_name = models.CharField(max_length=100)
	accounttype= models.ForeignKey('AccountType')
	group = models.ForeignKey('Group')
	contact_no = models.IntegerField(null=True)

class AccountType(models.Model):
	real_account = models.IntegerField()
	personal_account = models.IntegerField()
	nominal_account = models.IntegerField()

class AccountingYear(models.Model):
	start_date = models.DateField()
	end_date = models.DateField()
	company = models.ForeignKey('Company')

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
	machine = models.CharField(max_length=100)