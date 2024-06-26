from rest_framework import serializers
from .models import (MetamaskUser, Election,Vote,CampaignDonation,LoanRequest,LoanInterested,Campaign,Review,InterestConfirmedAndContractDone)
from django.db import models
class MetamaskUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetamaskUser
        fields = '__all__'

class ElectionSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model = Election
        fields = '__all__'
        
class CampaignDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model=CampaignDonation
        fields='__all__'
    
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

    def create(self, validated_data):
        election_foreign = validated_data.get('election_foreign')
        meta_user_key = validated_data.get('meta_user_key')
        existing_vote = Vote.objects.filter(election_foreign=election_foreign, meta_user_key=meta_user_key).first()
        if existing_vote:
            return existing_vote
        else:
            vote = Vote.objects.create(**validated_data)
            election = vote.election_foreign
            election.no_of_votes = models.F('no_of_votes') + 1
            election.save()
            return vote
        
class LoanRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=LoanRequest
        fields='__all__'
        
class LoanInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model=LoanInterested
        fields='__all__'
        
class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
class InterestConfirmedAndContractDoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=InterestConfirmedAndContractDone
        fields='__all__'
        