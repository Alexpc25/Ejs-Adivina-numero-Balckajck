import random

# va a escoger un número aleatoriamente, entre 0 y 99
# a = random.randint(0,99)
a = random.randint(0,99)
# le va a pedir al usuario que adivine este número

x = input("Adivine el número entre 0 y 99: ")

while  type(x)!=int or x<0 or x>99:
    try:
        x = int(x)
    except:
        pass
    if type(x)==int and x>=0 and x<=99:
        break

    x= input("Error, introduzca un número adecuado: ")


while x!=a :
    if x > a:
        print ("Demasiado grande")
    else:
        print ("Demasiado pequeño")

    x = input("Vuelva a intentarlo: ")

    while  type(x)!=int or x<0 or x>99:
        try:
            x = int(x)
        except:
            pass
        if type(x)==int and x>=0 and x<=99:
            break
        x = input("Error, introduzca un número adecuado: ")


print("Has adivinado el número!!")