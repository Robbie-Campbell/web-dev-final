from . import views
from django.urls import path

urlpatterns = [
    path('create/<int:id>/', views.create_ingredient, name="create_ingredient"),
    path('delete/<int:id>/', views.delete_ingredient, name="delete_ingredient"),
]
