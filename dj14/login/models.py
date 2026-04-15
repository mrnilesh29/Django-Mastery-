from django.db import models

# Create your models here.

class login_users(models.Model) : 
    username = models.CharField(max_length=500)
    password = models.IntegerField()
    
    