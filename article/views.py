from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Article

class ArticleList(ListView):
	model = Article

class ArticleDetail(DetailView):
	model = Article

class ArticleCreate(CreateView):
	model = Article
	fields = '__all__'

class ArticleUpdate(UpdateView):
	model = Article
	fields = ['title', 'text']

class ArticleDelete(DeleteView):
	model = Article
	context_object_name = 'article'