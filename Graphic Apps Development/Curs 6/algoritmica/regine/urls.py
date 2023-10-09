from django.contrib import admin
from django.urls import path, include
from .views import solutii_view

urlpatterns = [
    path('<int:regine>', solutii_view),
    
]
