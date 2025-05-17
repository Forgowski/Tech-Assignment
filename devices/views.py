from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Device
from .serializers import DeviceSerializer, DeviceSetLocationSerializer


@api_view(["POST"])
def assign_the_user(request, id):
    user_id = request.data.get("user_id")

    if Device.is_any_assigned_and_active(user_id):
        return Response(
            {
                "user_id": [
                    "A user can have only one assigned and active device at a time."
                ]
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        device = Device.objects.get(id=id)
    except Device.DoesNotExist:
        return Response(
            {"detail": "Device not found."}, status=status.HTTP_404_NOT_FOUND
        )

    request.data["is_active"] = True
    serializer = DeviceSerializer(instance=device, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def set_location(request, id):
    try:
        device = Device.objects.get(id=id)
    except Device.DoesNotExist:
        return Response(
            {"detail": "Device not found."}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = DeviceSetLocationSerializer(
        instance=device, data=request.data, partial=True
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_map(request):
    try:
        devices = Device.objects.filter(user_id__isnull=False)
        serializer = DeviceSerializer(devices, many=True)

        return Response(serializer.data)

    except Device.DoesNotExist:
        return Response(
            {"detail": "Devices not found."}, status=status.HTTP_404_NOT_FOUND
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_devices(request):
    try:
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)

        return Response(serializer.data)

    except Device.DoesNotExist:
        return Response(
            {"detail": "Devices not found."}, status=status.HTTP_404_NOT_FOUND
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)