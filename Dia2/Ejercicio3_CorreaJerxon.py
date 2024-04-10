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
    for i in range(1,(1+10)):
        intento=int(input("Intenta adiviar el numero: "))
        if intento == Aleatorio:
            print("Has ganado el juego felicitaciones :D, lo has completado en: ",i, " intentos.")

            break

        else:
            if intento > Aleatorio:
                print("Casi le pegas, un poco mas abajo :D")

            if intento < Aleatorio:
                print("Casi le pegas un poco mas arriba :D")        


       
     