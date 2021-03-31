from django.contrib import admin
from django.urls import path
from people.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register_person, name='url_register_people'),
    path('people/', get_people, name='url_get_people'),
    path('edit-person/<int:id>', edit_person, name='url_edit_people'),
    path('get_name/', get_name)
]
