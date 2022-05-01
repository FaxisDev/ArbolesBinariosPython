from arbol import Arbol

print("Bienvenido al programa de arboles binarios")
arbol = Arbol("")
nivel = 0
ramas = 0
grado = 2
opcion = 0
while(True):

    print("--------")
    print("1 - Crear un nuevo arbol y nivel")
    if(int(nivel) > 0):
        print("2 - Mostrar arbol preOrden")
        print("3 - Mostrar arbol inOrden")
        print("4 - Mostrar arbol posOrden")
        print("5 - Inserta un nuevo valor al arbol")
        print("6 - Mostrar numero de ramas")
        print("7 - Buscar en el arbol un elemento")
        print("8 - Mostrar las hojas del arbol ")
    print("0 - Salir")
    opcion = int(input("ingresa una opcion: "))
    print("--------")
    if(nivel == 0):
        if(opcion == 1):
            nodoPAdre = input("Ingresa el nodo padre/raiz: ")
            arbol = Arbol(nodoPAdre)
            nivel = int(input("ingresa el nivel del arbol: "))
            ramas = 0
        elif(opcion == 0):
            print("Gracias por ocupar el programa, saludos. ")
            break
        else:
            print("Esa opcion no existe")
    else:
        if(opcion == 1):
            nodoPAdre = input("Ingresa el nodo padre/raiz: ")
            arbol = Arbol(nodoPAdre)
            nivel = input("ingresa el nivel del arbol: ")
            ramas = 0
        elif(opcion == 2):
            print("Mostrando arbol en preOrden")
            arbol.preorden()
        elif(opcion == 3):
            print("Mostrando arbol en inOrden")
            arbol.inorden()
        elif(opcion == 4):
            print("Mostrando arbol en posOrden")
            arbol.postorden()
        elif(opcion == 5):
            if(ramas <= (grado ** nivel)):

                nuevoNodo = input("Ingresa un valor al arbol: ")
                arbol.agregar(nuevoNodo)
                ramas += 1
            else:
                print(
                    f"Ya no es posible ingresar mas nodos al arbol, el numero maximo de nodos para el arbol nivel {nivel} es {(grado ** nivel)}")
        elif(opcion == 6):
            print("La cantidad de ramas del arbol es: ", ramas)
        elif(opcion == 7):
            # Búsqueda
            busqueda = input("Busca elemento en el árbol: ")
            nodo = arbol.buscar(busqueda)
            if nodo == None:
                print(f"{busqueda} no existe")
            else:
                print(f"{busqueda} sí existe")
        elif(opcion == 8):
            arbol.hojas()
        elif(opcion == 0):
            print("Gracias por ocupar el programa, saludos. ")
            break
        else:
            print("Esa opcion no existe")
