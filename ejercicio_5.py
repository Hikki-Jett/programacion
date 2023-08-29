# La función max() del ejercicio 1 (primera parte) y 
# la función max_de_tres() del ejercicio 2 (primera parte), 
# solo van a funcionar para 2 o 3 números. Supongamos que tenemos 
# mas de 3 números o no sabemos cuantos números son. 
# Escribir una función max_in_list() 
# que tome una lista de números y devuelva el mas grande

def max_in_list(lista):
    y = 0
    for x in lista:
        if y > x:
            break
        elif y <= x:
            y = x
    return y

lista = [1,8,5,4]

print(max_in_list(lista))