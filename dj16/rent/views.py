from django.shortcuts import render
from django.http import HttpResponse
from .forms import Rented_PeopleForm

# Create your views here.

def rent2(request):
    if request.method == 'POST':
        form = Rented_PeopleForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request , 'success.html')
        else:
            return HttpResponse('error')
    return render(request, 'rent.html', {'form': Rented_PeopleForm()})


