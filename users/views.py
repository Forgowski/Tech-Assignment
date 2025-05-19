from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from devices.models import Device
from .serializers import UserGetLocationSerializer


@api_view(["GET"])
def get_location(request, id):
    try:
        user = User.objects.get(id=id)
        device = Device.objects.get(user=user)
        serializer = UserGetLocationSerializer(device)
        return Response(serializer.data)

    except User.DoesNotExist:
        return Response(
            {"detail": "Device not found."}, status=status.HTTP_404_NOT_FOUND
        )
