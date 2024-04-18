import os

#Listas
Usuarios=[]
Contraseñas=[]
Dinero=[200]

#Variables
Años=0
PrecioAño=200
DineroCliente=0

#Tuplas
Frutas=[("Banana",0.45,6),("Kiwi",4.55,5),("Sandia",5,2)]

while True: #Ciclo While que determinara todo el programa
    os.system("cls") #Borrar pantalla
    print("""
    ==========================================================================================
        Bienvenidos a PeriodicNewTime
        Para poder ver las noticias debes iniciar sesion con tu usuario y contraseña
        
        1). Iniciar sesion.
        2). Comprar cuenta.
        3). Añadir dinero a la cuenta bancaria.
        4). Fruteria.
        5). Terminar el programa.
    ==========================================================================================
    """)#Menu principal del programa

    opcion1=int(input(""))#Entrada que determinara a a la opcion deseada

    if opcion1==1:#Si la opcion es 1 entonces entrara y pedira un usuario y una contraseña
        Booleanito=True
        while Booleanito==True: #Ciclo del login
            os.system("cls")
            ComparadorU=input("Ingrese el usuario")
            if ComparadorU in Usuarios: #Compara los usuarios de la lista con el usuario que ingresa el cliente para intentar loguearse
                print("Usuario exitoso")
                ComparadorC=input("Ingrese su contraseña")
                if ComparadorC in Contraseñas: #Compara las contraseñas de la lista con la que ingresa el usuario
                    print("Contrase Correcta")
                    boole=True
                    while boole==True:
                        os.system("cls")
                        print("""
    ====================================Noticiera=========================
                    1). Ver las noticias mas importante
                    2). Tiempo de suscripcion
                    3). Volver al menu principa
    ======================================================================
    """)#Menu del noticiero en dado caso de poder iniciar sesion
                        OpcionMenu=int(input("Elije con un numero la opcion deseada: "))
                        if OpcionMenu==1:
                            print("""
    ===================================================================================
                    Noticias: Anoche se fue la luz D:
    ===================================================================================
    """)#Noticias super importante
                            print(input("Presione Enter para voler al menu"))
                        
                        elif OpcionMenu==2:#Tiempo de la suscripcion
                            print("Tiempo de suscripcion disponibles: ", Años, "Años")
                            print(input("Presione Enter para voler al menu"))
                        
                        elif OpcionMenu==3:#Volver al menu principal
                            print(input("Presione Enter para voler al menu principal"))
                            boole=False
                    

                else:
                    print("Contraseña incorrecta")
                    Salir=int(input("Presione 1 para seguir con el Login o 0 para ir denuevo al menu principal")) #En caso de ser incorrecta dira que es incorreco y pedira otra vez el usuario si el cliente asi lo desea
                
                if Salir == 0:
                    Booleanito=False
            else:
                print("Usuario incorrecto")
                Salir=int(input("Presione 1 para seguir con el Login o 0 para ir denuevo al menu principal"))#En caso de ser incorrecta dira que es incorreco y pedira otra vez el usuario si el cliente asi lo desea
                
                if Salir == 0:
                    Booleanito=False

    elif opcion1==2:#Opcion del menu principal
        BooleanitoC=True
        while BooleanitoC==True:
            os.system("cls")
            print("Comprar cuenta")#Permite comprar cuenta o regalarla 
            print("""
    ============================================================================
                1). Comprar cuenta.
                2). Comprar cuenta regalo.
                3). Volver al menu principal.
    ============================================================================
    """)#Menu con las opciones disponibles
            OpcionC=int(input("Ingrese con un numero la opcion deseada: "))
            if OpcionC==1:#
                print("====================================================================================")
                AñosC=int(input("¿Cuantos años deseas comprar?"))#Cuantos años desea comprar
                print("====================================================================================")
                PrecioCli=PrecioAño*AñosC#Hace la formulacion del precio que asumira el cliente

                if PrecioCli <= DineroCliente:#Si el precio es menor al que el cliente tiene le permitira comprar
                    Nombre=input("Escriba el nombre de usuario para la nueva cuenta:")
                    Contraseña=input("Escriba la contraseña para la cuenta: ")
                    Usuarios.append(Nombre)
                    Contraseñas.append(Contraseña)
                    Años +=AñosC

                    print("Cuenta comprada")
                    print(input("Presione Enter para continuar"))
                
                else:
                    print(input("No hay dinero suficiente en la cuenta, presione Enter para continuar"))#En caso que no lo sea lo devolvera al menu
            
            if OpcionC==2:
                print("====================Regalo====================")#Si quiere regaar un cuenta
                Regalo=int(input("¿Cuantos años deseas regalar?"))
                PrecioRegalo=PrecioAño*Regalo#Calculo del valor de la cuenta que deseas regalar

                if PrecioRegalo <= DineroCliente: #Si el precio es menor al que el cliente tiene le permitira comprar
                    NombreRe=input("Nombre de la cuenta a la que le deseas regalar la suscripcion")
                    print("Suscripcion regalada con exito")
                    print(input("Presione Enter para continuar"))
                
                else:
                    print(input("No hay dinero suficiente en la cuenta, presione Enter para continuar"))#En caso que no lo sea lo devolvera al menu

            if OpcionC==3: #Permite salir al menu principal
                print("Saliendo al menu principal")
                print(input("Presione Enter para continuar"))
                BooleanitoC=False

    elif opcion1==3:#Opcion numero 3
        Booleanito3=True
        while Booleanito3==True:
            os.system("cls")
            print("""
    ======================================Newi====================================================
                1).Agregar dinero.
                2).Ver saldo.
                3).Salir al menu principal.
    ==============================================================================================
    """)#Menu del banco fictisio

            Opcion2=int(input("Que deseas hacer en el Newi"))

            if Opcion2 ==1:
                print("Agregar dinero")#Permite agregar dinero a una cuenta del cliente
                DineroNeW=int(input("¿Cuanto dinero deseas agregar? "))
                DineroCliente+=DineroNeW
                print(input("Presione Enter para continuar"))

            if Opcion2 ==2:#Permite ver el dinero que posee el cliente
                print("Dinero que tienes en la cuenta: ", DineroCliente)
                print(input("Presione Enter para continuar"))
            
            if Opcion2 ==3:#Vuelve al menu principal
                print("Saliendo al menu principal")
                print(input("Presione Enter para continuar"))
                Booleanito3=False

    elif opcion1==4: #Fruteria
        print("Frutas que hay en stock")#Frutas que hay en stock
        for i in Frutas:print(i[0])
        
        print("Precio de las frutas que son menor a .50")#Frutas que su precio es menor a 0.50
        for a in Frutas: 
            if a[1] <= 0.50:
                print(a)
        
        print("La fruta que mas cantidades tiene")#La fruta que mas cantidad de unidades posee
        FrutasMa=max(Frutas, key=lambda x: x[2]); print(FrutasMa)
        
        print("La multiplicacion del precio de la fruta por su cantidad.")#Multiplica el precio de la fruta por las unidades que hay
        for i in Frutas:
            Precio=i[1]*i[2]
            print(Precio)

        
        print(input("Presione Enter para contuniar"))

    elif opcion1==5:
        print(input("Terminando programa, Presione Enter para salir"))#Terminar el programa.
        break