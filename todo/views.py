from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import TagForm, TaskForm
from .models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks")


class TaskCompleteView(generic.View):
    @staticmethod
    def get(request, pk):
        task = Task.objects.get(pk=pk)
        task.is_done = True
        task.save()

        return redirect(reverse_lazy("tasks"))


class TaskNotCompleteView(generic.View):
    @staticmethod
    def get(request, pk):
        task = Task.objects.get(pk=pk)
        task.is_done = False
        task.save()

        return redirect(reverse_lazy("tasks"))


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tags")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tags")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tags")
