from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField

class Article(models.Model):
	title = models.CharField(max_length=128)
	body = models.TextField()
	date = models.DateField(auto_now=True)
	slug = AutoSlugField(populate_from='title', unique_with='title', null=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	likes = models.ManyToManyField(User, related_name='likes')

	author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='article_author')
	tag = models.ForeignKey('Tag', blank=True, null=True, on_delete=models.PROTECT, related_name='article_tag')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("article", kwargs={"slug": self.slug})

class Tag(models.Model):
	tag = models.CharField(max_length=128)

	def __str__(self):
		return self.tag