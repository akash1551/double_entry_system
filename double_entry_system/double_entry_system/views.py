from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import admin
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from accounts.models import UserDetail,Group,TransactionType,TransactionRecord
from accounts.models import Transaction,AccountType,Account,AccountingYear
import json
from django import forms
from django.db import IntegrityError
import re
from datetime import datetime
from datetime import date
from datetime import timedelta
import time
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import calendar

def home(request):
    return render_to_response('loginIndex.html')

def userHome(request):
    return render_to_response('index.html')

def user_login(request):
    print request.body
    data_dict = json.loads(request.body)
    print request.COOKIES

    username = data_dict['username']
    password = data_dict['password']

    user = auth.authenticate(username=username,password=password)
    print user
    print username, password
    if user is not None:
        if user.is_active:
            auth.login(request,user)
            print "Login Successful"
            return HttpResponse(json.dumps({"validation":"Login Successful","status":True,'redirecturl':"/userHome"}), content_type="application/json")
        else:
            print "Login Failed"
            return HttpResponse(json.dumps({"validation":"Invalid Login","status":False}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"Invalid Login Credentials","status":False}), content_type="application/json")

def loggedin(request):
    return render_to_response('loggedin.html',{'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def registration(request):
    return render_to_response('html_templates/user/registration.html')

def userLogin(request):
    return render_to_response('html_templates/user/login.html')

def myAcc(request):
    return render_to_response('html_templates/user/myAccMaster.html')

def myAccHomePage(request):
    return render_to_response('html_templates/user/myAccHomePage.html')

def summary(request):
    return render_to_response('html_templates/user/myAccountSummary.html')

def accounting(request):
    return render_to_response('html_templates/user/accounting.html')

def newUserAccount(request):
    return render_to_response('html_templates/user/newUserAccount.html')

def footer(request):
    return render_to_response('html_templates/footer.html')

def menu(request):
    return render_to_response('html_templates/user/menu.html')


def accountDetailBasedOnYear(request):
    return render_to_response('html_templates/user/accountDetailBasedOnYear.html')

def logout(request):
    auth.logout(request)
    return HttpResponse(json.dumps({"validation":"You are now logged out..!!","status":True,"redirecturl":"/#/login"}))

def register_new_user(request):
    print request.body
    print request.user

    json_obj=json.loads(request.body)
    json_obj=json_obj['userInfo']

    if User.objects.filter(username = json_obj['userName']).exists():
        print "Username already Exist."
        return HttpResponse(json.dumps({"validation":"Username is already exist.","status":False}), content_type="application/json")
    username = json_obj['userName']
    first_name = json_obj['firstName']
    last_name = json_obj['lastName']

    password = json_obj['password']
    password1 = json_obj['confirmPassword']
    if password != password1:
        print "Passwords Are not Matching"
        return HttpResponse(json.dumps({"validation":"Passwords are not Matched","status":False}), content_type="application/json")
    else:
        if User.objects.filter(email = json_obj['email']).exists():
            print "Email is already Exist."
            return HttpResponse(json.dumps({"validation":"Email is already exist.Try with another Email.","status":False}), content_type="application/json")
        email = json_obj['email']

    if json_obj['addressLine1'] is None:
        return HttpResponse(json.dumps({"validation":"Please Enter Your Address...!","status":False}), content_type="application/json")
    else:
        address_line1 = json_obj['addressLine1']
    address_line2 = json_obj['addressLine2']

    contact_no = json_obj['mobileNo0']
    contact_no = int(contact_no)
    print contact_no
    contact_no1 = json_obj['mobileNo1']
    contact_no1 = int(contact_no1)
    city = json_obj['city']
    state = json_obj['state']
    country = json_obj['country']
    pin_code = json_obj['pincode']
    pin_code = int(pin_code)
    bank_account_name = "My Bank Account"
    cash_account_name = "My Cash Account"
    bank_account_obj = Account(account_name=bank_account_name,contact_no=contact_no,address_line1=address_line1,city=city,state=state,country=country,pin_code=pin_code)
    bank_account_obj.save()
    cash_account_obj = Account(account_name=cash_account_name,contact_no=contact_no,address_line1=address_line1,city=city,state=state,country=country,pin_code=pin_code)
    cash_account_obj.save()
    user_obj = User(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
    user_obj.set_password(password)
    user_obj.save()
    userdetail_obj = UserDetail(user=user_obj,address_line1=address_line1,address_line2=address_line2,contact_no=contact_no,city=city,
        state=state,country=country,pin_code=pin_code,contact_no1=contact_no1,bank_account=bank_account_obj,cash_account=cash_account_obj)
    userdetail_obj.save()
    print "Registration Successful"
    return HttpResponse(json.dumps({"validation":"Registration Successful","status":True}), content_type="application/json")

def account_creation_page(request):
    return render_to_response('create_account.html')

def transactions(request):
    if request.user.is_authenticated():
        print request.body
        print request.user

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
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

def date_conversion(request):
        start_date = 1454284800000/1000
        start_date_as_datetime = time.strftime('%Y-%m-%d',time.gmtime(start_date))
        print start_date_as_datetime
        return  render_to_response('sample.html')

def create_new_user_account(request):
    if request.user.is_authenticated():
        print request.body
        print request.user
        json_obj = json.loads(request.body)
        accountInfo = json_obj['accountInfo']
        account_name = accountInfo.get("account_name")
        alias = accountInfo.get("alias")
        group = accountInfo.get("group")
        grouptype = group.get("id") 
        first_name = accountInfo.get("first_name")
        last_name = accountInfo.get("last_name")
        email = accountInfo.get("email")
        address_line1 = accountInfo.get("addressLine1")
        address_line2 = accountInfo.get("addressLine2")
        city = accountInfo.get("city")
        state = accountInfo.get("state")
        country = accountInfo.get("country")
        pin_code = accountInfo.get("pincode")
        contact_no = accountInfo.get("mobileNo0")
        contact_no1 = accountInfo.get("mobileNo1")
        opening_balance = accountInfo.get("openingBalance")
        accounttype = accountInfo.get("accounttype")
        accounttype = accounttype.get("id")
        start_date = accountInfo.get("start_date")
        end_date = accountInfo.get("end_date")
        duration = accountInfo.get("duration")
        start_date_as_datetime = time.strftime('%Y-%m-%d',time.gmtime(start_date/1000))
        print start_date_as_datetime
        end_date_as_datetime = time.strftime('%Y-%m-%d',time.gmtime(end_date/1000))
        print end_date_as_datetime
        user_obj = User.objects.get(id=request.user.id)

        accounttype_obj = AccountType(optionType=accounttype)
        accounttype_obj.save()

        group_obj = Group(optionType=grouptype)
        group_obj.save()

        account_obj = Account(first_name=first_name,last_name=last_name,email=email,address_line1=address_line1,
            city=city,state=state,country=country,pin_code=pin_code,contact_no=contact_no
            ,contact_no1=contact_no1,account_name=account_name,opening_balance=opening_balance,group=group_obj,accounttype=accounttype_obj)
        account_obj.save()

        accountingyear_obj = AccountingYear(account=account_obj,duration=duration,user=request.user,start_date=start_date_as_datetime,end_date=end_date_as_datetime)
        accountingyear_obj.save()

        userdetail_obj = UserDetail.objects.get(user__id=request.user.id)
        userdetail_obj.account.add(account_obj)
        userdetail_obj.save()
        return HttpResponse(json.dumps({"validation":"New Account created Successfully","status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

def list_of_accounting_years(request):
    print request.COOKIES
    print request.user
    if request.user.is_authenticated():
        acc_years_list = AccountingYear.objects.filter(user__id=request.user.id)
        AccYearsList = []
        for i in acc_years_list:
            #start_date = str(i.start_date)
            print i.start_date
            start_date = int(i.start_date.strftime("%s")) * 1000
            print start_date
            print i.end_date
            end_date = int(i.end_date.strftime("%s")) * 1000
            print end_date

            obj = {"start_date":start_date,"end_date":end_date}
            AccYearsList.append(obj)
        return HttpResponse(json.dumps({"AccYearsList":AccYearsList,"status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue.","status":False}), content_type="application/json")

def get_groups_from_db(request):
    if request.user.is_authenticated():
        accGroupList = []
        [accGroupList.append({'choice_name':dict(Group.ACCOUNTCHOICES)[i], 'id': i, 'is_selected': False}) for i in dict(Group.ACCOUNTCHOICES)]
        # print type_of_property_list
        return HttpResponse(json.dumps({"accGroupList": accGroupList,"status": True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

def get_accounttype_from_db(request):
    if request.user.is_authenticated():
        accTypeList = []
        [accTypeList.append({'choice_name':dict(AccountType.ACCOUNTCHOICES)[i], 'id': i, 'is_selected': False}) for i in dict(AccountType.ACCOUNTCHOICES)]
        # print type_of_property_list
        return HttpResponse(json.dumps({"accTypeList": accTypeList,"status": True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

def get_transactiontype_from_db(request):
    if request.user.is_authenticated():
        TransactionTypeList = []
        [TransactionTypeList.append({'choice_name':dict(TransactionType.PAYMENTCHOICES)[i], 'id': i, 'is_selected': False}) for i in dict(TransactionType.PAYMENTCHOICES)]
        # print type_of_property_list
        return HttpResponse(json.dumps({"TransactionTypeList": TransactionTypeList,"status": True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue.","status":True}), content_type="application/json")

def add_acc_validity_date(request):
    if request.user.is_authenticated():
        print request.body
        print request.user
        json_obj = json.loads(request.body)
        start_date = json_obj['start_date']
        print start_date
        start_date_as_string = time.strftime('%Y-%m-%d',time.gmtime(start_date))
        print start_date_as_string
        date = datetime.datetime.strptime(start_date_as_string, '%Y-%m-%d')
        end_date = date + timedelta(days=365)
        end_date_as_string = datetime.datetime.strftime(end_date,'%Y-%m-%d')
        print end_date_as_string
        accountingyear_obj = AccountingYear(start_date=start_date_as_string,end_date=end_date_as_string,duration=1)
        accountingyear_obj.save()
        end_date_in_epoch = int(time.mktime(time.strptime(end_date_as_string,'%Y-%m-%d')))
        print accountingyear_obj.start_date, accountingyear_obj.end_date, accountingyear_obj.duration
        print end_date_in_epoch
        return HttpResponse(json.dumps({'exp_date':end_date_in_epoch}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

            ################################################################
            #################### Show Account Details ######################
            ################################################################

def show_account_details(request):
    if request.user.is_authenticated():
        print request.user
        json_obj = json.loads(request.body)
        start_date = json_obj['start_date']
        end_date = json_obj['end_date']
        print type(start_date)
        print type(end_date)
        start_date_as_string = time.strftime('%Y-%m-%d',time.gmtime(start_date/1000))
        print start_date_as_string
        end_date_as_string = time.strftime('%Y-%m-%d',time.gmtime(end_date/1000))
        print end_date_as_string
        cash_balance = 0
        userdetail_obj = UserDetail.objects.get(user__id=request.user.id)
        
        bank_account_obj = userdetail_obj.bank_account.current_balance
        print bank_account_obj
                        ##### For Bank Account Balance #########
        cash_account_obj = userdetail_obj.cash_account.current_balance
        print cash_account_obj
                        ######### Show Account Names ###########
        account_obj_list = []
        account_obj = userdetail_obj.account.filter(created_at__gte=start_date_as_string,created_at__lte=end_date_as_string)
        for i in account_obj:
            date = i.created_at.strftime('%s')
            obj = {"id":i.id,"account_name":i.account_name,"created_at":date}
            account_obj_list.append(obj)
        print account_obj_list
                        ######### Show Debit Amount ###########
        all_debit = 0
        transaction_obj = Transaction.objects.filter(user__id=request.user.id)
        for i in transaction_obj:
            transaction_record_obj = i.transaction_record.all()
            for j in transaction_record_obj:
                if j.is_debit == True:
                    all_debit = all_debit + j.amount
        print all_debit       
                   ############## Show Credit Amount ############
        all_credit = 0
        transaction_obj = Transaction.objects.filter(user__id=request.user.id)
        for i in transaction_obj:
            transaction_record_obj = i.transaction_record.all()
            for j in transaction_record_obj:
                if j.is_debit == False:
                    all_credit = all_debit + j.amount
        print all_credit
        return HttpResponse(json.dumps({"bank_balance":bank_account_obj,"cash_balance":cash_account_obj,"all_debit":all_debit,"all_credit":all_credit,"account_obj_list":account_obj_list}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

                ####################################################
                ############## Search Transactions #################
                ####################################################

def search_Transaction(request):
    if request.user.is_authenticated():
        print request.user
        transactiontype_obj = TransactionType.objects.filter(id=request.user.id,created_at__gte=datetime.date(2015, 12, 5),created_at__lte=datetime.date.today())
        transactionList = []
        for i in transactiontype_obj:
            [transactionList.append({'choice_name':dict(TransactionType.PAYMENTCHOICES)[i], 'id': i, 'is_selected': False}) for i in dict(TransactionType.PAYMENTCHOICES)]
        print transactionList
        return HttpResponse(json.dumps({"transactionList": transactionList,"status": True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

                ##############################################################
                #################### Send Account Names ######################
                ##############################################################

def show_account_names(request):
    if request.user.is_authenticated:
        print request.user
        account_obj_list = []
        userdetail_obj = UserDetail.objects.get(user__id=request.user.id)
        print userdetail_obj
        bank_account_obj = userdetail_obj.bank_account
        date = bank_account_obj.created_at.strftime('%s')
        obj1 = {"id":bank_account_obj.id,"account_name":bank_account_obj.account_name,"created_at":date}
        account_obj_list.append(obj1)
        cash_account_obj = userdetail_obj.cash_account
        date = cash_account_obj.created_at.strftime('%s')
        obj2 = {"id":cash_account_obj.id,"account_name":cash_account_obj.account_name,"created_at":date}
        account_obj_list.append(obj2)
        account_obj = userdetail_obj.account.all()
        for i in account_obj:
            date = i.created_at.strftime('%s')
            obj = {"id":i.id,"account_name":i.account_name,"created_at":date}
            account_obj_list.append(obj)
        print account_obj_list
        return HttpResponse(json.dumps({"account_obj_list":account_obj_list,"status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue.","status":False}), content_type="application/json")

def search_account_names(request):
    if request.user.is_authenticated:
        account_name_obj = Account.objects.filter(id=request.user.id,created_at__gte=datetime.date(2015, 12, 5),created_at__lte=datetime.date.today())
        account_name_list = []
        for i in account_name_obj:
            date = i.created_at.strftime('%s')
            obj = {"account_name":i.account_name,"created_at":date}
            account_name_list.append(obj)
        print account_name_list
        return HttpResponse(json.dumps({"account_name_list":account_name_list}), content_type="application/json")


            ##################################################################
            ################# Credit And Debit Transactions ##################
            ##################################################################

def transaction_for_account(request):
    if request.user.is_authenticated():
        print request.user
        print request.body
        json_obj = json.loads(request.body)
        data = json_obj['data']
        Acc_list = data.get("Acc_list")
        transaction_date = data.get("transaction_date")
        transactiontype = data.get("transactiontype")
        transactiontype_obj = TransactionType(optionType=transactiontype)
        transactiontype_obj.save()
        user_obj = User.objects.get(id=request.user.id)
        print type(transactiontype)
        transaction_date = time.strftime('%Y-%m-%d',time.gmtime(transaction_date/1000))
        description = data.get("description")
        transaction_obj = Transaction(transaction_date=transaction_date,description=description,transactiontype=transactiontype_obj,user=user_obj)
        transaction_obj.save()
        print Acc_list
        for i in Acc_list:
            amount = i['amount']
            account = i['account']
            account_id = account.get("id")
            print account_id
            is_debit = i['is_debit']
            print is_debit.capitalize()
            if is_debit == "D":
                is_debit = True
            else:
                is_debit = False
            account_obj = Account.objects.get(id=account_id)
            print account_obj
            transactionrecord_queries = TransactionRecord(amount=amount,is_debit=is_debit,account=account_obj)
            transactionrecord_queries.save()
            transaction_obj.transaction_record.add(transactionrecord_queries)
            transaction_obj.save()
        print "Transaction saved Successfully..."
        return HttpResponse(json.dumps({"validation":"Transaction Saved Successfully","status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")


                ###########################################################
                ########## Show All Debit And Credit Transactions #########
                ###########################################################

def show_all_transactions(request):
    if request.user.is_authenticated():
        print request.user
        transaction_obj = Transaction.objects.filter(user__id=request.user.id)
        print transaction_obj
        transactionList = []
        for i in transaction_obj:
            date = i.transaction_date.strftime('%s')
            transactiontype_obj = i.transactiontype.optionType
            obj = {"id":i.id,"transaction_date":date,"description":i.description,"transactiontype":dict(TransactionType.PAYMENTCHOICES)[transactiontype_obj]}
            transaction_record_obj = i.transaction_record.all()
            print obj
            transactionRecordList = []
            print transaction_record_obj
            for j in transaction_record_obj:
                account_obj = j.account
                obj1 = {"account_name":account_obj.account_name,"amount":j.amount,"is_debit":j.is_debit}
                transactionRecordList.append(obj1)
            obj.update({"transaction_record_list":transactionRecordList})
            transactionList.append(obj)
            

        return HttpResponse(json.dumps({"transactionList":transactionList}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

            #####################################################################
            ####### Show Total Of Debit And Credit Amount Of All Accounts #######
            #####################################################################

def show_all_debit_and_credit_amount(request):
    if request.user.is_authenticated():
        json_obj = json.loads(request.body)
        account_id = json_obj['account_id']
        all_debit = 0
        all_credit = 0
        transactionList = []
        transaction_record_obj = TransactionRecord.objects.filter(account__id=account_id)
        for i in transaction_record_obj:
            if i.is_debit == True:
                print i.amount
                all_debit = all_debit + i.amount
            if i.is_debit == False:
                all_credit = all_credit + i.amount
        return HttpResponse(json.dumps({"all_debit":all_debit,"all_credit":all_credit,"status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue.","status":False}), content_type="application/json")

def show_all_credit_amount(request):
    if request.user.is_authenticated():
        all_credit = 0
        json_obj = json.loads(request.body)
        start_date = json_obj['start_date']
        end_date = json_obj['end_date']
        print start_date
        start_date = time.strftime('%Y-%m-%d',time.gmtime(start_date))
        print end_date
        end_date = time.strftime('%Y-%m-%d',time.gmtime(end_date))
        transactionList = []
        userdetail_obj = UserDetail.objects.get(user__id=request.user.id)
        account_obj = userdetail_obj.account.filter(created_at__gte=start_date,created_at__lte=end_date)
        for i in account_obj:
            transaction_obj = i.transaction.all()
            for j in transaction_obj:
                all_credit = all_credit + j.credit_amount
        return HttpResponse(json.dumps({"all_credit":all_credit}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

def show_current_balance(request):
    if request.user.is_authenticated():
        json_obj = json.loads(request.body)
        account_id = json_obj['account_id']
        Account_obj = Account.objects.get(id=account_id)
        Account_obj.current_balance = Account_obj.my_bank_account + Account_obj.my_cash_account
        if datetime.datetime.now()>=datetime.datetime.today()-timedelta(days=1):
            Account_obj.opening_balance = Account_obj.current_balance
            Account_obj.save()
        return HttpResponse(json.dumps({"current_balance":Account_obj.current_balance}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

def add_group(request):
    if request.user.is_authenticated():
        json_obj = json.loads(request.body)
        group_name = json_obj['group_name']

def edit_account(request):
    if request.user.is_authenticated():
        print request.body
        print request.user
        json_obj = json.loads(request.body)
        accountInfo = json_obj['accountInfo']
        account_name = accountInfo.get("account_name")
        alias = accountInfo.get("alias")
        group = accountInfo.get("group")
        grouptype = group.get("id") 
        first_name = accountInfo.get("first_name")
        last_name = accountInfo.get("last_name")
        email = accountInfo.get("email")
        address_line1 = accountInfo.get("addressLine1")
        address_line2 = accountInfo.get("addressLine2")
        city = accountInfo.get("city")
        state = accountInfo.get("state")
        country = accountInfo.get("country")
        pin_code = accountInfo.get("pincode")
        contact_no = accountInfo.get("mobileNo0")
        contact_no1 = accountInfo.get("mobileNo1")
        opening_balance = accountInfo.get("openingBalance")
        accounttype = accountInfo.get("accounttype")
        accounttype = accounttype.get("id")
        start_date = accountInfo.get("start_date")
        end_date = accountInfo.get("end_date")
        duration = accountInfo.get("duration")
        start_date_as_datetime = time.strftime('%Y-%m-%d',time.gmtime(start_date/1000))
        print start_date_as_datetime
        end_date_as_datetime = time.strftime('%Y-%m-%d',time.gmtime(end_date/1000))
        print end_date_as_datetime
        user_obj = User.objects.get(id=request.user.id)

        accounttype_obj = AccountType(optionType=accounttype)
        accounttype_obj.save()

        group_obj = Group(optionType=grouptype)
        group_obj.save()

        account_obj = Account(first_name=first_name,last_name=last_name,email=email,address_line1=address_line1,
            city=city,state=state,country=country,pin_code=pin_code,contact_no=contact_no
            ,contact_no1=contact_no1,account_name=account_name,opening_balance=opening_balance,group=group_obj,accounttype=accounttype_obj)
        account_obj.save()

        accountingyear_obj = AccountingYear(account=account_obj,duration=duration,user=request.user,start_date=start_date_as_datetime,end_date=end_date_as_datetime)
        accountingyear_obj.save()

        userdetail_obj = UserDetail.objects.get(user__id=request.user.id)
        userdetail_obj.account.add(account_obj)
        userdetail_obj.save()
        return HttpResponse(json.dumps({"validation":"New Account created Successfully","status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

def get_account_details(request):
    if request.user.is_authenticated():
        json_obj =json.loads(request.body)
        account_id = json_obj['account_id']
        account_obj = Account.objects.get(id=account_id)
        group_obj = account_obj.group
        accounttype_obj = account_obj.accounttype
        accountList = []
        print accounttype_obj
        print group_obj
        accounttype_obj = {"id":accounttype_obj.id,"accounttype":dict(AccountType.ACCOUNTCHOICES)[accounttype_obj.optionType],"is_selected":True}
        group_obj = {"id":group_obj.id,"is_selected":True,
        "group":dict(Group.ACCOUNTCHOICES)[group_obj.optionType]}
        obj = {"account_name":account_obj.account_name,"alias":account_obj.alias,"first_name":account_obj.first_name,
        "last_name":account_obj.last_name,"email":account_obj.email,"address_line1":account_obj.address_line1,
        "address_line2":account_obj.address_line2,"city":account_obj.city,"state":account_obj.state,
        "country":account_obj.country,"pin_code":account_obj.pin_code,"contact_no":account_obj.contact_no,
        "contact_no1":account_obj.contact_no1,"opening_balance":account_obj.opening_balance,"group":group_obj,
        "accounttype":accounttype_obj}
        
        return HttpResponse(json.dumps({"obj":obj,"status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")