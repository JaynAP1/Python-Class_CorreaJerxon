import secrets
import string #Importamos bibliotecas para poder crear las contraseñas seguras

booleano=True
while booleano==True:#Creamos un While que hara el menu infinitamente, hasta que el usuario decida terminar el programa
     #Menu de seleccion
    print("""
    ==============BIENVENIDOS AL HIMALAYA===================== 
        1).Para averiguar que numero es primo.
        2).Para generar una contraseña segura.
        3).Cerrar programa.
    ==========================================================
    """)

    opcion=int(input("Escribe el numero de la opcion a la que deseas ir: "))#Selecion del menu

    if opcion==1:#Si se elije uno ira al menu de primos
        booleano2=True
        while booleano2==True:
            #Menu de primos
            print("""
        ==========================PRIMOS=============================
            En este programa averiguaremos si un numero dado por el
            usuario es primo.
                1).Averiguar si un numero es primo
                2).Volver al menu principal
                3).Informacion.
        =============================================================
        """)
            
            opcion1=int(input("Escribe el numero de la opcion a la que deseas ir: "))

            if opcion1==1:#Hara la formulacion de los numeros primos
                    print("===============================================================")
                    NumeroU=int(input("Ingrese el numero que deseas saber si es primo: "))
                    contador = 0

                    for i in range(1,(1+NumeroU)):#formulacion de numeros primos
                        if NumeroU % i == 0:
                            contador=contador+1

                    if contador==2:
                        print("Este numero es primo")
                    else:
                        print("Este numero no es primo")
            elif opcion1==2:#Regresar al menu principal
                 print("Regresaras al menu principal")
                 booleano2=False
            elif opcion1==3:#Informacion adicional
                 print("=====================INFORMACION===================")
                 print("""Autor:Jerxon Jair Correa Amaris
                          Edad:20
                          Creado:11/04/2024   
                         """)
    elif opcion==2:#Menu de contraseñas
         booleano3 = True
         while booleano3==True:
          
          LetrasMay = string.ascii_lowercase#Guarda las letras mayusculas en una variable
          LetrasMin = string.ascii_uppercase#Guarda las letras minusculas en una variable
          Digitos = string.digits#Guarda los numeros en una variable
          CaracteresEs = string.punctuation#Guarda los caracteres especiales en una variable

          Alfabeto=LetrasMay+LetrasMin+Digitos+CaracteresEs #Sumamos las variables en una sola para crear un diccionario

#Creamos un menu de las contraseñas con las opciones que tenemos
          print("""
     ======================CONTRASEÑAS================================
          En este programa crearemos una contraseña segura para nuestros usuarios
          todas las contraseñas son generadas al azar.
                    1).Crear contraseña
                    2).Volver al menu principal
                    3).Informacion.
     """)
          opcion2=int(input("Escribe el numero de la opcion deseada."))#Selector de opciones

          if opcion2==1:
               LlevarNu=str(input("Quieres que tu contraseña tenga numeros(SI/NO)"))#Si llevan numeros
               LLevarAlfa=str(input("Quieres que tu contraseña tenga caracteres especiales (SI/NO)"))#Si lleva caracteres especiales
               MayusONo=str(input("Desea que su contraseña tenga mayusculas(SI/NO)?"))#Si llevan mayusculas
               if MayusONo=="SI":
                    Alfabeto=LetrasMin+Digitos+CaracteresEs
                    if LlevarNu=="NO":
                         Alfabeto=LetrasMin+CaracteresEs
                         if LLevarAlfa=="NO":
                              Alfabeto=LetrasMin
                    if LlevarNu=="SI":
                         Alfabeto=LetrasMin+Digitos #Los condicionales :D
                         if LLevarAlfa=="SI":
                              Alfabeto=LetrasMin+CaracteresEs
                              
               if MayusONo=="NO":
                    Alfabeto=LetrasMay+Digitos+CaracteresEs
                    if LlevarNu=="NO":
                         Alfabeto=LetrasMay+CaracteresEs
                         if LLevarAlfa=="NO":
                              Alfabeto=LetrasMay
                              
               
               TamañoCon=int(input("Ingrese la cantidad de caracteres que tendra la contraseña: "))#Cantidad de digitos que tiene la contraseña

               print("Su contraseña segura se esta generando, presione enter para continuar.")
               Enter=input("") #Un esperar tecla muy improvisado

               Contraseña=""
               for i in range(1,(1+TamañoCon)): #Creamos un for que ira creando letra por letra la contraseña
                    Contraseña += "".join(secrets.choice(Alfabeto))

                    if i == TamañoCon: #Creamos una condicion que hasta que el ciclo no este completo no imprimira la contraseña, esto para que no genere una escalera
                         print(Contraseña)

          elif opcion2==2:
               booleano3=False #Cambiamos el booleano a falso para terminar con el while y salir al menu principal

          elif opcion2==3:#Informacion adicional
               print("""
=================================================================
          Una contraseña segura es aquella contraseña que es
          dificil de identificar y clonar, las contraseñas seguras
          tienen alrededor de 8 caracteres y caracteres
          especiales.
""")

    elif opcion==3:#Terminar el programa :D
         print("Saliendo del programa, presione enter para continuar")
         Enter=(input(""))
         booleano=False
         


                         
        
                   

                    
                  
                

              
              

            



