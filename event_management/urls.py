from django.contrib import admin
from django.urls import path, include
from core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('admin-dashboard/', include('admin_dashboard.urls')),
    path('participant/', include('participant.urls') ),
    path('organizer/', include('organizer.urls'))
]
