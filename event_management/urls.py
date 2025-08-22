from django.contrib import admin
from django.urls import path, include
from core.views import register,login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('event.urls')),
    path('register/', register, name="register" ),
    path('login/', login, name="login"),
    path('admin-dashboard/', include('admin_dashboard.urls')),
    path('participant/', include('participant.urls') ),
    path('organizer/', include('organizer.urls'))
]
