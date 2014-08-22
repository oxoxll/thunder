from django.contrib import admin
from models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id','account', 'passwd') 
    # search_fields = ('account',)

admin.site.register(Account, AccountAdmin)
