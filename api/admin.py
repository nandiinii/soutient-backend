from django.contrib import admin
from .models import (MetamaskUser,Election,Vote,CampaignDonation,LoanRequest,LoanInterested)

# Register your models here.
admin.site.register(MetamaskUser)
admin.site.register(Election)
admin.site.register(Vote)
admin.site.register(CampaignDonation)
admin.site.register(LoanInterested)
admin.site.register(LoanRequest)