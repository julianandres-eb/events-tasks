from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import (
    CreateView,
    UpdateView
)
from .models import Task
from django.urls import (
    reverse,
    reverse_lazy
)


class TaskList(ListView):
    model = Task


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks-list')


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks-list')

