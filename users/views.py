from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from devices.models import Device
from .serializers import UserGetLocationSerializer


@api_view(["GET"])
def get_location(request, id):
    try:
        device = Device.objects.get(id=id)

        serializer = UserGetLocationSerializer(device)

        return Response(serializer.data)

    except Device.DoesNotExist:
        return Response(
            {"detail": "Device not found."},
            status=status.HTTP_404_NOT_FOUND
        )
