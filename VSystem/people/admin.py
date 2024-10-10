from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "firstName", "lastName", "document", "phoneNumber", "email", "birthDate", "rol")