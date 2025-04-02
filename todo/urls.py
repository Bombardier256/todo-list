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
    TaskCompleteView,
    TaskNotCompleteView,
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
    path("<int:pk>/complete/",
         TaskCompleteView.as_view(),
         name="task-complete"
    ),
    path("<int:pk>/notcomplete/",
         TaskNotCompleteView.as_view(),
         name="task-not-complete"
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
