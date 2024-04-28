from django.contrib import admin
from .models import (MetamaskUser,Election,Vote,CampaignDonation,LoanRequest,LoanInterested,Campaign, Review,InterestConfirmedAndContractDone)

# Register your models here.
admin.site.register(MetamaskUser)
admin.site.register(Election)
admin.site.register(Vote)
admin.site.register(CampaignDonation)
admin.site.register(LoanInterested)
admin.site.register(LoanRequest)
admin.site.register(Campaign)
admin.site.register(Review)
admin.site.register(InterestConfirmedAndContractDone)
# admin.site.register(Review)