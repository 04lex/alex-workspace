from django.shortcuts import render
from .models import Course

# Create your views here.

def list_courses(request):
    cursurile = Course.objects.all()
    context = {'cursuri': cursurile}
    return render(request, 'list.html', context)

def course_detail(request, id):
    curs = Course.objects.get(pk=id)
    context = {'curs':curs}
    return render(request, 'detail.html', context)
