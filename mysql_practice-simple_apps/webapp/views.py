from django.shortcuts import render
from django.http import HttpResponse
from .models import Courses


# Create your views here.
def index(request):
    # return HttpResponse("This is ratting app")
    if request.method == 'POST':
        subject= request.POST.get('subject')
        course=request.POST.get('course')
        ratting=request.POST.get('ratting')
        ratting_info= Courses(subject1=subject,course1=course, ratting1=ratting)
        ratting_info.save()
        return render(request, 'ratting_app/form.html')
    else:
        return render(request, 'ratting_app/form.html')
    # F:\courses\edx-Web_Dev\django\mysql_practice\mysql_practice\webapp\templates\ratting-app\form.html