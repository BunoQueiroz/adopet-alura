from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tutor.views import TutorViewSet
from pet.views import PetViewSet

router = routers.DefaultRouter()
router.register('tutors', TutorViewSet, 'tutors')
router.register('pets', PetViewSet, 'pets')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
