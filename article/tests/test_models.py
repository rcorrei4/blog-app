from django.test import TestCase
from article.models import Article

class ArticleTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.article1 = Article.objects.create(title="Django Testing", text="how to write django tests")
        cls.article2 = Article.objects.create(title="Class-based views", text="class-based views updated tutorial")

    def test_model_str(self):
        self.assertEqual(str(self.article1), "Django Testing")
        self.assertEqual(str(self.article2), "Class-based views")

    def test_get_absolute_url(self):
        self.assertEqual("/article/django-testing/", self.article1.get_absolute_url())
        self.assertEqual("/article/class-based-views/", self.article2.get_absolute_url())