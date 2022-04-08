from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from accounts.models import User

class RegisterCreate(CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'auth/user_form.html'

class ProfileDetail(DetailView):
	model = User