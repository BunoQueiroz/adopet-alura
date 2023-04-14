from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tutor.views import TutorViewSet
from pet.views import PetViewSet, AdoptionViewSet
from shelter.views import ShelterViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('tutors', TutorViewSet, 'tutors')
router.register('pets', PetViewSet, 'pets')
router.register('shelters', ShelterViewSet, 'shelters')
router.register('adoptions', AdoptionViewSet, 'adoptions')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
