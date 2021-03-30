from django.contrib import admin
from .models import Person
from .form import PersonForm

admin.site.register(Person)
# Register your models here.
