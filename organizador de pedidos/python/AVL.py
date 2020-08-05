import Pila as p
pila = p.Pila()
class AVL:
    def __init__(self,dato,izq,der):
        self.__dato = dato
        self.__izq = izq
        self.__der = der 
        self.__delta = 0

    def getDato(self):
        return self.__dato

    def getIzq(self):
        return self.__izq

    def getDer(self):
        return self.__der

    #altura: None -> int 
    #entrega la altura del arbol correspondiente al self.
    #Ejemplo: (2,(1,None,None),(3,None,None)).altura() == 2 
    def altura(self):
        if self.__izq is None and self.__der is None:
            return 1
        elif self.__izq is None:
            return 1 + self.__der.altura()
        elif self.__der is None:
            return 1 + self.__izq.altura()
        else:
            return 1+max(self.__izq.altura(),self.__der.altura())

    #delta: None -> int
    #entrega la diferencia de altura entre el izq y el der de un arbol.
    #Ejemplo: (25 , ( 13 , (8) , (15) ) , ( 78 ) ).delta() = 1
    #si arbol.delta() > 0, izq > der
    #si arbol.delta() < 0, izq < der 
    def delta(self):
        return self.__izq.altura()-self.__der.altura()

    #agregarSinBalancear: int -> None
    #agrega un elemento a un arbol avl
    def agregarSinBalancear(self,dato):
        pila.push(self)
        if dato < self.getDato() :
            if self.__izq is None:
                self.__izq = AVL(dato,None,None)
            else:
                return self.__izq.agregarSinBalancear(dato)
        
        elif self.getDato() < dato:
            if self.__der is None:
                self.__der = AVL(dato, None , None )
            else:
                return self.__der.agregarSinBalancear(dato)
        
        else:
            raise Exception("Ya existe un dato con ese nombre")
    
    def balancear(self):
        assert !pila.estaVacia()
        while !pila.estaVacia():
            arbol=pila.pop()
            if arbol.delta() > 1: # izq > der
                #insercion exterior
                                


def main():
    avl = AVL(2,None,None)
    avl.agregarSinBalancear(1)
    avl.agregarSinBalancear(3)
main()