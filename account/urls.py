from . import views
from django.contrib.auth import views as auth_views
from django.urls import path

app_name = "account"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name="register"),
    path('register/success/', views.register_success, name="register_success"),
    path('activate/<slug:uidb64>/<slug:token>/', views.account_activate, name="activate"),
    path('dashboard/', views.dashboard, name="dashboard"),
]
