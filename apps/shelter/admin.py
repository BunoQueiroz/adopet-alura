from django.contrib import admin
from shelter.models import Shelter

class ShelterAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'state', 'phone']

admin.site.register(Shelter, ShelterAdmin)
