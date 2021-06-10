from django.contrib import admin
from django.urls import path, include
from recipe.views import home
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('recipe/', include('recipe.urls', namespace="recipe")),
    path('ingredient/', include('ingredient.urls', namespace="ingredients")),
    path('staff/', include('staff.urls', namespace="staff")),
    path('basket/', include('basket.urls', namespace="basket")),
    path('account/', include('account.urls', namespace="account")),
    path('payment/', include('payment.urls', namespace="payment")),
    path('orders/', include('orders.urls', namespace="orders")),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
