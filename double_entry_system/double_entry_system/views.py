from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import admin
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from accounts.models import Address
import json

def login(request):
    return render_to_response('login.html')

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


def show_registration_page(request):
    return render_to_response('register_user.html')

def register_user(request):
    print request.POST
    """first_name = request.POST['first_name']
    last_name = request.POST['last_name']"""
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    address = request.POST['address']
    city = request.POST['city']
    state = request.POST['state']
    pin_code = request.POST['pin_code']
    contact_no = request.POST['contact_no']
    password = request.POST['password']
    email = request.POST['email']

    user_obj = User(username=username,first_name=first_name,last_name=last_name,email=email)
    user_obj.set_password(password)
    user_obj.save()

    address_obj = Address(user=user_obj,address=address,city=city,state=state,pin_code=pin_code,contact_no=contact_no)
    address_obj.save()
    
    try:
        user_obj.save()
    except IntegrityError:
        print "User Already Exist"
    return render_to_response('login.html')