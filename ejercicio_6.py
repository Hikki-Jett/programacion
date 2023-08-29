# Escribir una función mas_larga() 
# que tome una lista de palabras y devuelva la mas larga.


def mas_larga(lista):
    palabra = lista[0]
    for x in lista:
        if len(x) >= len(palabra):
            palabra = x
        elif len(x) < len(palabra):
            palabra = palabra
    return palabra            




lista = ["Hola","paralelograma","Adios","Manuel","otorrinolaringologo"]
print(mas_larga(lista))