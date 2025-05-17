from django.contrib.auth.models import User
from django.db import models


class Device(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    ping_time = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Device {self.id} (user: {f'{self.user_id.username}, id: {self.user_id.id}' if self.user_id else 'none'})"

    @staticmethod
    def is_any_assigned_and_active(user_id):
        return Device.objects.filter(user_id=user_id, is_active=True).exists()
