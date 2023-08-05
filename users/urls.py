from django.contrib.auth import views as auth_views
from .views import  login_view, logout_view
from django.urls import path
from django.contrib.auth.views import LoginView

# app_name = 'users'
# app_name = 'orders_reporter'

urlpatterns = [

    path('login/', LoginView.as_view(template_name="login.html"),name='login'),
    path('logout/',logout_view, name="logout")
    ]
#path('login/', auth_views.LoginView.as_view(template_name='login.html', name="login")),
