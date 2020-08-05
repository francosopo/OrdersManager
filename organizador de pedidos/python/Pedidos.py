#-*- coding: UTF-8 -*-

import Arbol as A
import Cliente as C
import Cola as c
import minHeap as h
import time as t

fechaDeHoy = t.gmtime()

diaActual = fechaDeHoy[2]
mesActual = fechaDeHoy[1]
anoActual = fechaDeHoy[0]

prioridadActual = anoActual*10000+mesActual*100+diaActual

archivo = open("Datos.csv", "r+")
lineas = archivo.readlines()
archivo.close()
arbol="a"
colaDePrioridad = h.minHeap()
if lineas == []:
    inicializarCliente = C.Cliente("N",0,0,"0-0-0","n")
    arbol = A.Arbol(inicializarCliente,None,None)
    colaDePrioridad.insertar(inicializarCliente)
else:
    datos = lineas[0].split(",")
    nombre= datos[0]
    cantidad = int(datos[1])
    precio = int(datos[2])
    fechaDeEntrega=datos[3]
    modoDePago = datos[4]
    cliente= C.Cliente(nombre,cantidad,precio,fechaDeEntrega,modoDePago)
    arbol=A.Arbol(cliente,None,None)
    colaDePrioridad.insertar(cliente)

#sacar el primer cliente inicializador agregado ya
if len(lineas) > 0:
    lineas.pop(0)
if colaDePrioridad.top().getNombre() == "N":
    colaDePrioridad.extraer()

if lineas != []:
    #leer las lineas del archivo, construir el arbol y la cola de prioridad.
    for linea in lineas:
        if linea != "\n":
            datos = linea.split(",")
            nombre= datos[0]
            cantidad = int(datos[1])
            precio = int(datos[2])
            fechaDeEntrega=datos[3]
            modoDePago = datos[4]
            cliente= C.Cliente(nombre,cantidad,precio,fechaDeEntrega,modoDePago)
            arbol.agregar(cliente)
            colaDePrioridad.insertar(cliente)
#Con las lineas siguientes, se tienen los clientes para los cuales hay pedidos desde hoy en adelante en la cola de
#prioridad

if colaDePrioridad.getNumElementos() > 0:
    while prioridadActual>colaDePrioridad.top().getPrioridad():
        colaDePrioridad.extraer()
#fin comentario.

def volverAlMain():
    opcion = input("Presione \"M\" para volver al menu principal: ")
    if opcion == "M" or opcion == "m":
        return main()
    return volverAlMain()

def pago():
    #ingresar el modo de pago válido.
    modoDePago = input("Ingrese el modo de pago (e: efectivo, t: tarjeta, tr: transferencia): ")
    if modoDePago == "E" or modoDePago == "e":
        modoDePago = "efectivo"
        return modoDePago
    elif modoDePago == "T" or modoDePago == "t":
        modoDePago = "tarjeta"
        return modoDePago
    elif modoDePago == "TR" or modoDePago == "tr":
        modoDePago = "transferencia"
        return modoDePago
    else:
        print("")
        print("Ingrese un método de pago válido")
        print("")
        return pago()

def agregar():
    #agrega un cliente al arbol y a la cola de prioridad.
    nombre = input("Ingrese el nombre: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = int(input("Ingrese el precio: "))
    fechaDeEntrega = input("Ingrese la fecha de entrega (DD-MM-AAAA): ")
    modoDePago = pago()
    cliente = C.Cliente(nombre,cantidad,precio,fechaDeEntrega,modoDePago)
    arbol.agregar(cliente)
    colaDePrioridad.insertar(cliente)
    print("")
    print("Cliente agregado exitosamente")
    print("")
    return volverAlMain()

def eliminar():
    #eliminar del arbol y de la cola de prioridad
    nombre = input("Ingrese el nombre a eliminar: ")
    arbol.eliminar(None,nombre)
    colaDePrioridad.eliminar(nombre)
    return volverAlMain()

def buscar():
    #funcion que busca el nombre en los datos, usando busqueda implementada en el arbol
    nombre = input("Ingrese el nombre a buscar: ")
    check=arbol.buscar(nombre)
    if check[0]:
        print("")
        print("Nombre: "+check[1].getNombre())
        print("Cantidad: "+ str(check[1].getCantidad()))
        print("Precio: $"+str(check[1].getPrecio()))
        print("Fecha de entrega: "+check[1].getFechaDeEntrega())
        print("Modo de pago: "+ check[1].getModoDePago())
        print("")
    else:
        print("")
        print("No se encuentra")
        print("")
    return volverAlMain()


def hoy():
    today = []
    if colaDePrioridad.getNumElementos() > 0:
        #extraer el cliente inicializador
        if colaDePrioridad.top().getNombre() == "N":
            colaDePrioridad.extraer()

        #extraer los clientes de hoy
        while colaDePrioridad.getNumElementos() > 0 and colaDePrioridad.top().getPrioridad() == prioridadActual:
            clienteDeHoy = colaDePrioridad.extraer()
            today.append(clienteDeHoy)

        if today != []:
            # restaurar la cola de prioridad
            for i in range(len(today)):
                colaDePrioridad.insertar(today[i])
            print("")
            print("Clientes de hoy")

            #imprimir los clientes de hoy
            for i in range(len(today)):
                print("")
                print("Nombre: "+today[i].getNombre())
                print("Cantidad: "+str(today[i].getCantidad()))
                print("Precio: "+str(today[i].getPrecio()))
                print("Fecha de entrega: "+today[i].getFechaDeEntrega())
                print("Modo de Pago: "+today[i].getModoDePago())
                print("")
        else:
            print("")
            print("No hay pedidos para hoy")
            print("")
    else:
        print("No hay clientes para mostrar")
    return volverAlMain()

def proximosPedidos(numClientesProximos):
    n = 0
    proximosClientes = []
    today=[]
    if colaDePrioridad.getNumElementos()>0:
        if colaDePrioridad.top().getNombre() == "N":
            colaDePrioridad.extraer()

        #quitar los clientes de hoy
        while colaDePrioridad.getNumElementos()>0 and colaDePrioridad.top().getPrioridad() == prioridadActual:
            cliente = colaDePrioridad.extraer()
            today.append(cliente)
        #Extraer los clientes próximos, según el numero de clientes proximos
        while n < numClientesProximos:
            if colaDePrioridad.getNumElementos()>0:
                cliente = colaDePrioridad.extraer()
                proximosClientes.append(cliente)
                n += 1
            else:
                print("")
                print("No hay clientes próximos")
                print("")
                return volverAlMain()

        if proximosClientes != []:
            # restaurar la cola de prioridad e imprimir los clientes.
            print("")
            for i in range(len(proximosClientes)):
                colaDePrioridad.insertar(proximosClientes[i])
                print("Nombre: "+proximosClientes[i].getNombre())
                print("Cantidad: "+str(proximosClientes[i].getCantidad()))
                print("Precio: "+ str(proximosClientes[i].getPrecio()))
                print("Fecha de entrega: "+proximosClientes[i].getFechaDeEntrega())
                print("Modo de pago: "+proximosClientes[i].getModoDePago())

        #agregar los clientes de hoy, para restaurar la cola de prioridad.
        if today != []:
            for i in range(len(today)):
                colaDePrioridad.insertar(today[i])
    else:
        print("No hay próximos pedidos")
    return volverAlMain()

def guardarDatos():
    #funcion que guarda los datos, escribiendolos en el archivo "Datos.csv"
    print("Guardando datos...")
    cola = c.Cola()
    cola.encolar(arbol)
    archivo = open("Datos.csv", "w")
    while not cola.estaVacia():
        sacar = cola.sacar()
        if sacar is None:
            pass
        else:
            archivo.write(sacar.getDato().getNombre() + "," + str(sacar.getDato().getCantidad()) + "," + str(
                sacar.getDato().getPrecio()) + "," + sacar.getDato().getFechaDeEntrega() + "," + sacar.getDato().getModoDePago() + "\n")
            cola.encolar(sacar.getIzq())
            cola.encolar(sacar.getDer())

    archivo.close()
    print("Datos guardados exitosamente")
    return volverAlMain()

def salir():
    # funcion que guarda los datos, escribiendolos en el archivo "Datos.csv"
    print("Guardando datos...")
    cola = c.Cola()
    cola.encolar(arbol)
    archivo = open("Datos.csv", "w")
    while not cola.estaVacia():
        sacar = cola.sacar()
        if sacar is None:
            pass
        else:
            archivo.write(sacar.getDato().getNombre() + "," + str(sacar.getDato().getCantidad()) + "," + str(
                sacar.getDato().getPrecio()) + "," + sacar.getDato().getFechaDeEntrega() + "," + sacar.getDato().getModoDePago() + "\n")
            cola.encolar(sacar.getIzq())
            cola.encolar(sacar.getDer())

    archivo.close()
    print("Datos guardados exitosamente")
    return None

def main():
    print("")
    print("Organizador de pedidos")
    print("Menú principal")
    print("[A]gregar")
    print("[E]liminar")
    print("[B]uscar")
    print("[G]uardar los datos")
    print("Pedidos de [H]oy")
    print("Pedidos [P]róximos")
    print("[S]alir")
    opcion = input("Seleccione la operación a realizar: ")
    if opcion == "A" or opcion == "a":
        agregar()
    elif opcion == "E" or opcion =="e":
        eliminar()
    elif opcion == "B" or opcion == "b":
        buscar()
    elif opcion == "S" or opcion == "s":
        salir()
        return None
    elif opcion =="H" or opcion =="h":
        hoy()
    elif opcion=="G" or opcion =="g":
        guardarDatos()
        return main()
    elif opcion == "P" or opcion =="p":
        numClientesProximos=int(input("Ingrese el numero de clientes próximos: "))
        proximosPedidos(numClientesProximos)
    else:
        return main()

main()
