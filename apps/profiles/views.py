from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# home page


class homeViews(TemplateView):
    template_name = 'home/home.html'

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
