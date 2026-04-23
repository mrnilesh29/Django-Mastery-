from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import student_form 
from .models import student_table 

def student_add(request): 
    if request.method == 'POST': 
        form = student_form(request.POST)
        if form.is_valid(): 
            form.save()
            return render(request, "thankyou.html")
        else: 
            return HttpResponse("Enter valid values")

    form = student_form()
    return render(request, 'student_add.html', {'form': form})

def student_list(request): 
    student = student_table.objects.all()
    return render(request , 'studentlist.html' ,{'student' : student})

def student_details(request,id) : 
    student = student_table.objects.get(id = id)
    return render(request , 'studentdetails.html', {'student' : student})

def student_edit(request , id) : 
    student = student_table.objects.get(id=id)
    if request.method == 'POST' : 
        form = student_form(request.POST, instance = student ) 
        if form.is_valid(): 
            form.save()
        return redirect('studentlist')
    else : 
         form = student_form(instance=student)

    return render(request, 'student_add.html', {'form': form})


def student_delete(request , id) : 
    student = student_table.objects.get(id = id)
    if request.method == 'POST' :
        student.delete()
        return redirect('studentlist')
    return render(request , 'student_confrim_delete.html' , {'student' : student})

        
    

            
            
    
        
         

    