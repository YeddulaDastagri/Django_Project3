from django.shortcuts import render 
from django.htpp import HtppResponse  

# Create your views here. 

def Rohit(request):
    return HtppResponse('<h1>Captain of Mumbai Indians</h1>')
