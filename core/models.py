from django.db import models
from django import forms

# Create your models here.

class RegisterForm(forms.Form):
    first_name= forms.CharField(widget=forms.TextInput(attrs={"placeholder":"First Name"}))
    last_name= forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Last Name"}))
    phone= forms.IntegerField(widget=forms.NumberInput(attrs={
        "placeholder":"Phone Number",
        "class":"no-spinner"
        }))
    email= forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email Address"}))


