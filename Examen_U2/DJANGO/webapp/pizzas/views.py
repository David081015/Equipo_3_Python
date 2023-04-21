from django.shortcuts import render, redirect, get_object_or_404
from pizzas.models import Pizza
from pizzas.forms import Pizzaform
# Create your views here.
def nuevaPizza(request):
    if request.method == 'POST':
        formaPizza = Pizzaform(request.POST)
        if formaPizza.is_valid():
            formaPizza.save()
            return redirect('indexPizzas')
    else:
        formaPizza = Pizzaform()
    return render(request,'nueva.html',{'formaPizza':formaPizza})

def editarPizza(request,id):
    pizza = get_object_or_404(Pizza,pk=id)
    if request.method == 'POST':
        formaPizza = Pizzaform(request.POST,instance=pizza)
        if formaPizza.is_valid():
            formaPizza.save()
            return redirect('indexPizzas')
    else:
        formaPizza = Pizzaform(instance=pizza)
    return render(request,'editar.html',{'formaPizza':formaPizza})

def eliminarPizza(request, id):
    pizza = get_object_or_404(Pizza,pk=id)
    if pizza :
        pizza .delete()
    return redirect('indexPizzas')

def detallePizza(request,id):
    pizza = get_object_or_404(Pizza,pk=id)
    return render(request,'detalle.html',{'pizza ':pizza })