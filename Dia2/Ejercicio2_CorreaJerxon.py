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
opcion= int(input("Ingresa el numero para comenzar: "))#Creo una variable opcion que a su vez guardara el numero que especifique el usuario
if opcion==1:
    print("================El juego a comenzado===========")
    while intento != Aleatorio:#Un ciclo mientras que hara infinito el programa hasta que el jugador descubra el numero
        intento = int(input("Intenta adivinar el numero: "))#Variable de intento, guardara la informacion del numero del usuario
    

        if intento == Aleatorio: #Comparara las variabless y si son iguales imprimira
            print("Has ganado el juego :D")
            break

        else:#Si no son iguales entonces imprimira dependiendo de la condicion que se cumpla
            if intento > Aleatorio:
                print("Casi le pegas, un poco mas abajo :D")

            if intento < Aleatorio:
                print("Casi le pegas un poco mas arriba :D")        

     
