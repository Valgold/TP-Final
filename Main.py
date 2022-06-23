from functions import *
def main():
    cuentaT=98765
    menu=0
    tries=0
    saldoP=8500
    saldoS=3.564
    user=12345678
    pswd=1234
    historialP=[100,-3500,10500,7000,2500,-7000,15000,-9000,500]
    historialS=[3000,7500,-15500,-7500,4400,8000,-15000,-9500,-700]
    destino=1234

    while (tries<3):
        menu=0
        us=int(input("ingrese su numero de usuario: "))
        if(us==user):
            ps=int(input("ingrese su contraseña: "))
            if(ps==pswd):
                divisa=int(input("en que tipo de moneda desea operar:\n1.pesos\n2.soles\n"))
                while menu < 4:
                    tries=0
                    ps=0
                    menu=int(input("que operacion desea realizar:\n1. consultas\n2. retiros\n3. transferencias\n4.salir\n"))
                    if menu==1:
                        consultas(divisa,saldoP,saldoS,historialP,historialS)
                    elif menu==2:
                        saldoP,saldoS=retiros(divisa,saldoS,saldoP,pswd)
                    elif menu==3:
                        saldoP,saldoS=transferencias(divisa,destino,saldoS,saldoP)

            else:
                tries +=1
                print(f" contraseña invalida, le quedan {3-tries} intentos") 
                
        else:
            tries +=1
            print(f"numero de usuario invalido, le quedan {3-tries} intentos") 
            
    print("ha superado la cantidad maxima de intentos: su tarjeta ha sido retenida")



main()

