from . import views
from django.urls import path

app_name = "orders"

urlpatterns = [
    path('add/', views.add, name='add')
]
