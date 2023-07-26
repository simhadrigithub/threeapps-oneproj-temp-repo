from django.urls import path
from app2.views import *

urlpatterns =[
    path('third/',third,name='third'),
    path('fourth/',fourth,name='fourth'),
    path('home/',home,name='home'),
    
    
]