from django.contrib import admin
from django.urls import path, include
from recipe.views import home
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('recipe/', include('recipe.urls')),
    path('ingredient/', include('ingredient.urls')),
    path('staff/', include('staff.urls')),
    path('basket/', include('basket.urls')),
    path('auth/', include('login.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)