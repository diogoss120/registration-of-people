from django.contrib import admin
from django.urls import path
from people.viewsOLD import *


#  Old routes 
"""
    the project not will run correctly with function-based view because the templates html
    were modified for work with class-based view, but I left this archive here
    for consult
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', new_person, name='url_new_people'),
    path('people/', list_of_people, name='url_list_people'),
    path('edit-person/<int:id>/', edit_person, name='url_edit_people'),
    path('delete/<int:id>/', delete_person, name='url_delete_person'),
    path('search/<str:search>/', search, name='url_search_person'),
    path('get-name/', get_name),
]