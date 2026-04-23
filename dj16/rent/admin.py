from django.contrib import admin
from .models import Rented_people

# Register your models here.

@admin.register(Rented_people)
class Rented_peopleAdmin(admin.ModelAdmin):
    list_display = ('name','age')
    list_filter = ('age',)