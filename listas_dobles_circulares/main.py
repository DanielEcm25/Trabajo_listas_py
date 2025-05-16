# archivo: main.py

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
        +"9. Buscar posición de un dato\n"               # +++ NUEVO +++
        +"10. Eliminar dato en posición específica\n"  # +++ NUEVO +++
        +"11. Insertar dato en posición específica\n" # +++ NUEVO +++
        +"12. Salir\n")                                # número ajustado
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nuevo = input("Por favor ingrese el dato a agregar: ")
        listadc.agregar_inicio(nuevo)
        print("Dato agregado")
    elif opcion == "2":
        nuevo = input("Por favor ingrese el dato a agregar: ")
        listadc.agregar_final(nuevo)
        print("Dato agregado")
    elif opcion == "3":
        if listadc.esta_vacia():
            print("La lista está vacía")
        else:
            print("Lista de inicio a fin:")
            listadc.recorrer_inicio()
    elif opcion == "4":
        if listadc.esta_vacia():
            print("La lista está vacía")
        else:
            print("Lista de fin a inicio:")
            listadc.recorrer_final()
    elif opcion == "5":
        if listadc.esta_vacia():
            print("La lista está vacía")
        else:
            listadc.eliminar_inicio()
            print("Dato eliminado del inicio")
    elif opcion == "6":
        if listadc.esta_vacia():
            print("La lista está vacía")
        else:
            listadc.eliminar_final()
            print("Dato eliminado del final")
    elif opcion == "7":
        if listadc.esta_vacia():
            print("La lista está vacía")
        else:
            d = input("Ingrese el dato que desea buscar: ")
            res = listadc.buscar_dato(d)
            if res is None:
                print("El dato no fue encontrado")
            else:
                print(f"Dato '{res}' encontrado")
    elif opcion == "8":
        print(f"La lista tiene: {listadc.imprimir_longitud()} elementos.")
    # +++ NUEVO +++
    elif opcion == "9":
        if listadc.esta_vacia():
            print("La lista está vacía")
        else:
            d = input("Ingrese el dato para conocer su posición: ")
            pos = listadc.buscar_posicion(d)
            if pos is None:
                print("El dato no fue encontrado")
            else:
                print(f"El dato '{d}' está en la posición {pos}")
    elif opcion == "10":
        if listadc.esta_vacia():
            print("La lista está vacía")
        else:
            try:
                pos = int(input("Ingrese la posición a eliminar: "))
                listadc.eliminar_en_posicion(pos)
                print(f"Dato en posición {pos} eliminado")
            except (ValueError, IndexError) as e:
                print(f"Error: {e}")
    elif opcion == "11":
        try:
            pos = int(input("Ingrese la posición donde insertar: "))
            d = input("Ingrese el dato a insertar: ")
            listadc.insertar_en_posicion(pos, d)
            print(f"Dato '{d}' insertado en posición {pos}")
        except (ValueError, IndexError) as e:
            print(f"Error: {e}")
    # --- ANTIGUO: antes opción 9 era Salir ---
    elif opcion == "12":
        print("Gracias por usar el programa")
        break
    else:
        print("Opción no válida")
