# -*- coding: UTF-8 -*-
class Cliente:
    def __init__(self,nombre,cantidad,precio,fechaDeEntrega,modoDePago):
        self.__nombre = nombre
        self.__cantidad = cantidad 
        self.__precio = precio
        self.__fechaDeEntrega = fechaDeEntrega
        self.__modoDePago = modoDePago



    def getNombre(self):
        return self.__nombre

    def getCantidad(self):
        return self.__cantidad

    def getPrecio(self):
        return self.__precio

    def getFechaDeEntrega(self):
        return self.__fechaDeEntrega

    def getModoDePago(self):
        return self.__modoDePago

    def getPrioridad(self):
        self.__prioridad = 0
        fecha = self.__fechaDeEntrega.split("-")
        ano = fecha[2]
        mes = fecha[1]
        dia = fecha[0]
        self.__prioridad = int(ano)*10000+int(mes)*100+int(dia)
        return self.__prioridad


