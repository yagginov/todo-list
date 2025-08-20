from django.views import generic
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy

from todo_list.models import Task, Tag
from todo_list.forms import TaskForm, TagForm, FilterTaskForm


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")

    def get_queryset(self):
        self.filter_form = FilterTaskForm(self.request.GET)
        if self.filter_form.is_valid():
            tags = self.filter_form.cleaned_data.get("tags")
            if tags:
                return super().get_queryset().filter(tags__in=tags).distinct()
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = self.filter_form
        return context


class TagListView(generic.ListView):
    model = Tag


class ChangeStateView(generic.View):
    def get(
        self, request: HttpRequest, pk: int, *args, **kwargs
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
