from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from .form import RegisterForm

# Create your views here.

# home page


class homeViews(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = Profile.objects.get(user=self.request.user)
        context = {'user': user}
        return context

# register user


class registerViews(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'auth/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'auth/register.html', {'form': form})

# log in view


class loginViews(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')

        return render(request, 'login.html')


# log out view
class logoutViews(View):
    def get(self, request):
        logout(request)
        return redirect('login')
