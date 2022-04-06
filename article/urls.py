from django.urls import path

from . import views


urlpatterns = [
    path('', views.ArticleList.as_view(), name='articles'),
    path('article/new/', views.ArticleCreate.as_view(), name='new_article'),
    path('article/<slug:slug>/', views.ArticleDetail.as_view(), name='article'),
    path('article/<slug:slug>/edit', views.ArticleUpdate.as_view(), name='edit_article'),
    path('article/<slug:slug>/delete', views.ArticleDelete.as_view(), name='delete_article'),
    path('article/<slug:slug>/like', views.like_article, name='like_article')
]
