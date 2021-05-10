from . import views
from django.urls import path

urlpatterns = [
    path('category/', views.create_category, name="create_category"),
    path('measurement/', views.create_measurement, name='create_measurement'),
    path('edit/', views.edit, name='edit_cat_measurement'),
    path('edit/measurement/<int:id>/', views.edit_measurement, name='edit_measurement'),
    path('edit/category/<int:id>/', views.edit_category, name='edit_category'),
    path('delete/measurement/<int:id>/', views.delete_measurement, name='delete_measurement'),
    path('delete/category/<int:id>/', views.delete_category, name='delete_category'),
]
