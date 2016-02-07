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
    url(r'^$', 'double_entry_system.views.home'),
    url(r'^add_acc_validity_date/$', 'double_entry_system.views.add_acc_validity_date'),
    url(r'^create_new_user_account/$', 'double_entry_system.views.create_new_user_account'),
    url(r'^list_of_accounting_years/$', 'double_entry_system.views.list_of_accounting_years'),
    url(r'^search_Transaction/$', 'double_entry_system.views.search_Transaction'),
    url(r'^show_account_names/$', 'double_entry_system.views.show_account_names'),
    url(r'^search_account_names/$', 'double_entry_system.views.search_account_names'),
    url(r'^get_groups_from_db/$', 'double_entry_system.views.get_groups_from_db'),
    url(r'^get_transactiontype_from_db/$', 'double_entry_system.views.get_transactiontype_from_db'),
    url(r'^transaction_for_account/$', 'double_entry_system.views.transaction_for_account'),
    url(r'^show_all_transactions/$', 'double_entry_system.views.show_all_transactions'),
    url(r'^show_current_balance/$', 'double_entry_system.views.show_current_balance'),
    url(r'^show_all_debit_and_credit_amount/$', 'double_entry_system.views.show_all_debit_and_credit_amount'),
    url(r'^show_account_details/$', 'double_entry_system.views.show_account_details'),
    url(r'^get_accounttype_from_db/$', 'double_entry_system.views.get_accounttype_from_db'),
    url(r'^show_current_balance/$', 'double_entry_system.views.show_current_balance'),
    url(r'^add_group/$', 'double_entry_system.views.add_group'),
    url(r'^get_account_details/$', 'double_entry_system.views.get_account_details'),


    # akshay
    url(r'^registration/$', 'double_entry_system.views.registration'),
    url(r'^userLogin/$', 'double_entry_system.views.userLogin'),
    url(r'^userHome/$', 'double_entry_system.views.userHome'),

    url(r'^myAcc/$', 'double_entry_system.views.myAcc'),
    url(r'^myAccHomePage/$', 'double_entry_system.views.myAccHomePage'),
    url(r'^menu/$', 'double_entry_system.views.menu'),
    url(r'^summary/$', 'double_entry_system.views.summary'),
    url(r'^accounting/$', 'double_entry_system.views.accounting'),
    url(r'^newUserAccount/$', 'double_entry_system.views.newUserAccount'),
    url(r'^footer/$', 'double_entry_system.views.footer'),
    url(r'^accountDetailBasedOnYear/$', 'double_entry_system.views.accountDetailBasedOnYear'),
]
