from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import admin
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from accounts.models import UserDetail,Group,AccountType,Account,AccountingYear,TransactionType
from accounts.models import SelfMadeAccount,DebtorAndCreditor
import json
from django import forms
from django.db import IntegrityError
import re
from datetime import datetime
from datetime import date
from datetime import timedelta
import time
import datetime


def home(request):
    return render_to_response('index.html')

def user_login(request):
    data_dict = json.loads(request.body)
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
        print "Login Successful"
        return HttpResponse(json.dumps({"validation":"Login Successful","status":True,'redirecturl':"/home"}), content_type="application/json")
    else:
        print "Login Failed"
        return HttpResponse(json.dumps({"validation":"Invalid Login","status":False}), content_type="application/json")

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
    return render_to_response('logout.html')


#def register_user(request):
 #   return render_to_response('register_user.html')

def register_new_user(request):
    print request.body
    json_obj=json.loads(request.body)
    #json_obj=json_obj['newUser']

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
    
   # prog = re.compile(r'^\+?(91)?(0|7)\d{9,13}$')
    #if prog.match(json_obj['mobileNo0']):
     #   return HttpResponse(json.dumps({"validation":"This Mobile Number is already exist.","status":False}), content_type="application/json")
    contact_no = json_obj['mobileNo0']
    contact_no1 = json_obj['mobileNo1']
    city = json_obj['city']
    state = json_obj['state']
    country = json_obj['country']
    pin_code = json_obj['pincode']
    user_obj = User(first_name=first_name,last_name=last_name,username=username,email=email,password=password,)
    user_obj.save()
    user_obj.set_password(password)
  
    userdetail_obj = UserDetail(user=user_obj,address_line1=address_line1,address_line2=address_line2,contact_no=contact_no,city=city,
        state=state,country=country,pin_code=pin_code,contact_no1=contact_no1)
    
    if user_obj is not None:
        print "Registration Successful"
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

def create_new_user_account(request,user_id=None):
    print request.body    
    json_obj = json.loads(request.body)
#    json_obj=json_obj["newUserAccount"]
    username = json_obj['username']
    account_name = json_obj['account_name']
    alias = json_obj['alias']
    group = json_obj['group']
    first_name = json_obj['firstName']
    last_name = json_obj['lastName']
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

    user_obj = User(username=username,first_name=first_name,last_name=last_name,email=email)
    user_obj.save()
    
    userdetail_obj = UserDetail(user=user_obj,contact_no=contact_no,alias=alias,contact_no1=contact_no1,city=city,
        state=state,country=country,pin_code=pin_code)
    userdetail_obj.save()

    group_obj = Group(optionType=group)
    group_obj.save()

    opening_balance_obj = SelfMadeAccount(account_name=account_name,opening_balance=opening_balance)
    opening_balance_obj.save()

    return HttpResponse(json.dumps({"validation":"New User and Account registered Successfully","status":True}), content_type="application/json")

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
    accGroupList = []
    [accGroupList.append({'choice_name':dict(Group.ACCOUNTCHOICES)[i], 'id': i, 'is_selected': False}) for i in dict(Group.ACCOUNTCHOICES)]
    # print type_of_property_list
    return HttpResponse(json.dumps({"accGroupList": accGroupList,"status": True}), content_type="application/json")

def add_acc_validity_date(request):
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
    #accountingyear_obj_list = []
    #accountingyear_obj_list.append(accountingyear_obj)
    accountingyear_obj.save()

    end_date_in_epoch = int(time.mktime(time.strptime(end_date_as_string,'%Y-%m-%d')))
    print accountingyear_obj.start_date, accountingyear_obj.end_date, accountingyear_obj.duration
    print end_date_in_epoch    
    return HttpResponse(json.dumps({'exp_date':end_date_in_epoch}), content_type="application/json")
    
def list_of_accounting_years(request):

    print request.user
    acc_years_list = AccountingYear.objects.all()
    AccYearsList = []
    for i in acc_years_list:
        start_date = str(i.start_date)
        print start_date
        start_date = int(time.mktime(time.strptime(start_date,'%Y-%m-%d')))
        obj = {"start_date":start_date}
        AccYearsList.append(obj)
        print start_date

        end_date = str(i.end_date)
        end_date = int(time.mktime(time.strptime(end_date,'%Y-%m-%d')))
        obj = {"end_date":end_date}
        AccYearsList.append(obj)
        print end_date



    return HttpResponse(json.dumps({"AccYearsList":AccYearsList}), content_type="application/json")

def my_cash_accounts(request):
    print request.user
    acc_years_list = AccountingYear.objects.filter(id=request.user.id)
    start_date = datetime.date(2016, 1, 20)
    end_date = datetime.date(2017, 1, 19)
    cash_account_balance = UserDetail.objects.filter(created_at__range=(start_date,end_date))

    cash_account_balance_list = []
    for i in cash_account_balance:
        obj = {"my_cash_account":i.my_cash_account}
        cash_account_balance_list.append(obj)

    print cash_account_balance_list

    return HttpResponse(json.dumps({"cash_account_balance_list":cash_account_balance_list}), content_type="application/json")

def my_bank_accounts(request):
    print request.user
    acc_years_list = AccountingYear.objects.filter(id=request.user.id)
    start_date = datetime.date(2016, 1, 20)
    end_date = datetime.date(2017, 1, 19)
    bank_account_balance = UserDetail.objects.filter(created_at__range=(start_date,end_date))

    bank_account_balance_list = []
    for i in bank_account_balance:
        obj = {"my_bank_account":i.my_bank_account}
        bank_account_balance_list.append(obj)

    print bank_account_balance_list

    return HttpResponse(json.dumps({"bank_account_balance_list":bank_account_balance_list}), content_type="application/json")

def show_all_debtors(request):
    debtors_details = DebtorAndCreditor.objects.filter(id=request.user.id)
    debtors_details_list = []
    for i in debtors_details:
        obj = {"debtor_name":i.debtor_name,"debit_amount":i.debit_amount}
        debtors_details_list.append(obj)

    print debtors_details_list

    return HttpResponse(json.dumps({"debtors_details_list":debtors_details_list}), content_type="application/json")

def show_all_creditors(request):
    creditors_details = DebtorAndCreditor.objects.filter(id=request.user.id)
    
    creditors_details_list = []
    for i in creditors_details:
        obj = {"creditor_name":i.creditor_name,"credit_amount":i.credit_amount}
        creditors_details_list.append(obj)

    print creditors_details_list
   
#    args['creditors_details_list'] = creditors_details_list

    return HttpResponse(json.dumps({"creditors_details_list":creditors_details_list}), content_type="application/json")

def show_debtor(request):
    print request.user
    debtor = DebtorAndCreditor.objects.get(id=request.user.id)
    args = {}
    debtor_detail = []

    obj = {"debtor_name":debtor.debtor_name,"debtor_amount":debtor.debit_amount}
    debtor_detail.append(obj)
    args['debtor_detail'] = debtor_detail
    print debtor.debtor_name,debtor.debit_amount

    return render_to_response('sample.html',args)

def show_creditor(request):
    print request.user
    creditor = DebtorAndCreditor.objects.get(id=request.user.id)
    args = {}
    creditor_detail = []

    obj = {"creditor_name": creditor.creditor_name,"credit_amount":creditor.credit_amount}
    creditor_detail.append(obj)
    args['creditor_detail'] = creditor_detail
    print creditor.creditor_name, creditor.credit_amount
    return render_to_response('sample.html',args)

def search_SelfMadeAccount(request):
    selfmadeaccount_obj = SelfMadeAccount.objects.filter(id=request.user.id)
    args = {}
    selfmadeaccount_obj_list = []

    for i in selfmadeaccount_obj:
        obj = {"account":i.account}
        selfmadeaccount_obj_list.append(obj)

    args['selfmadeaccount_obj_list'] = selfmadeaccount_obj_list
    print selfmadeaccount_obj_list
    return render_to_response('sample.html',args)

@login_required
def search_Transaction(request):
    transactiontype_obj = TransactionType.objects.filter(id=request.user.id)
    args = {}
    transactiontype_obj_list = []

    for i in transactiontype_obj:
        obj = {"RECIEPT":i.RECIEPT,"PAYMENT":i.PAYMENT,"CONTRA":i.CONTRA,"JOURNAL":i.JOURNAL,"SALE":i.SALE}
        transactiontype_obj_list.append(obj)

    args['transactiontype_obj_list'] = transactiontype_obj_list
    return  render_to_response('sample.html',args)

@login_required
def show_all_transactions(request):
    transactiontype_obj = TransactionType.objects.filter(id=request.user.id)
    args = {}
    transactiontype_obj_list = []

    print transactiontype_obj

    for i in transactiontype_obj:
        obj = {"RECIEPT":i.RECIEPT,"PAYMENT":i.PAYMENT,"CONTRA":i.CONTRA,"JOURNAL":i.JOURNAL,"SALE":i.SALE}
        transactiontype_obj_list.append(obj)

    args['transactiontype_obj_list'] = transactiontype_obj_list
    print transactiontype_obj_list
    return  render_to_response('sample.html',args)

@login_required
def show_transaction(request):
    print request.user
    transactiontype_obj= TransactionType.objects.get(id=request.user.id)
    print transactiontype_obj
    
    args = {}
    args['transactiontype_obj'] = transactiontype_obj

    return render_to_response('sample.html',args)

def send_account_names(request):
    obj = Account.objects.all()

    account_name_list = []

    for i in obj:
        account_name_obj = {"id":i.id,"account_name":i.account_name}
        account_name_list.append(account_name_obj)
    print account_name_list
    return HttpResponse(json.dumps({"account_name_list":account_name_list}), content_type="application/json")


def add_debit_amount(request):
    print request.user
    json_obj = json.loads(request.body)

    total_debit_amount = 0
    
    debit_obj_list = []
    account_name_obj_list =[]
    
    for i in json_obj:
        amount = i['debit_amount']
        account_name = i['account_name']
        total_debit_amount = total_debit_amount + amount
        account_name_obj_list.append(account_name)
    print account_name_obj_list       
    print total_debit_amount

    debitandcredit_obj = DebtorAndCreditor.objects.get(id=1)

    debitandcredit_obj.debit_amount = debitandcredit_obj.debit_amount + total_debit_amount
    debitandcredit_obj.save()
    print debitandcredit_obj.debit_amount

    account_names_obj = Account.objects.get(id=1)

    return render_to_response('sample.html')

    #if j.debit_amount > 0:
     #   date = i.created_at.strftime('%s')
      #  obj = {"account_name":i.account_name,"description":i.description,"debit_amount":j.debit_amount,"created_at":date}
       # debit_obj_list.append(obj)
    #print debit_obj_list"""

def show_account_names(request):
    account_name_obj = SelfMadeAccount.objects.filter(id=request.user.id)
    account_name_list = []

    for i in account_name_obj:
        obj = {"account_name":i.account_name}
        account_name_list.append(obj)
    
    print account_name_list 
    return HttpResponse(json.dumps({"account_name_list":account_name_list}), content_type="application/json")

def search_account_names(request):
    account_name_obj = SelfMadeAccount.objects.filter(id=request.user.id)
    account_name_list = []

    for i in account_name_obj:
        obj = {"account_name":i.account_name}
        account_name_list.append(obj)
    
    print account_name_list 
    return HttpResponse(json.dumps({"account_name_list":account_name_list}), content_type="application/json")

def show_all_debit(request):
    debit_obj = Account.objects.filter(id=request.user.id)
    debit_obj_list = []

    for i in debit_obj:
        debitandcredit_queries = i.account.all()
        for j in debitandcredit_queries:
            if j.debit_amount > 0:
                date = i.created_at.strftime('%s')
                obj = {"account_name":i.account_name,"debit_amount":j.debit_amount,"created_at":date}
                debit_obj_list.append(obj)
    print debit_obj_list
    return HttpResponse(json.dumps({"debit_obj_list":debit_obj_list}), content_type="application/json")

def show_all_credit(request):
    print request.user.id
    credit_obj = Account.objects.filter(id=request.user.id)
    credit_obj_list = []

    for i in credit_obj:
        debitandcredit_queries = i.account.all()
        for j in debitandcredit_queries:
            if j.credit_amount > 0:
                date = i.created_at.strftime('%s')
                obj = {"account_name":i.account_name,"credit_amount":j.credit_amount,"created_at":date}
                credit_obj_list.append(obj)
        
    print credit_obj_list
    return HttpResponse(json.dumps({"credit_obj_list":credit_obj_list}), content_type="application/json")
