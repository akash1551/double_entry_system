from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import admin
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from accounts.models import UserDetail,Group,TransactionType
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
    return render_to_response('index.html')

def user_login(request):
    print request.body
    data_dict = json.loads(request.body)
    print request.COOKIES
    
    username = data_dict['username']
    password = data_dict['password']
    
    user = auth.authenticate(username=username,password=password)
    print username, password
    if user is not None:
        if user.is_active:
            auth.login(request,user)
            print "Login Successful"
            return HttpResponse(json.dumps({"validation":"Login Successful","status":True,'redirecturl':"/menu"}), content_type="application/json")
        else:
            print "Login Failed"
            return HttpResponse(json.dumps({"validation":"Invalid Login","status":False}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"Fill the login details","status":False}), content_type="application/json")

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

def accountingCredit(request):
    return render_to_response('html_templates/user/accountingCredit.html')

def accountingDebit(request):
    return render_to_response('html_templates/user/accountingDebit.html')

def newUserAccount(request):
    return render_to_response('html_templates/user/newUserAccount.html')

def menu(request):
    return render_to_response('html_templates/user/menu.html')

def credit(request):
    return render_to_response('html_templates/user/credit.html')

def debit(request):
    return render_to_response('html_templates/user/debit.html')

def accountDetailBasedOnYear(request):
    return render_to_response('html_templates/user/accountDetailBasedOnYear.html')

def logout(request):
    auth.logout(request)
    return HttpResponse(json.dumps({"validation":"You are now logged out..!!","status":True}))

def register_new_user(request):
    print request.body
    print request.user
    
    json_obj=json.loads(request.body)
    #json_obj=json_obj['userInfo']

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

    address_line1 = json_obj['addressLine1']
    address_line2 = json_obj['addressLine2']
    
    contact_no = json_obj['mobileNo0']
    contact_no1 = json_obj['mobileNo1']
    city = json_obj['city']
    state = json_obj['state']
    country = json_obj['country']
    pin_code = json_obj['pincode']

    user_obj = User(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
    user_obj.set_password(password)
    user_obj.save()
  
    userdetail_obj = UserDetail(user=user_obj,address_line1=address_line1,address_line2=address_line2,contact_no=contact_no,city=city,
        state=state,country=country,pin_code=pin_code,contact_no1=contact_no1)
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

def create_new_user_account(request):
    if request.user.is_authenticated():
        print request.body
        print request.user.first_name
        cash_account_balance = 0
        bank_account_balance = 0
        json_obj = json.loads(request.body)
        #json_obj=json_obj["newUserAccount"]
        account_name = json_obj['account_name']
        my_cash_account = cash_account_balance
        my_bank_account = bank_account_balance
        alias = json_obj['alias']   
        group = json_obj['group']   
        first_name = json_obj['firstName']
        last_name = json_obj['lastName']
        email = json_obj['email']
        address_line1 = json_obj['addressLine1']
        address_line2 = json_obj['addressLine2']
        city = json_obj['city']
        state = json_obj['state']
        country = json_obj['country']
        pin_code = json_obj['pincode']
        email = json_obj['email']
        contact_no = json_obj['mobileNo0']
        contact_no1 = json_obj['mobileNo1']
        opening_balance = json_obj['openingBalance']
        accounttype = json_obj['accounttype']
        start_date = json_obj['start_date']
        end_date = json_obj['end_date']
        duration = json_obj['duration']
        
        start_date_as_datetime = time.strftime('%Y-%m-%d',time.gmtime(start_date))
        print start_date_as_datetime
        end_date_as_datetime = time.strftime('%Y-%m-%d',time.gmtime(end_date))
        print end_date_as_datetime
        user_obj = User.objects.get(id=request.user.id)

        accounttype_obj = AccountType(optionType=accounttype)
        accounttype_obj.save()
        
        group_obj = Group(optionType=group)
        group_obj.save()
        
        account_obj = Account(account_name=account_name,opening_balance=opening_balance,group=group_obj,accounttype=accounttype_obj,my_cash_account=my_cash_account,my_bank_account=my_bank_account)
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
            start_date = str(i.start_date)
            print start_date
            start_date = int(time.mktime(time.strptime(start_date,'%Y-%m-%d')))
            end_date = str(i.end_date)
            print end_date
            end_date = int(time.mktime(time.strptime(end_date,'%Y-%m-%d')))
            obj = {"start_date":start_date,"end_date":end_date}
            AccYearsList.append(obj)
        return HttpResponse(json.dumps({"AccYearsList":AccYearsList}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

def get_groups_from_db1(request):

    json_obj = {"BANK_ACCOUNT": "Bank Account","BANK_OCC_AC": "Bank OCC A/C","BRANCH_OR_DIVISION": "Branch/Division","CAPITAL_ACCOUNT": "Capital Account","CASH_IN_HAND":"Cash in Hand","CURRENT_ASSETS":"Current Assets","CURRENT_LIABILITY": "Current Liabilities",
        "DEPOSITES_ASSETS": "Deposites (Assets)","DIRECT_EXPENSE":"Direct Expense","DIRECT_INCOME":"Direct Income",
        "DUTY_AND_TAX":"Duty & Tax","EXPENSE_DIRECT":"Expense (Direct)","EXPENSE_INDIRECT":"Expense (Indirect)",
        "FIXED_ASSETS":"fixed Assets","INCOME_DIRECT":"Income (Direct)","INCOME_INDIRECT":"Income (Indirect)",
        "INDIRECT_EXPENSE":"Indirect Expense","INDIRECT_INCOME":"Indirect Income","INVESTMENT":"Investments",
        "LOAN_AND_ADVANCE_ASSETS":"Loan & Advance Assets","LOAN_LIABILITY":"Loan Liability","MISC_EXPENSE_ASSETS":"Misc.Expense Assets",
        "PROVISION":"Provision","PURCAHSE_ACCOUNT":"Purchase Account","RESERVE_AND_SURPLUS":"Reserve & Surplus",
        "RETAINED_EARNING":"Retained Earning","SALES_ACCOUNTS":"Sales Accounts","SECURED_LOANS":"Secured Loans",
        "STOCK_IN_HAND":"Stock in Hand"}

    return HttpResponse(json.dumps({"json_obj":json_obj}),content_type="application/json")

def get_groups_from_db(request):
    if request.user.is_authenticated():
        accGroupList = []
        [accGroupList.append({'choice_name':dict(Group.ACCOUNTCHOICES)[i], 'id': i, 'is_selected': False}) for i in dict(Group.ACCOUNTCHOICES)]
        # print type_of_property_list
        return HttpResponse(json.dumps({"accGroupList": accGroupList,"status": True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

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
        
def add_amount_to_cash_account(request):
    print request.user
    json_obj = json.loads(request.body)
    start_date = json_obj['start_date']
    end_date = json_obj['end_date']
    amou0nt = json_obj['amount']
    account_id = json_obj['account_id']
    transactiontype = json_obj['transactiontype']
    group = json_obj['group']
    description = json_obj['description']
    userdetail_obj = UserDetail.objects.get(user__id=request.user.id)
    cash_account_balance = userdetail_obj.account.get(id=account_id,created_at__gte=start_date,created_at__lte=end_date)
    
    print cash_account_balance.my_cash_account
    cash_account_balance.my_cash_account = cash_account_balance.my_cash_account + my_cash_account
    cash_account_balance.save()

    print cash_account_balance.my_cash_account
    return HttpResponse(json.dumps({"validation":"cash amount added in your account."}), content_type="application/json")
##############################################################################################
################################## Cash Account Balance ######################################

def my_cash_account_balance(request):
    if request.user.is_authenticated():
        print request.user
        json_obj = json.loads(request.body)
        start_date = json_obj['start_date']
        end_date = json_obj['end_date']
        print type(start_date)
        print type(end_date)
        start_date_as_string = time.strftime('%Y-%m-%d',time.gmtime(start_date))
        start_date_as_datetime = datetime.datetime.strptime(start_date_as_string, '%Y-%m-%d')
        end_date_as_string = time.strftime('%Y-%m-%d',time.gmtime(end_date))
        end_date_as_datetime = datetime.datetime.strptime(end_date_as_string, '%Y-%m-%d')
        cash_balance = 0
        userdetail_obj = UserDetail.objects.get(user__id=request.user.id)
        cash_account_balance = userdetail_obj.account.filter(created_at__gte=start_date_as_datetime,created_at__lte=end_date_as_datetime)
        for i in cash_account_balance:
            cash_balance = cash_balance + i.my_cash_account  
        return HttpResponse(json.dumps({"cash_balance":cash_balance}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

###########################################################################################
    ###################### Bank Account Balance ######################################
###########################################################################################

def my_bank_account_balance(request):
    if request.user.is_authenticated():
        print request.user
        json_obj = json.loads(request.body)
        start_date = json_obj['start_date']
        end_date = json_obj['end_date']
        start_date = time.strftime('%Y-%m-%d',time.gmtime(start_date))
        print start_date
        end_date = time.strftime('%Y-%m-%d',time.gmtime(end_date))
        print end_date
        bank_balance = 0
        userdetail_obj = UserDetail.objects.get(user__id=request.user.id)
        cash_account_balance = userdetail_obj.account.filter(created_at__gte=start_date,created_at__lte=end_date)
        for i in cash_account_balance:
            bank_balance = bank_balance + i.my_bank_account  
        return HttpResponse(json.dumps({"bank_balance":bank_balance}), content_type="application/json")
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
        json_obj = json.loads(request.body)
        start_date = json_obj['start_date']
        end_date = json_obj['end_date']
        start_date = time.strftime('%Y-%m-%d',time.gmtime(start_date))
        print start_date
        end_date = time.strftime('%Y-%m-%d',time.gmtime(end_date))
        print end_date
        account_obj_list = []
        userdetail_obj = UserDetail.objects.get(user__id=request.user.id)
        print userdetail_obj
        account_obj = userdetail_obj.account.filter(created_at__gte=start_date,created_at__lte=end_date)
        print account_obj
        for i in account_obj:
            date = i.created_at.strftime('%s')
            obj = {"id":i.id,"account_name":i.account_name,"created_at":date}        
            account_obj_list.append(obj)
        return HttpResponse(json.dumps({"account_obj_list":account_obj_list}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

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

def debit_transaction_for_cash_account(request):
    if request.user.is_authenticated():
        print request.user
        json_obj = json.loads(request.body)
        Acc_list = json_obj['Acc_list']
        for i in Acc_list:
            amount = i['debit_amount']
            account_id = i['account_id']
            transactiontype = i['transactiontype']
            group = i['group']
            description = i['description']
            try:
                account_obj = Account.objects.get(id=account_id)
            except Account.DoesNotExist:
                return HttpResponse(json.dumps({"validation":"Something wrong.This account does not exist."}), content_type="application/json")
            account_obj.my_cash_account = account_obj.my_cash_account + amount
            transactiontype_obj = TransactionType(optionType=transactiontype)
            transactiontype_obj.save()
            group_obj = Group(optionType=group)
            group_obj.save()
            transaction_queries = Transaction(debit_amount=amount,transactiontype=transactiontype_obj,group=group_obj,description=description)
            transaction_queries.save()
            account_obj.transaction.add(transaction_queries)
            account_obj.save()
            print account_obj.my_cash_account
        return HttpResponse(json.dumps({"validation":"Transaction Saved Successfully","status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

def credit_transaction_for_cash_account(request):
    if request.user.is_authenticated():
        print request.user
        json_obj = json.loads(request.body)
        Acc_list = json_obj['Acc_list']
        for i in Acc_list:
            amount = i['credit_amount']
            account_id = i['account_id']
            transactiontype = i['transactiontype']
            group = i['group']
            description = i['description']
            try:
                account_obj = Account.objects.get(id=account_id)
            except Account.DoesNotExist:
                return HttpResponse(json.dumps({"validation":"Something wrong.This account does not exist."}), content_type="application/json")
            account_obj.my_cash_account = account_obj.my_cash_account - amount
            transactiontype_obj = TransactionType(optionType=transactiontype)
            transactiontype_obj.save()
            group_obj = Group(optionType=group)
            group_obj.save()
            transaction_queries = Transaction(credit_amount=amount,transactiontype=transactiontype_obj,group=group_obj,description=description)
            transaction_queries.save()
            account_obj.transaction.add(transaction_queries)
            account_obj.save()
            print account_obj.my_cash_account
        return HttpResponse(json.dumps({"validation":"Transaction Saved Successfully","status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

def debit_transaction_for_bank_account(request):
    if request.user.is_authenticated():
        print request.user
        json_obj = json.loads(request.body)
        Acc_list = json_obj['Acc_list']
        for i in Acc_list:
            amount = i['debit_amount']
            account_id = i['account_id']
            transactiontype = i['transactiontype']
            group = i['group']
            description = i['description']
            try:
                account_obj = Account.objects.get(id=account_id)
            except Account.DoesNotExist:
                return HttpResponse(json.dumps({"validation":"Something wrong.This account does not exist."}), content_type="application/json")
            account_obj.my_bank_account = account_obj.my_bank_account + amount
            transactiontype_obj = TransactionType(optionType=transactiontype)
            transactiontype_obj.save()
            group_obj = Group(optionType=group)
            group_obj.save()
            transaction_queries = Transaction(debit_amount=amount,transactiontype=transactiontype_obj,group=group_obj,description=description)
            transaction_queries.save()
            account_obj.transaction.add(transaction_queries)
            account_obj.save()
            print account_obj.my_bank_account
        return HttpResponse(json.dumps({"validation":"Transaction Saved Successfully","status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

def credit_transaction_for_bank_account(request):
    if request.user.is_authenticated():
        print request.user
        json_obj = json.loads(request.body)
        Acc_list = json_obj['Acc_list']
        for i in Acc_list:
            amount = i['credit_amount']
            account_id = i['account_id']
            transactiontype = i['transactiontype']
            group = i['group']
            description = i['description']
            try:
                account_obj = Account.objects.get(id=account_id)
            except Account.DoesNotExist:
                return HttpResponse(json.dumps({"validation":"Something wrong.This account does not exist."}), content_type="application/json")
            account_obj.my_cash_account = account_obj.my_cash_account + amount
            transactiontype_obj = TransactionType(optionType=transactiontype)
            transactiontype_obj.save()
            group_obj = Group(optionType=group)
            group_obj.save()
            transaction_queries = Transaction(credit_amount=amount,transactiontype=transactiontype_obj,group=group_obj,description=description)
            transaction_queries.save()
            account_obj.transaction.add(transaction_queries)
            account_obj.save()
            print account_obj.my_cash_account
        return HttpResponse(json.dumps({"validation":"Transaction Saved Successfully","status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")


                ###########################################################
                ########## Show All Debit And Credit Transactions #########
                ###########################################################

def show_all_debit_transactions(request):
    if request.user.is_authenticated():
        print request.user
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
        print account_obj
        for i in account_obj:
            transaction_obj = i.transaction.filter(debit_amount__gt=0,created_at__gte=start_date,created_at__lte=end_date)
            for j in transaction_obj:
                created_at_in_epoch = calendar.timegm(j.created_at.timetuple())
                obj = {"debit_amount":j.debit_amount,"description":j.description,"created_at":created_at_in_epoch}
                transactionList.append(obj)
        print transactionList
        return HttpResponse(json.dumps({"transactionList":transactionList}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

def show_all_credit_transactions(request):
    if request.user.is_authenticated():
        print request.user
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
        print account_obj
        for i in account_obj:
            transaction_obj = i.transaction.filter(credit_amount__gt=0,created_at__gte=start_date,created_at__lte=end_date)
            for j in transaction_obj:
                created_at_in_epoch = calendar.timegm(j.created_at.timetuple())
                obj = {"credit_amount":j.credit_amount,"description":j.description,"created_at":created_at_in_epoch}
                transactionList.append(obj)
        print transactionList
        return HttpResponse(json.dumps({"transactionList":transactionList}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

def show_all_debit_amount(request):
    if request.user.is_authenticated():
        all_debit = 0
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
                all_debit = all_debit + j.debit_amount
        return HttpResponse(json.dumps({"all_debit":all_debit}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

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
        return 
def show_current_balance(request):
    if request.user.is_authenticated():
        json_obj = json.loads(request.body)
        account_id = json_obj['account_id']
        Account_obj = Account.objects.get(id=account_id)
        current_balance = Account_obj.my_bank_account + Account_obj.my_cash_account
        if datetime.datetime.now()>=datetime.datetime.today()-timedelta(days=1):
            Account_obj = Account.objects.get(id=account_id)
            Account_obj.opening_balance = current_balance
            Account_obj.save()
        return HttpResponse(json.dumps({"current_balance":current_balance}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")
