################
# - - - Trabajo Integrador Final - - -
# - - - - - - - - Main - - - - - - - -
# Grupo - 6
# Integrantes - Valentin de Brito, Nicolas Levin y Franco Roma
# UNRN Andina - Introduccion a la Ingenieria en Computacion
################

"""
Su mision consiste en diseñar y desarrollar un algoritmo que tenga en cuenta el siguiente manejo del cajero:
a) El cliente presiona el boton de activacion, y de esta manera se solicita el ingreso de su tarjeta.
b) El cliente inserta su tarjeta en la ranura. El algoritmo del cajero automatico lee la informacion de la tarjeta y luego solicita la clave de acceso.
c) El cliente ingresa su clave de acceso, la cual es verificada con la base de datos del banco. Si es correcta le solicitara el numero del DNI y tambien se validara contra la Base de datos. 
En caso de ser correcto se le presentara en pantalla el menu de opciones. En caso de que haya superado mas 3 intentos fallidos de ingreso de la clave de acceso, el cajero retendra la tarjeta.
d) El menu de opciones tiene las siguientes funcionalidades: 1. Consultas, 2. Retiros, 3. Transferencias, 4. Salir
e) El cliente revisara las opciones y en base a su requerimiento, selecciona una opcion.
f) Si el cliente selecciona la opcion 1, le permitira consultar sus cuentas, teniendo dos opciones: 'Posicion GLOBAL' que es el Saldo disponible, o 'Movimientos', que mostrara los ultimos 10 movimientos (generados al azar). 
En cualquiera de ambos casos, se debe solicitar el tipo de moneda ('Soles' / 'Pesos'). Ademas, el usuario podra elegir entre visualizar la consulta en pantalla o imprimir el reporte. 
Luego de ello se finalizara la operacion. En caso de que requiera realizar otra operacion debera regresar al paso e.
g) Si el cliente selecciona la opcion 2, el cajero le solicitara el tipo de moneda ('Soles' / 'Pesos') y el monto a retirar, para luego solicitar la cuenta a debitar. El cajero verifica la disponibilidad de saldo,
en el caso de que no tenga saldo disponible, se le mostrara un mensaje y le permitira modificar el monto 'solo por una vez', o salir de la transaccion. Para el caso de contar con disponibilidad, el
cajero solicita nuevamente que ingrese la clave de acceso, y pregunta si desea impresion de vouchero No, luego finaliza la operacion. En caso de que requiera realizar otra operacion debera regresar
al paso e.
h) Si el cliente selecciona la opcion 3, el cajero solicita el numero de cuenta destino, el tipo de moneda ('Soles' / 'Pesos') y el monto a transferir. Se debe verificar la disponibilidad del saldo de
su cuenta. Ademas, si el numero de la cuenta de destino no es correcto, recien despues de tres dias el cliente podra observar la devolucion de su dinero en sus 'movimientos'. Luego finaliza la operacion. 
En caso de que requiera realizar otra operacion debera regresar al paso e.
i) Si el cliente selecciona la opcion 4, se finaliza la transaccion en el cajero y se expulsa la tarjeta.
Nota: Para poner a prueba el programa implementado, teniendo en cuenta que no estamos manejando Base de Datos, se probara contra el siguiente usuario registrado.
Clave: 12345
DNI: 12345678
Cuenta de destino en la cual se hara la transferencia: 98765
Saldo de la cuenta: en Pesos Argentinos 85.000 (en Soles Peruanos 3.564)
Esta informacion se mantendra constante (a excepcion del saldo) durante la ejecucion del algoritmo.
"""
# Funciones // def - while - if - return - print - input 

from functions import *
def main():
    
    menu = 0
    tries = 0
    saldoP = 8500
    saldoS = 3.564
    user = 12345678
    pswd = 1234
    historialP = [100,-3500,10500,7000,2500,-7000,15000,-9000,500,100]
    historialS = [3000,7500,-15500,-7500,4400,8000,-15000,-9500,-700,12]
    destino = 98765
   
    """
    Se declaran todas las variables que seran necesarias para la correcta ejecucion del cajero.
    """

    while (tries<3):
        
        """
        El programa se ejecuta tantas veces como sea necesario hasta que
        se ingresen erroneamente 3 las credenciales de acceso.
        """
        menu = 0
        
        us = int(input("ingrese su numero de usuario: ")) # aqui se le solicita los datos al usuario
        if(us == user):
            ps = int(input("ingrese su contraseña: ")) # aqui se solicita su contraseña
            if(ps == pswd):
                
                """
                Esta parte del codigo seria el equivalente a un inicio de sesion del banco.
                """
             
                divisa = int(input("en que tipo de moneda desea operar:\n1.pesos\n2.soles\n"))
                """
                Se solicita la divisa con la que se va a operar en esta sesion.
                """
                
                while menu < 4:
                    tries = 0
                    ps = 0
                    menu = int(input("que operacion desea realizar:\n1. consultas\n2. retiros\n3. transferencias\n4.salir\n"))              
                    if menu == 1:
                        consultas(divisa,saldoP,saldoS,historialP,historialS)
                    elif menu == 2:
                        saldoP,saldoS,nuevo,cuenta=retiros(divisa,saldoS,saldoP,pswd)
                        historialP,historialS=actualizar_listas(historialP, historialS,cuenta,nuevo)
                    elif menu==3:
                        saldoP,saldoS,nuevo,cuenta=transferencias(divisa,destino,saldoS,saldoP)
                        historialP,historialS=actualizar_listas(historialP, historialS,cuenta,nuevo)
                        
                        """
                        Esta parte del codigo es el menú de seleccion de operaciones,
                        se encarga de llamar a las funciones correspondientes segun el input del usuario.
                        """

            else:
                tries +=1
                print(f" contraseña invalida, le quedan {3-tries} intentos") 
                """
                Cuenta los ingresos erroneos de la contraseña y/o usuario.
                """
                
        else:
            tries +=1
            print(f"numero de usuario invalido, le quedan {3-tries} intentos") 
            """
            Cuenta los ingresos erroneos de la contraseña y/o del usuario.
            """
    print("ha superado la cantidad maxima de intentos: su tarjeta ha sido retenida")
    """
    En caso de superar la cantidad maxima de intentos se detiene el programa con un mensaje
    que advierte que se retuvo la tarjeta.
    """


if __name__ == "__main__":
    main()
