#2 Manejo y manipulación de elementos de una lista
# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen
# posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
lista = ['a','b','c','d','e','f','g','h','i','j',
       'k','l','m','n','ñ','o','p','q','r','s',
       't','u','v','w','x','y','z']
abc = [lista[i-1] for i in range(1, len(lista)) if i % 3 != 0]
print(' '.join(abc))