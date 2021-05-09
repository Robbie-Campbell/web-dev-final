from . import views
from django.urls import path

urlpatterns = [
    path('category/', views.create_category, name="create_category"),
    path('measurement/', views.create_measurement, name='create_measurement'),
]
