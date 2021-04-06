from django.contrib import admin
from django.urls import path
from people.views import *
from people.viewsOLD import *

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', PersonCreateView.as_view(), name='url_new_people'),
    path('people/', HomePageView.as_view(), name='url_list_people'),
    path('edit-person/<int:pk>/', PersonUpdateView.as_view(), name='edit-person'),
    path('delete/<int:pk>/', PersonDeleteView.as_view(), name='url_delete_person'),
    path('search/<str:search>/', SearchPeopleView.as_view(), name='url_search_person'),
    path('get-name/', GenerateNameView.as_view()),
]

"""
#  Old routes 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', new_person, name='url_new_people'),
    path('people/', list_of_people, name='url_list_people'),
    path('edit-person/<int:id>/', edit_person, name='url_edit_people'),
    path('delete/<int:id>/', delete_person, name='url_delete_person'),
    path('search/<str:search>/', search, name='url_search_person'),
    path('get-name/', get_name),
]
"""