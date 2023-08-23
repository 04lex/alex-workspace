from django.contrib import admin
from django.urls import path, include
from .views import *

from django.contrib.sitemaps.views import sitemap as view
# from django.contrib.sites import sitemaps
from store.sitemaps import ProductSitemap

app_name = "store"
urlpatterns = [
    path('categories/', store_list_view),
    path('jsonproducts/', jsonproducts_view),
    path('csvproducts/', csvproducts_view),
    path('pdfproducts/', pdfproducts_view),
     path('xmlhardcodat/', xml_view),
     path('sitemap.xml/', view, {'sitemaps': {'products':ProductSitemap, }},
     name="django.contrib.sitemaps.views"),
    path('testcookie/', cookie_view),
    path('testsession/', session_view),
    # Aici e greseala -> trebuia adaugat name="store_details_view"
    path('<slug>/', store_details_view, name="store_details_view"),
    # 
    
    
]