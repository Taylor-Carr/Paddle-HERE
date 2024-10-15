from django.urls import path
from .views import UserRegisterView, profile_view, edit_profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name ='register'),
    path('profile/<str:username>/', profile_view, name ='profile'),
    path('profile/<str:username>/edit/', edit_profile, name ='edit_profile'),
]