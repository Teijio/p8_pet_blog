from django.contrib import admin

from .models import Project, Review, Tag, Message


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ProjectReview(admin.ModelAdmin):
    pass


@admin.register(Tag)
class ProjectTag(admin.ModelAdmin):
    pass


@admin.register(Message)
class ProjectMessage(admin.ModelAdmin):
    pass
