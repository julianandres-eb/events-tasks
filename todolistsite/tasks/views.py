# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .models import Task
from django.urls import (
    reverse_lazy
)


class TaskLogin(LoginView):
    pass


class TaskLogout(LogoutView):
    pass


class TaskList(LoginRequiredMixin, ListView):

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)


class TaskCreate(CreateView):
    model = Task
    fields = ['name_task', 'priority', 'done']
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.object = form.save()
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(UpdateView):
    model = Task
    fields = ['name_task', 'priority', 'done']
    success_url = reverse_lazy('task-list')


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')

