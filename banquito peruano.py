"""from pynput import keyboard as kb
from os import system, name
def clear():   
  
    if name == 'nt':   
        _ = system('cls')  
def get_key:
    
def consultas:
    moneda=
tries = 0
saldop = 80000
saldos = saldop*0.8
user = 44120913
passwd = 1234
menu = 0 
idle=False
while True:
    while idle:
        if get_cr == "key.space":
            idle=False
    
    ps = int(input("ingrese su contraseña: \n"))
    clear()

    if ps == passwd:
        us =int(input("ingrese num de usuario: \n"))
        clear()
        if us == user:
                while menu <4:
                    menu=int(input("1 = consultas \n2 = retiros \n3 = transferencias \n4= salir \n"))
                    print(menu)
                    clear()
                
    else:
        tries +=1
        print(f"contraseña invalida, intentros restantes:  {3 - tries}")
    if 3-tries==0:
        print("su tarjeta ha sido retenida, por favor comuniquese con su entidad bancaria de preferencia")"
"""
from pynput.keyboard import Key, Controller

keyboard = Controller()

# Press and release space
keyboard.press(Key.space)
keyboard.release(Key.space)

# Type a lower case A; this will work even if no key on the
# physical keyboard is labelled 'A'
keyboard.press('a')
keyboard.release('a')

# Type two upper case As
keyboard.press('A')
keyboard.release('A')
with keyboard.pressed(Key.shift):
    keyboard.press('a')
    keyboard.release('a')
#testbranch
