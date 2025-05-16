from django.urls import path
from . import views

urlpatterns =[
    path('<id>/assign/', views.assign_the_user),
    path('<id>/location/', views.set_location)
]