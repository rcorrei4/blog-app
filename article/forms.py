from django import forms

from .models import Article, ArticleComment

class ArticleForm(forms.ModelForm):
	new_tag = forms.CharField(max_length=128, required=False)

	class Meta:
		model = Article
		fields = ['title', 'body', 'tag']

class ArticleCommentForm(forms.ModelForm):
	class Meta:
		model = ArticleComment
		fields = ['body']