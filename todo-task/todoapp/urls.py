from django.urls import path
from . import views

app_name = "todoapp"

urlpatterns = [
    path('',views.todoapp, name="list"),
    path('addTodo/',views.addTodo, name='add'),
    path('deleteTodo/<int:i>/',views.deleteTodo, name='delete'),  
]