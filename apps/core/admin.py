from django.contrib import admin
from core.models import APIUser

class APIUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'company_or_user', 'type']
    list_display_links = ['email',]

admin.site.register(APIUser, APIUserAdmin)

