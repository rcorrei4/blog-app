from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import UserCreateForm

from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterCreate(CreateView):
	form_class = UserCreateForm
	success_url = reverse_lazy('login')
	template_name = 'auth/user_form.html'

class ProfileDetail(DetailView):
	model = User