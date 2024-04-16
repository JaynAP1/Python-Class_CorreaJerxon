NumerosL=[] #Lista que guardara los numeros ingresados 
SumNum=[] #Lista que guardara la sumatoria de las parejas

CantidadI=int(input("")) #Cantidad de casos
for Intentos in range(0,CantidadI):
    CantidadN=int(input(""))#La cantidad de digitos que va a entrar al algoritmo
    Division=int(input(""))#Por quien se va a dividir el algoritmo

    for i in range(0,CantidadN): #Un ciclo para que va a guardar cada entrada en una lista de forma independiente
        NumerosA=(input())#La entrada
        NumerosL.append(int(NumerosA))#Agrega el numero al final de la lista

    con = 0 #Contador en 0 que parara el condicional
    for i in range(1,10): #Ciclo para que ira del 1 hasta el 9
        for a in range(2,10): #ciclo para que ira del 2 hasta el 9
            if i in NumerosL and a in NumerosL: #Condicional que si los contadores del para estaban dentro de la lista
                if i < a and con < 7: #Condicional que permitia sumar mientras la condicion de que i fuera menor que a y el contador creado arriba fuera menor a 7
                    SumNuma=i+a #Suma de las parejas de la lista
                    SumNum.append(SumNuma)#Agrega la suma a una lista
                    con = con+1 #La sumatoria del contador al llegar a 6 parara y por ende seguira al siguiente para

    Contador=0 #Creo un nuevo contador con valor en 0 que sera el que llevara la cuenta de la cantidad de divisiones posibles
    for div in SumNum: #Un para que contara toda la lista de la sumatoria de las parejas
        if div % Division == 0:#La condicional que mientras la division de un objeto de la lista por la variable por la que se va a modular sea 0 sumara 1 al contador
            Contador=Contador+1 #Asi el contador llevara la cuenta de cuantas parejas son divisibles
            
    print("Case 1: ",Contador)#Salida

    #Jerxon Jair Correa Amaris // C.C 1004922559 

