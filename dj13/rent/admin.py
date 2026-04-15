from django.contrib import admin
from rent import models

# Register your models here.

@admin.register(models.rent_details)
class rent_register(admin.ModelAdmin) : 
    list_display = ['name' , 'age' , 'created_at']
    search_fields = ['name']
    sortable_by = ['name']
    list_filter = ['name']
    