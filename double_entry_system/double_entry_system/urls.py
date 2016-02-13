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

from .views import(
   register_new_user,
   user_login,
   logout,
   home,
   add_acc_validity_date,
   create_new_user_account,
   list_of_accounting_years,
   show_account_names,
   get_groups_from_db,
   get_transactiontype_from_db,
   transaction_for_account,
   show_all_transactions,
   show_current_balance,
   show_account_details,
   get_accounttype_from_db,
   add_group,
   get_account_details,
   save_edit_account,
   show_transactions_of_single_account,
   registration,
   userLogin,
   userHome,
   myAcc,
   myAccHomePage,
   menu,
   summary,
   accounting,
   newUserAccount,
   footer,
   accountDetailBasedOnYear,
   accountMenu,
   account,
   activities,
   show_all_transactions_of_one_year,
   show_user_details,
   transactionDetails,
   )

urlpatterns = [
    # Akash
    url(r'^admin/', admin.site.urls),
    url(r'^register_new_user/$', register_new_user),
    url(r'^user_login/$', user_login),
    url(r'^logout/$', logout),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', home),
    url(r'^add_acc_validity_date/$', add_acc_validity_date),
    url(r'^create_new_user_account/$', create_new_user_account),
    url(r'^list_of_accounting_years/$', list_of_accounting_years),
    url(r'^show_account_names/$', show_account_names),
    url(r'^get_groups_from_db/$', get_groups_from_db),
    url(r'^get_transactiontype_from_db/$', get_transactiontype_from_db),
    url(r'^transaction_for_account/$', transaction_for_account),
    url(r'^show_all_transactions/$', show_all_transactions),
    url(r'^show_account_details/$', show_account_details),
    url(r'^get_accounttype_from_db/$', get_accounttype_from_db),
    url(r'^show_current_balance/$', show_current_balance),
    url(r'^add_group/$', add_group),
    url(r'^get_account_details/$', get_account_details),
    url(r'^save_edit_account/$', save_edit_account),
    url(r'^show_transactions_of_single_account/$', show_transactions_of_single_account),
    url(r'^show_all_transactions_of_one_year/$', show_all_transactions_of_one_year),
    url(r'^show_user_details/$', show_user_details),


    # akshay
    url(r'^registration/$', registration),
    url(r'^userLogin/$', userLogin),
    url(r'^userHome/$', userHome),

    url(r'^myAcc/$', myAcc),
    url(r'^myAccHomePage/$', myAccHomePage),
    url(r'^menu/$', menu),
    url(r'^summary/$', summary),
    url(r'^accounting/$', accounting),
    url(r'^newUserAccount/$', newUserAccount),
    url(r'^footer/$', footer),
    url(r'^accountDetailBasedOnYear/$', accountDetailBasedOnYear),
    url(r'^accountMenu/$', accountMenu),
    url(r'^account/$', account),
    url(r'^activities/$', activities),
    url(r'^transactionDetails/$', transactionDetails),
]
