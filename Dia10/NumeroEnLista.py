#Lista
N=input("")
Lista=list(sorted(set(map(int, N.split(",")))))#Guarda en la lista
#Variable
Con=0 #Contador inicia en 0

Numero=int(input("")) #Numero que va a buscar
Lista.append(Numero) #Agrega el numero
Lista.sort() #Ordenar la lista
#Ciclo
for i in Lista: #Ciclamos la lista
    Con+=1 #Contador que va a llevar la posicion
    if Numero == i: #Si el numero se encuentra imprimira la posicion
        print(Con-1)
        break #Morira el codigo
