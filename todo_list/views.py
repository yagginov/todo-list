from django.views import generic
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy

from todo_list.models import Task, Tag


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
