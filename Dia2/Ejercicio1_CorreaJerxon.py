#Fibonacci

print("""Haremos un programa que genere la serie de Fibonacci
La serie de Fibonacci es una sucesion infinita de numeros""")

while True:
    x = 1
    a = 0
    b = 1

    n = int(input("\nEscribe hasta que numero quieres que llegue la serie de fibonacci: "))

    while x <= n:
        if x % 2 == 1:
            print(a)
            a=a+b
        else:
            print(b)
            b=b+a

        x=x+1

    opcion=int(input("Ingrese 1 para repetir el programa o 0 para terminarlo"))

    if opcion==1:
        print("El programa a comenzado denuevo")

    elif opcion==0:
        break