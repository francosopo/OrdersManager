import Lista as l
class Pila:
    def __init__(self):
        self.__pila = None

    def push(self, elemento):
        self.__pila = l.Lista(elemento, self.__pila)

    def top(self):
        return self.__pila.getDato()

    def pop(self):
        elemento = self.__pila.getDato()
        self.__pila = self.__pila.getCola()
        return elemento
    
    def vaciar(self):
        self.__pila = None
    
    def estaVacia(self):
        return self.__pila is None
def main():
    pila = Pila()
    pila.push(1)
    pila.push(2)

main()