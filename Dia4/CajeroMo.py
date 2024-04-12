#Algoritmo de cambio de monedas

Monedas = [10,5,1]

Booleanito=True
while Booleanito==True:
    UserMoney=int(input("Escribe la cantidad de dinero que tienes: "))
    if UserMoney > 0:
        for i in Monedas:
            if UserMoney >= i:
                Plata = UserMoney // i
                print("La cantidad de monedas de",i,"Es de: ",Plata)
                UserMoney=UserMoney%i

                print("""Deseas terminar el programa o volver reptir
                      1). Para repetir
                      2). Para salir del programa
                      """)
                opcion=int(input("Ingrese un numero de la opcion del menu"))

                if opcion==1:
                     print("Presiona enter para repetir el programa")
                     Enter=input("")

                elif opcion==2:
                    print("Hasta la proxima :D")
                    Booleanito=False
                

    elif UserMoney <=0:
             print("Ingrese un numero valido, que sea mayor a 0")



