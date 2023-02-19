#6 Razonamiento y prueba de código
# Escribir un programa que reciba un numero entre 0 y 20 e imprimir el numero en letra, no utilizar
# condicionales, máximo 5 líneas de código.
def NumLet(numero):
    dic = {'0':"Cero",'1':"Uno",'2':"Dos", '3':"Tres",'4':"Cuatro",'5':"Cinco",'6':"Seis",'7':"Siete", '8':"Ocho", '9':"Nueve",
    '10':"Diez",'11':"Once",'12':"Doce",'13':"Trece",'14':"Catorce",'15':"Quince",'16':"Dieciseis",'17':"Diecisiete",'18':"Dieciocho",'19':"Diecinueve",'20':"Veinte"}
    print(dic.get(str(numero)))
NumLet(input("Teclee un numero del 0 al 20: "))