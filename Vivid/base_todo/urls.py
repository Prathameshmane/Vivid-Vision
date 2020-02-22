from django.urls import path
from base_todo.views import todoView,addTodo,deleteTodo
from . import views
urlpatterns = [
    path('todo/',views.todoView,name='todo'),
    path('todo/base_todo/addTodo/',addTodo),
    path('todo/base_todo/deleteTodo/<int:todo_id>',deleteTodo),
]
