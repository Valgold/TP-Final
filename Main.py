from functions import *
def main():
    cuentaT = 98765
    menu = 0
    tries = 0
    saldoP = 8500
    saldoS = 3.564
    user = 12345678
    pswd = 1234
    historialP = [100,-3500,10500,7000,2500,-7000,15000,-9000,500]
    historialS = [3000,7500,-15500,-7500,4400,8000,-15000,-9500,-700]
    destino = 1234
   
""""
se declaran todas las variables que seran necesarias para la correcta ejecucion del cajero
""""

    while (tries<3):
        """
        el programa se ejecuta tantas veces como sea necesario hasta que
        se ingresen mal las credenciales de acceso repetidas veces
        """
        menu = 0
        
        us = int(input("ingrese su numero de usuario: ")) # aqui se le solicita los datos al usuario
        if(us == user):
            ps = int(input("ingrese su contraseña: ")) # aqui se solicita su contraseña
            if(ps == pswd):
         """
         esta parte del codigo seria el equivalente a un log in del banco
         """
             
                divisa = int(input("en que tipo de moneda desea operar:\n1.pesos\n2.soles\n"))
                """
                se solicita la divisa con la que se va a operar en esta sesion
                """
                
                while menu < 4:
                    tries = 0
                    ps = 0
                    menu = int(input("que operacion desea realizar:\n1. consultas\n2. retiros\n3. transferencias\n4.salir\n"))              
                    if menu == 1:
                        consultas(divisa,saldoP,saldoS,historialP,historialS)
                    elif menu == 2:
                        saldoP,saldoS=retiros(divisa,saldoS,saldoP,pswd)
                    elif menu==3:
                        saldoP,saldoS=transferencias(divisa,destino,saldoS,saldoP)
             """
             esta parte del codigo es el menú de seleccion de operaciones,
             se encarga de llamar a las funciones correspondientes segun el input del usuario
             """

            else:
                tries +=1
                print(f" contraseña invalida, le quedan {3-tries} intentos") 
                """
                cuenta los ingresos erroneos de la contraseña y/o uduario
                """
                
        else:
            tries +=1
            print(f"numero de usuario invalido, le quedan {3-tries} intentos") 
            """
            cuenta los ingresos erroneos de la contraseña /o del usuario
            """
    print("ha superado la cantidad maxima de intentos: su tarjeta ha sido retenida")
    
    """
    en caso de superar la cantidad maxima de intentos se detiene el programa con un mensaje
    que advierte que se retuvo la tarjeta
    """



main()

