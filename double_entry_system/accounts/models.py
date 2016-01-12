from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from time import time

# Create your models here.

class Address(models.Model):
	user = models.ForeignKey(User)
	address_line1 = models.CharField(max_length=200,null=False)
	address_line2 = models.CharField(max_length=200,null=True)
	contact_no = models.IntegerField(null=False)
	city = models.CharField(max_length=50,null=False)
	state = models.CharField(max_length=50,null=False)
	country = models.CharField(max_length=100,null=False)
	pin_code = models.IntegerField(null=False)

class Account(models.Model):
	accounttype= models.ForeignKey('AccountType')
	group = models.ForeignKey('Group')

class AccountType(models.Model):
	account_name = models.CharField(max_length=100)

class AccountingYear(models.Model):
	start_date = models.DateField()
	end_date = models.DateField()
	company = models.ForeignKey('Company',null=True)
	duration = models.IntegerField()

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
	name_of_group = models.CharField(max_length=100)