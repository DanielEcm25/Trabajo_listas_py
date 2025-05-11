class Nodo():
    def __init__(self,dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class lista_doble():
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
        else: 
            aux = nuevo_dato
            aux.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_dato
            self.cabeza = aux
        self.longitud += 1

    def agregar_final(self,dato):
        nuevo_dato = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo_dato
        else:
            aux = self.cola
            self.cola = aux.siguiente = nuevo_dato
            self.cola.anterior = aux
        self.longitud += 1
    
    def recorrer_inicio(self):
        aux = self.cabeza
        while aux != None:
            print(aux.dato, end=" -> ")
            aux = aux.siguiente
        print("None\n")
    
    def recorrer_final(self):
        aux = self.cola
        while aux is not None:
            print(aux.dato, end=" <- ")
            aux = aux.anterior
        print("None\n")

    def imprimir_longitud(self):
        return self.longitud
    
    def eliminar_inicio(self):
        if self.cabeza.siguiente == None:
            self.cabeza = self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
        self.longitud -=1

    def eliminar_final(self):
        if self.cabeza.siguiente == None:
            self.cabeza = self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        self.longitud -= 1

    def buscar(self, dato):
        aux = self.cabeza
        while aux is not None:
            if aux.dato == dato:
                return True
            aux = aux.siguiente
        return False
    
    def insertar_en_posicion(self, pos, dato):
        if pos < 0 or pos > self.longitud:
            print("Posición inválida")
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
            siguiente = aux.siguiente
            aux.siguiente = nuevo
            nuevo.anterior = aux
            nuevo.siguiente = siguiente
            siguiente.anterior = nuevo
            self.longitud += 1
    
    def eliminar_en_posicion(self, pos):
        if self.esta_vacia():
            print("La lista está vacía.")
            return
        if pos < 0 or pos >= self.longitud:
            print("Posición inválida")
            return
        if pos == 0:
            self.eliminar_inicio()
        elif pos == self.longitud - 1:
            self.eliminar_final()
        else:
            aux = self.cabeza
            for _ in range(pos):
                aux = aux.siguiente
            anterior = aux.anterior
            siguiente = aux.siguiente
            anterior.siguiente = siguiente
            siguiente.anterior = anterior
            self.longitud -= 1