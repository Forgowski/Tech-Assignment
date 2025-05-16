from rest_framework import serializers

from devices.models import Device


class UserGetLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'latitude', 'longitude', 'timestamp']

