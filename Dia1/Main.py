#-------------------------------------------------
#--------DIA 1 CHEAT SHEET PYTHON-----------------
#-------------------------------------------------
 
# Imprimir hola mundo.
print("Hola mundo")


#Datos primitivos.

#Numero
Numerito = 3 #Nombre valor = valor
print(Numerito)#Imprimir(variable)
print(type(Numerito))#Imprimir(tipo(variable))

#Decimal
NumeritoDecimal = 1.2
print(NumeritoDecimal)
print(type(NumeritoDecimal))

#Booleano
MiBooleanito=True
print(MiBooleanito)
print(type(MiBooleanito))

#Cadena Texo
Texto= "Mi Tibu"
print(Texto)
print(type(Texto))

#Ingresa por teclado la infomarcion
Entrada=input("Ingresa un dato: ")
print("El dato ingresado es: ", Entrada)

#Conversion de tipos de variable
print(int(2.5))
print(float(2))
print(str("Dos"))
print(bool(True))
print(bool(False))

#Bucles For y While
En=int(input("Cuantos numeros deseas contar: "))
for i in range(1,(1+En)):
    print("Numeros: ",i)

booleana = True
while booleana:
    print("""
1). Seguir con el menu :D
2). Salir del trabajo :( 
""")

    opcion=int(input("Que opciones deseas hacer?"))

    if opcion == 1:
        print("Funciones :D")

        #Funciones

        #Funcion 1:
        def hi():
            print(1+1)
            
        #Funcion 2:
        def diHola():
            print("Hola!")

        #Funcion 3:
        def holaConNombre(name):
            print("Hello " + name + "!")     

        #Funcion 4:
        def multiplica(val1, val2):
            return val1 * val2    
    
    else:
        booleana=False
