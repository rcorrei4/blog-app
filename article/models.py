from accounts.models import User
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from django.contrib.contenttypes.fields import GenericRelation

from hitcount.models import HitCountMixin
from hitcount.settings import MODEL_HITCOUNT

import markdown as md
import readtime

class Article(models.Model, HitCountMixin):
	title = models.CharField(max_length=128)
	body = models.TextField(blank=True, null=True)
	date = models.DateField(auto_now=True)
	slug = AutoSlugField(populate_from='title', unique_with='title', null=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	reading_time = models.CharField(max_length=128)

	likes = models.ManyToManyField(User, related_name='likes')
	comments = models.ManyToManyField('ArticleComment', related_name='comments')
	views = models.IntegerField(default=0)
	hit_count_generic = GenericRelation(
		MODEL_HITCOUNT, object_id_field='object_pk',
		related_query_name='hit_count_generic_relation'
	)

	author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='article_author')
	tag = models.ForeignKey('Tag', blank=True, null=True, on_delete=models.PROTECT, related_name='article_tag')

	def save(self, *args, **kwargs):
		self.reading_time = readtime.of_text(md.markdown(self.body))
		super(Article, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("article", kwargs={"slug": self.slug})

	def get_article_body_truncated(self):
		return md.markdown(self.body[:200], extensions=['markdown.extensions.fenced_code']).strip()

	def get_article_img(self):
		markdown_text = md.markdown(self.body, extensions=['markdown.extensions.fenced_code'])

		try:
			markdown_cuted = markdown_text[markdown_text.index('<img'):]
		
			return markdown_cuted[:markdown_cuted.index('/>')+2]
		except ValueError:
			return False
		

class ArticleComment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
	tag = models.CharField(max_length=128, unique=True)

	def __str__(self):
		return self.tag