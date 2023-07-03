from django.urls import path
from . import views
app_name = "app"
urlpatterns = [  
    path('', views.index, name="filter_post"),
    # path("edit", views.edit, name="edit-profile"),
]
