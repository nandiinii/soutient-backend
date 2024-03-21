from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import MetamaskUserViewSet

router=DefaultRouter()
router.register('metamask-user-detail',MetamaskUserViewSet,basename='metamask-user-detail')
urlpatterns = [
    path('',include(router.urls)),
]