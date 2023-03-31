from django.shortcuts import render
from personas.models import Persona
from tiendas.models import Tienda
from celulares.models import Celular
# Create your views here.
def index(request):
    noPersonas = Persona.objects.count()
    personas = Persona.objects.order_by('id')

    noTiendas = Tienda.objects.count()
    tiendas = Tienda.objects.order_by('id')

    noCelulares = Celular.objects.count()
    celulares = Celular.objects.order_by('id')

    return render(request,'index.html',{'noPersonas':noPersonas, 'personas':personas,
                                        'noTiendas':noTiendas, 'tiendas':tiendas,
                                        'noCelulares':noCelulares, 'celulares':celulares})