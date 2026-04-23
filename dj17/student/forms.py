from django import forms 
from .models import student_table 

class student_form(forms.ModelForm):
    class Meta : 
        model = student_table 
        fields = ['name' , 'age' ,'roll_No' , 'wclass']
                
     