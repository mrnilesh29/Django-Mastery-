from django.db import models
from django.urls import reverse
# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    shop_No = models.CharField(max_length=200)

    def __str__(self):
        return self.name

def get_absolute_url(self):
    return reverse('shop_detail', kwargs={'pk': self.pk})

