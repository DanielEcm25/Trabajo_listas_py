from listas_circulares import *

list_Circular = lista_circular()
while True:
    print("\n----Menú----\n"
    +"1. Agregar un dato al inicio\n"
    +"2. Agregar un dato al final\n"
    +"3. Eliminar un dato al inicio\n"
    +"4. Eliminar un dato al final\n"
    +"5. Recorrer la lista\n"
    +"6. Imprimir longitud de la lista\n"
    +"7. Insertar en una posición específica\n"
    +"8. Eliminar en una posición específica\n"
    +"9. Buscar un dato en la lista\n"     
    +"10. Salir")
    print("Seleccione una opción: ")
    opcion = input()        
    if opcion == "1":
        nuevo_dato = input("Por favor ingrese el dato a agregar: ")
        list_Circular.agregar_inicio(nuevo_dato)
        print("Dato agregado al inicio de la lista")
        
    elif opcion == "2":
        nuevo_dato = input("Por favor ingrese el dato a agregar: ")
        list_Circular.agregar_final(nuevo_dato)
        print("Dato agregado al final de la lista")

    elif opcion == "3":
        if list_Circular.esta_vacia():
            print("La Lista está vacía")
        else:
            list_Circular.eliminar_inicio()
            print("Dato eliminado al inicio de la lista")

    elif opcion == "4":
        if list_Circular.esta_vacia():
            print("La lista está vacía")
        else:
            list_Circular.eliminar_final()
            print("Dato eliminado al final de la lista")

    elif opcion == "5":
        if list_Circular.esta_vacia():
            print("La lista está vacía")
        else:
            print("Elementos de la lista:")
            list_Circular.recorrer_lista()

    elif opcion == "6":
        longitud = list_Circular.imprimir_longitud()
        print(f"La lista tiene: {longitud} elementos")

    elif opcion =="7": 
        try:
            dato = input("Ingrese el dato a insertar: ")
            posicion = int(input("Ingrese la posición donde desea insertar: "))
            list_Circular.insertar_en_posicion(dato,  posicion)
            print("Dato insertado en la posición: "+posicion)
        except ValueError:
            print("Posición inválida. Debe ser un número entero.")

    elif opcion == "8":
        try:
            posicion = int(input("Ingrese la posición del dato a eliminar: "))
            list_Circular.eliminar_en_posicion(posicion)
            print("Dato eliminado en la posición"+posicion)
        except ValueError:
            print("Entrada inválida. Debe ser un número entero.")
            
    elif opcion == "9":
        dato = input("Ingrese el dato a buscar: ")
        posicion = list_Circular.buscar_dato(dato)
        if posicion != -1:
            print(f"El dato '{dato}' está en la posición {posicion}.")
        else:
            print(f"El dato '{dato}' no se encontró en la lista.")

    elif opcion == "10":
        print("Gracias por usar el programa")
        break
    else:
        print("Opción no válida")
