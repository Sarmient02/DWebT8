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

from .forms import DocumentosForm

from .models import TipoDocumento

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
