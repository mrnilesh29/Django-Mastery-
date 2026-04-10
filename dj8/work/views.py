from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def work1(request) : 
    name = "Akarsh vyas"
    user1 = {
        "name" : "nilesh shah",
        "work" : "AI engineer",
        "branch" : "AIML", 
        "year" : 3 ,
        "skills" : ["python","django","FastApi","AiMl"]
    }
    return render(request,"work1.html", user1 )