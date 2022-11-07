from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from mi_familia.models import Person

def arbol(request):

    archivo = open(r'.\mi_familia\templates\arbol.html')
    template = Template(archivo.read())
    archivo.close()

    contexto = Context()
    documento = template.render(contexto)

    return HttpResponse(documento)
