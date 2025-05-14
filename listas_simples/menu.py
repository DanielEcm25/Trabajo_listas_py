import listas_enlazadas as listas_enlazadas
from listas_enlazadas import *

lista_simple = ListaEnlazada()

while True:
    print("\n---- Menú ----")
    print("1. Agregar un dato al inicio")
    print("2. Agregar un dato al final")
    print("3. Eliminar un dato al inicio")
    print("4. Eliminar un dato al final")
    print("5. Recorrer la lista")
    print("6. Imprimir longitud de la lista")
    print("7. Buscar un dato")
    print("8. Insertar un dato en una posición")
    print("9. Eliminar un dato en una posición")
    print("10. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nuevo_dato = input("Ingrese el dato: ")
        lista_simple.agregar_inicio(nuevo_dato)
        print("Dato agregado al inicio.")

    elif opcion == "2":
        nuevo_dato = input("Ingrese el dato: ")
        lista_simple.agregar_final(nuevo_dato)
        print("Dato agregado al final.")

    elif opcion == "3":
        try:
            lista_simple.eliminar_inicio()
            print("Dato eliminado del inicio.")
        except IndexError as e:
            print(e)

    elif opcion == "4":
        try:
            lista_simple.eliminar_final()
            print("Dato eliminado del final.")
        except IndexError as e:
            print(e)

    elif opcion == "5":
        if lista_simple.esta_vacia():
            print("La lista está vacía.")
        else:
            print("Contenido de la lista:")
            lista_simple.recorrer()

    elif opcion == "6":
        longitud = lista_simple.obtener_longitud()
        print(f"La lista tiene {longitud} elementos.")

    elif opcion == "7":
        dato = input("Ingrese el dato a buscar: ")
        posicion = lista_simple.buscar(dato)
        if posicion != -1:
            print(f"Dato encontrado en la posición {posicion}.")
        else:
            print("Dato no encontrado en la lista.")

    elif opcion == "8":
        try:
            dato = input("Ingrese el dato a insertar: ")
            posicion = int(input("Ingrese la posición donde insertar: "))
            lista_simple.insertar_en_posicion(dato, posicion)
            print(f"Dato '{dato}' insertado en la posición {posicion}.")
        except (ValueError, IndexError) as e:
            print("Error:", e)

    elif opcion == "9":
        try:
            posicion = int(input("Ingrese la posición a eliminar: "))
            lista_simple.eliminar_en_posicion(posicion)
            print(f"Elemento en la posición {posicion} eliminado.")
        except (ValueError, IndexError) as e:
            print("Error:", e)

    elif opcion == "10":
        print("Gracias por usar el programa.")
        break

    else:
        print("Opción no válida. Intente de nuevo.")

    input("Presione Enter para continuar...")
