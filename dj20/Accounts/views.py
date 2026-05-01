from django.contrib import messages
from django.shortcuts import render,redirect

from .form import ProfileForm
from .models import Profile


# Create your views here.

def upload_profile(request):
    if request.method == 'POST':
       form = ProfileForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           messages.success(request, 'Profile successfully uploaded')
           return redirect('view_profile')
       else:
           messages.error(request, 'Please correct the error below.')
           return None
    else:
        form = ProfileForm()
        return render(request, 'upload_profile.html', {'form': form})

def view_profile(request):
    profile = Profile.objects.all()
    return render(request, 'view_profile.html', {'profile': profile})