from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import TodoItem
# Create your views here.

@login_required
def todoView(request):
    log_user = request.user
    all_todo_items = TodoItem.objects.filter(user=log_user)
    return render(request, 'todo.html',
        {'all_items':all_todo_items})
@login_required
def addTodo(request):
    c = request.POST['content']
    new_item = TodoItem(content = request.POST['content'], user=request.user)
    new_item.save()
    return HttpResponseRedirect('/base_todo/todo/')
    # create a new todo all_items
    # save
    # redirect the browser to '/todo/'
@login_required
def deleteTodo(request,todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id, user=request.user)
    item_to_delete.delete()
    return HttpResponseRedirect('/base_todo/todo/')
