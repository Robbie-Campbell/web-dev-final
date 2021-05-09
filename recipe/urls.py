from . import views
from django.urls import path



urlpatterns = [
    path('<int:pk>/', views.single, name="single"),
    path('create/', views.create_recipe, name="create_recipe"),
    path('edit/<int:id>/', views.edit_recipe, name="edit_recipe"),
    path('create/ingredient/<int:id>/', views.create_ingredient, name="create_ingredient"),
    path('delete/ingredient/<int:id>/', views.delete_ingredient, name="delete_ingredient"),
    path('delete/<int:id>/', views.delete_recipe, name="delete_recipe"),
    path('category/<int:id>/', views.category, name="category"),
    path('search/', views.search_results, name='search_results'),
]
