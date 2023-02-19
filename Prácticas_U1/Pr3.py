#3 Entrada de datos y manipulación.
# Escribir un programa que permita al usuario capturar su nombre completo e imprima su nombre de
# manera inversa letra por letra
print("Ingrese su nombre")
nom = input()
print(''.join(reversed(nom))) 