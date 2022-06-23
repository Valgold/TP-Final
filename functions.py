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
    Menu de retiros.
    Admite hasta dos ingresos de monto invalidos. La transaccion se cancela si el reingreso de contraseña es invalido.
    Retorna la tupla resultante de la funcion restarCuenta a la funcion principal.
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
                sP,sS,monedaR,reporte = restarCuenta(div,cuenta,sS,sP,operacion)
                imprimir=int(input("Desea imprimir un voucher?\n1. si\n2. no\n"))
                if imprimir<2:
                    print("Su voucher se esta imprimiendo...")
                    print(f"""·······················································································
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
---------------------------------------------------------------------------------------
Fecha: 22/06/22                  BancoFraNiVaEstacion 6                  Hora: 18:12:37
                                      !Retiro!
                            AV. ZARAZA ZAZA 869, BARILOCHE
                                    DNI:-12345678-
AP: A00000000000012345678                                               Debit FraNiVA
NRO.COM 9812345678                                                      TERM: 129321843
NRO.LOTE: 4449                                                          CUPON: 12423
************5678 *                                                                **/**
02213P786
Cuenta ************5678{monedaR}
Saldo Retirado = $  {operacion}
Saldo Actual = $    {reporte}
                                    (00) APROBADO
                                    Copia Cliente
---------------------------------------------------------------------------------------
_______________________________________________________________________________________
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
·······················································································
                    
                    """)
            else:
                print("Contraseña invalida, cancelando transaccion...")
            reingreso=2
        else:
            if first:
                first=False
                reingreso=int(input("No cuenta con saldo suficiente, desea reigresar el monto?\n1. si\n2. no\n"))
            else:
                reingreso=2
    operacion = (-1)*operacion
    nuevosaldo=(sP,sS,operacion,cuenta)
    return nuevosaldo


def consultas(div,sP,sS,hP,hS):
    """
    Menu de Consultas.
    Imprime el historial de movimientos en funcion de la divisa especificada.
    No retorna un valor en especifico.
    """
    PGoM=int(input("que desea consultar:\n1.Posicion Global\n2.Movimientos\n"))
    if PGoM<2:
        divisa=int(input("que cuenta desea observar?\n1.pesos\n2.soles\n"))
        if div<2:
            print(f'su saldo en pesos es de ${sP}')
            reporte=sP
            monedaR="(AR$)"
        else:
            print(f'su saldo en soles es de ${sS}')
            reporte=sS
            monedaR="($oles)"
    else:
        if div<2:
            print(f'sus ultimos movimientos en su cuenta en pesos son:')
            imprimir_historial(hP)
            reporte=hP
            monedaR="(AR$)"
        else:
            print(f'sus ultimos movimientos en su cuenta en soles son:')
            imprimir_historial(hS)
            reporte=hS
            monedaR="($oles)"
    imprimir=int(input("desea imprimir un reporte?\n1. si\n2. no\n"))
    if imprimir<2:
        print("su reporte se esta imprimiendo...")
        if PGoM<2:
            print(f"""·······················································································
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
---------------------------------------------------------------------------------------
                                 BancoFraNiVaEstacion 6                  
                                    |Posicion Global|
                            AV. ZARAZA ZAZA 869, BARILOCHE
                                    DNI:-12345678-
AP: A00000000000012345678                                               Debit FraNiVA
NRO.COM 9812345678                                                      TERM: 129321843
NRO.LOTE: 4449                                                          CUPON: 12423
************5678 * {monedaR}                                            **/**
02213P786
Saldo Actual = $ {reporte}
                                    (00) APROBADO
                                    Copia Cliente
---------------------------------------------------------------------------------------
_______________________________________________________________________________________
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
·······················································································"""
)
        else:
            print(f"""·······················································································
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
---------------------------------------------------------------------------------------
Fecha: 22/06/22                  BancoFraNiVaEstacion 6                  Hora: 18:12:37
                               !Historial de Movimientos!
                            AV. ZARAZA ZAZA 869, BARILOCHE
                                    DNI:-12345678-
AP: A00000000000012345678                                               Debit FraNiVA
NRO.COM 9812345678                                                      TERM: 129321843
NRO.LOTE: 4449                                                          CUPON: 12423
Numero de Trajeta                                                          
************5678 - 0001                                                           **/**
Ultimos Movimientos en Caja de Ahorros $
Cuenta ************5678 {monedaR}
FECHA 
22/06    XXXXXXXXXX   $         {reporte[0]}      
29/05    XXXXXXXXXX   $         {reporte[1]}     
29/05    XXXXXXXXXX   $         {reporte[2]}   
29/05    XXXXXXXXXX   $         {reporte[3]}   
28/05    XXXXXXXXXX   $         {reporte[4]}
27/05    XXXXXXXXXX   $         {reporte[5]}
27/05    XXXXXXXXXX   $         {reporte[6]}
25/05    XXXXXXXXXX   $         {reporte[7]}
21/05    XXXXXXXXXX   $         {reporte[8]}       
21/05    XXXXXXXXXX   $         {reporte[9]}
                                    (00) APROBADO
                                    Copia Cliente
---------------------------------------------------------------------------------------
_______________________________________________________________________________________
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
·······················································································
            
            """)
            
    else:
        print("gracias por su consulta")

def transferencias(div,cuentaT,sS,sP):
    """
    Menu de transferencias.
    Retorna la tupla resultante de la funcion restarCuenta a la funcion principal.
    """
    destino=int(input("ingrese la cuenta de destino: "))
    cuenta=int(input("que cuenta desea usar:\n1. pesos\n2. soles\n "))
    monto=float(input("ingrese el monto a retirar: "))
    valid=montoValido(div,cuenta,sS,sP,monto)
    if valid:
        sP,sS,_,_=restarCuenta(div,cuenta,sS,sP,monto)
        if destino==cuentaT: 
            print("transaccion realizada con exito")
        else: 
            print("transaccion fallida, su dinero sera reintegrado pasados 3 dias habiles")
    else: 
        print("no cuenta con fondos suficientes en la cuenta seleccionada, vuela a intentarlo")
    monto=(-1)*monto
    nuevosaldo = (sP,sS,monto,cuenta)
    return nuevosaldo

def montoValido(div,cuenta,sS,sP,op,):
    """
    Verifica que la cuenta espeficicada tenga saldo suficiente dependiendo de la operacion.
        div:    1 = Pesos
                2 = Soles
        cuenta:
                1 = Cuenta en Pesos
                2 = Cuenta en Soles
        sS = Saldo de la cuenta en soles
        sP = Saldo de la cuenta en Pesos
        op = Saldo a extraer
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
            v = (sS-op) >= 0
    return v
def restarCuenta(div,cuenta,sS,sP,op):
    """
    Extrae una cantidad determinada de dinero en funcion de una divisa especificada.
        div:    1 = Pesos
                2 = Soles
        cuenta:
                1 = Cuenta en Pesos
                2 = Cuenta en Soles
        sS = Saldo de la cuenta en soles
        sP = Saldo de la cuenta en Pesos
        op = Saldo a extraer
    Retorna una tupla indicando los valores de saldo actualizados luego de la operacion.
    """
    if div<2:
        if cuenta<2:
            sP = (sP-op)
            reporte = sP
            monedaR = "(AR$)"
        else:
            sS=(sS-op*0.04194)
            reporte = sS
            monedaR = "($oles)"
    else:
        if cuenta<2:
            sP=(sP-op/0.04194)
            reporte = sP
            monedaR = "(AR$)"
        else:
            sS=(sS-op)
            reporte = sS
            monedaR = "($oles)"
    
    nuevosaldo=(sP,sS,monedaR,reporte)
    return nuevosaldo

def actualizar_listas(historialP,historialS,divisa,valor_nuevo):
    """
    Actualiza el historial de movimientos a los 10 mas recientes, agregando el ultimo movimiento correspondiente a la lista y eliminando el movimiento mas antiguo.
    Retorna una tupla con los historiales actualizados.
    """
    transicion = []
    if divisa < 2:
        for i in range(len(historialP)-1):
            transicion = transicion + [historialP[i+1]]
        transicion = transicion + [valor_nuevo]
        historialP = transicion
    else:
        for i in range(len(historialS)-1):
            transicion = transicion + [historialS[i+1]]
        transicion = transicion + [valor_nuevo]
        historialS = transicion
    return (historialP,historialS)

def imprimir_historial(lista):
    """
    Transcribe el historial en forma de columna.
    """
    x=0
    while x<len(lista):
        print(lista[x])
        x +=1
        
            

