from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tutor.views import TutorViewSet
from pet.views import PetViewSet
from shelter.views import ShelterViewSet

router = routers.DefaultRouter()
router.register('tutors', TutorViewSet, 'tutors')
router.register('pets', PetViewSet, 'pets')
router.register('shelters', ShelterViewSet, 'shelters')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
