from django.contrib import admin
from .models import Account,Task
# Register your models here.
admin.site.register(Task)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['email','first_name', 'last_name','phone','address','gender']
admin.site.register(Account, AccountAdmin)
