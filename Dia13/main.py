import json,os

bol=True
with open("info.json", encoding="utf-8") as archivo:
    Data=json.load(archivo)
while bol:
    os.system("cls")
    print("""
===============================Crud===============================
          1).Crear
          2).Ver
          3).Actualizar
          4).Eliminar
          5).Salir del programa
===================================================================
""")
    
    opcion=int(input("Escribe un numero para ir a la opcion deseada: "))

    if opcion==1:
        os.system("cls")
        print("===============================Crear===============================")
        IdGrup=int(input("Ingrese el numero de grupo al que deseas añadir el estudiante: "))
        IdGrupo=IdGrup-1
        IdComparado=int(input("Ingrese el codigo del estudiante que desea crear: "))
        IdComparador=IdComparado-1
        for i in range(0,(len(Data[IdGrupo]["estudiantes"]))):
            if IdComparado != Data[IdGrupo]["estudiantes"][i]["id"]:
                print(input("Presione Enter para continuar"))
                NewName=str(input("Ingrese el nombre del estudiante.\n"))
                NewApellido=str(input("Ingrese el nombre del apellido.\n"))
                NewEdad=int(input("Ingrese la edad.\n"))
                NewFecha=str(input("Ingrese la fecha de nacimiento del estudiante. (DD-MM-AAAA)\n"))
                NewCedula=int(input("Ingrese la cedula del estudiante.\n"))
                NewEmail=str(input("Ingrese el correo del estudiante.\n"))
                NewGit=str(input("Ingrese el git del estudiante\n"))
                Data[IdGrupo]["estudiantes"].append({
                    "id": IdComparador,
                    "nombre": NewName,
                    "apellido": NewApellido,
                    "edad": NewEdad,
                    "fechaNacimiento": NewFecha,
                    "cedula": NewCedula,
                    "email": NewEmail,
                    "github": NewGit
                })
                with open("info.json", "w") as archivo1:
                    json.dump(Data,archivo1)
                break
            else:
                print("Ya un estudiante tiene ese codigo, intente utilizando otro codigo :D")
                print(input("Presione Enter para continuar al menu principal"))
                break

    elif opcion==2:
        os.system("cls")
        print("===============================Crear===============================")
        IdGrup=int(input("Ingrese el numero de grupo que deseas ver: "))
        IdGrupo=IdGrup-1
        IdComparado=int(input("Ingrese el codigo del estudiante que desea ver: "))
        IdComparador=IdComparado-1
        if IdComparado == Data[IdGrupo]["estudiantes"][IdGrupo]["id"] and Data[IdGrupo]["estudiantes"][IdGrupo]["id"] !=0:
            print("ID:",Data[IdGrupo]["estudiantes"][IdComparador]["id"])
            print("Nombre:",Data[IdGrupo]["estudiantes"][IdComparador]["nombre"])
            print("Apellido:",Data[IdGrupo]["estudiantes"][IdComparador]["apellido"])
            print("Edad:",Data[IdGrupo]["estudiantes"][IdComparador]["edad"])
            print("Fecha:",Data[IdGrupo]["estudiantes"][IdComparador]["fechaNacimiento"])
            print("Cedula:",Data[IdGrupo]["estudiantes"][IdComparador]["cedula"])
            print("Email:",Data[IdGrupo]["estudiantes"][IdComparador]["email"])
            print("GitHub:",Data[IdGrupo]["estudiantes"][IdComparador]["github"],"\n")
            print(input("Presione Enter para continuar"))
        else:
            print("Este codigo no se encuentra en la base de datos.")
            print(input("Presione Enter para continuar"))

    elif opcion==3:
        os.system("cls")
        print("===============================Actualizar===============================")
        IdGrup=int(input("Ingrese el numero de grupo que deseas actualizar: "))
        IdGrupo=IdGrup-1
        IdComparado=int(input("Ingrese el codigo del estudiante que desea ver: "))
        IdComparador=IdComparado-1
        if IdComparado == Data[IdGrupo]["estudiantes"][IdComparador]["id"] and Data[IdGrupo]["estudiantes"][IdComparador]["id"] != 0 :
            bol1=True
            while bol1:
                os.system("cls")
                print("""
    "===============================Actualizar==============================="
        1).Actualizar nombre y apellido
        2).Actualizar edad.
        3).Actualizar fecha de nacimiento.
        4).Actualizar cedula.
        5).Actualizar Email.
        6).Actualizar GitHub.
        7).Salir al menu principal.
    """)
                opcion=int(input("Ingrese el numero de la opcion deseada.\n"))

                if opcion==1:
                    ActNombre=str(input("Ingrese el nombre actualizado del estudiante: "))
                    ActApellido=str(input("Ingrese el apellido actualizado del estudiante: "))
                    Data[IdGrupo]["estudiantes"][IdComparador]["nombre"]=ActNombre
                    Data[IdGrupo]["estudiantes"][IdComparador]["apellido"]=ActApellido
                    print(input("Presione Enter para continuar"))
                elif opcion==2:
                    ActEdad=int(input("Ingrese la edad del estudiante actualizado.\n"))
                    Data[IdGrupo]["estudiantes"][IdComparador]["edad"]=ActEdad
                    print(input("Presione Enter para continuar"))
                elif opcion==3: 
                    Actfecha=str(input("Ingrese la fecha de nacimiento del estudiante. (DD/MM/AAAA)\n"))
                    Data[IdGrupo]["estudiantes"][IdComparador]["fechaNacimiento"]=Actfecha
                    print(input("Presione Enter para continuar"))
                elif opcion==4:
                    ActCedula=int(input("Ingrese la cedula del estudiante actualizada.\n"))
                    Data[IdGrupo]["estudiantes"][IdComparador]["cedula"]=ActCedula
                    print(input("Presione Enter para continuar"))
                elif opcion==5:
                    ActEmail=str(input("Ingrese el email del estudiante actualizado"))
                    Data[IdGrupo]["estudiantes"][IdComparador]["email"]=ActEmail
                    print(input("Presione Enter para continuar"))
                elif opcion==6:
                    ActGit=str(input("Ingrese la direccion de git del estudiante.\n"))
                    Data[IdGrupo]["estudiantes"][IdComparador]["github"]=ActGit
                    print(input("Presione Enter para continuar"))
                elif opcion==7:
                    print(input("Presiona Enter para salir al menu principal"))
                    bol1=False
                    with open("info.json", "w") as archivo1:
                        json.dump(Data,archivo1)
        else:
            print("Ese estudiante no esta en la base de datos")
            print(input("Presione Enter para ir al menu principal"))
    
    elif opcion==4:
        os.system("cls")
        print("===============================Ver===============================")
        IdGrup=int(input("Ingrese el numero de grupo que deseas ver: "))
        IdGrupo=IdGrup-1
        IdComparado=int(input("Ingrese el codigo del estudiante que desea ver: "))
        IdComparador=IdComparado-1
        if IdComparado == Data[IdGrupo]["estudiantes"][IdComparador]["id"]:
            Data[IdGrupo]["estudiantes"][IdComparador]["id"]=0
            print("Estudiante eliminado con exito")
            print(input("Presiona Enter para salir al menu principal"))
            with open("info.json", "w") as archivo1:
                json.dump(Data,archivo1)
        else:
            print("Este estudiante no existe en la base de datos")

    elif opcion==5:
        print("===============================Salir===============================")
        print(input("Presiona Enter para salir"))
        bol=False
#Hecho por Jerxon Correa // CC 1004922559