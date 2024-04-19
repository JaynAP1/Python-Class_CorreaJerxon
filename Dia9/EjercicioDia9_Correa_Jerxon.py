import os

#Listas
Producto=[] #Lista que llevara el nombre del producto
Precio=[] #Lista que llevara el precio del producto
Cantidad=[] #LIsta que llevara la cantidad del producto

while True: #Un ciclo while que ira con el menu para que despues de hacer cada iteracion puedas volver al menu principal
    os.system("cls") #Borrar pantalla :D
    print("""
=================================================================
            1).Añadir producto al carrito.
            2).Ver productos añadidos al carrito.
            3).Salir del progrma.
=================================================================
    """) #Menu con opciones multiples

    opcion=int(input("Ingrese el numero de la opcion deseada: ")) #Selector del menu

    if opcion==1: #En caso de elegir 1 entonces podras añadir productos
        Bol=True
        while Bol==True:
            os.system("cls")
            print("=================================================================")
            print("Añadir productos al carrito") # Añades :D
            print("=================================================================")
            NombreP=str(input("Nombre del producto que deseas añadir al producto\n")) #Guarda nombre
            CantidadP=int(input("Ingresa la cantidad de productos que desea ingresar al carrito\n")) #Guarda cantidad
            PrecioP=int(input("Precio del producto que se añadira al carrito\n")) #Guarda precio

            Producto.append(NombreP);Precio.append(PrecioP);Cantidad.append(CantidadP) #Añade las variables a lista

            Repetir1=str(input("Desea volver a añadir un producto. (SI/NO)\n")) #Te permite volver al menu principal o seguir añadiendo

            if Repetir1=="NO": #Corta el ciclo 
                Bol=False
                
    elif opcion==2: #Si eliges 2 entonces permitira ver los productos del carrito
        if len(Producto) > 0: #Si no hay productos no te dejara entrar al carrito
            os.system("cls")
            print("=================================================================")
            print("Productos que hay en el carrito")
            print("=================================================================")
            for i in range(0,len(Producto)): #Un ciclo for que imprimira los productos
                print(i+1,") Producto:",Producto[i],"Precio U:", Precio[i],"Cantidad:", Cantidad[i], "Precio T:",Precio[i]*Cantidad[i])
        
        else:
            print("=================================================================")
            print("No hay productos en el carrito") #No hay
            print("=================================================================")

        print(input("Presione Enter para continuar"))

    elif opcion ==3:
        print("=================================================================")
        print("Terminando el programa")
        print("=================================================================")
        print(input("Presione Enter para continuar"))
        break #Terminamos el programa

#Elaborado por Jerxon Correa Amaris C.C 1004922559




