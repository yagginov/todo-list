from django.urls import path

from todo_list.views import (
    TaskListView,
    TagListView
)

app_name = "todo-list"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]
