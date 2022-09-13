from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('follow/<int:pk>/', views.follow_user, name='follow_user'),
]