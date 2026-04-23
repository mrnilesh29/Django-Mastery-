from django.contrib import admin
from.models import student_table 

# Register your models here.

@admin.register(student_table) 
class studetadmin(admin.ModelAdmin):
    list_display = ['name' ,'age' ,'roll_No' ,]