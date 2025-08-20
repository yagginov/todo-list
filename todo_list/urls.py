from django.urls import path

from todo_list.views import (
    TaskListView,
    TagListView,
    ChangeStateView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

app_name = "todo-list"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("task/<int:pk>", ChangeStateView.as_view(), name="change-state"),
    path("task/create", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
    path("tag/create", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),
]
