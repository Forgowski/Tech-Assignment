from django.urls import path
from . import views

urlpatterns =[
    path('<id>/location/', views.get_location),
]