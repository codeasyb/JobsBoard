from rest_framework import serializers

from joboffer.models import JobOffer

class JobOfferSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobOffer
        fields = "__all__"