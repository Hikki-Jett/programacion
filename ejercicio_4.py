# Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
# ****
# *********
# *******

def procedimiento(lista):
    for x in lista:
        for y in range(x):
            print("*",end="")
        print("\b")    


lista = [2,7,1,4]

procedimiento(lista)