from django.db import models

# Create your models here.

class shop(models.Model):
    shop_name = models.CharField()
    owner_name = models.CharField()
    contact_number = models.IntegerField()
    email_id = models.EmailField(unique=True)
    open_date = models.DateTimeField(auto_now_add=True)
    
    