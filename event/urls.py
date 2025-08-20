from django.urls import path
from event.views import home, event_details
urlpatterns = [
 path('', home, name='home'),
 path('event-details/<id>', event_details, name='event-details')
]