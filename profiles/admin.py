from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from profiles.models import User


class MyUserAdmin(ModelAdmin):
    model = User
    icon = '<i class="material-icons">supervisor_account</i>'

admin.site.register(User, MyUserAdmin)