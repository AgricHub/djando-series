from django.urls import path
from . import views

urlpatterns = [
    path('', views.daniel_home, name='daniel_home'),
    # Add more URL patterns for other pages
]
