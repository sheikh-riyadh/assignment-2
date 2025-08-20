from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


def event_details(request, id):
    return render(request, 'event_details.html')
