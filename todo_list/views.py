from django.views import generic
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy

from todo_list.models import Task, Tag
from todo_list.forms import TaskForm, TagForm


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")


class TagListView(generic.ListView):
    model = Tag


class ChangeStateView(generic.View):
    def get(
        self,
        request: HttpRequest,
        pk: int,
        *args,
        **kwargs
    ) -> HttpResponseRedirect:
        task = get_object_or_404(Task, pk=pk)
        task.is_done ^= True
        task.save()
        return HttpResponseRedirect(reverse("todo-list:task-list"))


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo-list:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo-list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo-list:task-list")


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo-list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo-list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo-list:tag-list")
