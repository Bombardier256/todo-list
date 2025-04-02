from django.contrib import admin

from todo.models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name",]
    search_fields = ["name",]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "datetime", "deadline", "is_done"]
    search_fields = ["content",]
    list_filter = ["is_done",]
