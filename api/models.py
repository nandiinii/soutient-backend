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