from django.db import models
from distutils.command.upload import upload
from email.policy import default
# Create your models here.
class MetamaskUser(models.Model):
    metamask_id = models.CharField(max_length = 100)
    date_time = models.DateTimeField()
    def __str__(self):
        return self.metamask_id

class Election(models.Model):
    name=models.CharField(max_length=100)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    no_of_votes=models.IntegerField(blank=True,null=True)
    image=models.ImageField(upload_to='elction_images',blank=True,null=True)
    owner=models.CharField(max_length=200,blank=True,null=True)
    description=models.CharField(max_length=1000 ,blank=True,null=True)
    location=models.CharField(max_length=200,blank=True,null=True)
    is_open=models.BooleanField(default=True)
    def __str__(self):
        return self.name
    
class Vote(models.Model):
    election_foreign=models.ForeignKey(Election,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    meta_user_key=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class CampaignDonation(models.Model):
    from_address=models.CharField(max_length=200)
    to_address=models.CharField(max_length=200)
    campaign_address=models.CharField(max_length=200)
    date_time=models.DateTimeField()
    amount=models.DecimalField(max_digits = 20, decimal_places = 10)
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class LoanRequest(models.Model):
    requester_metamask_id=models.CharField(max_length=200)
    requester_name=models.CharField(max_length=100)
    institutional_address=models.TextField(max_length=2000)
    need=models.CharField(max_length=200)
    grade=models.CharField(max_length=10)
    image=models.ImageField(upload_to='student_loan_images',blank=True,null=True)
    fund_needed=models.DecimalField(max_digits = 20, decimal_places = 10)
    
    def __str__(self):
        return self.need
    
class LoanInterested(models.Model):
    donator_metamask_id=models.CharField(max_length=200)
    loan_request_foreign=models.ForeignKey(LoanRequest,on_delete=models.CASCADE)
    needy_name=models.CharField(max_length=100)
    needy_metamask_id=models.CharField(max_length=200)
    datetime=models.DateTimeField()
    contact_email=models.EmailField()
    message=models.CharField(max_length=2000)
    def __str__(self):
        return self.needy_name

class Campaign(models.Model):
    owner=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    target=models.DecimalField(max_digits = 20, decimal_places = 8)
    deadline=models.IntegerField()
    image_url=models.URLField()
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    reviewer_metamask_id = models.CharField(max_length=200)
    reviewer_name = models.CharField(max_length=100,default="Anonymous")
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.reviewer_name

class InterestConfirmedAndContractDone(models.Model):
    student_address=models.CharField(max_length=300)
    loan_provider_address=models.CharField(max_length=300)
    amount=models.DecimalField(max_digits = 20, decimal_places = 10)
    description=models.TextField(max_length=1000)
    created_date=models.DateTimeField()
    proposed_date_repayment=models.DateField()
    
    def __str__(self):
        return self.description