
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('profile/<int:id>', views.get_user_by_id, name='profile'),
]