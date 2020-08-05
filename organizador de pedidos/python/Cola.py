import Lista as l
class Cola:
    def __init__(self):
        self.__cola = None

    def encolar(self,elemento):
        if self.__cola is None:
            self.__cola = l.Lista(elemento,None)
        else:
            self.__cola.agregar(elemento)

    def sacar(self):
        elemento = self.__cola.getDato()
        self.__cola = self.__cola.getCola()
        return elemento

    def estaVacia(self):
        return self.__cola == None