from rest_framework import serializers
from .models import MetamaskUser

class MetamaskUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetamaskUser
        fields = "__all__"