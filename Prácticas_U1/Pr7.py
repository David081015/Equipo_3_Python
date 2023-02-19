#7 Formateo y conversiones
# Escribir un programa que muestre un menú con 2 opciones la primera opción “1.- Imprimir
# YYYY/MM/DD” la segunda “2.- Imprimir MM/DD/YYYY” una vez seleccionada la opción imprimir la fecha
# del día de hoy en el formato seleccionado.
from datetime import date
from datetime import datetime

print("1.- Imprimir YYYY/MM/DD")
print("2.- Imprimir MM/DD/YYYY")
op = int(input())
if op == 1:
    fecha= date.today()
    print(fecha)
else:
    fecha= date.today()
    print(fecha.__format__("%m-%d-%Y"))