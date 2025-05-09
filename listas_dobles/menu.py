import listas_dobles
from listas_dobles import *

list_doble = listas_dobles.lista_doble()
while True:
    print("\n----Menú----\n"
    +"1. Agregar un dato al inicio\n"
    +"2. Agregar un dato al final\n"
    +"3. Eliminar un dato al inicio\n"
    +"4. Eliminar un dato al final\n"
    +"5. Recorrer la lista en orden ascendente\n"
    +"6. Recorrer la lista en orden descendente\n"
    +"7. Imprimir longitud de la lista\n"
    +"8. Salir")
    print("Seleccione una opción: ")
    opcion = input()        
    if opcion == "1":
        nuevo_dato = input("Por favor ingrese el dato a agregar: ")
        list_doble.agregar_inicio(nuevo_dato)
        print("Dato agregado")
    elif opcion == "2":
        nuevo_dato = input("Por favor ingrese el dato a agregar: ")
        list_doble.agregar_final(nuevo_dato)
        print("Dato agregado")
    elif opcion == "3":
        if list_doble.esta_vacia():
            print("La Lista está vacía")
        else:
            list_doble.eliminar_inicio()
            print("Dato eliminado al inicio de la lista")
    elif opcion == "4":
        if list_doble.esta_vacia():
            print("La lista está vacía")
        else:
            list_doble.eliminar_final()
            print("Dato eliminado al final de la lista")
    elif opcion == "5":
        if list_doble.esta_vacia():
            print("La lista está vacía")
        else:
            print("Elementos de la lista:")
            list_doble.recorrer_inicio()
    elif opcion == "6":
        if list_doble.esta_vacia():
            print("La lista está vacía")
        else:
            print("Elementos de la lista:")
            list_doble.recorrer_final()
    elif opcion == "7":
        longitud = list_doble.imprimir_longitud()
        print(f"La lista tiene: {longitud} elementos")
    elif opcion == "8":
        print("Gracias por usar el programa")
        break
    else:
        print("Opción no válida")