from django.urls import path
from . import views

urlpatterns = [
    path('shop/<int:id>/', views.shop1, name="shop1"),
    path('shop/<str:name>' , views.shop1_name,name="shop1_name"),
    path('allshop/<int:name>/<int:name>' , views.allshops , name="all_shops")
    
]