from django.shortcuts import render  
from django.htpp import HtppResponse  


# Create your views here. \


def Dhoni(request):
    return HtppResponse('<h1>Captain of csk</h1>')  
