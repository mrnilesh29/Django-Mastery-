from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Shop

class ShopListing(ListView):
    model = Shop
    template_name = 'shop_listing.html'
    context_object_name = 'shop_list'


class ShopDetail(DetailView):
    model = Shop
    template_name = 'shop_detail.html'
    context_object_name = 'shop'

class ShopCreate(CreateView):
    model = Shop
    template_name = 'shop_create.html'
    fields = '__all__'
    success_url = reverse_lazy('shop_list')

class ShopUpdate(UpdateView):
    model = Shop
    template_name = 'shop_update.html'
    fields = '__all__'

class ShopDelete(DeleteView):
    model = Shop
    template_name = 'shop_delete.html'
    success_url = reverse_lazy('shop_list')
    context_object_name = 'shop'

