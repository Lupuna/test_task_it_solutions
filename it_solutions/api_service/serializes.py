from rest_framework import serializers
from api_service.models import Advertisement


class AdvertisementGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertisement
        fields = ('__all__')
