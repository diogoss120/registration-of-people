from django.shortcuts import render, redirect
from .models import Person
from .form import PersonForm

def get_people(request):
    
    list_people = []
    people = Person.objects.all()
    for person in people:
        #if person.name is None:

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