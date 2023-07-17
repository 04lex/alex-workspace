from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = "store"
urlpatterns = [
    path('categories/', store_list_view),
    path('jsonproducts/', jsonproducts_view),
    path('csvproducts/', csvproducts_view),
    # Aici e greseala -> trebuia adaugat name="store_details_view"
    path('<slug>/', store_details_view, name="store_details_view"),
    
]