class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.longitud = 0

    def esta_vacia(self):
        return self.cabeza is None

    def agregar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        self.longitud += 1

    def agregar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.longitud += 1

    def eliminar_inicio(self):
        if self.esta_vacia():
            raise IndexError("La lista está vacía. No se puede eliminar.")
        self.cabeza = self.cabeza.siguiente
        self.longitud -= 1

    def eliminar_final(self):
        if self.esta_vacia():
            raise IndexError("La lista está vacía. No se puede eliminar.")
        if self.cabeza.siguiente is None:
            self.cabeza = None
        else:
            actual = self.cabeza
            while actual.siguiente.siguiente:
                actual = actual.siguiente
            actual.siguiente = None
        self.longitud -= 1

    def buscar(self, dato):
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1  # Dato no encontrado

    def insertar_en_posicion(self, dato, posicion):
        if posicion < 0 or posicion > self.longitud:
            raise IndexError("Posición inválida.")
        if posicion == 0:
            self.agregar_inicio(dato)
            return
        nuevo_nodo = Nodo(dato)
        actual = self.cabeza
        for _ in range(posicion - 1):
            actual = actual.siguiente
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo
        self.longitud += 1

    def eliminar_en_posicion(self, posicion):
        if self.esta_vacia():
            raise IndexError("La lista está vacía. No se puede eliminar.")
        if posicion < 0 or posicion >= self.longitud:
            raise IndexError("Posición inválida.")
        if posicion == 0:
            self.eliminar_inicio()
            return
        actual = self.cabeza
        for _ in range(posicion - 1):
            actual = actual.siguiente
        actual.siguiente = actual.siguiente.siguiente
        self.longitud -= 1

    def recorrer(self):
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print(" -> ".join(elementos) + " -> None")

    def obtener_longitud(self):
        return self.longitud
