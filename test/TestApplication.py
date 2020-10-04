import unittest
from application import Cliente
import datetime


class TestApplication(unittest.TestCase):
    def setUp(self):
        self.__nombreCliente = "nombre1"
        self.__apellidoCliente = "apellido1"
        self.__cantidad = 10
        self.__precio = self.__cantidad*1000
        self.__fechaDeEntrega = datetime.date(2020,12, 30)

    def tearDown(self):
        self.__cliente.resetDatabase()

    def test_AgregarClienteEfectivo(self):
        self.__cliente = Cliente.Cliente(self.__nombreCliente,self.__apellidoCliente, self.__cantidad, self.__precio, self.__fechaDeEntrega, "efectivo")
        self.__cliente.agregar()
        name = self.__cliente.getCursor().execute("SELECT nombre FROM pedidos WHERE nombre=?", [self.__nombreCliente]).fetchone()[0]
        self.assertEqual(self.__nombreCliente, name)

    def test_AgregarClienteTarjeta(self):
        self.__cliente = Cliente.Cliente(self.__nombreCliente, self.__apellidoCliente, self.__cantidad, self.__precio, self.__fechaDeEntrega, 'credito')
        self.__cliente.agregar()
        name = self.__cliente.getCursor().execute("SELECT nombre FROM pedidos WHERE nombre = ?", [self.__nombreCliente]).fetchone()[0]
        self.assertEqual(self.__nombreCliente, name)

    def test_BuscarCliente(self):
        self.__cliente = Cliente.Cliente(self.__nombreCliente,self.__apellidoCliente, self.__cantidad, self.__precio, self.__fechaDeEntrega,"efectivo")
        self.__cliente.agregar()
        result = self.__cliente.buscar(self.__nombreCliente, self.__apellidoCliente)
        self.assertEqual(self.__nombreCliente, result[0])
        self.assertEqual(self.__apellidoCliente, result[1])
