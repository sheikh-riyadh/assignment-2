from django.urls import path
from dashboard.views import dashboard,add_event,add_organizer

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('add-event/', add_event, name='add-event'),
    path('add-organizer/', add_organizer, name='add-organizer'),
]