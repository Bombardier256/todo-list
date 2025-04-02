from asyncio import tasks

from django.urls import path

from .views import (
    TaskListView,
    TagListView,

)


urlpatterns = [
    path("",
         TaskListView.as_view(),
         name="tasks"
    ),

    path("tags/",
         TagListView.as_view(),
         name="tags"
    ),
]