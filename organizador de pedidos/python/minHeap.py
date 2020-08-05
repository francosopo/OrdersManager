import math as m
class minHeap:
    def __init__(self):
        self.__heap = [0]
        self.__numElementos = 0

    def insertar(self, elemento):
        self.__heap.append(elemento)
        self.__numElementos += 1
        j = self.__numElementos
        while j > 1 and self.__heap[j].getPrioridad() < self.__heap[m.floor(j / 2)].getPrioridad():
            t = self.__heap[j]
            self.__heap[j] = self.__heap[m.floor(j / 2)]
            self.__heap[m.floor(j / 2)] = t
            j = m.floor(j / 2)

    def extraer(self):
        mini = self.__heap[1]  # el minimo
        self.__heap[1] = self.__heap[self.__numElementos]
        self.__heap.pop(self.__numElementos)
        self.__numElementos -= 1
        j = 1
        while 2 * j <= self.__numElementos:
            k = 2 * j
            if k + 1 <= self.__numElementos and self.__heap[k + 1].getPrioridad() < self.__heap[k].getPrioridad():
                k = k + 1
            if self.__heap[j].getPrioridad() < self.__heap[k].getPrioridad():
                break
            t = self.__heap[j]
            self.__heap[j] = self.__heap[k]
            self.__heap[k] = t
            j = k
        return mini

    def top(self):
        if self.__numElementos > 0:
            return self.__heap[1]
        else:
            print("No hay elementos para mostrar")
            #raise Exception()

    def getNumElementos(self):
        return self.__numElementos

    def eliminar(self,nombre):
        n = 1
        while n<=self.__numElementos:
            if self.__heap[n].getNombre() == nombre:
                self.__heap.pop(n)
                self.__numElementos -=1
                break
            n += 1
