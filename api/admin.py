from django.contrib import admin
from .models import (MetamaskUser,Election,Vote)

# Register your models here.
admin.site.register(MetamaskUser)
admin.site.register(Election)
admin.site.register(Vote)