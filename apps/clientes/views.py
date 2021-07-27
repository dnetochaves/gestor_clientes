from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from . models import Person, Docs
from . forms import PersonForm, DocsForm


def clientes(request):
    list_persons = Person.list_persons()
    return render(request, 'clientes/index.html', {'list_persons': list_persons})

def documentos(request):
    listar_docs = Docs.listar_docs()
    return render(request, 'clientes/documentos.html', {'listar_docs': listar_docs})


def person_new(request):
    list_persons = Person.list_persons()
    form = PersonForm(request.POST or None, request.FILES)
    if form.is_valid():
        frist_name = request.POST['frist_name']
        print(frist_name)
        form.save()
        return HttpResponseRedirect("/clientes/clientes")

    return render(request, 'clientes/person_form.html', {'form': form, 'list_persons': list_persons})

def doc_new(request):
    form = DocsForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/clientes/documentos")

    return render(request, 'clientes/doc_form.html', {'form': form })


def update(request, id):
   person = get_object_or_404(Person, pk=id)
   form = PersonForm(request.POST or None, request.FILES or None, instance=person)
   if form.is_valid():
        form.save()
        return HttpResponseRedirect("/clientes/clientes")
   return render(request, 'clientes/person_form.html', {'form': form}) 
      
       
def delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if request.method == 'POST':
        person.delete()
        return HttpResponseRedirect("/clientes/clientes")
    return render(request, 'clientes/person_delete_confirm.html', {'person': person}) 


def update_doc(request, id):
   doc = get_object_or_404(Docs, pk=id)
   form = DocsForm(request.POST or None, request.FILES or None, instance=doc)
   if form.is_valid():
        form.save()
        return HttpResponseRedirect("/clientes/documentos")
   return render(request, 'clientes/doc_form.html', {'form': form}) 
      
       
def delete_doc(request, id):
    doc = get_object_or_404(Docs, pk=id)
    #form = DocsForm(request.POST or None, request.FILES or None, instance=doc)

    if request.method == 'POST':
        doc.delete()
        return HttpResponseRedirect("/clientes/documentos")
    return render(request, 'clientes/doc_delete_confirm.html', {'doc': doc}) 