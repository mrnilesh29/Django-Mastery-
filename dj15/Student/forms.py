from django import forms 
from .models import Student_details 

class Student_Form(forms.ModelForm): 
    class Meta: 
        model = Student_details 
        fields = ['name', 'age', 'email']
        
        
  
