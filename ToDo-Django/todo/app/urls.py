from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path("", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout, name="logout"),
    path("home", views.home, name="home"),
   
   
]
