from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .form import PersonForm
import requests

path_form = "people/form.html"
path_home = "people/home.html"

# old funcion-based view
"""
    the project not will run correctly with function-based view because the templates html
    were modified for work with class-based view, but I left this archive here
    for consult
"""
def list_of_people(request):
    people = Person.objects.all()  # getting all the people in database

    data = {}  # dictionary with information that will be sent to template
    data['message'] = 'Create a new person'
    data["people"] = people
    return render(request, path_home, data)


def new_person(request):
    form = PersonForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('url_list_people')

    data = {}  # dictionary with information that will be sent to template
    data['form'] = form
    data['type'] = 'new'
    data['message'] = 'Register a new Person'

    return render(request, path_form, data)


def edit_person(request, id: int):

    # getting a person that is in edition
    person = get_object_or_404(Person, pk=id)

    form = PersonForm(request.POST or None, instance=person)

    if form.is_valid():  # validate form and save if ok
        form.save()
        return redirect('url_list_people')

    data = {}  # dictionary with information that will be sent to template
    data['form'] = form
    data['type'] = 'edit'
    data['id_person'] = person.id
    data['message'] = 'Edit the Person selected'

    return render(request, path_form, data)


def get_name(request):  # a method python that will get aleators names in web api

    url = 'http://gerador-nomes.herokuapp.com/nome/aleatorio'

    r = requests.get(url)  # will make request to api

    myList = ["Person", "Middle name", "Last name"]

    if (r.status_code == 200):
        myList = eval(r.text)  # converting a list of strings to a python list

    new_user = Person  # a Person object that will receive the data and that will be returned
    if request.method == "POST":
        # catching a person data yet in edition
        new_user.name = myList[0]  # setting name
        new_user.last_name = myList[1] + " " + myList[2]  # setting last name

        # getting existent data of form
        new_user.years_old = request.POST["years_old"]
        new_user.birth = request.POST["birth"]
        new_user.email = request.POST["email"]
        new_user.nickname = request.POST["nickname"]
        new_user.obervation = request.POST["obervation"]

    form = PersonForm(instance=new_user)  # defining a PersonForm to the view

    data = {}  # dictionary with information that will be sent to template
    data["form"] = form
    data['type'] = 'new'
    data['message'] = 'Register a new Person'
    return render(request, path_form, data)


def delete_person(request, id: int):
    # getting the id and deleting of database
    person = get_object_or_404(Person, pk=id)
    person.delete()
    return redirect('url_list_people')

def search(request, search: str):
    people = Person.objects.filter(name__icontains=search)
    data = {}  # dictionary with information that will be sent to template
    data['message'] = 'Create a new person'
    data["people"] = people
    return render(request, path_home, data)