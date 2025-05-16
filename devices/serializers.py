from rest_framework import serializers
from .models import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class DeviceSetLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['latitude', 'longitude', 'ping_time']
