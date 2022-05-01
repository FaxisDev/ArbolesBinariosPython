class Nodo:
    def __init__(self, dato):
        # "dato" puede ser de cualquier tipo, incluso un objeto si se sobrescriben los operadores de comparación
        self.dato = dato
        self.izquierda = None
        self.derecha = None

    def imprimirArbol(self):
        if self.derecha:
            self.derecha.imprimirArbol()
        print(self.dato),
        if self.izquierda:
            self.izquierda.imprimirArbol()
