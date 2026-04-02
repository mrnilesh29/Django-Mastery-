from django.shortcuts import render
from django.http import HttpResponse , request

# Create your views here.

def work1(request): 
    return HttpResponse("this is work 1")


def work2(request) : 
    return HttpResponse("this is work 2")


