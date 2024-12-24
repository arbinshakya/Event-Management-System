from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *



class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username = username).exists():
            raise forms.ValidationError('Username already exists.')
        return username
    

class LoginUser(AuthenticationForm):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
    class Meta:
        model = User
        fields = ['username','password']


class CreateEventForm(forms.ModelForm):
    class Meta:
        model = CreateEvent
        fields = '__all__'
        




class UpdateEventForm(forms.ModelForm):
    class Meta:
        model = CreateEvent
        fields = '__all__'



class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'


