from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
	path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('register/', views.RegisterCreate.as_view(), name='register'),
	path('profile/<int:pk>', views.ProfileDetail.as_view(), name='profile')
]