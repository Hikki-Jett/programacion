import pywhatkit
import datetime

_Usuario = False
V_Usuario = ""

def confirmacion_mensaje(Numero_de_Telefono, Mensaje, Hora, Minuto):
    print("---------- Esta es la confirmacion del mensaje ----------")
    print(f"El numero al que enviaras el mensaje es: {Numero_de_Telefono}")
    print(f"El mensaje que enviaras es: {Mensaje}")
    print(f"La hora a la que sera enviado el mensaje es {Hora}:{Minuto}")
    print("---------------------------------------------------------")


    confirmacion_usuario = str(input("Si es correcta la informacion escribe Aceptar en caso de ser incorrecta escribe Cancelar: "))
    confirmacion_usuario.lower()
    if confirmacion_usuario == "Aceptar":
        print("Mensaje en proceso de envio")
        return "Si"
    elif confirmacion_usuario == "Cancelar":
        print("Confirmacion cancelada mensaje no enviado")
        return "No"

def envio_mensaje(Numero_de_Telefono, Mensaje, Hora, Minuto):
    pywhatkit.sendwhatmsg(Numero_de_Telefono, Mensaje, Hora, Minuto)       

while _Usuario == False:

    Numero_de_Telefono = str(input("Ingresa el numero con todo y el lada: "))
    Mensaje = str(input("Ingresa el mensaje a enviar: "))
    Hora = int(input("Ingresa la hora a la que quieres mandar el mensaje: "))
    Minuto = int(input("Ingresa el minuto: "))

    resp = confirmacion_mensaje(Numero_de_Telefono, Mensaje, Hora, Minuto)

    if resp == "Si":
        envio_mensaje(Numero_de_Telefono,Mensaje,Hora,Minuto)
    elif resp == "No":
        break    
    V_Usuario = str(input("Quieres enviar otro mensaje?: SI/NO: "))
    V_Usuario.lower()
    
    while V_Usuario != "si" and V_Usuario != "no":  
        print("Esa opcion no existe")
        V_Usuario = str(input("Solo puedes responder con si o no "))
        V_Usuario.lower()
           
    if V_Usuario == "si":       
        _Usuario = False
    elif V_Usuario == "no":
        _Usuario = True
    