from django.contrib import admin
from . import models


class UserView(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']


admin.site.register(models.CustomUser, UserView)
