from django.shortcuts import render, redirect, get_object_or_404
from dueños.models import Dueño
from dueños.forms import Dueñoform
# Create your views here.
def nuevoDueño(request):
    if request.method == 'POST':
        formaDueño = Dueñoform(request.POST)
        if formaDueño.is_valid():
            formaDueño.save()
            return redirect('indexDueños')
    else:
        formaDueño = Dueñoform()
    return render(request,'nuevo.html',{'formaDueño':formaDueño})

def editarDueño(request,id):
    dueño = get_object_or_404(Dueño,pk=id)
    if request.method == 'POST':
        formaDueño = Dueñoform(request.POST,instance=dueño)
        if formaDueño.is_valid():
            formaDueño.save()
            return redirect('indexDueños')
    else:
        formaDueño = Dueñoform(instance=dueño)
    return render(request,'editar.html',{'formaDueño':formaDueño})

def eliminarDueño(request, id):
    dueño = get_object_or_404(Dueño,pk=id)
    if dueño :
        dueño .delete()
    return redirect('indexDueños')

def detalleDueño(request,id):
    dueño = get_object_or_404(Dueño,pk=id)
    return render(request,'detalle.html',{'dueño ':dueño })