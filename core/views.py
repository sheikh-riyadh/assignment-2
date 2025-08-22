from django.shortcuts import render
from core.models import RegisterForm, LoginForm

# Create your views here.

def register(request):
    return render(request, 'register.html',{"form":RegisterForm})

def login(request):
    return render(request, 'login.html',{'form':LoginForm})