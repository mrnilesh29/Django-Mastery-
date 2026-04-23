from django.shortcuts import render,redirect,get_object_or_404
from .forms import Student_Form
from django.http import HttpResponse
from .models import Student_details

# Create your views here.


def student1(request) : 
    if request.method == 'POST' : 
        form = Student_Form(request.POST) 
        if form.is_valid(): 
            form.save()
            return render(request , 'thankyou.html')
        else : 
            return HttpResponse("Enter a vaild values") 
    return render(request, 'add_student.html', {'form': Student_Form()})


def student_list(request): 
    student = Student_details.objects.all()
    return render(request , 'student_list.html' , {'student' : student})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Student_details
from .forms import Student_Form

def student_edit(request, id):   # 👈 id lena zaruri hai
    student = get_object_or_404(Student_details, id=id)  # ✔️ model use karo

    if request.method == "POST":
        form = Student_Form(request.POST, instance=student)  # ✔️ instance pass

        if form.is_valid():
            form.save()
            return redirect('studentlist')

    else:
        form = Student_Form(instance=student)  # ✔️ existing data show

    return render(request, "studentedit.html", {'form': form})
    
        
        
    

    

