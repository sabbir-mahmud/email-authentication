# imports
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# urls patterns
urlpatterns = [
    path('', views.loginViews.as_view(), name='login'),
    path('/register', views.registerViews.as_view(), name='register'),
    path('/logout', views.logoutViews.as_view(), name='log-out'),
    path('/home', views.homeViews.as_view(), name='homepage'),
    path("password_change/", auth_views.PasswordChangeView.as_view(
        template_name='auth/reset_password.html'), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(),
         name="password_change_done"),
]
