from django.shortcuts import render,redirect
from django.http import HttpResponse
from login.models import login_users

# Create your views here.

def login(request):
    if request.method == 'POST' : 
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        try :
            user = login_users.objects.get(username = username , password = password) 
            request.session['username'] = username
            return redirect(home)
        except Exception as err : 
            return HttpResponse(f"{err} hehhhheehehhehhhe")

    return render(request , 'login.html')

def home(request) : 
    if 'username' in request.session : 
        return render(request , 'home.html', {
            'username' : request.session['username']
        })
    else : 
        return HttpResponse("username session me store nhi hai bhai ")
    
    
def logout(request): 
    if 'username' in request.session: 
        request.session.pop("username")
        return redirect(login)
    return HttpResponse("Fake logout")


def signup(request) : 
    if request.method == "POST" :
        username = request.POST.get("username")
        password = request.POST.get("password") 
        
        if login_users.objects.filter(username = username).exists() : 
            return HttpResponse("user already exist")
        
        login_users.objects.create(username = username , password = password) 
        return redirect(login)
    return render(request , "signup.html")
            
        
    
    
        
    