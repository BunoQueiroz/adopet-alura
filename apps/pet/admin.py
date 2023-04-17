from django.contrib import admin
from pet.models import Adoption, Pet

class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'shelter', 'size', 'adopted']

admin.site.register(Adoption)
admin.site.register(Pet, PetAdmin)
