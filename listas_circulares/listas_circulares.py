class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

class lista_circular:

    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.longitud = 0

    def esta_vacia(self):
        return self.cabeza == None

    def agregar_inicio(self,dato):
        nuevo_dato = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo_dato
            self.cabeza.siguiente = self.cabeza
        else:
            aux = nuevo_dato
            aux.siguiente = self.cabeza
            self.cabeza = aux
            self.cola.siguiente = self.cabeza
        self.longitud += 1

    def agregar_final(self,dato):
        nuevo_dato = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo_dato 
            self.cabeza.siguiente = self.cabeza
        else:
            aux = self.cola
            self.cola = aux.siguiente = nuevo_dato
            self.cola.siguiente = self.cabeza
        self.longitud += 1

    def recorrer_lista(self):
        aux = self.cabeza
        while True:
            print(aux.dato,end=" -> ")
            aux = aux.siguiente
            if aux == self.cabeza:
                break
        print(f"({self.cabeza.dato})")

    def eliminar_inicio(self):
        if self.cabeza == self.cola:
            self.cabeza = self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cola.siguiente = self.cabeza 
        self.longitud -= 1

    def eliminar_final(self):
        if self.cabeza == self.cola:
            self.cabeza = self.cola = None
        else:
            aux = self.cabeza
            while aux.siguiente != self.cola:
                aux = aux.siguiente
            aux.siguiente = self.cabeza
            self.cola = aux
        self.longitud -= 1

    def eliminar_en_posicion(self, pos):
        if pos < 0 or pos >= self.longitud:
            print("Posición inválida.")
            return
        if pos == 0:
            self.eliminar_inicio()
        elif pos == self.longitud - 1:
            self.eliminar_final()
        else:
            aux = self.cabeza
            for _ in range(pos - 1):
                aux = aux.siguiente
            aux.siguiente = aux.siguiente.siguiente
            self.longitud -= 1

    def insertar_en_posicion(self, dato, pos):
        if pos < 0 or pos > self.longitud:
            print("Posición inválida.")
            return
        if pos == 0:
            self.agregar_inicio(dato)
        elif pos == self.longitud:
            self.agregar_final(dato)
        else:
            nuevo = Nodo(dato)
            aux = self.cabeza
            for _ in range(pos - 1):
                aux = aux.siguiente
            nuevo.siguiente = aux.siguiente
            aux.siguiente = nuevo
            self.longitud += 1

    def buscar_dato(self, dato):
        if self.esta_vacia():
            return -1
        aux = self.cabeza
        pos = 0
        while True:
            if aux.dato == dato:
                return pos
            aux = aux.siguiente
            pos += 1
            if aux == self.cabeza:
                break
        return -1

    def imprimir_longitud(self):
        return self.longitud