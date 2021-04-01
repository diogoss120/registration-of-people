from django.contrib import admin
from django.urls import path
from people.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', new_person, name='url_new_people'),
    path('people/', list_of_people, name='url_list_people'),
    path('edit-person/<int:id>/', edit_person, name='url_edit_people'),
    path('get-name/', get_name),
    path('delete/<int:id>', delete_person, name='url_delete_person'),
]
