from django.contrib import admin
from .models import Person
from .form import PersonForm


class PersonAdmin(admin.ModelAdmin):
    list_display = ["name", "last_name", "birth", "email"]
    search_fields = ["name", "last_name"]


admin.site.register(Person, PersonAdmin)
# Register your models here.
