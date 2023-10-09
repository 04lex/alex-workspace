from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def blog_list_view(request):
    print(request.GET.get("search"))
    search = request.GET.get("search")
    if search:
        posts = Post.objects.filter(title__contains=search) 
    else:
        posts =  Post.objects.all()
    return render(request, 'blog_list.html', {'posts':posts})

def blog_details_view(request, slug):
    post_details = get_object_or_404(Post, slug=slug)
    return render(request, 'blog_details.html', {'post': post_details})
