from django.contrib import admin

from .models import Account

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ['email','phone','address','gender', 'country']
admin.site.register(Account, AccountAdmin)
