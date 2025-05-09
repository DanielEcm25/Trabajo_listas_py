class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class listas_enlazadas:
    def __init__(self):
        self.cabeza = None
        self.longitud = 0

    def esta_vacia(self):
        return self.cabeza == None
                
    def agregar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        self.longitud += 1

    def eliminar_inicio(self):
        if self.cabeza.siguiente == None:
            self.cabeza = None
            self.longitud = 0
        else:
            self.cabeza = self.cabeza.siguiente
        self.longitud -=1

    def eliminar_final(self):
        if self.cabeza.siguiente == None:
            self.cabeza = None
            self.longitud = 0
        else:
            aux = self.cabeza
            while aux.siguiente.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = None
            self.longitud -=1

    def agregar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.longitud += 1

    def recorrer(self):
        actual = self.cabeza
        while actual != None:
            print(actual.dato , end= " -> ")
            actual = actual.siguiente
        print("None\n")
        
    def imprimir_longitud(self):
        return self.longitud