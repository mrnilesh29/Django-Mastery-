from django.db import models

# Create your models here.

class Student(models.Model): 
    name = models.CharField()
    age = models.IntegerField()
    city = models.CharField()
    
    def __str__(self): 
        return self.name
    
    
    
class college(models.Model):
    college_name = models.CharField()
    year = models.IntegerField()
    admission_year = models.IntegerField()
    
    def __str__(self):
        return str(self.college_name)
    
    