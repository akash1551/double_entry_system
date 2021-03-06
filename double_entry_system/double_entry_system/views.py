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
from django.db import transaction
from django.core.validators import EmailValidator
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def validateEmail(email):
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False
def home(request):
    return render_to_response('html_templates/loginIndex.html')

def userHome(request):
    return render_to_response('html_templates/index.html')


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

def accountMenu(request):
    return render_to_response('html_templates/user/myAccMaster/accountMenu.html')

def account(request):
    return render_to_response('html_templates/user/myAccMaster/account.html')

def accountDetailBasedOnYear(request):
    return render_to_response('html_templates/user/accountDetailBasedOnYear.html')

def activities(request):
    return render_to_response('html_templates/user/activities.html')

def transactionDetails(request):
    return render_to_response('html_templates/user/transactionDetails.html')

def logout(request):
    auth.logout(request)
    return HttpResponse(json.dumps({"validation":"You are now logged out..!!","status":True,"redirecturl":"/#/login"}))

def user_login(request):
    data_dict = json.loads(request.body)
    username = data_dict['username']
    password = data_dict['password']

    user = auth.authenticate(username=username,password=password)
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

@transaction.atomic
def register_new_user(request):
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
    email = validateEmail(json_obj['email'])
    if email != True:
        print "Email is already Exist."
        return HttpResponse(json.dumps({"validation":"Email is already exist.Try with another Email.","status":False}), content_type="application/json")
    else:
        email = json_obj['email']

    if json_obj['addressLine1'] is None:
        return HttpResponse(json.dumps({"validation":"Please Enter Your Address...!","status":False}), content_type="application/json")
    else:
        address_line1 = json_obj['addressLine1']
    address_line2 = json_obj['addressLine2']

    contact_no = json_obj['mobileNo0']
    contact_no = int(contact_no)
    contact_no = validate_mobile(str(contact_no))
    if contact_no == False:
        return HttpResponse(json.dumps([{"validation": "This mobile number is already used..please try with another one.", "status": False}]), content_type = "application/json")
    else:
        contact_no1 = json_obj['mobileNo1']
        city = json_obj['city']
        state = json_obj['state']
        country = json_obj['country']
        pin_code = json_obj['pincode']
        accounttype_obj = AccountType(optionType=1)
        accounttype_obj.save()
        group_obj_for_bank_acc = Group(optionType=0)
        group_obj_for_bank_acc.save()
        group_obj_for_cash_acc = Group(optionType=4)
        group_obj_for_cash_acc.save()
        bank_account_name = "My Bank Account"
        cash_account_name = "My Cash Account"
        bank_account_obj = Account(account_name=bank_account_name,first_name=first_name,last_name=last_name,contact_no=contact_no,address_line1=address_line1,city=city,state=state,country=country,pin_code=pin_code,accounttype=accounttype_obj,group=group_obj_for_bank_acc)
        bank_account_obj.save()
        cash_account_obj = Account(account_name=cash_account_name,first_name=first_name,last_name=last_name,contact_no=contact_no,address_line1=address_line1,city=city,state=state,country=country,pin_code=pin_code,accounttype=accounttype_obj,group=group_obj_for_cash_acc)
        cash_account_obj.save()
        user_obj = User(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
        user_obj.set_password(password)
        user_obj.save()
        userdetail_obj = UserDetail(user=user_obj,address_line1=address_line1,address_line2=address_line2,contact_no=contact_no,city=city,
            state=state,country=country,pin_code=pin_code,contact_no1=contact_no1,bank_account=bank_account_obj,cash_account=cash_account_obj)
        userdetail_obj.save()
        print "Registration Successful"
        return HttpResponse(json.dumps({"validation":"Registration Successful.","redirecturl":"#/login","status":True}), content_type="application/json")

def show_user_details(request):
    if request.user.is_authenticated():
        print request.user.id
        print "------------------------------------"
        user_obj = UserDetail.objects.get(user__id=request.user.id)
        obj = {"username":user_obj.user.username,"firstName":user_obj.first_name,"lastName":user_obj.last_name,
        "user_obj":user_obj.alias,"addressLine1":user_obj.address_line1,"email":user_obj.email}
        return HttpResponse(json.dumps({"User":obj,"status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue.","status":False}), content_type="application/json")

def account_creation_page(request):
    return render_to_response('create_account.html')

def validate_mobile(value):
    rule = re.compile(r'^(\+91[\-\s]?)?[0]?[1789]\d{9}$')
    if not rule.search(value):
        return False
    else:
        return value

@transaction.atomic
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
        first_name = accountInfo.get("firstName")
        last_name = accountInfo.get("lastName")
        email = accountInfo.get("email")
        address_line1 = accountInfo.get("addressLine1")
        address_line2 = accountInfo.get("addressLine2")
        city = accountInfo.get("city")
        state = accountInfo.get("state")
        country = accountInfo.get("country")
        try:
            pin_code = accountInfo.get("pincode")
        except ValueError:
            return HttpResponse(json.dumps([{"validation": "Please Enter Valid PinCode.", "status": False}]), content_type = "application/json")
        contact_no = accountInfo.get("mobileNo0")
        contact_no1 = accountInfo.get("mobileNo1")
        opening_balance = accountInfo.get("openingBalance")
        accounttype = accountInfo.get("accounttype")
        accounttype = accounttype.get("id")
        user_obj = User.objects.get(id=request.user.id)

        accounttype_obj = AccountType(optionType=accounttype)
        accounttype_obj.save()

        group_obj = Group(optionType=grouptype)
        group_obj.save()

        account_obj = Account(first_name=first_name,last_name=last_name,email=email,address_line1=address_line1,
            city=city,state=state,country=country,pin_code=pin_code,contact_no=contact_no
            ,contact_no1=contact_no1,account_name=account_name,opening_balance=opening_balance,group=group_obj,accounttype=accounttype_obj)
        account_obj.save()

        userdetail_obj = UserDetail.objects.get(user__id=request.user.id)
        userdetail_obj.account.add(account_obj)
        userdetail_obj.save()
        return HttpResponse(json.dumps({"validation":"New Account created Successfully","status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

def list_of_accounting_years(request):
    if request.user.is_authenticated():
        try:
            acc_years_list = AccountingYear.objects.filter(user__id=request.user.id)
        except AccountingYear.DoesNotExist:
            return HttpResponse(json.dumps({"validation":"Please create Financial year for your transactions."}), content_type="application/json")
        AccYearsList = []
        for i in acc_years_list:
            start_date = int(i.start_date.strftime("%s")) * 1000
            end_date = int(i.end_date.strftime("%s")) * 1000
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
        json_obj = json.loads(request.body)
        start_year = json_obj['start_year']
        accountingyears = AccountingYear.objects.filter(user__id=request.user.id)
        for i in accountingyears:
            if i.start_date.year == start_year:
                return HttpResponse(json.dumps({'validation':"This year for Financial transactions is already used by you...Please select another year..","status":False}), content_type="application/json")
        end_year = start_year + 1
        start_date = datetime.datetime(start_year, 04, 01, 00, 00, 00)
        end_date = datetime.datetime(end_year, 03, 31, 23, 59, 59)
        user_obj = User.objects.get(id=request.user.id)
        accountingyear_obj = AccountingYear(start_date=start_date,end_date=end_date,duration=1,user=user_obj)
        accountingyear_obj.save()
        return HttpResponse(json.dumps({'validation':"New Financial Year created for your transactions...","redirecturl":"#/myAccMaster","status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

            ################################################################
            ########++++++++++++ Show Account Details +++++++++++++#########
            ################################################################

def show_account_details(request):
    if request.user.is_authenticated():
        print request.body
        data_dictonary = json.loads(request.body)
        pageNo = data_dictonary['pageNo']
        entriesPerPage = data_dictonary['entriesPerPage']
        print pageNo
        print entriesPerPage
        entriesPerPage = entriesPerPage - 2
        excludePageEntries = (pageNo - 1) * entriesPerPage
        nextPageEntries = excludePageEntries + entriesPerPage
        cash_balance = 0
        userdetail_obj = UserDetail.objects.get(user__id=request.user.id)
        accountList = []
        #start_date = datetime.datetime(startYear, 04, 01, 00, 00, 00)

                        ######## For Bank Account Balance #########

        all_debit_for_bank = 0
        all_credit_for_bank = 0
        bank_account_obj = userdetail_obj.bank_account
        #accountingYearObj = AccountingYear.objects.get(start_date=start_date)
        transaction_obj = Transaction.objects.filter(user__id=request.user.id)
        for a in transaction_obj:
            transaction_record_obj = a.transaction_record.filter(account=bank_account_obj)
            for b in transaction_record_obj:
                if b.is_debit == True:
                    all_debit_for_bank = all_debit_for_bank + b.amount
                if b.is_debit == False:
                    all_credit_for_bank = all_credit_for_bank + b.amount
        if all_credit_for_bank > all_debit_for_bank:
            bank_account_obj.current_balance = all_credit_for_bank - all_debit_for_bank
            value = bank_account_obj.current_balance
            bankObj = {"id":bank_account_obj.id,"amount":str(value)+" Cr","account_name":bank_account_obj.account_name}
        elif all_debit_for_bank > all_credit_for_bank:
            bank_account_obj.current_balance = all_debit_for_bank - all_credit_for_bank
            value = bank_account_obj.current_balance
            bankObj = {"id":bank_account_obj.id,"amount":str(value)+" Dr","account_name":bank_account_obj.account_name}
        elif all_debit_for_bank == all_credit_for_bank:
            bankObj = {"id":bank_account_obj.id,"amount":"Nil","account_name":bank_account_obj.account_name}
        accountList.append(bankObj)

                    ####### For Cash Account Balance ########

        all_debit_for_cash = 0
        all_credit_for_cash = 0
        cash_account_obj = userdetail_obj.cash_account
        transaction_obj = Transaction.objects.filter(user__id=request.user.id)
        for a in transaction_obj:
            transaction_record_obj = a.transaction_record.filter(account__id=cash_account_obj.id)
            for b in transaction_record_obj:
                if b.is_debit == True:
                    all_debit_for_cash = all_debit_for_cash + b.amount
                if b.is_debit == False:
                    all_credit_for_cash = all_credit_for_cash + b.amount
        if all_credit_for_cash > all_debit_for_cash:
            cash_account_obj.current_balance = all_credit_for_cash - all_debit_for_cash
            value1 = cash_account_obj.current_balance
            cashObj = {"id":cash_account_obj.id,"amount":str(value1)+" Cr","account_name":cash_account_obj.account_name}
        elif all_debit_for_cash > all_credit_for_cash:
            cash_account_obj.current_balance = all_debit_for_cash - all_credit_for_cash
            value1 = cash_account_obj.current_balance
            cashObj = {"id":cash_account_obj.id,"amount":str(value1)+" Dr","account_name":cash_account_obj.account_name}
        elif all_debit_for_cash == all_credit_for_cash:
            cashObj = {"id":cash_account_obj.id,"amount":"Nil","account_name":cash_account_obj.account_name}
        accountList.append(cashObj)

                        ######### Show Account Names ###########

        userdetail_obj = UserDetail.objects.get(user__id=request.user.id)
        bank_account_obj = userdetail_obj.bank_account.id
        cash_account_obj = userdetail_obj.cash_account.id
        transaction_obj = Transaction.objects.filter(user__id=request.user.id)
        account_obj = userdetail_obj.account.all()[excludePageEntries:nextPageEntries]
        paginator = Paginator(account_obj, 2)
        for i in account_obj:
            all_debit = 0
            all_credit = 0
            all_debit1 = 0
            all_credit1 = 0
            transaction_record_obj = TransactionRecord.objects.filter(account=i).exclude(account__id__in=[bank_account_obj,cash_account_obj])
            for j in transaction_record_obj:
                if j.is_debit==True:
                    all_debit = all_debit + j.amount
                else:
                    all_credit = all_credit + j.amount
            if all_debit > all_credit:
                all_debit1 = all_debit - all_credit
                obj = {"id":i.id,"amount":str(all_debit1)+" Dr","account_name":i.account_name}
            elif all_credit > all_debit:
                all_credit1 = all_credit - all_debit
                obj = {"id":i.id,"amount":str(all_credit1)+" Cr","account_name":i.account_name}
            else:
                obj = {"id":i.id,"amount":"Nil","account_name":i.account_name}

            accountList.append(obj)
        return HttpResponse(json.dumps({"accountList":accountList,"status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"Invalid User","status":False}), content_type="application/json")

                ##############################################################
                #################### Send Account Names ######################
                ##############################################################

def show_account_names(request):
    if request.user.is_authenticated:
        account_obj_list = []
        userdetail_obj = UserDetail.objects.get(user__id=request.user.id)
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
        return HttpResponse(json.dumps({"account_obj_list":account_obj_list,"status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue.","status":False}), content_type="application/json")

            ##################################################################
            ################# Credit And Debit Transactions ##################
            ##################################################################

@transaction.atomic
def transaction_for_account(request):
    if request.user.is_authenticated():
        json_obj = json.loads(request.body)
        data = json_obj['data']
        Acc_list = data.get("Acc_list")
        transaction_date = data.get("transaction_date")
        transactiontype = data.get("transactiontype")
        transactiontype_obj = TransactionType(optionType=transactiontype)
        transactiontype_obj.save()
        user_obj = User.objects.get(id=request.user.id)
        transaction_date = datetime.datetime.fromtimestamp(transaction_date/1000)
        description = data.get("description")
        try:
            accountingyear_obj = AccountingYear.objects.get(start_date__lte=transaction_date,end_date__gte=transaction_date,user__id=request.user.id)
        except AccountingYear.DoesNotExist:
            if transaction_date <= datetime.datetime(transaction_date.year, 03, 31, 23, 59, 59):
                start_date = datetime.datetime(transaction_date.year-1, 04, 01, 00, 00, 00)
                end_date = datetime.datetime(transaction_date.year, 03, 31, 23, 59, 59)
                user_obj = User.objects.get(id=request.user.id)
                accountingyear_obj = AccountingYear(start_date=start_date,end_date=end_date,duration=1,user=user_obj)
                accountingyear_obj.save()
            else:
                year = int(transaction_date.year)
                start_date = datetime.datetime(transaction_date.year, 04, 01, 00, 00, 00)
                end_date = datetime.datetime(transaction_date.year+1, 03, 31, 23, 59, 59)
                user_obj = User.objects.get(id=request.user.id)
                accountingyear_obj = AccountingYear(start_date=start_date,end_date=end_date,duration=1,user=user_obj)
                accountingyear_obj.save()
        transaction_obj = Transaction(transaction_date=transaction_date,description=description,transactiontype=transactiontype_obj,user=user_obj)
        transaction_obj.save()
        accountingyear_obj.transaction.add(transaction_obj)
        accountingyear_obj.save()
        for i in Acc_list:
            amount = i['amount']
            account = i['account']
            account_id = account.get("id")
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

def show_all_transactions_of_one_year(request):
    if request.user.is_authenticated():
        json_obj = json.loads(request.body)
        start_date = json_obj['start_date']
        pageNo = json_obj['pageNo']
        entriesPerPage = json_obj['entriesPerPage']
        print pageNo
        print entriesPerPage
        entriesPerPage = entriesPerPage - 2
        excludePageEntries = (pageNo - 1) * entriesPerPage
        nextPageEntries = excludePageEntries + entriesPerPage
        start_date = time.strftime('%Y-%m-%d',time.gmtime(start_date/1000))
        #start_date = datetime.datetime(startYear, 04, 01, 00, 00, 00)

        try:
            accountingyear_obj = AccountingYear.objects.get(start_date=start_date,user__id=request.user.id)
        except AccountingYear.DoesNotExist:
            return HttpResponse(json.dumps({"validation":"You did not create current financial year."}), content_type="application/json")
        try:
            transaction_obj = accountingyear_obj.transaction.filter(user__id=request.user.id)[excludePageEntries:nextPageEntries]
        except ObjectDoesNotExist:
            return HttpResponse(json.dumps({"validation":"Data Not Found","status":True}), content_type="application/json")

        transactionList = []
        for i in transaction_obj:
            date = int(i.transaction_date.strftime('%s'))*1000
            transactiontype_obj = i.transactiontype.optionType
            obj = {"id":i.id,"transaction_date":date,"description":i.description,"transactiontype":dict(TransactionType.PAYMENTCHOICES)[transactiontype_obj]}
            transaction_record_obj = i.transaction_record.all()
            transactionRecordList = []
            for j in transaction_record_obj:
                account_obj = j.account
                obj1 = {"account_name":account_obj.account_name,"amount":j.amount,"is_debit":j.is_debit}
                transactionRecordList.append(obj1)
            obj.update({"transaction_record_list":transactionRecordList})
            transactionList.append(obj)
        return HttpResponse(json.dumps({"transactionList":transactionList}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

def show_all_transactions(request):
    if request.user.is_authenticated():
        data_dictonary = json.loads(request.body)
        pageNo = data_dictonary['pageNo']
        entriesPerPage = data_dictonary['entriesPerPage']
        excludePageEntries = (pageNo - 1) * entriesPerPage
        nextPageEntries = excludePageEntries + entriesPerPage
        try:
            transaction_obj = Transaction.objects.filter(user__id=request.user.id)[excludePageEntries:nextPageEntries]
        except Transaction.DoesNotExist:
            return HttpResponse(json.dumps({"validation":"No Record Found."}), content_type="application/json")
        transactionList = []
        for i in transaction_obj:
            date = int(i.transaction_date.strftime('%s'))*1000
            transactiontype_obj = i.transactiontype.optionType
            obj = {"id":i.id,"transaction_date":date,"description":i.description,"transactiontype":dict(TransactionType.PAYMENTCHOICES)[transactiontype_obj]}
            transaction_record_obj = i.transaction_record.all()
            transactionRecordList = []
            for j in transaction_record_obj:
                account_obj = j.account
                obj1 = {"account_name":account_obj.account_name,"amount":j.amount,"is_debit":j.is_debit}
                transactionRecordList.append(obj1)
            obj.update({"transaction_record_list":transactionRecordList})
            transactionList.append(obj)
        return HttpResponse(json.dumps({"transactionList":transactionList,"status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue.","status":False}), content_type="application/json")

            #####################################################################
            ####### Show Total Of Debit And Credit Amount Of All Accounts #######
            #####################################################################

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
        group_obj = Group(group_name=group_name)
        group_obj.save()
        return HttpResponse(json.dumps({"validation":"New Group created Successfully...","status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

@transaction.atomic
def save_edit_account(request):
    if request.user.is_authenticated():
        json_obj = json.loads(request.body)
        accountInfo = json_obj['accountInfo']
        account_id = json_obj["account_id"]
        account_name = accountInfo.get("account_name")
        alias = accountInfo.get("alias")
        group = accountInfo.get("group")
        grouptype = group.get("id")
        first_name = accountInfo.get("firstName")
        last_name = accountInfo.get("lastName")
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
        accountTypeOptionId = accounttype.get("id")
        user_obj = User.objects.get(id=request.user.id)

        accounttype_obj = AccountType.objects.get(optionType = accountTypeOptionId)

        group_obj = Group(optionType=grouptype)
        group_obj.save()
        account_obj = Account.objects.get(id=account_id)

        account_obj.account_name = account_name
        account_obj.first_name = first_name
        account_obj.last_name = last_name
        account_obj.alias = alias
        account_obj.email = email
        account_obj.address_line1 = address_line1
        account_obj.address_line2 = address_line2
        account_obj.contact_no = contact_no
        account_obj.contact_no1 = contact_no1
        account_obj.city = city
        account_obj.state = state
        account_obj.country = country
        account_obj.pin_code = pin_code
        account_obj.opening_balance = opening_balance
        account_obj.group = group_obj
        account_obj.accounttype = accounttype_obj
        account_obj.save()
        userdetail_obj = UserDetail.objects.get(user__id=request.user.id)
        userdetail_obj.account.add(account_obj)
        userdetail_obj.save()
        return HttpResponse(json.dumps({"validation":"Account details updated Successfully","status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

def get_account_details(request):
    if request.user.is_authenticated():
        json_obj =json.loads(request.body)
        account_id = json_obj['account_id']
        account_obj = Account.objects.get(id=account_id)
        group_obj = account_obj.group
        accounttype_obj = account_obj.accounttype
        print type(accounttype_obj)
        accountList = []
        accounttype_obj_new = {"id":accounttype_obj.optionType,
        "choice_name":dict(AccountType.ACCOUNTCHOICES)[accounttype_obj.optionType],"is_selected":False}
        group_obj = {"id":group_obj.optionType,"is_selected":False,
        "choice_name":dict(Group.ACCOUNTCHOICES)[group_obj.optionType]}
        accountInfo = {"account_name":account_obj.account_name,"alias":account_obj.alias,"firstName":account_obj.first_name,
        "lastName":account_obj.last_name,"email":account_obj.email,"addressLine1":account_obj.address_line1,
        "addressLine2":account_obj.address_line2,"city":account_obj.city,"state":account_obj.state,
        "country":account_obj.country,"pincode":account_obj.pin_code,"mobileNo0":account_obj.contact_no,
        "mobileNo1":account_obj.contact_no1,"openingBalance":account_obj.opening_balance,"group":group_obj,
        "accounttype":accounttype_obj_new}
        return HttpResponse(json.dumps({"accountInfo":accountInfo,"status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")

def show_transactions_of_single_account(request):
    if request.user.is_authenticated():
        json_obj = json.loads(request.body)
        pageNo = data_dictonary['pageNo']
        entriesPerPage = data_dictonary['entriesPerPage']
        excludePageEntries = (pageNo - 1) * entriesPerPage
        nextPageEntries = excludePageEntries + entriesPerPage

        if json_obj['start_date'] == None:
            account_id = json_obj['account_id']
            account_id = int(account_id)
            transactionList = []
            account_obj_new = Account.objects.get(id=account_id)
            obj_new = {"account_name":account_obj_new.account_name}
            transaction_obj = Transaction.objects.filter(transaction_record__account__id=account_id)[excludePageEntries:nextPageEntries]
            for i in transaction_obj:
                date = int(i.transaction_date.strftime('%s')) * 1000
                transactiontype_obj = i.transactiontype.optionType
                obj = {"id":i.id,"transaction_date":date,"description":i.description,"transactiontype":dict(TransactionType.PAYMENTCHOICES)[transactiontype_obj]}
                transaction_record_obj = i.transaction_record.all()
                transactionRecordList = []
                for j in transaction_record_obj:
                    account_obj = j.account
                    obj1 = {"account_name":j.account.account_name,"amount":j.amount,"is_debit":j.is_debit}
                    transactionRecordList.append(obj1)
                obj.update({"transaction_record_list":transactionRecordList})
                transactionList.append(obj)
        else:
            start_date = json_obj['start_date']
            start_date = int(start_date)
            account_id = json_obj['account_id']
            account_obj_new = Account.objects.get(id=account_id)
            obj_new = {"account_name":account_obj_new.account_name}
            start_date = datetime.datetime.fromtimestamp(start_date/1000)
            accountingyear_obj = AccountingYear.objects.get(start_date=start_date,user__id=request.user.id)
            try:
                transaction_obj = accountingyear_obj.transaction.filter(transaction_record__account__id=account_id)
            except AccountingYear.DoesNotExist:
                return HttpResponse(json.dumps({'validation':"There are no transactions for this account yet.","status":False}), content_type="application/json")
            transactionList = []
            for i in transaction_obj:
                date = int(i.transaction_date.strftime('%s')) * 1000
                transactiontype_obj = i.transactiontype.optionType
                obj = {"id":i.id,"transaction_date":date,"description":i.description,"transactiontype":dict(TransactionType.PAYMENTCHOICES)[transactiontype_obj]}
                transaction_record_obj = i.transaction_record.all()
                transactionRecordList = []
                for j in transaction_record_obj:
                    account_obj = j.account
                    obj1 = {"account_name":j.account.account_name,"amount":j.amount,"is_debit":j.is_debit}
                    transactionRecordList.append(obj1)
                obj.update({"transaction_record_list":transactionRecordList})
                transactionList.append(obj)
        return HttpResponse(json.dumps({"transactionList":transactionList,"account_details":obj_new,"status":True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"You are not logged in yet.Please login to continue."}), content_type="application/json")
