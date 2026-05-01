from django.urls import path
from .views import upload_profile, view_profile

urlpatterns = [
    path('upload/', upload_profile, name='upload'),
    path('view/', view_profile, name='view_profile'),   # 👈 IMPORTANT
]