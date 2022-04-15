from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
	following = models.ManyToManyField('User', related_name='user_following')
	articles = models.ManyToManyField('article.Article', related_name='user_articles')