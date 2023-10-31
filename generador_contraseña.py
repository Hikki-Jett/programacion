import random



def generador_de_contraseñas():
    letras_minuscula = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q"
                        , "r", "s", "t", "w", "x", "y", "z"]

    letras_mayuscula = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q"
                        , "R", "S", "T", "W", "X", "Y", "Z"]

    simbolos = ["@","!","-","_","#","$"]

    contraseña = ""

    for x in range(1,17):
        ran_cont = random.randint(0,3)
        ran_letras = random.randint(0,24)
        ran_simbolos = random.randint(0,5)

        if ran_cont == 0:
            contraseña += letras_minuscula[ran_letras]
        elif ran_cont == 1:
            contraseña += letras_mayuscula[ran_letras]
        elif ran_cont == 2:
            contraseña += simbolos[ran_simbolos]    

    return contraseña

print(generador_de_contraseñas())         

         
