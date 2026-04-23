from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Rented_people(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    licnece = models.BooleanField(default=False)
    hours = models.IntegerField(validators=[MinValueValidator(2)])

    def __str__(self):
        return self.name




