from django.urls import path
from . import views

# urlpatterns for Loginify app
urlpatterns = [
    # home view that currently returns "Hello World"
    path('home/', views.home_view, name='home'),    
    # login page
    path('', views.login, name='login'),
    # signup page
    path('signup/', views.signup, name='signup'),
]
