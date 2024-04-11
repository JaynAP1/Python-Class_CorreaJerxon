import secrets
import string

booleano=True
while booleano==True:
     
    print("""
    ==============BIENVENIDOS AL HIMALAYA=====================
        1).Para averiguar que numero es primo.
        2).Para generar una contraseña segura.
        3).Cerrar programa.
    ==========================================================
    """)

    opcion=int(input("Escribe el numero de la opcion a la que deseas ir: "))

    if opcion==1:
        booleano2=True
        while booleano2==True:
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

            if opcion1==1:
                    print("===============================================================")
                    NumeroU=int(input("Ingrese el numero que deseas saber si es primo: "))
                    contador = 0

                    for i in range(1,(1+NumeroU)):
                        if NumeroU % i == 0:
                            contador=contador+1

                    if contador==2:
                        print("Este numero es primo")
                    else:
                        print("Este numero no es primo")
            elif opcion1==2:
                 print("Regresaras al menu principal")
                 booleano2=False
            elif opcion1==3:
                 print("=====================INFORMACION===================")
                 print("""Autor:Jerxon Jair Correa Amaris
                          Edad:20
                          Creado:11/04/2024   
                         """)
    elif opcion==2:
         
         LetrasMay = string.ascii_lowercase
         LetrasMin = string.ascii_uppercase
         Digitos = string.digits
         CaracteresEs = string.punctuation

         Alfabeto=LetrasMay+LetrasMin+Digitos+CaracteresEs

         print("""
======================CONTRASEÑAS================================
        En este programa crearemos una contraseña segura para nuestros usuarios
        todas las contraseñas son generadas al azar.
                1).Crear contraseña
                2).Volver al menu principal
                3).Informacion.
""")
         opcion2=int(input("Escribe el numero de la opcion deseada."))

         if opcion2==1:
              LlevarNu=str(input("Quieres que tu contraseña tenga numeros(SI/NO)"))
              LLevarAlfa=str(input("Quieres que tu contraseña tenga caracteres especiales (SI/NO)"))
              MayusONo=str(input("Desea que su contraseña tenga mayusculas(SI/NO)?"))
              if MayusONo=="SI":
                   Alfabeto=LetrasMin+Digitos+CaracteresEs
                   if LlevarNu=="NO":
                        Alfabeto=LetrasMin+CaracteresEs
                        if LLevarAlfa=="NO":
                             Alfabeto=LetrasMin
                   if LlevarNu=="SI":
                        Alfabeto=LetrasMin+Digitos
                        if LLevarAlfa=="SI":
                             Alfabeto=LetrasMin+CaracteresEs
                             
              if MayusONo=="NO":
                   Alfabeto=LetrasMay+Digitos+CaracteresEs
                   if LlevarNu=="NO":
                        Alfabeto=LetrasMay+CaracteresEs
                        if LLevarAlfa=="NO":
                             Alfabeto=LetrasMay
                             
              
              TamañoCon=int(input("Ingrese la cantidad de caracteres que tendra la contraseña: "))

              print("Su contraseña segura se esta generando, presione enter para continuar.")
              Enter=input("")

              Contraseña=""
              for i in range(1,(1+TamañoCon)):
                   Contraseña += "".join(secrets.choice(Alfabeto))

                   if i == TamañoCon:
                        print(Contraseña)



                         
        
                   

                    
                  
                

              
              

            



