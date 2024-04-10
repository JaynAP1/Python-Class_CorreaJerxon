#Fibonacci

print("""Haremos un programa que genere la serie de Fibonacci
La serie de Fibonacci es una sucesion infinita de numeros""")

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
