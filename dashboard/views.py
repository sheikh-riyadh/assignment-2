from django.shortcuts import render

# Create your views here.

def dashboard(request):

    data = [
        {'name':"Dashboard", 'url':'dashboard'},
    ]

    return render(request, 'dashboard_base.html', {"data":data})
