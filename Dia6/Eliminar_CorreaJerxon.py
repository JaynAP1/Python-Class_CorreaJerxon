Numeros=[1,1,2]
NumerosO=[]

Booleanito = True
while Booleanito ==True:

    if len(Numeros) < 300:

        contador=0
        for i in range(0,100):
            if i in Numeros:
                NumerosO.append(i)
            
        print(NumerosO)
        break
    else:
        print("Ingrese un numero menor de 300")
