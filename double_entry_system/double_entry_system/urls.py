"""double_entry_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Akash
    url(r'^admin/', admin.site.urls),
    url(r'^register_new_user/$', 'double_entry_system.views.register_new_user'),
    url(r'^user_login/$', 'double_entry_system.views.user_login'),
    url(r'^logout/$', 'double_entry_system.views.logout'),
    url(r'^account_creation_page/$', 'double_entry_system.views.account_creation_page'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^transactions/$', 'double_entry_system.views.transactions'),
    url(r'^$', 'double_entry_system.views.userLogin'),
    url(r'^add_acc_validity_date/$', 'double_entry_system.views.add_acc_validity_date'),
    url(r'^create_new_user_account/$', 'double_entry_system.views.create_new_user_account'),
    url(r'^list_of_accounting_years/$', 'double_entry_system.views.list_of_accounting_years'),
    url(r'^search_Transaction/$', 'double_entry_system.views.search_Transaction'),
    url(r'^show_account_names/$', 'double_entry_system.views.show_account_names'),
    url(r'^search_account_names/$', 'double_entry_system.views.search_account_names'),
    url(r'^get_groups_from_db/$', 'double_entry_system.views.get_groups_from_db'),
    url(r'^add_amount_to_cash_account/$', 'double_entry_system.views.add_amount_to_cash_account'),
    url(r'^debit_transaction_for_cash_account/$', 'double_entry_system.views.debit_transaction_for_cash_account'),
    url(r'^credit_transaction_for_cash_account/$', 'double_entry_system.views.credit_transaction_for_cash_account'),
    url(r'^debit_transaction_for_bank_account/$', 'double_entry_system.views.debit_transaction_for_bank_account'),
    url(r'^credit_transaction_for_bank_account/$', 'double_entry_system.views.credit_transaction_for_bank_account'),
    url(r'^show_all_debit_transactions/$', 'double_entry_system.views.show_all_debit_transactions'),
    url(r'^show_all_credit_transactions/$', 'double_entry_system.views.show_all_credit_transactions'),
    # url(r'^todays_debit/$', 'double_entry_system.views.todays_debit'),
    # url(r'^todays_credit/$', 'double_entry_system.views.todays_credit'),
    url(r'^show_current_balance/$', 'double_entry_system.views.show_current_balance'),
    url(r'^show_all_debit_amount/$', 'double_entry_system.views.show_all_debit_amount'),
    url(r'^show_all_credit_amount/$', 'double_entry_system.views.show_all_credit_amount'),
    url(r'^show_account_details/$', 'double_entry_system.views.show_account_details'),
    url(r'^get_accounttype_from_db/$', 'double_entry_system.views.get_accounttype_from_db'),


    # akshay
    url(r'^registration/$', 'double_entry_system.views.registration'),
    # url(r'^userLogin/$', 'double_entry_system.views.userLogin'),
    url(r'^myAcc/$', 'double_entry_system.views.myAcc'),
    url(r'^myAccHomePage/$', 'double_entry_system.views.myAccHomePage'),
    url(r'^menu/$', 'double_entry_system.views.menu'),
    url(r'^credit/$', 'double_entry_system.views.credit'),
    url(r'^debit/$', 'double_entry_system.views.debit'),
    url(r'^summary/$', 'double_entry_system.views.summary'),
    url(r'^accounting/$', 'double_entry_system.views.accounting'),
    url(r'^accountingCredit/$', 'double_entry_system.views.accountingCredit'),
    url(r'^accountingDebit/$', 'double_entry_system.views.accountingDebit'),
    url(r'^newUserAccount/$', 'double_entry_system.views.newUserAccount'),
    url(r'^footer/$', 'double_entry_system.views.footer'),
    url(r'^accountDetailBasedOnYear/$', 'double_entry_system.views.accountDetailBasedOnYear'),
]
