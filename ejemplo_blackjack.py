import random

puntuacion1= 0 
puntuacion2= 0

mano1= []
mano2= []

def gen_baraja(y,nombres_cartas):
    baraja = []
    for i in range(y):
        x= list(nombres_cartas)
        baraja+=x
    return baraja



def saca_carta(y,puntuacion, mano):
    for i in range(y):
        x= random.randint(0,len(baraja)-1) 
        carta = baraja[x]
        baraja.pop(x)
        puntuacion += cartas[carta]
        mano +=  carta
    return puntuacion 


def fin_juego(a,b):
    print("esta es mi puntación:", b)
    if (a > b and a <= 21) or (b > 21 and a <= 21):
        print("Ha ganado la partida!")
    
    elif (a == b) or (a > 21 and b >21):
        print("Usted ha empatado con la banca")

    else:
        print("Ha perdido")
    

cartas = { 
    "as" : 11, 
    "2" : 2, 
    "3": 3, 
    "4" : 4, 
    "5" : 5, 
    "6" : 6, 
    "7" : 7, 
    "8" : 8, 
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10, 
    "K" : 10,  
}


#valores de cada carta

baraja = gen_baraja(4,list(cartas.keys()))

print(baraja)

#generado la baraja

respuesta= input("¿Quiere jugar al black jack? [Y/N]: ")

while  respuesta != "Y" and respuesta != "N" :

    respuesta= input("La respuesta no es valida: ")

puntuacion1 = saca_carta(2,puntuacion1,mano1)

print("Estas son sus cartas:", mano1 , "y esta es su puntuación actual:", puntuacion1)

#hemos generado dos cartas aleatorias y sumado sus valores

print("Ahora jugará la banca") 

puntuacion2 = saca_carta(2,puntuacion2, mano2)
    
carta1 = mano2[0]
print("Esta es una de mis cartas:", carta1)

decision = input("Desea plantarse [Y/N]: ")
while  decision != "Y" and decision != "N" :

    decision= input("La respuesta no es valida: ")

if decision == "Y" or puntuacion1 > 21:
    fin_juego(puntuacion1,puntuacion2)

else: 
    print("Le repartire otra carta")

    puntuacion1 = saca_carta(1,puntuacion1,mano1)
    print("Estas son sus cartas:", mano1 , "y esta es su puntuación actual:", puntuacion1)

    if puntuacion2 < 17:
        puntuacion2 = saca_carta(2,puntuacion2, mano2)
        
    fin_juego(puntuacion1,puntuacion2)


















