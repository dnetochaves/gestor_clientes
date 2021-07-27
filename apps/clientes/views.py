from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from . models import Person
from . forms import PersonForm


def index(request):
    list_persons = Person.list_persons()
    return render(request, 'clientes/index.html', {'list_persons': list_persons})


def person_new(request):
    list_persons = Person.list_persons()
    form = PersonForm(request.POST or None, request.FILES)
    if form.is_valid():
        frist_name = request.POST['frist_name']
        print(frist_name)
        form.save()
        return HttpResponseRedirect("/clientes/")

    return render(request, 'clientes/person_form.html', {'form': form, 'list_persons': list_persons})


def update(request, id):
   person = get_object_or_404(Person, pk=id)
   form = PersonForm(request.POST or None, request.FILES or None, instance=person)
   if form.is_valid():
        form.save()
        return HttpResponseRedirect("/clientes/")
   return render(request, 'clientes/person_form.html', {'form': form}) 
      
       
def delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if request.method == 'POST':
        person.delete()
        return HttpResponseRedirect("/clientes/")
    return render(request, 'clientes/person_delete_confirm.html', {'person': person}) 