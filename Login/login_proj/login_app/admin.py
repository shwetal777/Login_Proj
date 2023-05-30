from django.contrib import admin
from login_app.models import AccountsData, SignUp, Contact

# Register your models here.


class SignUpAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'address')
    list_filter = ('username',)


class AccountsDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'account_no', 'account_balance', 'currency', 'city')
    search_fields = ('name',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'desc', 'date')
    search_fields = ('name',)


admin.site.register(SignUp, SignUpAdmin)
admin.site.register(AccountsData, AccountsDataAdmin)
admin.site.register(Contact, ContactAdmin)