from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    # post views
    path('login/', views.user_login, name='login'),
]