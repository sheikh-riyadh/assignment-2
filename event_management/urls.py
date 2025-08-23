from django.contrib import admin
from django.urls import path, include
from core.views import sign_up,sign_in

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('event.urls')),
    path('sign-up/', sign_up, name="sign-up" ),
    path('sign-in/', sign_in, name="sign-in"),
    path('dashboard/', include('dashboard.urls')),
    path('participant/', include('participant.urls') ),
    path('organizer/', include('organizer.urls'))
]
