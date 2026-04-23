from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator


# Create your models here.

class student_table(models.Model):
    name = models.CharField()
    age = models.IntegerField(validators= [MinValueValidator(10) , MaxValueValidator(60)])
    roll_No = models.IntegerField() 
    wclass = models.IntegerField()  
    
    
    def __str__(self):
        return self.name 
     
    