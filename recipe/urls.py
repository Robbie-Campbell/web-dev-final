from . import views
from django.urls import path



urlpatterns = [
    path('<int:pk>/', views.single, name="single"),
    path('create/', views.create_recipe, name="add_recipe"),
    path('category/<int:id>/', views.category, name="category"),
    path('search/', views.search_results, name='search_results'),
]
