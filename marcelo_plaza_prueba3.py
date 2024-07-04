def menu():
    print()
    print("*************menu principal*****************")
    print("1) filtro jugador")
    print("2) filtro precio")
    print("3) filtro consola y año")
    print("4) escribir archivo")
    print("5) salir")


def jugador(op2):
    single=[]
    multi=[]
    arch1=open("juegos.csv","r")
    for i in arch1:
        l1=i.strip().split(",")
        if op2=="s":
            if l1[1]=="1":
                single.append(l1)

        if op2=="m":
            if l1[1]!="1":
                multi.append(l1)

    if op2=="s":
        print(single)
    elif op2=="m":
        print(multi)

    arch1.close()


def precio(minimo,maximo):
    rango=[]
    arch2=open("juegos.csv","r")
    for i in arch2:
        l2=i.strip().split(",")
        if l2[2]>=minimo and l2[2]<=maximo:
            rango.append(l2)
        else:
            print("no hay juegos en ese rango de precios")

    print(rango)
    arch2.close()


def consola_año(consola,año):
    lista1=[]
    arch3=open("juegos.csv","r")
    for i in arch3:
        l3=i.strip().split(",")
        if l3[-1]==año and l3[-2]==consola:
            lista1.append(l3)
        else:
            print("no hay juegos con esos filtros")

    print(lista1)
    arch3.close()






#**************main****************
    
while True:
    menu()
    op1=int(input("ingrese opcion: "))

    if op1==1:
        op2=input("ingrese busqueda singleplayer/multiplayer (s/m): ")
        jugador(op2)


    elif op1==2:
        minimo=input("ingrese precio minimo: ")
        maximo=input("ingrese precio maximo: ")
        precio(minimo,maximo)



    elif op1==3:
        consola=input("ingrese consola a buscar: ")
        año=input("ingrese año: ")
        consola_año(consola,año)


    elif op1==4:
        print("generar archivo segun filtro")
        print("1) filtro jugador")
        print("2) filtro precio")
        print("3) filtro consola-año")
        op3=int(input("ingrese opcion: "))

        if op3==1:
            jugador(op2)
            op4=input("ingrese opcion single/multi: ")

            arch4=open("filtro_juegos_jugador.txt","w")
            if op4=="single":
                for a in single:
                    s=",".join(a)
                    arch4.write(s+"\n")
                    print("archivo creado")

            elif op4=="multi":
                for b in multi:
                    z=",".join(b)
                    arch4.write(z+"\n")
                    print("archivo creado")

            else:
                print("no hay informacion que escribir")

            arch4.close()



        elif op3==2:
            precio()

            arch5=open("filtro_juegos_precio.txt","w")
            for c in rango:
                y=",".join(c)
                arch5.write(y+"\n")
                print("archivo creado")

            arch5.close()


        elif op3==3:
            consola_año()

            arch6=open("filtro_juegos_consola_año.txt","w")
            for d in lista1:
                w=",".join(d)
                arch6.write(w+"\n")
                print("archivo creado")

            arch6.close()


    elif op1==5:
        print("saliendo del sistema")
        break






        


