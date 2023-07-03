from . import views
from django.urls import path

app_name = 'account'

urlpatterns = [
    path("", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout, name="logout"),
    path("success/", views.home, name="home")
]
