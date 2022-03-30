from django.forms import ModelForm

from .models import Article

class NewArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = '__all__'