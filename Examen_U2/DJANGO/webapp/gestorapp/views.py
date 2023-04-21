from django.shortcuts import render
from repartidores.models import Repartidor
from dueños.models import Dueño
from pizzas.models import Pizza
# Create your views here.
def index(request):
    return render(request,'Bienvenido.html')

def indexRepartidores(request):
    noRepartidores = Repartidor.objects.count()
    repartidores = Repartidor.objects.order_by('id')
    return render(request,'indexRepartidores.html',{'noRepartidores':noRepartidores, 'repartidores':repartidores})

def indexDueños(request):
    noDueños = Dueño.objects.count()
    dueños = Dueño.objects.order_by('id')
    return render(request,'indexDueños.html',{'noDueños':noDueños, 'dueños':dueños})

def indexPizzas(request):
    noPizzas = Pizza.objects.count()
    pizzas = Pizza.objects.order_by('id')
    return render(request,'indexPizzas.html',{'noPizzas':noPizzas, 'pizzas':pizzas})