import os

Motos={
    "Moto1":{
        "Marca": "Suzuki","Modelo": "GN 125","Precio": 9000000,"ID": 203012
    },
    "Moto2":{"Marca": "Vespa","Modelo": "SXL 150","Precio": 5000000,"ID": 23923
    },
    "Moto3":{
        "Marca": "TVS","Modelo": "Apache 160 4v","Precio": 10000000,"ID": 32131
    },
    "Moto4":{
        "Marca": "Yamaha","Modelo": "FZ 150 2.0","Precio": 10000000,"ID": 123123
    },
    "Moto5":{
        "Marca": "Kawasaki","Modelo": "Ninja 300","Precio": 15000000,"ID": 456456
    },
}
Cantidad={"Moto1":5, "Moto2":4, "Moto3":2, "Moto4":3,"Moto5":3}

DiccionarioC={"Moto1":0, "Moto2":0, "Moto3":0, "Moto4":0,"Moto5":0}

SumaPrecios={"Moto1":0, "Moto2":0, "Moto3":0, "Moto4":0,"Moto5":0}

print("""
================================================================
      Bienvenidos a MotoCompraMotora
      A continucion le mostraremos los productos disponibles
=================================================================
""")


print("=====================================================")

Enter=input("Presione Enter para continuar")

booleanito=True
while booleanito==True:
    os.system("cls")
    print("Catalogo: ")
    print(Motos["Moto1"]);print(Motos["Moto2"]);print(Motos["Moto3"]);print(Motos["Moto4"]);print(Motos["Moto5"])
    SumaST=sum(SumaPrecios.values())
    print("""
    ==============================Menu============================
        1). Agregar productos al carrito.
        2). Ver el contenido del carrito.
        3). Mostras el total de la compra.
        4). Finalizar programa 
    """)

    Opcion=int(input("Escriba el numero de la opcion deseada: "))

    if Opcion==1:
        os.system("cls")
        print("=====================Productos=======================")
        print("Productos disponibles")
        for i,j in Cantidad.items():
            if j >= 1:
                print(i,f"Nombre: {Motos[i]['Marca']} Modelo:{Motos[i]['Modelo']} Precio:{Motos[i]["Precio"]} ID:{Motos[i]["ID"]} Cantidad: {j}")
        
        Opcion1=int(input("Elije el numero de moto que quiere comprar "))
        if Opcion1==1:
            IdentificadorS=int(input("Escribe el identificador de la moto GN: "))
            if IdentificadorS == 203012:
                Enter=input("Codigo exitoso, presione Enter para continuar")
                CantidadS=int(input("Cuantas motos deseas: "))
                if CantidadS <= Cantidad["Moto1"]:
                    Cantidad["Moto1"]-=CantidadS
                    print("Has comprado",CantidadS,"motos :D")
                    DiccionarioC["Moto1"]+=CantidadS
                    TotalS=9000000*CantidadS
                    SumaPrecios["Moto1"]+=TotalS
                else:
                    Enter=input("La cantidad que deseas comprar supera el stock, presione Enter para ir al menu principal")
            
            else:
                print("El codigo dado no coincide")
                Enter=input("Regresaras al menu principal, presiona Enter para continuar")

        elif Opcion1==2:
            IdentificadorV=int(input("Escribe el identificador de la moto Vespa: "))
            if IdentificadorV==23923:
                Enter=input("Codigo exitoso, presione Enter para continuar")
                CantidadV=int(input("Cuantas motos deseas: "))
                if CantidadS <= Cantidad["Moto2"]:
                    Cantidad["Moto2"]-=CantidadV
                    print("Has comprado",CantidadV,"motos :D")
                    DiccionarioC["Moto2"]+=CantidadV
                    TotalV=5000000*CantidadV
                    SumaPrecios["Moto2"]+=TotalV
                else:
                    Enter=input("La cantidad que deseas comprar supera el stock, presione Enter para ir al menu principal")

            else:
                print("El codigo dado no coincide")
                Enter=input("Regresaras al menu principal, presiona Enter para continuar")

        elif Opcion1==3:
            IdentificadorT=int(input("Escribe el identificador de la moto TVS: "))
            if IdentificadorT==32131:
                Enter=input("Codigo exitoso, presione Enter para continuar")
                CantidadT=int(input("Cuantas motos deseas: "))
                if CantidadS <= Cantidad["Moto3"]:
                    Cantidad["Moto3"]-=CantidadT
                    print("Has comprado",CantidadT,"motos :D")
                    DiccionarioC["Moto3"]+=CantidadT
                    TotalT=10000000*CantidadT
                    SumaPrecios["Moto3"]+=TotalT
                else:
                    Enter=input("La cantidad que deseas comprar supera el stock, presione Enter para ir al menu principal")

            else:
                print("El codigo dado no coincide")
                Enter=input("Regresaras al menu principal, presiona Enter para continuar")


        elif Opcion1==4:
            IdentificadorY=int(input("Escribe el identificador de la moto Yamaha: "))
            if IdentificadorY==123123:
                Enter=input("Codigo exitoso, presione Enter para continuar")
                CantidadY=int(input("Cuantas motos deseas: "))
                if CantidadS <= Cantidad["Moto4"]:
                    Cantidad["Moto4"]-=CantidadY
                    print("Has comprado",CantidadY,"motos :D")
                    DiccionarioC["Moto4"]+=CantidadY
                    TotalY=10000000*CantidadY
                    SumaPrecios["Moto4"]+=TotalY
                else:
                    Enter=input("La cantidad que deseas comprar supera el stock, presione Enter para ir al menu principal")

            else:
                print("El codigo dado no coincide")
                Enter=input("Regresaras al menu principal, presiona Enter para continuar")


        elif Opcion1==5:
            IdentificadorK=int(input("Escribe el identificador de la moto Kawasaki: "))
            if IdentificadorK==456456:
                Enter=input("Codigo exitoso, presione Enter para continuar")
                CantidadK=int(input("Cuantas motos deseas: "))
                if CantidadS <= Cantidad["Moto5"]:
                    Cantidad["Moto5"]-=CantidadK
                    print("Has comprado",CantidadK,"motos :D")
                    DiccionarioC["Moto5"]+=CantidadK
                    TotalK=15000000*CantidadK
                    SumaPrecios["Moto5"]+=TotalK

                else:
                    Enter=input("La cantidad que deseas comprar supera el stock, presione Enter para ir al menu principal")


            else:
                print("El codigo dado no coincide")
                Enter=input("Regresaras al menu principal, presiona Enter para continuar")




    elif Opcion==2:
        os.system("cls")
        print("=====================Motico====================")
        print("Productos en motico")
        MotosTC=sum(DiccionarioC.values())
        if MotosTC >= 1:
            for i,j in DiccionarioC.items():
                if j >= 1:
                    print(i,f"Nombre: {Motos[i]['Marca']} Modelo:{Motos[i]['Modelo']} Precio:{Motos[i]["Precio"]} ID:{Motos[i]["ID"]} Cantidad: {j}")
                    
            Opcion2=int(input("Selecione 1 para terminar la compra o cualquier otro numero para volver al menu principal: "))
            if Opcion2==1:
                print("Valor a pagar: ",SumaST)
                Pagare=int(input("""
                                1). Pagar y salir del programa
                                2). Volver al menu principal
                                """))
                if Pagare==1:
                    break

                else:
                    print("Volveras al menu principal")
                    Enter=input("Presione Enter para continuar")
        else:
            print("No hay productos")        


    elif Opcion==3:
        os.system("cls")
        print("=====================Total de compra=====================")
        print("Precio a pagar")
        print("El precio a pagar",SumaST )
        Enter=input("Presione Enter para ir al menu principal")


    elif Opcion==4:
        os.system("cls")
        break

#Hecho por Yessica Perez C.C 1005044824 y Jerxon Correa C.C 1004922559
