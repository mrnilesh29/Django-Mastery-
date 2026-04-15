from django.contrib import admin
from login.models import login_users

# Register your models here.

@admin.register(login_users) 
class show_login_users(admin.ModelAdmin) : 
    list_display = ["username" , "password"]
    
    