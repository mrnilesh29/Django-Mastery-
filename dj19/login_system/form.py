from django import forms

from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'age', 'password','mobile')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already registered.')
        return email
