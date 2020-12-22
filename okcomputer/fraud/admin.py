from django.contrib import admin
from fraud.models import UserProfileInfo,Transaction
# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(Transaction)
