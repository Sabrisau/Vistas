from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.

def saludo(request):
    nombre = request.GET.get('nombre')
    return HttpResponse(f"Hola {nombre}, soy la vista basada en funciones!!")

class NuevoSaludo(View):
    def get(self, request):
        nombre = request.GET.get('nombre')
        return HttpResponse(f"Hola {nombre}, soy la vista basada en clases!!")
