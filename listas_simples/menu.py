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
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nuevo_dato = input("Por favor ingrese el dato: ")
        lista_simple.agregar_inicio(nuevo_dato)
        print("Dato agregado al inicio.")
    
    elif opcion == "2":
        nuevo_dato = input("Por favor ingrese el dato: ")
        lista_simple.agregar_final(nuevo_dato)
        print("Dato agregado al final.")
    
    elif opcion == "3":
        if lista_simple.esta_vacia():
            print("La lista está vacía.")
        else:
            lista_simple.eliminar_inicio()
            print("Dato eliminado del inicio.")
    
    elif opcion == "4":
        if lista_simple.esta_vacia():
            print("La lista está vacía.")
        else:
            lista_simple.eliminar_final()
            print("Dato eliminado del final.")
    
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
        print("Gracias por usar el programa.")
        break

    else:
        print("Opción no válida. Intente de nuevo.")

    input("Presione Enter para continuar...")
