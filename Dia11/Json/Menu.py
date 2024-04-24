import json,os #Llamo las bibliotecas de Json y Os

#Listas
ListaE=[]#Lista vacia que guardara todos los eventos unitariamente

with open("C:/Users/Jair/Desktop/Python-Class_CorreaJerxon/Dia11/Json/large-file.json", encoding="utf-8") as file:#Llamo al documento JSON
    datos = json.load(file)#Lo guardo en una variable datos

ListaC=[0,0,0,0,0,0,0,0,0,0,0,0,0,0] #Lista que guardara cuantos eventos hay por cada uno

for i in datos: #Un contador y repartidor de eventos, contara cada evento y lo repartira dependiendo de cuantos hayan en todo el JSON
    ListaE.append(i["type"])
    if i["type"] == "MemberEvent":
        ListaC[0]+=1
    elif i["type"] =="IssuesEvent":
        ListaC[1]+=1
    elif i["type"] =="PushEvent":
        ListaC[2]+=1
    elif i["type"] =="ReleaseEvent":
        ListaC[3]+=1
    elif i["type"] =="CommitCommentEvent":
        ListaC[4]+=1
    elif i["type"] =="DeleteEvent":
        ListaC[5]+=1
    elif i["type"] =="PullRequestEvent":
        ListaC[6]+=1
    elif i["type"] =="CreateEvent":
        ListaC[7]+=1
    elif i["type"] =="IssueCommentEvent":
        ListaC[8]+=1
    elif i["type"] =="GollumEvent":
        ListaC[9]+=1
    elif i["type"] =="PublicEvent":
        ListaC[10]+=1
    elif i["type"] =="WatchEvent":
        ListaC[11]+=1
    elif i["type"] =="PullRequestReviewCommentEvent":
        ListaC[12]+=1
    elif i["type"] =="ForkEvent":
        ListaC[13]+=1
        
res=0
ListaO=list(set(ListaE)) #Eliminara los eventos repetidos y asi dejara una lista solamente con la cantidad de eventos
bol=True
while bol: #
    os.system("cls") #Borrar pantalla
    print("""
    ======================Menu===========================
        1). Crear un nuevo evento.
        2). Eliminar un evento.
        3). Revisar la cantidad de eventos.
        4). Actualizar eventos.
        5). Salir del programa.
    =====================================================
    """)#Menu con las opciones

    opcion= int(input("Ingrese un numero con la opcion deseada: ")) #Un selector que se comparara

    if opcion==1: #En caso de ser uno nos permitira agregar un evento junto con la cantidad de eventos
        os.system("cls")
        print("""
=====================================================================
        -Agregar evento-
=====================================================================
""")
        NombreEN=input("Ingrese el nombre del nuevo evento que se creara\n") #Ingresa el nombre y lo agregara al utlimo punto de la lista
        if NombreEN in ListaO:
            print("Este evento ya existe solo ve a actualizar la cantidad")#En caso de que ya exista le dira que solo debe actualizar los eventos
        else:
            CantidadEN=input("Ingrese la cantidad de eventos que se crearan\n") #Cuantos eventos se crearan y seran añadidos al ultimo punto de la lista
            print("Evento creado con exito")
            ListaO.append(NombreEN) #Agrega a las listas
            ListaC.append(CantidadEN)
        
        print(input("Presione Enter para continuar"))

    elif opcion ==2:
        os.system("cls")
        print("""
=====================================================================
        -Eliminar evento-
=====================================================================
""")
        con=0
        NombreEE=input("Ingrese el nombre del evento que desea eliminar\n") #Ingresa el nombre del evento que desea eliminar, debe estar en la lista para que se pueda eliminar
        if NombreEE in ListaO:
            while NombreEE in ListaO: #Este while recorrera la lista hasta que encuentre el objeto con el mismo nombre
                if NombreEE== ListaO[con]:
                    ListaO.remove(NombreEE) #Eliminara el nombre del evento
                    ListaC.pop(con) #Eliminara la cantidad de eventos que hayan con ese nombre
                    print("Evento eliminado con exito") 
                    print(input("Presione Enter para continuar"))
                else:
                    con+=1
        else:
            print("Este evento no esta en la lista") #En caso de no estar en lista mandara que no se encuentra
            print(input("Presione Enter para continuar"))

    elif opcion ==3:
        os.system("cls")
        print("""
=====================================================================
        -Eventos-
=====================================================================
""")

        for i in range(0,len(ListaO)): #Imprimira los eventos uno por uno junto a la cantidad que acompaña a cada uno
            print("Evento:",ListaO[i], "Cantidad:",ListaC[i])
    
        print(input("Presione Enter para continuar"))

    elif opcion==4: #Te permitira agregar o quitar eventos de la lista
        os.system("cls")
        print("""
=====================================================================
        -Actualizar eventos-
=====================================================================
""")
        ConS=0 #Contador que hara como una variable en un for
        boleano=True
        NombreAc=input("Nombre del evento que deseas actualizar\n")#Nombre del evento que se desea actualizar
        if NombreAc in ListaO:
            CantidadAc=int(input("Ingrese la cantidad que deseas actualizar, si deseas restar eventos coloca el numero en negativo :D\n"))#Sumara o restara a la cantidad de eventos
            while NombreAc in ListaO and boleano==True:#El while recorrera toda la lista hasta encontrar el evento que sea igual al nombre que guardo en la variable
                if NombreAc== ListaO[ConS]:
                    ListaC[ConS]+=CantidadAc
                    print("Evento actualizado con exito")
                    print(input("Presione Enter para continuar"))
                    boleano=False
                else:
                    ConS+=1
        else:
            print("Este evento no esta en la lista D:") #En caso de no estar en la lista entonces lo imprimira
            print(input("Presione Enter para continuar"))

    elif opcion==5: #Salir del programa :D
        os.system("cls")
        print("""
=====================================================================
        -Salir-
=====================================================================
""")
        print(input("Presione Enter para salir :D"))
        print("Sale bay")
        bol=False

#Hecho por Jerxon Correa :D