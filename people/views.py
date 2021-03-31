from django.shortcuts import render, redirect
from .models import Person
from .form import PersonForm
import requests


def get_people(request):

    list_people = []
    people = Person.objects.all()

    for person in people:
        list_people.append(person)

    data = {}
    data['message'] = 'Select the person that you want'
    data["people"] = list_people

    return render(request, "people/home.html", data)


def register_person(request):
    form = PersonForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('url_get_people')

    # dictionary que será enviado para o template django
    data = {}
    data['form'] = form
    data['message'] = 'Register a new Person'

    return render(request, 'people/form.html', data)


def edit_person(request, id: int):

    person = Person.objects.get(pk=id)
    form = PersonForm(request.POST or None, instance=person)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('url_get_people')

    # dictionary que será enviado para o template django
    data = {}
    data['form'] = form
    data['message'] = 'Edit the Person selected'

    return render(request, 'people/form.html', data)


def get_name(request):

    url = 'http://gerador-nomes.herokuapp.com/nome/aleatorio'

    r = requests.get(url)

    myList = []

    if (r.status_code == 200):
        myList = eval(r.text)
    else:
        myList[0] = "Person"
        myList[1] = "Middle name"
        myList[2] = "Last name"

    new_user = Person
    if request.method == "POST":
        # catching a person yet in edition
        new_user.name = myList[0]
        new_user.last_name = myList[1] + " " + myList[2]
        new_user.years_old = request.POST["years_old"]
        new_user.birth = request.POST["birth"]
        new_user.email = request.POST["email"]
        new_user.nickname = request.POST["nickname"]
        new_user.obervation = request.POST["obervation"]

    form = PersonForm(instance=new_user)
    data = {}
    data["form"] = form
    data['message'] = 'Register a new Person'
    return render(request, 'people/form.html', data)