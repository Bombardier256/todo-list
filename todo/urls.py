from asyncio import tasks

from django.urls import path

from .views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)


urlpatterns = [
    path("",
         TaskListView.as_view(),
         name="tasks"
    ),
    path("create/",
         TaskCreateView.as_view(),
         name="task-create"
    ),
    path("<int:pk>/update/",
         TaskUpdateView.as_view(),
         name="task-update"
    ),
    path("<int:pk>/delete/",
         TaskDeleteView.as_view(),
         name="task-delete"
    ),

    path("tags/",
         TagListView.as_view(),
         name="tags"
    ),
    path("tags/create/",
         TagCreateView.as_view(),
         name="tag-create"
    ),
    path("tags/<int:pk>/update/",
         TagUpdateView.as_view(),
         name="tag-update"
    ),
    path("tags/<int:pk>/delete/",
         TagDeleteView.as_view(),
         name="tag-delete"
    ),
]