from django import forms
from .models import Rented_people

class Rented_PeopleForm(forms.ModelForm):
    class Meta :
        model = Rented_people
        fields = '__all__'




