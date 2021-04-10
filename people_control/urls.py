from django.contrib import admin
from django.urls import path
from people_control.people.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', PersonCreateView.as_view(), name='url_new_people'),
    path('people/', HomePageView.as_view(), name='url_list_people'),
    path('edit-person/<int:pk>/', PersonUpdateView.as_view(), name='edit-person'),
    path('delete/<int:pk>/', PersonDeleteView.as_view(), name='url_delete_person'),
    path('search/<str:search>/', SearchPeopleView.as_view(), name='url_search_person'),
    path('get-name/', GenerateNameView.as_view()),
]