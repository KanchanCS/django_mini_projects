from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.Home, name="home"),
    path("register", views.sign_up, name="signup"),
    path("logout", views.Logout, name="logout"),
    path("login", views.Login, name="login"),
    path("detail/<int:id>/", views.blog_detail, name="detail"),
    path("addpost", views.add_post, name="addpost"),
    path("edit/<int:id>/", views.edit_post, name="editpost"),
    path("delete/<int:id>/", views.delete_post, name="deletepost"),
    #path("category/", views.category_search,name="category"),
    
]
