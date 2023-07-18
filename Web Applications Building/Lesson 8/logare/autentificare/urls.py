from django.contrib import admin
from django.urls import path, include
from .views import registerView

urlpatterns = [
    path('register/', registerView),
    
]
