from django.contrib import admin
from .models import *


# Регистрация Новых моделей  06.07.23
@admin.register(NewTeacher)
class NewTeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    search_fields = ('full_name',)

@admin.register(NewLocation)
class NewLocationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(NewClassroom)
class NewClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location__name')
    list_filter = ('location',)

@admin.register(NewGroup)
class NewGroupAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'course')
    search_fields = ('number', 'name')
    list_editable = ('course',)
    list_filter = ('course',)

@admin.register(NewSubject)
class NewSubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'classroom')
    search_fields = ('name', 'teacher__full_name', 'classroom__name')
    list_filter = ('teacher', 'classroom')

@admin.register(NewEvent)
class NewEventAdmin(admin.ModelAdmin):
    list_display = ('start', 'end', 'subject', 'group')
    search_fields = ('start', 'end', 'subject__name', 'group__number')
    list_filter = ('start', 'subject', 'group')
