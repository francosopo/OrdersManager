import Cliente as c
class Arbol:
    def __init__(self, dato, izq, der):
        self.__dato = dato
        self.__izq = izq
        self.__der = der

    def getDato(self):
        return self.__dato

    def getIzq(self):
        return self.__izq

    def getDer(self):
        return self.__der

    def setDato(self,dato):
        self.__dato = dato

    def setIzq(self,izq):
        self.__izq = izq

    def setDer(self,der):
        self.__der = der


    def agregar(self, elemento):
        if elemento.getNombre() > self.__dato.getNombre():
            if self.__der is None:
                self.__der = Arbol(elemento, None, None)
            else:
                return self.__der.agregar(elemento)
        elif elemento.getNombre() < self.__dato.getNombre():
            if self.__izq is None:
                self.__izq = Arbol(elemento, None, None)
            else:
                return self.__izq.agregar(elemento)
        else:
            raise Exception("Ya existe un cliente con ese nombre")



    def getMin(self):
        if self.__izq is None:
            return self.__dato
        else:
            return self.__izq.getMin()


    def getMax(self):
        if self.__der is None:
            return self.__dato
        else:
            return self.__der.getMax()

    def eliminar(self,padre,elemento):
        assert type(elemento) == str
        if padre is not None:
            if self is not None:
                if self == padre.getIzq():
                    if self.__dato.getNombre() == elemento:
                        if self.__izq is None and self.__der is None:
                            padre.setIzq(None)
                            return True
                        elif self.__izq is None:
                            padre.setIzq(self.__der)
                            return True
                        elif self.__der is None:
                            padre.setIzq(self.__izq)
                            return True
                        else:
                            maximo = self.__izq.getMax()
                            self.__dato = maximo
                            return self.__izq.eliminar(self,maximo.getNombre())
                    elif elemento < self.__dato.getNombre():
                        return self.__izq.eliminar(self,elemento)
                    else:
                        return self.__der.eliminar(self,elemento)
                elif self == padre.getDer():
                    if self.__dato.getNombre() == elemento :
                        if self.__izq is None and self.__der is None:
                            padre.setDer(None)
                            return True
                        elif self.__izq is None:
                            padre.setDer(self.__der)
                            return True
                        elif self.__der is None:
                            padre.setDer(self.__izq)
                            return True
                        else:
                            maximo = self.__izq.getMax()
                            self.__dato = maximo
                            return self.__izq.eliminar(self,maximo.getNombre())
                    elif elemento < self.__dato.getNombre():
                        if self.__izq is None:
                            return False
                        else:
                            return self.__izq.eliminar(self,elemento)
                    else:
                        if self.__der is None:
                            return False
                        else:
                            return self.__der.eliminar(self,elemento)
                else:
                    print("arbol errado")
                    raise Exception()
            else:
                return False
        else:
            if self.__dato.getNombre() == elemento:

                if self.__izq is not None:
                    maximo= self.__izq.getMax()
                    self.__dato = maximo
                    return self.__izq.eliminar(self,maximo.getNombre())
                elif self.__der is not None:
                    minimo= self.__der.getMin()
                    self.__dato = minimo
                    return self.__der.eliminar(self,minimo.getNombre())
                else:
                    cliente = c.Cliente("N",0,0,"0-0-0","None")
                    self.__dato = cliente
                    return True
            else:
                if elemento < self.__dato.getNombre():
                    if self.__izq is None:
                        return False
                    else:
                        return self.__izq.eliminar(self,elemento)
                else:
                    if self.__der is None:
                        return False
                    else:
                        return self.__der.eliminar(self,elemento)

    def buscar(self,nombre):
        if self.__dato.getNombre() == nombre:
            return (True,self.__dato)
        else:
            if nombre < self.__dato.getNombre():
                if self.__izq is None:
                    return (False,None)
                else:
                    return self.__izq.buscar(nombre)
            else:
                if self.__der is None:
                    return (False,None)
                else:
                    return self.__der.buscar(nombre)
    def numElementos(self):
        if self.__izq is None and self.__der is None:
            return 1
        elif self.__izq is None:
            return 1+self.__der.numElementos()
        elif self.__der is None:
            return 1+self.__izq.numElementos()
        else:
            return 1+self.__izq.numElementos()+self.__der.numElementos()




