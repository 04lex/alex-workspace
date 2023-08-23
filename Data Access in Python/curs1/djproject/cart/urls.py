
from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "cart"
urlpatterns = [
    path('', cart_view, name="cart_details"),
    path('clearcart/', clear_cart_view, name="clear"),
    path('addtocart/', add_product_to_cart_view, name="add")
   
]
