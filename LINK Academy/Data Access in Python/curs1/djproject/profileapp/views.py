from django.shortcuts import render

# Create your views here.

def profile_view(request):
    return render(request, 'profile.html')