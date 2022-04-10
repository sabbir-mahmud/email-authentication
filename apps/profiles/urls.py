# imports
from django.urls import path
from . import views
# urls patterns
urlpatterns = [
    path('', views.loginViews.as_view(), name='login'),
    path('/logout', views.logoutViews.as_view(), name='log-out'),
    path('/home', views.homeViews.as_view(), name='homepage'),
]
