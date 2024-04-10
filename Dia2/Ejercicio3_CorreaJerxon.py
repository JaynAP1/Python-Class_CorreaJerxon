import random #Importo una biblioteca ramdon a python

Aleatorio = random.randint(1,100)#Creo la variable que guardara el numero aleatorio
#Imprimo un menu de juego

print("""
Vamos a jugar un juego
Intenta adivinar un numero del 1 al 100
Presiona 1 para comenzar :D
Presiona 2 para terminar el programa :(
""")
intento = int#Establezco la variable intento como un entero
opcion= int(input("Ingresa el numero para comenzar: "))
if opcion==1:
    print("================El juego a comenzado===========")
    for i in range(1,(1+10)):#Ciclo for que determinara los 10 intento posibles en el juego
        intento=int(input("Intenta adiviar el numero: "))#Variable de intento, guardara la informacion del numero del usuario
        if intento == Aleatorio:#Si el numero guardado en la variable intento es igual a aleatorio dara el juego por terminado
            print("Has ganado el juego felicitaciones :D, lo has completado en: ",i, " intentos.")
            break

        else:#Si no son iguales entonces imprimira dependiendo de la condicion que se cumpla
            if intento > Aleatorio:
                print("Casi le pegas, un poco mas abajo :D")

            if intento < Aleatorio:
                print("Casi le pegas un poco mas arriba :D")        


       
     