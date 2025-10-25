from django.shortcuts import render
from django.views.generic import ListView , DeleteView
from .models import Task


class TaskListViews(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"