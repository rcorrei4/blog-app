from django.urls import path

from . import views


urlpatterns = [
    path('', views.ArticleList.as_view(), name='article'),
    path('new/', views.ArticleCreate.as_view(), name='new_article'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article'),
    path('<slug:slug>/edit', views.ArticleUpdate.as_view(), name='edit_article'),
    path('<slug:slug>/delete', views.ArticleDelete.as_view(), name='delete_article')
]
