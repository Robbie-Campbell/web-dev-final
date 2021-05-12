from . import views
from django.urls import path

urlpatterns = [
    path('<int:id>/', views.single, name="recipe_single"),
    path('list/', views.index, name="recipe_list"),
    path('create/', views.create_recipe, name="create_recipe"),
    path('edit/<int:id>/', views.edit_recipe, name="edit_recipe"),
    path('delete/<int:id>/', views.delete_recipe, name="delete_recipe"),
    path('category/<int:id>/', views.category, name="category"),
    path('search/', views.search_results, name='search_results'),
]
