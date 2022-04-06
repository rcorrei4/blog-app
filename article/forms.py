from django.forms import CharField, ModelForm

from .models import Article

class ArticleForm(ModelForm):
	new_tag = CharField(max_length=128, required=False)

	class Meta:
		model = Article
		fields = ['title', 'body', 'tag']