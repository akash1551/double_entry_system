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
    url(r'^account_creation_page/$', 'double_entry_system.views.account_creation_page'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^transactions/$', 'double_entry_system.views.transactions'),
    url(r'^$', 'double_entry_system.views.home'),
    url(r'^add_acc_validity_date/$', 'double_entry_system.views.add_acc_validity_date'),
    url(r'^create_new_user_account/$', 'double_entry_system.views.create_new_user_account'),
    url(r'^list_of_accounting_years/$', 'double_entry_system.views.list_of_accounting_years'),
    url(r'^my_cash_accounts/$', 'double_entry_system.views.my_cash_accounts'),
    url(r'^my_bank_accounts/$', 'double_entry_system.views.my_bank_accounts'),
    url(r'^show_all_transactions/$', 'double_entry_system.views.show_all_transactions'),
    url(r'^show_transaction/$', 'double_entry_system.views.show_transaction'),
    url(r'^search_Transaction/$', 'double_entry_system.views.search_Transaction'),
    url(r'^show_creditor/$', 'double_entry_system.views.show_creditor'),
    url(r'^show_debtor/$', 'double_entry_system.views.show_debtor'),
    url(r'^show_all_creditors/$', 'double_entry_system.views.show_all_creditors'),
    url(r'^show_all_debtors/$', 'double_entry_system.views.show_all_debtors'),
    url(r'^add_debit_transaction/$', 'double_entry_system.views.add_debit_transaction'),
    url(r'^show_account_names/$', 'double_entry_system.views.show_account_names'),
    url(r'^search_account_names/$', 'double_entry_system.views.search_account_names'),
    url(r'^show_all_debit/$', 'double_entry_system.views.show_all_debit'),
    url(r'^show_all_credit/$', 'double_entry_system.views.show_all_credit'),
    url(r'^get_groups_from_db/$', 'double_entry_system.views.get_groups_from_db'),
    url(r'^send_account_names/$', 'double_entry_system.views.send_account_names'),
    url(r'^add_credit_transaction/$', 'double_entry_system.views.add_credit_transaction'),


    # akshay
    url(r'^registration/$', 'double_entry_system.views.registration'),
    url(r'^userLogin/$', 'double_entry_system.views.userLogin'),
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
    url(r'^accountDetailBasedOnYear/$', 'double_entry_system.views.accountDetailBasedOnYear'),
]
