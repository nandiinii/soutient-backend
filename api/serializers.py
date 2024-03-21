from rest_framework import serializers
from .models import MetamaskUser, Election

class MetamaskUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetamaskUser
        fields = '__all__'

class ElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Election
        fields = '__all__'