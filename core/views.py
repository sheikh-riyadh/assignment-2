from django.shortcuts import render
from core.models import RegisterForm

# Create your views here.

def register(request):
    return render(request, 'register.html',{"form":RegisterForm})