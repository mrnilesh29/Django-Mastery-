from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class rent_details(models.Model): 
    name = models.CharField()
    purpose = models.TextField()
    age = models.IntegerField(
        validators=[
            MinValueValidator(18),
            MaxValueValidator(65)
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): 
        return self.name 
    