from email import message
import http
from xml.dom.minidom import Document
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .forms import DocumentosForm, CiudadesForm, PersonasForm

from .models import TipoDocumento, Ciudad, Persona

# Create your views here.

def home(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context,request))

def documentos(request):
    documentos = TipoDocumento.objects.all()
    template = loader.get_template('personas/documentos.html')
    context = {
        'documentos':documentos,
    }
    return HttpResponse(template.render(context, request))

def new_document(request):

    if request.method == 'POST':

        form = DocumentosForm(request.POST)

        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            doc = TipoDocumento(nombre=nombre,descripcion=descripcion)
            doc.save()
            return HttpResponseRedirect(reverse('documentos'))

    else:
            form = DocumentosForm()

    return render(request, 'personas/create_documentos.html', {'form':form})

def edit_document(request, pk):
    doc = get_object_or_404(TipoDocumento, pk=pk)

    if request.method == 'POST':
        form = DocumentosForm(request.POST, instance=doc)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('documentos'))
    else:
        form = DocumentosForm(instance=doc)

        return render(request, 'personas/edit_documentos.html', {'form':form})

def delete_document(request, pk):

    TipoDocumento.objects.filter(id=pk).delete()

    documentos = TipoDocumento.objects.all()

    template = loader.get_template('personas/documentos.html')

    context = {
        'documentos':documentos,
    }
    
    return HttpResponse(template.render(context, request))

def ciudades(request):
    ciudades = Ciudad.objects.all()
    template = loader.get_template('personas/ciudades.html')
    context = {
        'ciudades':ciudades,
    }
    return HttpResponse(template.render(context, request))

def new_ciudad(request):

    if request.method == 'POST':

        form = CiudadesForm(request.POST)

        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            doc = Ciudad(nombre=nombre,descripcion=descripcion)
            doc.save()
            return HttpResponseRedirect(reverse('ciudades'))

    else:
            form = CiudadesForm()

    return render(request, 'personas/create_ciudades.html', {'form':form})

def edit_ciudad(request, pk):
    doc = get_object_or_404(Ciudad, pk=pk)

    if request.method == 'POST':
        form = CiudadesForm(request.POST, instance=doc)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ciudades'))
    else:
        form = DocumentosForm(instance=doc)

        return render(request, 'personas/edit_ciudades.html', {'form':form})

def delete_ciudad(request, pk):

    Ciudad.objects.filter(id=pk).delete()

    documentos = Ciudad.objects.all()

    template = loader.get_template('personas/ciudades.html')

    context = {
        'ciudades':ciudades,
    }
    
    return HttpResponse(template.render(context, request))

def personas(request):
    personas = Persona.objects.all()
    template = loader.get_template('personas/personas.html')
    context = {
        'personas':personas,
    }
    return HttpResponse(template.render(context, request))

def new_persona(request):
    ciudades = Ciudad.objects.all()
    documentos = TipoDocumento.objects.all()

    if request.method == 'POST':

        form = PersonasForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            lastname = form.cleaned_data['lastname']
            tipodocumento = form.cleaned_data['tipodocumento']
            documento = form.cleaned_data['documento']
            lugarnacimiento = form.cleaned_data['lugarnacimiento']
            fechanacimiento = form.cleaned_data['fechanacimiento']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #cpassword = request.POST.cleaned_data['cpassword']
            doc = Persona(
                name=name,lastname=lastname,
                tipodocumento=tipodocumento,
                documento=documento,
                lugarnacimiento=lugarnacimiento,
                fechanacimiento=fechanacimiento,
                email=email,
                telefono=telefono,
                username=username,
                password=password
                )
            doc.save()
            return HttpResponseRedirect(reverse('personas'))

    else:
            form = PersonasForm()

    return render(request, 'personas/create_personas.html', {'form':form, 'ciudades':ciudades, 'documentos':documentos})

def edit_persona(request, pk):
    personas = Persona.objects.get(pk=pk)
    doc = get_object_or_404(Persona, pk=pk)
    
    ciudades = Ciudad.objects.all()
    documentos = TipoDocumento.objects.all()

    if request.method == 'POST':
        form = PersonasForm(request.POST, instance=doc)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('personas'))
    else:
        form = PersonasForm(instance=doc)

        return render(request, 'personas/edit_personas.html', {'form':form, 'ciudades':ciudades, 'documentos':documentos, 'personas':personas})

def delete_persona(request, pk):

    Persona.objects.filter(id=pk).delete()

    personas = Persona.objects.all()

    template = loader.get_template('personas/personas.html')

    context = {
        'personas':personas,
    }
    
    return HttpResponse(template.render(context, request))
