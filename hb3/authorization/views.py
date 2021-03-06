from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	return HttpResponse(
		"accounts/ login/ [name='login']<br>\
		 accounts/ logout/ [name='logout']<br>\
		 accounts/ password_change/ [name='password_change']<br>\
		 accounts/ password_change/done/ [name='password_change_done']<br>\
		 accounts/ password_reset/ [name='password_reset']<br>\
		 accounts/ password_reset/done/ [name='password_reset_done']<br>\
		 accounts/ reset/&lt;uidb64&gt;/&lt;token&gt;/ [name='password_reset_confirm']<br>\
		 accounts/ reset/done/ [name='password_reset_complete']"
		)

# https://medium.com/@himanshuxd/how-to-create-registration-login-webapp-with-django-2-0-fd33dc7a6c67
@login_required
def secret_page(request):
	return HttpResponse("secret page")

@login_required
def user_information(request):
	return render(request, 'registration/user_information.html')

class UserList(generic.ListView):
	model = User 
	context_object_name = 'user_list'
	queryset = User.objects.filter(username__icontains='')[:5]
	template_name = 'registration/user_list.html'

class UserItem(generic.DetailView):
	model = User 
	template_name = 'registration/user_detail.html'

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'