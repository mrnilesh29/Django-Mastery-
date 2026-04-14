from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.rentdelatis)
class rented(admin.ModelAdmin): 
    list_display = ["name" , "age" , "hours","purpose"]
    search_fields = ['name', "purpose"]
    list_filter = ['name']
    ordering = ("age" , "name")
                    
                    
                    