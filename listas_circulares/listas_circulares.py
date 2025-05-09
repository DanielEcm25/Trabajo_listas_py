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
    
    def imprimir_longitud(self):
        return self.longitud