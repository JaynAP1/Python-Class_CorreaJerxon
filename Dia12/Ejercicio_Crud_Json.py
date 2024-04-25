import json, os

bol=True
while bol:
    with open("large-file.json", encoding="utf-8") as archivito:
        Datos=json.load(archivito)

    Evento1=[];Evento2=[];Evento3=[];Evento4=[];Evento5=[];Evento6=[];Evento7=[];Evento8=[];Evento9=[];Evento10=[];Evento11=[];Evento12=[];Evento13=[];Evento14=[]
    EventosT=[]
    for i in range(0,len(Datos)):
        EventosT.append(Datos[i]["type"])
        if Datos[i]["type"]=="MemberEvent":
            Evento1.append(Datos[i])
        elif Datos[i]["type"]=="IssuesEvent":
            Evento2.append(Datos[i])
        elif Datos[i]["type"]=="PushEvent":
            Evento3.append(Datos[i])
        elif Datos[i]["type"]=="ReleaseEvent":
            Evento4.append(Datos[i])
        elif Datos[i]["type"]=="CommitCommentEvent":
            Evento5.append(Datos[i])
        elif Datos[i]["type"]=="DeleteEvent":
            Evento6.append(Datos[i])
        elif Datos[i]["type"]=="PullRequestEvent":
            Evento7.append(Datos[i])
        elif Datos[i]["type"]=="CreateEvent":
            Evento8.append(Datos[i])
        elif Datos[i]["type"]=="IssueCommentEvent":
            Evento9.append(Datos[i])
        elif Datos[i]["type"]=="GollumEvent":
            Evento10.append(Datos[i])
        elif Datos[i]["type"]=="PublicEvent":
            Evento11.append(Datos[i])
        elif Datos[i]["type"]=="WatchEvent":
            Evento12.append(Datos[i])
        elif Datos[i]["type"]=="PullRequestReviewCommentEvent":
            Evento13.append(Datos[i])
        elif Datos[i]["type"]=="ForkEvent":
            Evento14.append(Datos[i])

    EventosO=list(set(EventosT))

    with open("Event1.json","w") as Archivo2:
        json.dump(Evento1,Archivo2)
    with open("Event2.json","w") as Archivo2:
        json.dump(Evento2,Archivo2)
    with open("Event3.json","w") as Archivo3:
        json.dump(Evento3,Archivo3)
    with open("Event4.json","w") as Archivo4:
        json.dump(Evento4,Archivo4)
    with open("Event5.json","w") as Archivo5:
        json.dump(Evento5,Archivo5)
    with open("Event6.json","w") as Archivo6:
        json.dump(Evento6,Archivo6)
    with open("Event7.json","w") as Archivo7:
        json.dump(Evento7,Archivo7)
    with open("Event8.json","w") as Archivo8:
        json.dump(Evento8,Archivo8)
    with open("Event9.json","w") as Archivo9:
        json.dump(Evento9,Archivo9)
    with open("Event10.json","w") as Archivo10:
        json.dump(Evento10,Archivo10)
    with open("Event11.json","w") as Archivo11:
        json.dump(Evento11,Archivo11)
    with open("Event12.json","w") as Archivo12:
        json.dump(Evento12,Archivo12)
    with open("Event13.json","w") as Archivo13:
        json.dump(Evento13,Archivo13)
    with open("Event14.json","w") as Archivo14:
        json.dump(Evento14,Archivo14)

    os.system("cls")
    print("""
    =========================================-Menu-=========================================
        1).Crear 
        2).Actualizar
        3).Eliminar
        4).Ver
        5).Salir
    ========================================================================================
    """)

    opcion=int(input("Ingrese una opcion deseada para continuar: "))

    if opcion==1:
        os.system("cls")
        print("=================-Agregar-====================")
        for i in range(0,len(EventosO)):
            print("Tipo:",EventosO[i])

        EventoSel=str(input("Escribe el nombre del evento que se le desea agregar.\n"))
        NewId=str(input("Ingrese el nuevo ID\n"))
        NewId2=str(input("Ingrese el ID del actor\n"))
        print("=================-Actor-=================")
        NewLogin=str(input("Ingrese un nombre para el login\n"))
        NewUrl=str(input("Ingrese una Url\n"))
        NewAvatarUrl=str(input("Ingrese un avatar url\n"))
        print("=================-Repo-=================")
        NewId3=str(input("Ingrese un id para el repo\n"))
        NewName=str(input("Ingrese un nombre\n"))
        NewUrl=str(input("Ingrese url del repo\n"))
        print("=================-Publico-==================")
        NewPublic=str(input("Ingrese True o False\n"))

        Datos.append({
            "id": NewId,
            "type": EventoSel,
            "actor": {
                "id": NewId2,
                "login": NewLogin,
                "gravatar_id": "",
                "url":  NewUrl,
                "avatar_url": NewAvatarUrl
            },
            "repo": {
                "id": NewId3,
                "name": NewName,
                "url": NewUrl
            },
            "public": NewPublic,
        })

        # Guardar la lista actualizada en el archivo
        with open("large-file.json", "w") as archivo1:
            json.dump(Datos, archivo1)

        print("Evento guardado con éxito")
    
    if opcion ==2:
        os.system("cls")
        print("==================-Actualizar-===================")
        CodigoCom=str(input("Escribe el codigo del elemnto que deseas actualizar"))

        for i in range(0,len(Datos)):
            if CodigoCom == Datos[i]["id"]:
                EventoSel=str(input("Nombre actualizado del evento:\n"))
                NewId2=str(input("ID actualizado del actor:\n"))
                print("=================-Actor-=================")
                NewLogin=str(input("Nombre actualizado del login:\n"))
                NewUrl=str(input("Url actualizada:\n"))
                NewAvatarUrl=str(input("Url Actualizada:\n"))
                print("=================-Repo-=================")
                NewId3=str(input("ID para la repo:\n"))
                NewName=str(input("Nombre para la repo:\n"))
                NewUrl=str(input("Url de la repo:\n"))
                print("=================-Publico-==================")
                NewPublic=str(input("Ingrese True o False:\n"))

                Datos[i]=({
                    "id": CodigoCom,
                    "type": EventoSel,
                    "actor": {
                        "id": NewId2,
                        "login": NewLogin,
                        "gravatar_id": "",
                        "url":  NewUrl,
                        "avatar_url": NewAvatarUrl
                    },
                    "repo": {
                        "id": NewId3,
                        "name": NewName,
                        "url": NewUrl
                    },
                    "public": NewPublic,
                })

                # Guardar la lista actualizada en el archivo
                with open("large-file.json", "w") as archivo1:
                    json.dump(Datos, archivo1)

                print("Evento guardado con éxito")

        print(input("Presiona Enter para continuar"))

    if opcion==3:
        os.system("cls")
        print("===========================-Eliminar===============================================")
        CodigoCom=str(input("Escribe el codigo del elemento que deseas eliminar: "))
        print("====================================================================================")
        for i in range(0,len(Datos)):
            if CodigoCom == Datos[i]["id"]:
                Datos[i]["id"]="0"
                print("Elemento elimnado con exito")
                with open("large-file.json", "w") as archivo1:
                    json.dump(Datos, archivo1)
                break
            
        print(input("Presiona Enter para continuar"))

    if opcion==4:
        os.system("cls")
        bol2=True
        while bol2:
            print("""
            ======================================================
                    1).Ver un elemento en especifico.
                    2).Salir al menu principal.
            """)
            opcion2=int(input("Use un numero para ir a la opcion deseada: "))
            if opcion2 ==1:
                CodigoBus=str(input("Ingrese el codigo para buscarlo en la base de datos: "))
                for i in range(0,len(Datos)):
                    if CodigoBus == Datos[i]["id"] and Datos[i]["id"]!="0":
                        print("Nombre evento:",Datos[i]["type"])
                        print("ID:",Datos[i]["id"])
                        print("===============Actor===============")
                        print("ID:",Datos[i]["actor"]["id"])
                        print("Login:",Datos[i]["actor"]["login"])
                        print("===================================")
                        print("Publico:",Datos[i]["public"])

                        print(input("Presiona Enter para continuar"))
                        bol2=False
                    

            elif opcion2==2:  
                print(input("Presiona Enter para continuar"))
                bol2=False
    
    if opcion==5:
        os.system("cls")
        print("==================Saliendo=================")
        print(input("Presiona Enter para continuar"))
        print("===========================================")
        bol=False

#Jerxon Jair Correa Amairs // C.C 1004922559