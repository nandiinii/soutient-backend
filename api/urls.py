from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (MetamaskUserViewSet, ElectionViewSet,VoteViewSet,CampaignDonationViewset,LoanInterestViewset,LoanRequestViewset)

router=DefaultRouter()
router.register('metamask-user-detail',MetamaskUserViewSet,basename='metamask-user-detail')
router.register('election',ElectionViewSet,basename='election')
router.register('vote', VoteViewSet, basename='vote')
router.register('campaign-donate', CampaignDonationViewset, basename='campaign-donate')
router.register('loan-request', LoanRequestViewset, basename='loan-request')
router.register('loan-interest', LoanInterestViewset, basename='loan-interest')
urlpatterns = [
    path('',include(router.urls)),
]
