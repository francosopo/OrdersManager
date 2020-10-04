import sqlite3
from . import ApplicationException

class Cliente:
    def __init__(self, nombre, apellido, cantidad, precio, fecha_de_entrega, modo_de_pago):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cantidad = cantidad
        self.__precio = precio
        self.__fechaDeEntrega =fecha_de_entrega
        self.__modoDePago = modo_de_pago
        self.__connection = sqlite3.connect("database.db")
        self.__cursor = self.__connection.cursor()

    def agregar(self):
        id = 0
        result = None
        try:
            self.__cursor.execute("SELECT id, nombre, apellido FROM pedidos ORDER BY id DESC")
            result = self.__cursor.fetchone()
            id = result[0]+1
        except :
            id = 1
        if id:
            try:
                if result is not None and self.__nombre == result[1] and self.__apellido == result[2]:
                    raise ApplicationException.DuplicatedValue(self.__nombre, self.__apellido)
                self.__cursor.execute("INSERT INTO pedidos VALUES(?,?,?,?,?,?,?)", [id,self.__nombre, self.__apellido, self.__cantidad, self.__precio, self.__fechaDeEntrega,self.__modoDePago])
                self.__connection.commit()
                return True
            except:
                return False


    def getCursor(self):
        return self.__cursor

    def resetDatabase(self):
        self.__cursor.execute("DELETE FROM pedidos")
        self.__connection.commit()

    def buscar(self, nombreCliente, apellidoCliente):

        result = None
        try:
            self.__cursor.execute("SELECT nombre, apellido FROM pedidos WHERE nombre = ? AND apellido=?",
                                  [nombreCliente, apellidoCliente])
            result = self.__cursor.fetchone()
        except sqlite3.OperationalError:
            return None
        return result

    def eliminar(self, nombreCliente, apellidoCliente):
        self.__cursor.execute("DELETE FROM pedidos WHERE nombre = ? AND apellido = ?", [nombreCliente,apellidoCliente])
        self.__connection.commit()
        return self.buscar(nombreCliente, apellidoCliente)







