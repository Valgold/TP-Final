def retiros(div,sS,sP,psw):
    """
    Realiza un retiro de dinero desde una caja especificada en funcion de un tipo de moneda.
    Admite hasta dos ingresos de monto invalidos.
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
    return sP, sS


def consultas(div,sP,sS,hP,hS):
    """
    
    """
    PGoM=int(input("Que desea consultar:\n1.Posicion Global\n2.Movimientos\n"))
    if PGoM<2:
        divisa=int(input("Que cuenta desea observar?\n1.pesos\n2.soles\n"))
        if div<2:
            print(f'Su saldo en pesos es de ${sP}')
            reporte=sP
        else:
            print(f'Su saldo en soles es de ${sS}')
            reporte=sS
    else:
        if div<2:
            print(f'sus ultimos movimientos en su cuenta en pesos son: {hP}')
            reporte=sP
        else:
            print(f'sus ultimos movimientos en su cuenta en soles son:{hS}')
            reporte=sS
    imprimir=int(input("desea imprimir un reporte?\n1. si\n2. no\n"))
    if imprimir<2:
        print("su reporte se esta imprimiendo...")
        print("""———————————No recivo?———————————""")
    else:
        print("gracias por su consulta")
    

def transferencias(div,cuentaT,sS,sP):
    """
     
    """
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
    return sP,sS

def montoValido(div,cuenta,sS,sP,op):
    """
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
    """
    Extrae una cantidad determinada de dinero en funcion de una divisa especificada.
        div:    1 = Pesos
                2 = Soles
        cuenta:
                1 = Cuenta en Pesos
                2 = Cuenta en Soles
        sS = Saldo de la cuenta en soles
        sP = Saldo de la cuenta en Pesos
        op = Saldo a restar
    Retorna una tupla indicando los valores de saldo actualizados luego de la operacion.
    
    """
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
    return sP,sS


