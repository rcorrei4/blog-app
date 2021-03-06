from django.http import JsonResponse
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .forms import UserCreateForm

from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterCreate(CreateView):
	form_class = UserCreateForm
	success_url = reverse_lazy('login')
	template_name = 'auth/user_form.html'

@login_required
def follow_user(request, pk):
	user = get_object_or_404(User, username=request.user.username)
	profile = get_object_or_404(User, id=pk)

	if user == profile:
		return JsonResponse({'result': 'cant follow yourself'})
	else:
		if User.objects.filter(id=user.id, following__in=[profile]).count() == 0:
			user.following.add(profile)
			profile.followers.add(user)
			user.save()
			profile.save()

			return JsonResponse({'result': 'Unfollow'})
		else:
			user.following.remove(profile)
			profile.followers.add(user)
			user.save()
			profile.save()

			return JsonResponse({'result': 'Follow'})