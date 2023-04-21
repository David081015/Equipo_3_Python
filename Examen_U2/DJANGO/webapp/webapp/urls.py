"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestorapp.views import *
from repartidores.views import *
from dueños.views import *
from pizzas.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('indexRepartidores',indexRepartidores,name='indexRepartidores'),
    path('nuevoRepartidor',nuevoRepartidor),
    path('editarRepartidor/<int:id>',editarRepartidor),
    path('eliminarRepartidor/<int:id>',eliminarRepartidor),
    path('detalleRepartidor/<int:id>',detalleRepartidor),

    path('indexDueños',indexDueños,name='indexDueños'),
    path('nuevoDueño',nuevoDueño),
    path('editarDueño/<int:id>',editarDueño),
    path('eliminarDueño/<int:id>',eliminarDueño),
    path('detalleDueño/<int:id>',detalleDueño),

    path('indexPizzas',indexPizzas,name='indexPizzas'),
    path('nuevaPizza',nuevaPizza),
    path('editarPizza/<int:id>',editarPizza),
    path('eliminarPizza/<int:id>',eliminarPizza),
    path('detallePizza/<int:id>',detallePizza)
]
