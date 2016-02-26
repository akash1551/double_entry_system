from django.contrib import admin
admin.autodiscover()
from accounts.models import UserDetail,Account,AccountType,AccountingYear,TransactionType,Company,Group
from accounts.models import Transaction,TransactionRecord
# Register your models here.

admin.site.register(UserDetail)
admin.site.register(Account)
admin.site.register(AccountType)
admin.site.register(AccountingYear)
admin.site.register(TransactionType)
admin.site.register(Company)
admin.site.register(Group)
admin.site.register(Transaction)
admin.site.register(TransactionRecord)
