from django.contrib import admin
admin.autodiscover()
from accounts.models import Address,Account,AccountType,AccountingYear,TransactionType,Company
# Register your models here.

admin.site.register(Address)
admin.site.register(Account)
admin.site.register(AccountType)
admin.site.register(AccountingYear)
admin.site.register(TransactionType)
admin.site.register(Company)
