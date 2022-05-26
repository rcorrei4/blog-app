from django.test import TestCase
from accounts.models import User
from article.models import Article, Tag

class ArticleTestCase(TestCase):

	@classmethod
	def setUpTestData(cls):
		cls.user = User.objects.create_user(username='testuser', password='12345')
		cls.article1 = Article.objects.create(
			title='Django Testing', 
			body='how to write django tests <img alt="Homepage LibriumSwap" src="https://raw.githubusercontent.com/LibriumSwap/LibriumSwap/main/presentation.jpg" />', 
			author=cls.user)

		cls.article2 = Article.objects.create(
			title='Class-based views', 
			body='class-based views updated tutorial', 
			author=cls.user)

	def test_model_str(self):
		self.assertEqual(str(self.article1), 'Django Testing')
		self.assertEqual(str(self.article2), 'Class-based views')

	def test_reading_time(self):
		self.assertEqual(str(self.article1.reading_time), '1 min read')
		self.assertEqual(str(self.article2.reading_time), '1 min read')

	def test_get_absolute_url(self):
		self.assertEqual('/article/django-testing/', self.article1.get_absolute_url())
		self.assertEqual('/article/class-based-views/', self.article2.get_absolute_url())

	def test_get_article_img(self):
		self.assertEqual('<img alt="Homepage LibriumSwap" src="https://raw.githubusercontent.com/LibriumSwap/LibriumSwap/main/presentation.jpg" />',
						  self.article1.get_article_img())
		self.assertEqual(False ,self.article2.get_article_img())

class TagTestCase(TestCase):

	@classmethod
	def setUpTestData(cls):
		cls.tag = Tag.objects.create(tag='tagname')

	def test_model_str(self):
		self.assertEqual(str(self.tag), 'tagname')