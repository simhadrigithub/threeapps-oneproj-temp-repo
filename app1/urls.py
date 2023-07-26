from django.urls import path
from app1.views import *

urlpatterns =[
    path('first/',first,name='first'),
    path('second',second,name='second'),
    path('home',home,name='home'),
]