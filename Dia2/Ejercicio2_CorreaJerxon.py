import random 

Aleatorio = random.randint(1,100)

print("""
Vamos a jugar un juego
Intenta adivinar un numero del 1 al 100
Presiona 1 para comenzar :D
Presiona 2 para terminar el programa :(
""")
intento = int
opcion= int(input("Ingresa el numero para comenzar: "))
if opcion==1:
    print("================El juego a comenzado===========")
    while intento != Aleatorio:
        intento = int(input("Intenta adivinar el numero: "))
    

        if intento == Aleatorio:
            print("Has ganado el juego :D")

        else:
            if intento > Aleatorio:
                print("Casi le pegas, un poco mas abajo :D")

            if intento < Aleatorio:
                print("Casi le pegas un poco mas arriba :D")        

     
