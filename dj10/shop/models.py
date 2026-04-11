from django.db import models

# Create your models here.

class surendera_store(models.Model):
    name = models.CharField(max_length=100 , unique=True , null= False,blank=False)
    stable = models.IntegerField()
    owner = models.CharField()
    
    def __init__(self):
        return self.name  
        
    
        