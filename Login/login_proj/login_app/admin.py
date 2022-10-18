from django.contrib import admin
from login_app.models import AccountsData, SignUp, Contact

# Register your models here.
admin.site.register(SignUp)
admin.site.register(AccountsData)
admin.site.register(Contact)