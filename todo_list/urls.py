from django.urls import path

from todo_list.views import (
    TaskListView,
    TagListView,
    ChangeStateView
)

app_name = "todo-list"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("task/<int:pk>", ChangeStateView.as_view(), name="change-state"),
]
