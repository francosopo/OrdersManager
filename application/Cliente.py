import sqlite3
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
        self.__cursor.execute("SELECT id FROM pedidos ORDER BY id DESC")
        try:
            self.__cursor.fetchone()
            id = self.__cursor[0]['id']+1
        except:
            id = 1
        if id:
            self.__cursor.execute("INSERT INTO pedidos VALUES(?,?,?,?,?,?,?)", [id,self.__nombre, self.__apellido, self.__cantidad, self.__precio, self.__fechaDeEntrega,self.__modoDePago])
            self.__connection.commit()

    def getCursor(self):
        return self.__cursor

    def resetDatabase(self):
        self.__cursor.execute("DELETE FROM pedidos")
        self.__connection.commit()

    def buscar(self, nombreCliente, apellidoCliente):
        self.__cursor.execute("SELECT nombre, apellido FROM pedidos WHERE nombre = ? AND apellido=?", [nombreCliente,apellidoCliente])
        return self.__cursor.fetchone()






