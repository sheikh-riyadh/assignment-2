from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard_base.html')


def add_event(request):
    return render(request, 'add_event.html')

def add_organizer(request):
    return render(request, 'add_organizer.html')
