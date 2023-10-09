
from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = 'profileapp'

urlpatterns = [
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  
    path('accounts/profile/', profile_view)
]



