from django.http import JsonResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User
from .models import Article, Tag
from .forms import ArticleForm

class ArticleList(ListView):
	model = Article

class ArticleDetail(DetailView):
	model = Article

@method_decorator(login_required, name='dispatch')
class ArticleCreate(CreateView):
	model = Article
	form_class = ArticleForm

	def form_valid(self, form):
		form.instance.author_id = self.request.user.pk

		if form.cleaned_data['new_tag']:
			tag = Tag.objects.create(tag=form.cleaned_data['new_tag'])
			form.instance.tag_id = tag.pk

		return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ArticleUpdate(UpdateView):
	model = Article
	form_class = ArticleForm

	def get_queryset(self):
		user = self.request.user
		return Article.objects.filter(author=user)

@method_decorator(login_required, name='dispatch')
class ArticleDelete(DeleteView):
	model = Article
	context_object_name = 'article'
	success_url = '/'

	def get_queryset(self):
		user = self.request.user
		return Article.objects.filter(author=user)

class ArticleTagList(ListView):
	model = Article
	
	def get_queryset(self):
		self.tag = get_object_or_404(Tag, tag=self.kwargs['tag'])
		return Article.objects.filter(tag=self.tag)

@login_required
def like_article(request, slug):
	user = get_object_or_404(User, username=request.user.username)
	article = get_object_or_404(Article, slug=slug)

	if Article.objects.filter(slug=slug, likes__in=[user]).count() == 0:
		article.likes.add(user)

		return JsonResponse({'result': 'liked'})
	else:
		article.likes.remove(user)

		return JsonResponse({'result': 'unliked'})