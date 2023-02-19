#4 Entrada de datos y estructuración.
# Revisar su retícula para escribir un programa que cree un diccionario vacío para que el usuario capture
# las materias y créditos de su semestre preferido (inferior a 8vo) al final imprimir en el formato
# “{asignatura}” tiene “{créditos}” créditos. Y la suma de todos los créditos del semestre
di = {}
def suma(**kwargs):
    suma = 0
    for key, value in kwargs.items():
        suma+=value
        print(key,'tiene',value)
    return suma

seguir = True
while seguir != False:
    print("Ingrese la asignatura")
    asig = input()
    print("Ingrese los creditos")
    cre = int(input())
    di[asig] = cre
    print("¿Quiere agregar otra?   si/no")
    pre = input()
    if pre == "no":
        seguir = False
    print("\n")

print("Total creditos: ", suma(**di))