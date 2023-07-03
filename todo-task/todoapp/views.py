from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .models import *
# Create your views here.

def todoapp(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_todo_items})   

def addTodo(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/') 

def deleteTodo(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/')           