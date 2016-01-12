from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import admin
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from accounts.models import Address,Group,AccountType,Account,AccountingYear
import json
from django import forms

#def login(request):
 #   return render_to_response('login.html')

def home(request):
    return render_to_response('index.html')

def auth_view(request):
    data_dict=json.loads(request.body)
    print request.POST
    username = data_dict['username']
    
    password = data_dict['password']
    # user = User(username=username)
    # user.set_password(password)
    # user.save()

    print username, password
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return HttpResponse(json.dumps({"validation":"Login Successful","status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"Invalid Login","status":False}), content_type="application/json")

def loggedin(request):
    return render_to_response('loggedin.html',{'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


#def register_user(request):
 #   return render_to_response('register_user.html')

def register_auth(request):
    print request.body
    json_obj=json.loads(request.body)

    username = json_obj['username']
    first_name = json_obj['first_name']
    last_name = json_obj['last_name']
    password = json_obj['password']
    password1 = json_obj['password1']
    email = json_obj['email']
    address_line1 = json_obj['address_line1']
    address_line2 = json_obj['address_line2']
    contact_no = json_obj['contact_no']
    city = json_obj['city']
    state = json_obj['state']
    country = json_obj['country']
    pin_code = json_obj['pin_code']

    if password != password1:
       # raise forms.ValidationError("Passwords not Matched.")
        return HttpResponse(json.dumps({"validation":"Passwords are not Matched","status":False}), content_type="application/json")
    else:    
        user_obj = User(first_name=first_name,last_name=last_name,username=username,email=email,password=password,)
        user_obj.save()
        user_obj.set_password(password)

        address_obj = Address(address_line1=address_line1,address_line2=address_line2,contact_no=contact_no,city=city,
            state=state,country=country,pin_code=pin_code)
    
    if user_obj is not None:
        user_obj.append
        return HttpResponse(json.dumps({"validation":"Registration Successful","status":True}), content_type="application/json")

def account_creation_page(request):
    return render_to_response('create_account.html')

def transactions(request):
    print request.body
    
    user = User.objects.all()
    user_list = []
    for i in user:
        user_obj = {"username":i.username,"email":i.email}
        user_list.append(user_obj)

    accounttype = AccountType.objects.all()
    accounttype_list = []
    for i in accounttype:
        accounttype_obj = {"account_name":i.account_name}
        accounttype_list.append(accounttype_obj)

    accountingyear = AccountingYear.objects.all()
    accountingyear_list = []
    for i in accountingyear:
        accountingyear_obj = {"start_date":i.start_date,"end_date":i.end_date,"duration":i.duration}
        accountingyear_list.append(accountingyear_obj)

    print user_list

    return HttpResponse(json.dumps({"user_list":user_list,"accounttype_list":accounttype_list,"accountingyear_list":accountingyear_list}), content_type="application/json")
