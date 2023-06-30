from django.contrib import admin
from django.urls import path, include
from .views import list_courses, course_detail 

urlpatterns = [
    path('toate/', list_courses),
    path('<int:id>/', course_detail),
    
]