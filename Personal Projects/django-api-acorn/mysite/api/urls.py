from django.urls import path
from . import views

urlpatterns = [
    # path pentru a crea un post
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blogpost-view-create'),
    # path pentru a putea updata, delete, retrieve post
    path('blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name='update'),
]
