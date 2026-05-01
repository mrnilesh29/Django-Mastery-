from django.core.paginator import Paginator
from django.shortcuts import render
from pygments.lexers import q

from .models import Customer
# Create your views here.

def shop(request):
    customer = Customer.objects.all().order_by('first_name')
    paginator = Paginator(customer, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop.html', {'customer': page_obj})