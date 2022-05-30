from django.http import JsonResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.db.models import Q

from accounts.models import User
from .models import Article, ArticleComment, Tag
from .forms import ArticleForm, ArticleCommentForm

class UserIndexList(ListView):
	model = Article

	def get_queryset(self):
		if self.request.user.is_authenticated:
			self.template_name = 'article/user_index.html'
			user = self.request.user
			return user.following.all()
		else:
			self.template_name = 'article/article_list.html'
			return Article.objects.all().order_by('-views')[:6]

class ArticleDetail(DetailView):
	model = Article

	def get_object(self, queryset=None):
		object = super(ArticleDetail, self).get_object()
		object.views += 1
		object.save()

		return object

@method_decorator(login_required, name='dispatch')
class ArticleCreate(CreateView):
	model = Article
	form_class = ArticleForm

	def form_valid(self, form):
		form.instance.author_id = self.request.user.pk

		if form.cleaned_data['new_tag']:
			tag = Tag.objects.create(tag=form.cleaned_data['new_tag'])
			form.instance.tag_id = tag.pk

		self.object = form.save()

		user = User.objects.get(id=self.request.user.pk)
		user.articles.add(self.object)
		user.save()

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

@method_decorator(login_required, name='dispatch')
class ArticleCommentCreate(CreateView):
	model = ArticleComment
	form_class = ArticleCommentForm
	template_name = 'article/article_comment_form.html'

	def form_valid(self, form):
		form.instance.author_id = self.request.user.pk

		self.object = form.save()

		article = Article.objects.get(slug=self.kwargs['slug'])
		article.comments.add(self.object)
		article.save()

		self.success_url = article.get_absolute_url()

		return super().form_valid(form)

class ArticleTagList(ListView):
	model = Article
	template_name = 'article/article_tag_list.html'
	
	def get_queryset(self):
		self.tag = get_object_or_404(Tag, tag=self.kwargs['tag'])
		return Article.objects.filter(tag=self.tag)

class ArticleProfileDetail(ListView):
	model = Article
	template_name = 'article/article_profile_list.html'

	def get_queryset(self):
		return Article.objects.filter(author__id=self.kwargs['pk'])

class FollowingList(ListView):
	model = User
	template_name = 'article/following.html'

	def get_queryset(self):
		self.user = get_object_or_404(User, username=self.request.user.username)
		return self.user

class SearchArticleView(ListView):
	model = Article
	template_name = 'article/article_results.html'

	def get_queryset(self):
		query = self.request.GET.get('q')

		return Article.objects.filter(
			Q(title__icontains=query) | Q(slug__icontains=query)
		)

class SavedArticlesView(ListView):
	model = User
	template_name = 'article/article_results.html'

	def get_queryset(self):
		self.user = get_object_or_404(User, username=self.request.user.username)
		return self.user.saved_articles.all()

@login_required
def save_article(request, slug):
	user = get_object_or_404(User, username=request.user.username)
	article = get_object_or_404(Article, slug=slug)

	if article not in user.saved_articles.all():
		user.saved_articles.add(article)

		return JsonResponse({'result': 'saved'})
	else:
		user.saved_articles.remove(article)

		return JsonResponse({'result': 'removed'})

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