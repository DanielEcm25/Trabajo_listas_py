class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None
    
class ListaDobleCircular:
    def __init__(self):
        self.longitud = 0
        self.cabeza = None
        self.cola = None

    def __unir_nodos(self):
        if self.cabeza != None:
            self.cabeza.anterior = self.cola
            self.cola.siguiente = self.cabeza

    def esta_vacia(self):
        return self.cabeza == None
    
    def agregar_inicio(self,dato):
        nuevo_dato = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo_dato
        else:
            aux = nuevo_dato
            aux.siguiente = self.cabeza
            self.cabeza.anterior = aux
            self.cabeza = aux
        self.__unir_nodos()
        self.longitud += 1

    def agregar_final(self,dato):
        nuevo_dato = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = self.cola = nuevo_dato
        else: 
            aux = self.cola
            self.cola = aux.siguiente = nuevo_dato
            self.cola.anterior = aux
        self.__unir_nodos()
        self.longitud += 1

    def recorrer_inicio(self):
        aux = self.cabeza
        while True:
            print(aux.dato,end=" -> ")
            aux = aux.siguiente
            if aux == self.cabeza:
                break
        print(f"{self.cabeza.dato}")

    def recorrer_final(self):
        aux = self.cola
        while True: 
            print(aux.dato,end=" -> ")
            aux = aux.anterior
            if aux == self.cola:
                break
        print(f"{self.cola.dato}")
    
    def eliminar_inicio(self):
        if self.cabeza == self.cola:
            self.cabeza = self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.__unir_nodos()
        self.longitud -= 1

    def eliminar_final(self):
        if self.cabeza == self.cola:
            self.cabeza = self.cola = None
        else:
            self.cola = self.cola.anterior
            self.__unir_nodos()
        self.longitud -= 1
            
    def buscar_dato(self,dato):
        aux = self.cabeza
        while aux:
            if aux.dato == dato:
                return aux.dato
            else:
                aux = aux.siguiente
                if aux == self.cabeza:
                    return None

    def imprimir_longitud(self):
        return self.longitud