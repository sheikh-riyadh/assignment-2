from django.shortcuts import render
from core.models import RegisterForm, LoginForm

# Create your views here.

def sign_up(request):
    return render(request, 'sign_up.html',{"form":RegisterForm})

def sign_in(request):
    return render(request, 'sign_in.html',{'form':LoginForm})


def custom_404_view(request, exception=None):
    return render(request, "404.html", status=404)