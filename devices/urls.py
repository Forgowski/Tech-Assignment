from django.urls import path

from . import views

urlpatterns = [
    path("devices/<id>/assign/", views.assign_the_user),
    path("devices/<id>/location/", views.set_location),
    path("map/", views.get_map),
    path("devices/", views.get_devices)
]
