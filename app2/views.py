from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def third(request):
    return render(request,'third.html')
def fourth(request):
    return render(request,'fourth.html')

def home(request):
    return HttpResponse("<h1>http response is in the form of string</h1>")
