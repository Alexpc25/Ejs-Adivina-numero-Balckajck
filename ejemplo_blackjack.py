import random

puntuacion1= 0 
puntuacion2= 0

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

baraja = [] 

while len(baraja) < 52: 
    x= list(cartas.keys())
    baraja+=x

#generado la baraja

respuesta= input("¿Quiere jugar al black jack? [Y/N]: ")

while  respuesta != "Y" and respuesta != "N" :

    respuesta= input("La respuesta no es valida: ")

while len(baraja) > 50:
    x= random.randint(0,len(baraja)-1) 
    carta = baraja[x]
    baraja.pop(x)
    print("Aquí tiene su carta:", carta)
    puntuacion1 += cartas[carta] 

print("Esta es su puntuación actual:", puntuacion1)

#hemos generado dos cartas aleatorias y sumado sus valores

print("Ahora jugará la banca") 

while len(baraja) > 48:
    x= random.randint(0,len(baraja)-1) 
    carta = baraja[x]
    baraja.pop(x)
    puntuacion2 += cartas[carta] 
    
banca= puntuacion2 - cartas[carta]
print("Esta es mi puntuación:", banca)

decision = input("Desea plantarse [Y/N]")
while  decision != "Y" and decision != "N" :

    decision= input("La respuesta no es valida: ")


if decision == "Y":
    print("esta es mi puntiación:", puntuacion2)
    if (puntuacion1 > puntuacion2 and puntuacion1 <= 21) or (puntuacion2 > 21 and puntuacion1 <= 21):
        print("Ha ganado la partida!")
    
    elif puntuacion1 == puntuacion2:
        print("Usted ha empatado con la banca")

    else:
        print("Ha perdido")





