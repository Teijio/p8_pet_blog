from django.contrib import admin

from .models import Profile, Skill, Message


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class ProjectMessage(admin.ModelAdmin):
    pass
