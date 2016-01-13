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
    url(r'^admin/', admin.site.urls),
#    url(r'^show_registration_page/', 'double_entry_system.views.show_registration_page'),
#    url(r'^register_user/', 'double_entry_system.views.register_user'),
    url(r'^register_new_user/$', 'double_entry_system.views.register_new_user'),
    url(r'^user_login/', 'double_entry_system.views.user_login'),
    url(r'^auth_view/', 'double_entry_system.views.auth_view'),
    url(r'^account_creation_page/', 'double_entry_system.views.account_creation_page'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^transactions/', 'double_entry_system.views.transactions'),
    url(r'^$', 'double_entry_system.views.home'),

    # akshay
    url(r'^registration/$', 'double_entry_system.views.registration'),
    url(r'^userLogin/$', 'double_entry_system.views.userLogin'),
    url(r'^myAcc/$', 'double_entry_system.views.myAcc'),


]
