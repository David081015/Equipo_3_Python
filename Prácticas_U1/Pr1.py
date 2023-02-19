#1 Funciones con n parámetros
# Escribir un programa que contenga una función que reciba n parámetros de tipo numérico y calcule el
# producto total.
def producto(*numeros:int)->int:
    total = 1
    for n in numeros:
        total*=n
    return total
print(producto(1,2,3,4,5))