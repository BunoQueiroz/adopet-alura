from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tutor.views import TutorViewSet, ProfileTutorViewSet
from pet.views import PetViewSet, AdoptionViewSet
from shelter.views import ShelterViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import ObtainAuthToken
from core.views import APIUserViewSet

router = routers.DefaultRouter()
router.register('tutors', TutorViewSet, 'tutors')
router.register('pets', PetViewSet, 'pets')
router.register('shelters', ShelterViewSet, 'shelters')
router.register('adoptions', AdoptionViewSet, 'adoptions')
router.register('tutor-profiles', ProfileTutorViewSet, 'tutor-profiles')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', ObtainAuthToken.as_view(), name='api-tokens'),
    path('api-users/', APIUserViewSet.as_view({'post': 'create'}), name='api-users'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
