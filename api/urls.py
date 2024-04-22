from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (MetamaskUserViewSet, ElectionViewSet,VoteViewSet,CampaignViewset,CampaignDonationViewset,LoanInterestViewset,
                    LoanRequestViewset,ReviewViewset,InterestConfirmedAndContractDoneViewSet)

router=DefaultRouter()
router.register('metamask-user-detail',MetamaskUserViewSet,basename='metamask-user-detail')
router.register('election',ElectionViewSet,basename='election')
router.register('vote', VoteViewSet, basename='vote')
router.register('campaign-donate', CampaignDonationViewset, basename='campaign-donate')
router.register('loan-request', LoanRequestViewset, basename='loan-request')
router.register('loan-interest', LoanInterestViewset, basename='loan-interest')
router.register('campaign', CampaignViewset, basename='campaign')
router.register('review', ReviewViewset, basename='review')
router.register('interest-confirmed-and-contract-done', InterestConfirmedAndContractDoneViewSet, basename='interest-confirmed-and-contract-done')
urlpatterns = [
    path('',include(router.urls))
]
