from django.shortcuts import render
from datetime import datetime 
# Create your views here.

class user : 
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        
        
def blog(request):
    context = {
        'name' : 'kanyakumari',
        'age' : '30',
        'skill' : ["python" , "django" , "react" , "fastapi" , "flask"],
        'user' : user("Nilesh shah" , 20),
        
        
    }
    
    return render(request , 'blog.html', context)
        
    
        
        
        
    
