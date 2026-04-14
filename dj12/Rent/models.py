from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class rentdelatis(models.Model):
    name = models.CharField()
    age  = models.IntegerField(
        validators=[
            MinValueValidator(18) ,
            MaxValueValidator(65) 
        ]
    )
    purpose = models.CharField()
    hours = models.IntegerField()
    
    
    def __str__(self) : 
        return self.name
    