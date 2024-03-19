from django.db import models

# Create your models here.
class MetamaskUser(models.Model):
    metamask_id = models.CharField(max_length = 100)
    date_time = models.DateTimeField()
    def __str__(self):
        return self.metamask_id
    
    