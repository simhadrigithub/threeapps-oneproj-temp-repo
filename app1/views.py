from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return render(request,'first.html')

def second(request):
    return render(request,'second.html')

def home(request):
    return HttpResponse("iam fine")