from django.forms import ModelForm

from .models import Article

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = ['title', 'text']

		def form_valid(self, form):
			form.instance.author = self.request.user
			return super().form_valid(form)