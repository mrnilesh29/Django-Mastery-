from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

def demo(request):
    data = {'name': 'Nilesh', 'age': 20}
    return JsonResponse(data)

# Create your views here.

def teacher1(request) : 
   return HttpResponse("this is the htttp response from teacher")