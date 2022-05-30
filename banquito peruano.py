from os import system, name
from random import randint, uniform,randrange

def clear():   
  
    if name == 'nt':   
        _ = system('cls')  

def movimientos():
    global simbolo, moneda
    yi = 2019
    mi= 1
    di = 1
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(10):
        yaux = yi
        maux = mi
        yi = randint(yaux, 2022)
        mi = randint(maux, 12)
        di = randint(di, days[mi - 1])
        mov = round(uniform(-9999.99, 9999.99), 2)
        print(f"{yi}-{mi}-{di} - {simbolo[moneda-1]} {mov}")
        if yaux != yi:
            mi = 1
            di = 1
        elif maux != mi:
            di = 1

def consultas():
    global simbolo,moneda,menu
    opcion = 0
    moneda = 0
    while opcion != 1 and opcion != 2: #Seleccionar 1 o 2
        clear()
        opcion = int(input("Consultas:\n1 = Posicion GLOBAL\n2 = Movimientos"))
    if opcion == 1: #Posicion GLOBAL
        while moneda != 1 and moneda != 2: #Seleccionar el tipo de moneda
            clear()
            moneda = int(input("Seleccione el tipo de moneda:\n1 = Soles\n2 = Pesos"))
        texto = f"{simbolo[moneda-1]}{saldo*cambio[moneda-1]}"
        print(f"Su saldo es de {texto}")
    elif opcion == 2: #Movimientos
        while moneda != 1 and moneda != 2: #Seleccionar el tipo de moneda
            clear()
            moneda = int(input("Seleccione el tipo de moneda:\n1 = Soles\n2 = Pesos"))
        movimientos()
    opcion = 0
    while opcion != 1 and opcion != 2:
        opcion = int(input("Desea realizar otra operacion?:\n1 = Si\n2 = No"))
    if opcion == 2:
        menu = 4

def retiros():
    print("Retiros") #cambiar
    #clear()


def transferencias():
    print("Transferencias") #cambiar
    #clear()


cambio = [1, 0.8]
simbolo = ["S","P"]
moneda = 0
user = 12#44120913
passwd = 1234
menu = 0
idle=True
while True:
    menu = 0
    tries = 0
    while idle:
        clear()
        start = input("Bienvenido al cajero\nPresione ENTER para continuar...")
        idle=False
        clear()
    ps = int(input("ingrese su contraseña: \n"))
    clear()

    if ps == passwd:
        us =int(input("Ingrese num de usuario: \n"))
        clear()
        if us == user:
                saldo = round(uniform(100.00, 99999.99), 2)
                print(saldo)
                while menu <4:
                    menu=int(input("1 = Consultas \n2 = Retiros \n3 = Transferencias \n4= Salir \n"))
                    print(menu)
                    if menu == 1: consultas()
                    elif menu == 2: retiros()
                    elif menu == 3: transferencias()
                    clear()
                idle = True
        else:
            tries += 1
            print(f"usuario invalido, intentos restantes:  {3 - tries}")
    else:
        tries +=1
        print(f"Contraseña invalida, intentos restantes:  {3 - tries}")
    if tries == 3:
        print("Su tarjeta ha sido retenida, por favor comuniquese con su entidad bancaria de preferencia")
        idle = True