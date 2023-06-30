from django.shortcuts import render
from .models import CustomUser

# Create your views here.
from .forms import CustomUserRegistrationForm

def registerView(request):
    form = CustomUserRegistrationForm
    context = {"form": form}
    return render(request, "register.html", context)