################
# - - - Trabajo Integrador Final - - -
# - - - - - - - Functions - - - - - - -
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

# Funciones // def - while - if - return - print - input - tuple - listas

def retiros(div,sS,sP,psw):
    """
    Realiza un retiro de dinero desde una caja especificada en funcion de un tipo de moneda.
    Admite hasta dos ingresos de monto invalidos.
    Retorna una tupla con los valores de saldo posteriores al procesamiento.
    """
    first=True
    reingreso=0
    while reingreso<2:
        operacion=float(input("Inserte el monto a retirar: "))
        cuenta=int(input("Seleccione la cuenta con la que desea operar:\n1.cuenta en pesos\n2.cuenta en soles\n"))
        valido=montoValido(div,cuenta,sS,sP,operacion)
        if valido:
            p=int(input("Ingrese su clave de acceso nuevamente: "))
            if p==psw:
                sP,sS=restarCuenta(div,cuenta,sS,sP,operacion)
                imprimir=int(input("Desea imprimir un voucher?\n1. si\n2. no\n"))
                if imprimir<2:
                    print("Su voucher se esta imprimiendo...")
                    print("""———————————No recivo?———————————""")
            else:
                print("Contraseña invalida, cancelando transaccion...")
            reingreso=2
        else:
            if first:
                first=False
                reingreso=int(input("No cuenta con saldo suficiente, desea reigresar el monto?\n1. si\n2. no\n"))
            else:
                reingreso=2
    nuevosaldo=[sP,sS]
    return nuevosaldo


def consultas(div,sP,sS,hP,hS):
    """
    
    """
    PGoM=int(input("que desea consultar:\n1.Posicion Global\n2.Movimientos\n"))
    if PGoM<2:
        divisa=int(input("que cuenta desea observar?\n1.pesos\n2.soles\n"))
        if div<2:
            print(f'su saldo en pesos es de ${sP}')
            reporte=sP
        else:
            print(f'su saldo en soles es de ${sS}')
            reporte=sS
    else:
        if div<2:
            print(f'sus ultimos movimientos en su cuenta en pesos son {hP}')
            reporte=sP
        else:
            print(f'sus ultimos movimientos en su cuenta en soles son:{hS}')
            reporte=sS
    imprimir=int(input("desea imprimir un reporte?\n1. si\n2. no\n"))
    if imprimir<2:
        print("su reporte se esta imprimiendo...")
        print("""———————————No recivo?———————————
⠀⣞⢽⢪⢣⢣⢣⢫⡺⡵⣝⡮⣗⢷⢽⢽⢽⣮⡷⡽⣜⣜⢮⢺⣜⢷⢽⢝⡽⣝
⠸⡸⠜⠕⠕⠁⢁⢇⢏⢽⢺⣪⡳⡝⣎⣏⢯⢞⡿⣟⣷⣳⢯⡷⣽⢽⢯⣳⣫⠇
⠀⠀⢀⢀⢄⢬⢪⡪⡎⣆⡈⠚⠜⠕⠇⠗⠝⢕⢯⢫⣞⣯⣿⣻⡽⣏⢗⣗⠏⠀
⠀⠪⡪⡪⣪⢪⢺⢸⢢⢓⢆⢤⢀⠀⠀⠀⠀⠈⢊⢞⡾⣿⡯⣏⢮⠷⠁⠀⠀
⠀⠀⠀⠈⠊⠆⡃⠕⢕⢇⢇⢇⢇⢇⢏⢎⢎⢆⢄⠀⢑⣽⣿⢝⠲⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡿⠂⠠⠀⡇⢇⠕⢈⣀⠀⠁⠡⠣⡣⡫⣂⣿⠯⢪⠰⠂⠀⠀⠀⠀
⠀⠀⠀⠀⡦⡙⡂⢀⢤⢣⠣⡈⣾⡃⠠⠄⠀⡄⢱⣌⣶⢏⢊⠂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢝⡲⣜⡮⡏⢎⢌⢂⠙⠢⠐⢀⢘⢵⣽⣿⡿⠁⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠨⣺⡺⡕⡕⡱⡑⡆⡕⡅⡕⡜⡼⢽⡻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣳⣫⣾⣵⣗⡵⡱⡡⢣⢑⢕⢜⢕⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣾⣿⣿⣿⡿⡽⡑⢌⠪⡢⡣⣣⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡟⡾⣿⢿⢿⢵⣽⣾⣼⣘⢸⢸⣞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠁⠇⠡⠩⡫⢿⣝⡻⡮⣒⢽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
—————————————————————————————""")
    else:
        print("gracias por su consulta")

def transferencias(div,cuentaT,sS,sP):
    destino=int(input("ingrese la cuenta de destino: "))
    cuenta=int(input("que cuenta desea usar:\n1. pesos\n2. soles\n "))
    monto=float(input("ingrese el monto a retirar: "))
    valid=montoValido(div,cuenta,sS,sP,monto)
    if valid:
        sP,sS=restarCuenta(div,cuenta,sS,sP,monto)
        if destino==cuentaT: 
            print("transaccion realizada con exito")
        else: 
            print("transaccion fallida, su dinero sera reintegrado pasados 3 dias habiles")
    else: 
        print("no cuenta con fondos suficientes en la cuenta seleccionada, vuela a intentarlo")
    nuevosaldo=[sP,sS]
    return nuevosaldo

def montoValido(div,cuenta,sS,sP,op):
    """
    montovalido(divisa, numero de cuenta, saldo cuenta 1, saldo cuenta 2, operacion)
    Verifica que la cuenta espeficicada tenga saldo suficiente dependiendo de la operacion:
    Retorna:
        True si tiene saldo suficiente
        False no tiene saldo suficiente
    """
    if div<2:
        if cuenta<2:
            v=(sP-op)>=0
        else:
            v=(sS-op*0.04194)>=0
    else:
        if cuenta<2:
            v=(sP-op/0.04194)>=0
        else:
            v=(sS-op)>=0
    return v
def restarCuenta(div,cuenta,sS,sP,op):
    if div<2:
        if cuenta<2:
            sP=(sP-op)
        else:
            sS=(sS-op*0.04194)
    else:
        if cuenta<2:
            sP=(sP-op/0.04194)
        else:
            sS=(sS-op)
    nuevosaldo=[sP,sS]
    return nuevosaldo


