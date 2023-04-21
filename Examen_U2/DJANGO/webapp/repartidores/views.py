from django.shortcuts import render, redirect, get_object_or_404
from repartidores.models import Repartidor
from repartidores.forms import Repartidorform
# Create your views here.
def nuevoRepartidor(request):
    if request.method == 'POST':
        formaRepartidor = Repartidorform(request.POST)
        if formaRepartidor.is_valid():
            formaRepartidor.save()
            return redirect('indexRepartidores')
    else:
        formaRepartidor = Repartidorform()
    return render(request,'nuevo.html',{'formaRepartidor':formaRepartidor})

def editarRepartidor(request,id):
    repartidor = get_object_or_404(Repartidor,pk=id)
    if request.method == 'POST':
        formaRepartidor = Repartidorform(request.POST,instance=repartidor)
        if formaRepartidor.is_valid():
            formaRepartidor.save()
            return redirect('indexRepartidores')
    else:
        formaRepartidor = Repartidorform(instance=repartidor)
    return render(request,'editar.html',{'formaRepartidor':formaRepartidor})

def eliminarRepartidor(request, id):
    repartidor = get_object_or_404(Repartidor,pk=id)
    if repartidor :
        repartidor .delete()
    return redirect('indexRepartidores')

def detalleRepartidor(request,id):
    repartidor = get_object_or_404(Repartidor,pk=id)
    return render(request,'detalle.html',{'repartidor ':repartidor })