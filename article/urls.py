from django.urls import path

from . import views


urlpatterns = [
    path('', views.UserIndexList.as_view(), name='articles'),
    path('article/search', views.SearchArticleView.as_view(), name="search_article"),
    path('article/new/', views.ArticleCreate.as_view(), name='new_article'),
    path('article/<slug:slug>/', views.ArticleDetail.as_view(), name='article'),
    path('article/<slug:slug>/edit', views.ArticleUpdate.as_view(), name='edit_article'),
    path('article/<slug:slug>/delete', views.ArticleDelete.as_view(), name='delete_article'),
    path('article/<slug:slug>/like', views.like_article, name='like_article'),
    path('article/<slug:slug>/save', views.save_article, name='save_article'),
    path('article/<slug:slug>/saved', views.SavedArticlesView.as_view(), name='saved_articles'),
    path('article/profile/<int:pk>', views.ProfileDetail.as_view(), name='profile'),
    path('article/<slug:slug>/comment/new', views.ArticleCommentCreate.as_view(), name='new_article_comment'),
    path('tag/<str:tag>', views.ArticleTagList.as_view(), name='tag'),
]
