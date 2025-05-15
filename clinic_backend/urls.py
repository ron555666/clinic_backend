from django.contrib import admin
from django.urls import path, include
from appointments.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), 
    path('api/', include('appointments.urls')),
]


