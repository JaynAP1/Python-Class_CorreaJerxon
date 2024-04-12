#Algoritmo de cambio de monedas

Monedas = [10,5,1] #Creamos una lista que contenga el valor de las monedas

Booleanito=True #Asignamos un True a una variable que usaremos para el mientras
while Booleanito==True:#Creamos un mientras que nos repita el ciclo para las veces que queramos hacer el programa tengamos la posibilidad
    UserMoney=int(input("Escribe la cantidad de dinero que tienes: "))#La variable UserMoney es donde se va a guardar el dinero que tiene el ciente y que necesita desglosar
    if UserMoney > 0 and UserMoney < 1001:#Creamos un condicional que se encargara de decirle al usuario que debe ingreesar un numero mayor a 0 para hacer el desglose de monedas
        for i in Monedas:#Creamos un bucle que se va a encargar junto al condicional de revisar el valor la lista uno por uno junto a la cantidad que el usuario ingrese
            if UserMoney >= i:#condicional que comparara el valor del cliente junto a las monedas
                Plata = UserMoney // i #Creamos una division enteros para que en el resultado no nos de por ejemplo de 25/10=2.5 pero con el // nos dara 2
                print("La cantidad de monedas de",i,"Es de: ",Plata)#Imprimimos la cantidad de monedas que tenemos
                UserMoney=UserMoney%i#Division residual que remplazara el valor del cliente
#Menu que nos permitira repetir o salir del programa
        print("Se daran un total de",Plata,"monedas")

        print("""Deseas terminar el programa o volver reptir
                      1). Para repetir
                      2). Para salir del programa
                      """)
        opcion=int(input("Ingrese un numero de la opcion del menu"))#se guardara las opciones que determinara la decision tomada

        if opcion==1:
                print("Presiona enter para repetir el programa")#Repetira el programa
                Enter=input("")

        elif opcion==2:
                print("Hasta la proxima :D")#Terminara el programa
                Booleanito=False
                

    elif UserMoney <=0:
        print("Ingrese un numero valido, que sea mayor a 0")#Debes ingresar un numero valido
    elif UserMoney >1000:
        print("Ingrese un numero valido, que sea menor de 1001")#Debes ingresar un numero valido



