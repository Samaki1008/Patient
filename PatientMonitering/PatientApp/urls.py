from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='app-index'),
    path('login/', auth_views.LoginView.as_view(template_name ='registration/login.html'), name ='app-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name ='registration/logout.html'), name = 'app-logout'),
    path('accounts/profile/', views.profile, name='app-profile'),
    path('register', views.register, name ='app-register')


]