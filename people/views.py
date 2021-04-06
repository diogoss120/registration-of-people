from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .form import PersonForm
import requests

from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, FormView, CreateView, DeleteView

from django.urls import reverse

path_form = "people/form.html"
path_home = "people/home.html"
path_form_delete = "people/form_delete.html"


class HomePageView(ListView):
    template_name = path_home  # a template that the view will return
    model = Person  # a model class necessary

class PersonCreateView(CreateView):
    template_name = path_form
    model = Person
    form_class = PersonForm  # explicit indication of the people form
    type_form = 'new'  # return custom inforation for the template

    def get_success_url(self):  # redirect the page after the action
        return reverse('url_list_people')


class PersonUpdateView(UpdateView):
    template_name = path_form
    model = Person
    form_class = PersonForm
    success_url = "/people/"  # other option for redirect the page after action


class PersonDeleteView(DeleteView):
    template_name = path_form_delete
    model = Person
    form_class = PersonForm

    def get_success_url(self):
        return reverse('url_list_people')


class SearchPeopleView(ListView):
    template_name = path_home

    def get_queryset(self): # an override on the native django method  
        return Person.objects.filter(name__icontains=self.kwargs['search']).order_by("name")


class GenerateNameView(View):
    type_form = 'new'
    form_class = PersonForm

    def get_data_from_api(self):
        url = 'http://gerador-nomes.herokuapp.com/nome/aleatorio'  # url of api
        r = requests.get(url)  # will make request to api

        names_list = ["Person", "Middle name", "Last name"]

        if (r.status_code == 200):
            # converting a list of strings to a python list
            names_list = eval(r.text)

        return names_list

    def post(self, request, *args, **kwargs):
        person = Person
        my_names = self.get_data_from_api()
        # setting data of api
        person.name = my_names[0]  # setting name
        person.last_name = my_names[1] + " " + my_names[2]  # setting last name

        # getting existent data of form
        person.years_old = request.POST["years_old"]
        person.birth = request.POST["birth"]
        person.email = request.POST["email"]
        person.nickname = request.POST["nickname"]
        person.obervation = request.POST["obervation"]

        # returning dict with data
        context = {}
        context["view"] = self
        context['form'] = self.form_class(instance=person)

        return render(request, path_form, context)