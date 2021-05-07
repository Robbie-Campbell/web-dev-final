from django.contrib import admin
from django.urls import path, include
from login.views import home

urlpatterns = [
    path('', home, name="home"),
    path('auth/', include('login.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
