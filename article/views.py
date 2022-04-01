from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article

class ArticleList(ListView):
	model = Article

class ArticleDetail(DetailView):
	model = Article

class ArticleCreate(LoginRequiredMixin, CreateView):

	model = Article
	fields = '__all__'

class ArticleUpdate(LoginRequiredMixin, UpdateView):
	model = Article
	fields = ['title', 'text']

class ArticleDelete(LoginRequiredMixin, DeleteView):
	model = Article
	context_object_name = 'article'