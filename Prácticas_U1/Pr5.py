#5 Manejo de información
# Escribir una función que reciba n parámetros de llave valor e imprima la información en formato
# “{llave}”: “{Valor}”
def informacion(**kwargs):
    for key, value in kwargs.items():
        print(key,value)
    return ""

print(informacion(Casa = "azul", Carro = "Rojo", Perro = "Cafe"))