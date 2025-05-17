from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from devices.models import Device
from .serializers import UserGetLocationSerializer


@api_view(["GET"])
def get_location(request, id):
    try:
        device = Device.objects.get(id=id)
        if not device.user_id or not device.is_active:
            return Response(
                {"detail": "Device is not assigned or not active."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    except Device.DoesNotExist:
        return Response(
            {"detail": "Device not found."}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = UserGetLocationSerializer(device)
    return Response(serializer.data)
