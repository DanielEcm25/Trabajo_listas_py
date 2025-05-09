import listas_dobles_circulares as ldc
from listas_dobles_circulares import *

listadc = ldc.ListaDobleCircular()
while True:
    print("\n----Menú----\n"
    +"1. Agregar un dato al inicio\n"
    +"2. Agregar un dato al final\n"
    +"3. Recorrer la lista de inicio a fin\n"
    +"4. Recorrer la lista de fin a inicio\n"
    +"5. Eliminar un dato al inicio de la lista\n"
    +"6. Eliminar un dato al final de la lista\n"
    +"7. Buscar un dato en la lista\n"
    +"8. Imprimir longitud de la lista\n"
    +"9. Salir\n")
    print("Seleccione una opción: ")
    opcion = input()        
    if opcion == "1":
        nuevo_dato = input("Por favor ingrese el dato a agregar: ")
        listadc.agregar_inicio(nuevo_dato)
        print("Dato agregado")
    elif opcion == "2":
        nuevo_dato = input("Por favor ingrese el dato a agregar: ")
        listadc.agregar_final(nuevo_dato)
        print("Dato agregado")
    elif opcion == "3":
        if listadc.esta_vacia():
            print("La Lista está vacía")
        else:
            print("Lista:\n")
            listadc.recorrer_inicio()
    elif opcion == "4":
        if listadc.esta_vacia():
            print("La lista está vacía")
        else:
            print("Lista:\n")
            listadc.recorrer_final()
    elif opcion == "5":
        if listadc.esta_vacia():
            print("La lista está vacía")
        else:
            listadc.eliminar_inicio()
            print("Dato eliminado de la lista")
    elif opcion == "6":
        if listadc.esta_vacia():
            print("La lista está vacía")
        else:
            listadc.eliminar_final()
            print("Dato eliminado de la lista")
    elif opcion == "7":
        if listadc.esta_vacia():
            print("La lista está vacía")
        else:
            dato = input("Ingrese el dato que desea buscar: ")
            if listadc.buscar_dato(dato) == None:
                print("El dato no fue encontrado")
            else:
                print(f"Dato {listadc.buscar_dato(dato)} encontrado")
    elif opcion == "8":
        longitud = listadc.imprimir_longitud()
        print(f"La lista tiene: {longitud} elementos.")
    elif opcion == "9":
        print("Gracias por usar el programa")
        break
    else:
        print("Opción no válida")