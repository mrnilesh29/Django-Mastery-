from django.urls import path
from .views import ShopListing, ShopDetail, ShopCreate, ShopUpdate, ShopDelete

urlpatterns = [
    # 📄 List view
    path('', ShopListing.as_view(), name='shop_list'),

    # 🔍 Detail view
    path('shop/<int:pk>/', ShopDetail.as_view(), name='shop_detail'),

    # ➕ Create
    path('shop/create/', ShopCreate.as_view(), name='shop_create'),

    # ✏️ Update
    path('shop/<int:pk>/update/', ShopUpdate.as_view(), name='shop_update'),

    # ❌ Delete
    path('shop/<int:pk>/delete/', ShopDelete.as_view(), name='shop_delete'),
]