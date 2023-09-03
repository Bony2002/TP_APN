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
            nuevo_auto.gap=self.ultimo.pos - nuevo_auto.pos - 4
            nuevo_auto.adelante = self.ultimo
            self.ultimo.atras = nuevo_auto
            self.ultimo = nuevo_auto
    
    def prepend(self, Auto):
        nuevo_auto = Auto
        if not self.primero:
            self.primero = nuevo_auto
            self.ultimo = nuevo_auto
        else:
            nuevo_auto.next = self.primero
            self.primero.adelante = nuevo_auto
            self.primero = nuevo_auto
    def analisis(self):
        if self.ultimo!=None:
            actual=self.ultimo
            while actual.adelante != None:
                actual.decision()
                actual=actual.adelante 
            actual.decision()

    def actualizacion(self):
        actual=self.ultimo
        while actual.adelante != None:
            actual.update()
            actual=actual.adelante    
        actual.update()

    def display(self):
        current = self.primero
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")