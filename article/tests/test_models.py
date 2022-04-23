from django.test import TestCase
from accounts.models import User
from article.models import Article, Tag

class ArticleTestCase(TestCase):

	@classmethod
	def setUpTestData(cls):
		cls.user = User.objects.create_user(username='testuser', password='12345')
		cls.article1 = Article.objects.create(
			title="Django Testing", 
			body="how to write django tests", 
			author=cls.user)

		cls.article2 = Article.objects.create(
			title="Class-based views", 
			body="class-based views updated tutorial", 
			author=cls.user)

	def test_model_str(self):
		self.assertEqual(str(self.article1), "Django Testing")
		self.assertEqual(str(self.article2), "Class-based views")

	def test_get_absolute_url(self):
		self.assertEqual("/article/django-testing/", self.article1.get_absolute_url())
		self.assertEqual("/article/class-based-views/", self.article2.get_absolute_url())

class TagTestCase(TestCase):

	@classmethod
	def setUpTestData(cls):
		cls.tag = Tag.objects.create(tag='tagname')

	def test_model_str(self):
		self.assertEqual(str(self.tag), "tagname")