from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Device


class DeviceSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)

    class Meta:
        model = Device
        fields = "__all__"


class DeviceSetLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ["latitude", "longitude", "ping_time"]
