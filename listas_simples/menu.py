import listas_enlazadas as listas_enlazadas
from listas_enlazadas import *

lista_simple = listas_enlazadas()
while True:
    print("----Menú----\n"
    +"1. Agregar un dato al inicio\n"
    +"2. Agregar un dato al final\n"
    +"3. Eliminar un dato al inicio\n"
    +"4. Eliminar un dato al final\n"
    +"5. Recorrer la lista\n"
    +"6. Imprimir longitud de la lista\n"
    +"7. Salir")
    print("Seleccione una opción")
    opcion = input()        
    if opcion == "1":
        print("Por favor ingrese el dato: ")
        nuevo_dato = input()
        lista_simple.agregar_inicio(nuevo_dato)
        print("Dato agregado")
    elif opcion == "2":
        print("Por favor ingrese el dato: ")
        nuevo_dato = input()
        lista_simple.agregar_final(nuevo_dato)
        print("Dato agregado")
    elif opcion == "3":
        if lista_simple.esta_vacia():
            print("La lista está vacía")
        else: 
            lista_simple.eliminar_inicio()
            print("Dato eliminado")
    elif opcion == "4":
        if lista_simple.esta_vacia():
            print("La lista está vacía")
        else: 
            lista_simple.eliminar_final()
            print("Dato eliminado")
    elif opcion == "5":
        if lista_simple.esta_vacia():
            print("La lista está vacía")
        else:
            print("Lista: ")
            lista_simple.recorrer()
    elif opcion == "6":
        longitud = lista_simple.imprimir_longitud()
        print(f"La lista tiene: {longitud} elementos.")
    elif opcion == "7":
        print("Gracias por usar el programa")
        break
    else:
        print("Opción no válida")