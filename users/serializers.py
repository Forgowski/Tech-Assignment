from rest_framework import serializers

from devices.models import Device

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']

class UserGetLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'latitude', 'longitude', 'timestamp']

