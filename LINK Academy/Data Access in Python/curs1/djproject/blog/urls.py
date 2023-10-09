from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = "blog"
urlpatterns = [
    path('all/', blog_list_view),
    # Aici e greseala -> trebuia adaugat name="blog_details_view"
    path('<slug>/', blog_details_view, name="blog_details_view")
]