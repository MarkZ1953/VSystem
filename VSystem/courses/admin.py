from django.contrib import admin
from .models import Course, Course_Student


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "maxCapacity", "teacher", "isActive")


@admin.register(Course_Student)
class CourseStudentAdmin(admin.ModelAdmin):
    list_display = ("id", "course", "student", "startDate", "endDate", "state", "isActive")
