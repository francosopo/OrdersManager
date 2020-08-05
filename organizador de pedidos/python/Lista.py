class Lista:
    def __init__(self, cabeza, cola):
        self.__cabeza = cabeza
        self.__cola = cola

    def getDato(self):
        return self.__cabeza

    def getCola(self):
        return self.__cola

    def setDato(self,dato):
        self.__cabeza = dato

    def setCola(self,cola):
        assert type(cola) == Lista
        self.__cola = cola
    def agregar(self,elemento):
        puntero = self
        while puntero.getCola() is not None:
            puntero = puntero.getCola()
        puntero.setCola(Lista(elemento,None))
def main():
    l = Lista(1,None)
    l.agregar(2)
    l.agregar(3)
main()
