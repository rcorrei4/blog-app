from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField

class Article(models.Model):
	title = models.CharField(max_length=128)
	text = models.CharField(max_length=528)
	date = models.DateField(auto_now=True)
	slug = AutoSlugField(populate_from='title', unique_with='title', null=False)

	author = models.ForeignKey(User, on_delete=models.PROTECT)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("article", kwargs={"slug": self.slug})