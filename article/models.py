from accounts.models import User
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
import markdown as md

class Article(models.Model):
	title = models.CharField(max_length=128)
	body = models.TextField(blank=True, null=True)
	date = models.DateField(auto_now=True)
	slug = AutoSlugField(populate_from='title', unique_with='title', null=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	likes = models.ManyToManyField(User, related_name='likes')
	comments = models.ManyToManyField('ArticleComment', related_name='comments')

	author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='article_author')
	tag = models.ForeignKey('Tag', blank=True, null=True, on_delete=models.PROTECT, related_name='article_tag')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("article", kwargs={"slug": self.slug})

	def get_article_img(self):
		markdown_text = md.markdown(self.body, extensions=['markdown.extensions.fenced_code'])
		markdown_cuted = markdown_text[markdown_text.index('<img'):]
	
		return markdown_cuted[:markdown_cuted.index('/>')+2]

class ArticleComment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
	tag = models.CharField(max_length=128, unique=True)

	def __str__(self):
		return self.tag