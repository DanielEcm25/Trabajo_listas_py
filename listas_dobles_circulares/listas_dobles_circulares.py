# archivo: listas_dobles_circulares.py

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaDobleCircular:
    def __init__(self):
        self.longitud = 0
        self.cabeza = None
        self.cola = None

    def __unir_nodos(self):
        if self.cabeza is not None:
            self.cabeza.anterior = self.cola
            self.cola.siguiente = self.cabeza

    def esta_vacia(self):
        return self.cabeza is None

    def agregar_inicio(self, dato):
        nuevo = Nodo(dato)
        # --- ANTIGUO ---
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo
        else:
            aux = nuevo
            aux.siguiente = self.cabeza
            self.cabeza.anterior = aux
            self.cabeza = aux
        # --- /ANTIGUO ---
        self.__unir_nodos()
        self.longitud += 1

    def agregar_final(self, dato):
        nuevo = Nodo(dato)
        # --- ANTIGUO ---
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo
        else:
            aux = self.cola
            self.cola = aux.siguiente = nuevo
            self.cola.anterior = aux
        # --- /ANTIGUO ---
        self.__unir_nodos()
        self.longitud += 1

    def recorrer_inicio(self):
        if self.esta_vacia():
            return
        aux = self.cabeza
        while True:
            print(aux.dato, end=" -> ")
            aux = aux.siguiente
            if aux == self.cabeza:
                break
        print(f"{self.cabeza.dato}")

    def recorrer_final(self):
        if self.esta_vacia():
            return
        aux = self.cola
        while True:
            print(aux.dato, end=" -> ")
            aux = aux.anterior
            if aux == self.cola:
                break
        print(f"{self.cola.dato}")

    def eliminar_inicio(self):
        if self.esta_vacia():
            return
        # --- ANTIGUO ---
        if self.cabeza == self.cola:
            self.cabeza = self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.__unir_nodos()
        # --- /ANTIGUO ---
        self.longitud -= 1

    def eliminar_final(self):
        if self.esta_vacia():
            return
        # --- ANTIGUO ---
        if self.cabeza == self.cola:
            self.cabeza = self.cola = None
        else:
            self.cola = self.cola.anterior
            self.__unir_nodos()
        # --- /ANTIGUO ---
        self.longitud -= 1

    def buscar_dato(self, dato):
        # --- ANTIGUO: retornaba solo el dato o None ---
        aux = self.cabeza
        while aux:
            if aux.dato == dato:
                return aux.dato
            aux = aux.siguiente
            if aux == self.cabeza:
                break
        return None
        # --- /ANTIGUO ---

    # +++ NUEVO +++: buscar posición de la primera ocurrencia (0-based)
    def buscar_posicion(self, dato):
        if self.esta_vacia():
            return None
        indice = 0
        aux = self.cabeza
        while True:
            if aux.dato == dato:
                return indice
            aux = aux.siguiente
            indice += 1
            if aux == self.cabeza:
                break
        return None

    # +++ NUEVO +++: eliminar nodo en posición específica (0 ≤ pos < longitud)
    def eliminar_en_posicion(self, pos):
        if pos < 0 or pos >= self.longitud or self.esta_vacia():
            raise IndexError("Posición fuera de rango")
        # si es primero o último, delegar
        if pos == 0:
            return self.eliminar_inicio()
        if pos == self.longitud - 1:
            return self.eliminar_final()
        # recorrer hasta el nodo en pos
        aux = self.cabeza
        for _ in range(pos):
            aux = aux.siguiente
        # desconectar aux
        ant = aux.anterior
        sig = aux.siguiente
        ant.siguiente = sig
        sig.anterior = ant
        self.longitud -= 1
        self.__unir_nodos()

    # +++ NUEVO +++: insertar dato en posición específica (0 ≤ pos ≤ longitud)
    def insertar_en_posicion(self, pos, dato):
        if pos < 0 or pos > self.longitud:
            raise IndexError("Posición fuera de rango")
        # insert al inicio o final
        if pos == 0:
            return self.agregar_inicio(dato)
        if pos == self.longitud:
            return self.agregar_final(dato)
        # insertar en medio
        nuevo = Nodo(dato)
        aux = self.cabeza
        for _ in range(pos):
            aux = aux.siguiente
        ant = aux.anterior
        # enlazar: ant <-> nuevo <-> aux
        ant.siguiente = nuevo
        nuevo.anterior = ant
        nuevo.siguiente = aux
        aux.anterior = nuevo
        self.longitud += 1
        self.__unir_nodos()

    def imprimir_longitud(self):
        return self.longitud
