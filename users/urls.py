from django.urls import path

from . import views # 5 impor views and go to view file.
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register, name='register'),  # 4 create a path with new features
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

]