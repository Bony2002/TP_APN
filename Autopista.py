from Auto import Auto

class Autopista:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def append(self, Auto):
        nuevo_auto = Auto
        if not self.primero:
            self.primero = nuevo_auto
            self.ultimo = nuevo_auto
        else:
            nuevo_auto.prev = self.ultimo
            self.ultimo.prox = nuevo_auto
            self.ultimo = nuevo_auto
    
    def prepend(self, Auto):
        nuevo_auto = Auto
        if not self.primero:
            self.primero = nuevo_auto
            self.ultimo = nuevo_auto
        else:
            nuevo_auto.next = self.primero
            self.primero.prev = nuevo_auto
            self.primero = nuevo_auto
    def analisis(self):
        actual=self.ultimo
        while actual.prox() != None:
            actual.decision()
            actual=actual.prox()    
        actual.decision()

    def actualizacion(self):
        actual=self.ultimo
        while actual.prox() != None:
            actual.update()
            actual=actual.prox()    
        actual.update()

    def display(self):
        current = self.primero
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")