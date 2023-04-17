from django.contrib import admin
from .models import Tutor

class TutorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email']
    search_fields = ['email', 'full_name']
    list_editable = ['full_name',]
    list_display_links = ['email',]
    ordering = ['id',]

admin.site.register(Tutor, TutorAdmin)
