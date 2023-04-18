from django.contrib import admin
from pet.models import Adoption, Pet

class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'shelter', 'size', 'adopted']

class AdoptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'pet', 'tutor', 'date']
    list_display_links = ['id',]
    list_filter = ['tutor',]
    ordering = ['date',]
    search_fields = ['pet',]

admin.site.register(Adoption, AdoptionAdmin)
admin.site.register(Pet, PetAdmin)
