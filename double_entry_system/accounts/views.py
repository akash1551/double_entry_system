
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from books.models import Books
from books.forms import BookForm
import json
from django.core.context_processors import csrf
from django.contrib import admin	
from django.contrib.auth.models import User

# Create your views here.

def create_account(request):
	print request.body
	json_obj = json.loads(request.body)
	account_name = json_obj['account_name']
	accounttype = json_obj['accounttype']
	group_name = json_obj['group_name']
	contact_no = json_obj['contact_no']

	group_obj = Group(group_name=group_name)
	group_obj.save()

	account_obj = Account(account_name=account_name,accounttype=accounttype,group=group_obj,contact_no=contact_no)
	account_obj.save()

	return render_to_response('create_account.html')


