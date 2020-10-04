import sqlite3
import time as t
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msg

import Cliente as C

fechaDeHoy = t.localtime()

diaActual = fechaDeHoy[2]
mesActual = fechaDeHoy[1]
anoActual = fechaDeHoy[0]





class Aplicacion:
    def __init__(self,ventana):
        self.__ventana = ventana
        self.__conection = sqlite3.connect('database.db')
        self.__ventana.geometry("400x200")
        
        #titulo de la ventana
        self.__ventana.title("Organizador de pedidos")
        self.__notebook = ttk.Notebook(self.__ventana,width = 400, height=100)
        

        #pestaña agregar
        self.__agregar = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__agregar, text = "Agregar")

        #pestaña eliminar
        self.__eliminar = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__eliminar, text = "Eliminar")

        #pestaña buscar
        self.__buscar = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__buscar, text = "Buscar")

        #pestaña pedidos de hoy
        self.__pedidosDeHoy = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__pedidosDeHoy, text = "Pedidos de Hoy")

        #pestaña proximos pedidos
        self.__proximosPedidos = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__proximosPedidos, text = "Próximos pedidos")

        #labels y entries agregar
        self.__titulos = ["Nombre: ", "Cantidad: ", "Precio: ", "Fecha de entrega: ", "Modo de pago: "]
        self.__Entry = []
        for i in range(5):
            tk.Label(self.__agregar, text = self.__titulos[i]).grid(row = i, column = 1)
            self.__Entry.append(tk.Entry(self.__agregar,width = 40))
            self.__Entry[i].grid(row = i, column = 2)

        #boton agregar
        self.__botonAgregar = tk.Button(self.__agregar, text = "Agregar",command = self.agregar, bg= "green")
        self.__botonAgregar.grid(row = 6 , column =2)
    
        #label y entry eliminar 
        self.__labelEliminar = tk.Label(self.__eliminar, text= "Nombre: ")
        self.__labelEliminar.grid(row = 1, column = 2)
        
        self.__EntryEliminar = tk.Entry(self.__eliminar)
        self.__EntryEliminar.grid(row = 1, column = 3)

        #boton eliminar
        self.__botonEliminar = tk.Button(self.__eliminar, text = "Eliminar", command = self.eliminar,bg = "pink")
        self.__botonEliminar.grid(row = 4, column = 3)

        #bind eliminar con intro
        #self.__eliminar.bind("<Return>",command = self.eliminar)

        #label y entry Buscar
        self.__labelBuscar = tk.Label(self.__buscar, text = "Nombre: ")
        self.__labelBuscar.grid(row = 1, column = 1)

        self.__EntryBuscar = tk.Entry(self.__buscar)
        self.__EntryBuscar.grid(row = 1,column = 2 )


        #boton buscar
        self.__botonBuscar = tk.Button(self.__buscar,text = "Buscar", command = self.buscar, bg= "pink")
        self.__botonBuscar.grid(row = 2, column = 2)

        #pedidos de hoy
        self.__tabla = ttk.Treeview(self.__pedidosDeHoy,columns = 5,selectmode = "browse")
        self.__tabla["columns"]=("Nombre","Cantidad", "Precio", "Fecha de Entrega", "Modo de pago")
        self.__tabla.column("#0", width=2, minwidth=2, stretch=tk.NO)

        #scrollbar pedidos hoy
        yscroll = ttk.Scrollbar(self.__pedidosDeHoy, orient ="vertical",command = self.__tabla.yview)
        yscroll.pack(side="right", fill="y")

        self.__tabla.configure(yscrollcommand=yscroll.set)

        for categoria in self.__tabla["columns"]:
            self.__tabla.column(categoria, width=27, minwidth=27)
            self.__tabla.heading(categoria,text=categoria,anchor=tk.W)

        #boton cargar datos hoy
        self.__botonCargar = tk.Button(self.__pedidosDeHoy,text = "Actualizar", command = self.cargarDatosHoy,bg = "pink")
        self.__botonCargar.pack()

        #pedidos proximos
        self.__tablaProximosPedidos = ttk.Treeview(self.__proximosPedidos, columns = 5, selectmode= "browse")
        self.__tablaProximosPedidos["columns"]=("Nombre","Cantidad", "Precio", "Fecha de Entrega", "Modo de pago")
        self.__tablaProximosPedidos.column("#0", width=2, minwidth=2, stretch=tk.NO)

        #scrollbar pedidos proximos
        yscroll = ttk.Scrollbar(self.__proximosPedidos, orient ="vertical",command = self.__tablaProximosPedidos.yview)
        yscroll.pack(side="right", fill="y")

        self.__tablaProximosPedidos.configure(yscrollcommand=yscroll.set)

        for categoria in self.__tablaProximosPedidos["columns"]:
            self.__tablaProximosPedidos.column(categoria, width=27, minwidth=27)
            self.__tablaProximosPedidos.heading(categoria,text=categoria,anchor=tk.W)

        #boton cargar datos proximos pedidos
        self.__botonCargar = tk.Button(self.__proximosPedidos,text = "Actualizar", command = self.cargarDatosProximosPedidos,bg ="pink")
        self.__botonCargar.pack()


        self.__notebook.pack(expand = 1 , fill = "both")

        #boton guardar datos
        self.__botonGuardar = tk.Button(self.__ventana, text = "Guardar datos", command = self.guardar, bg= "skyblue")
        self.__botonGuardar.pack()
        
        #cargar pedidos de hoy y proximos
        self.cargarDatosHoy()
        self.cargarDatosProximosPedidos()

        self.__ventana.mainloop()
        
    def dialogo(self,tituloVentana,tamanoVentana,textoLabel,textoBoton):
        #cuadro de dialogo
        ventana = tk.Tk()
        ventana.title(tituloVentana)
        ventana.geometry(tamanoVentana)
        label = tk.Label(ventana, text = textoLabel)
        label.pack()
        #boton
        boton = tk.Button(ventana,text= textoBoton, command = ventana.destroy,bg = "green")
        boton.pack()

    def agregar(self):

        try:
            if cliente.getPrioridad() >= prioridadActual:
                arbol.agregar(cliente)
                colaDePrioridad.insertar(cliente)
                self.dialogo("Mensaje", "200x50","Cliente agregado exitosamente","Hecho")
            else:
                self.dialogo("Mensaje", "300x50", "Ingrese una fecha válida, Cliente no agregado", "Aceptar")
        except Exception:
            self.dialogo("Mensaje", "200x50",cliente.getNombre()+" ya existe","Aceptar")
        
        
    
    def eliminar(self):
        nombre = self.__EntryEliminar.get()
        resultadoBusqueda = arbol.buscar(nombre)
        if resultadoBusqueda[0]:
            colaDePrioridad.eliminar(nombre)
            arbol.eliminar(None,nombre)
            if resultadoBusqueda[1].getPrioridad() == prioridadActual:
                self.__tabla.delete(nombre)
            else:
                self.__tablaProximosPedidos.delete(nombre)
            self.dialogo("Mensaje","200x50","Cliente eliminado exitosamente", "Hecho")
        else:
            self.dialogo("Mensaje","200x50","No existe cliente","Aceptar")

    def buscar(self):
        nombre = self.__EntryBuscar.get()
        resultado = arbol.buscar(nombre)
        if resultado[0]:
            ventana = tk.Tk()
            ventana.title("Resultado")
            ventana.geometry("200x110")
            titulosLabel = ["Nombre: ", "Cantidad: ", "Precio: ", "Fecha de entrega: ", "Modo de pago: "]
            for i in range(len(titulosLabel)):
                tk.Label(ventana, text =titulosLabel[i]).grid(row= i, column = 1)
            tk.Label(ventana,text= resultado[1].getNombre()).grid(row = 0, column = 2)
            tk.Label(ventana,text= resultado[1].getCantidad()).grid(row = 1, column = 2)
            tk.Label(ventana,text= resultado[1].getPrecio()).grid(row = 2, column = 2)
            tk.Label(ventana,text= resultado[1].getFechaDeEntrega()).grid(row = 3, column = 2)
            tk.Label(ventana,text= resultado[1].getModoDePago()).grid(row = 4, column = 2)
        else:
            self.dialogo("Mensaje", "200x50","No se encuentra","Aceptar")
        
    def cargarDatosHoy(self):
        clientesAcargar = [] 
        #tomar los clientes de hoy
        while colaDePrioridad.getNumElementos()>0 and colaDePrioridad.top().getPrioridad() == prioridadActual:
            clientesAcargar.append(colaDePrioridad.extraer())

        #restaurar la cola de prioridad
        for cliente in clientesAcargar:
            colaDePrioridad.insertar(cliente)
        
        for i in range(len(clientesAcargar)):
            try:
                self.__tabla.insert("",i,clientesAcargar[i].getNombre(),text = i ,values = (clientesAcargar[i].getNombre(), clientesAcargar[i].getCantidad(),clientesAcargar[i].getPrecio(),clientesAcargar[i].getFechaDeEntrega(),clientesAcargar[i].getModoDePago()))
            except tk.TclError:
                pass
        self.__tabla.pack(side=tk.TOP,fill=tk.X)

    def cargarDatosProximosPedidos(self):
        clientesAcargar = [] 
        clientesDeHoy= []
        #tomar los clientes de hoy
        while colaDePrioridad.getNumElementos() >0 and colaDePrioridad.top().getPrioridad() == prioridadActual:
            clientesDeHoy.append(colaDePrioridad.extraer())
        #tomar los clientes proximos    
        while colaDePrioridad.getNumElementos() >0 and colaDePrioridad.getNumElementos()>0:
            clientesAcargar.append(colaDePrioridad.extraer())

        #restaurar la cola de prioridad
        for cliente in clientesDeHoy:
            colaDePrioridad.insertar(cliente)

        #restaurar los clientes proximos
        for cliente in clientesAcargar:
            colaDePrioridad.insertar(cliente)
        
        for i in range(len(clientesAcargar)):
            try:
                self.__tablaProximosPedidos.insert("",i,clientesAcargar[i].getNombre(),text = i ,values = (clientesAcargar[i].getNombre(), clientesAcargar[i].getCantidad(),clientesAcargar[i].getPrecio(),clientesAcargar[i].getFechaDeEntrega(),clientesAcargar[i].getModoDePago()))
            except tk.TclError:
                pass
        self.__tablaProximosPedidos.pack(side=tk.TOP,fill=tk.X)
    def guardar(self):
         #Quitar el cliente inicializador 
        resultadoBuscar = arbol.buscar("N")
        if resultadoBuscar[0]:
            arbol.eliminar(None,"N")
            
        cola = c.Cola()
        archivo = open("Datos.csv","w")
        cola.encolar(arbol)
        ventanaProgreso = tk.Tk()
        ventanaProgreso.title("Guardando Datos")
        ventanaProgreso.geometry("150x80")
        label = tk.Label(ventanaProgreso,text= "Guardando Datos...")
        label.pack()
        numElementos = arbol.numElementos()
        valorActual = 0.0 #para iniciar la barra de progreso
        largoBarra = 150.0
        barraDeProgreso = ttk.Progressbar(ventanaProgreso,orient = "horizontal", length = largoBarra,mode = "determinate")
        barraDeProgreso["value"]= valorActual
        barraDeProgreso["maximum"]= largoBarra
        barraDeProgreso.pack()
        def progreso(numero):
            barraDeProgreso["value"]= numero
        while not cola.estaVacia():
            Nodo =cola.sacar()
            if Nodo is None:
                pass
            else:
                archivo.write(Nodo.getDato().getNombre()+","+str(Nodo.getDato().getCantidad())+","+str(Nodo.getDato().getPrecio())+","+Nodo.getDato().getFechaDeEntrega()+","+Nodo.getDato().getModoDePago()+"\n")
                valorActual += 1/float(numElementos)*largoBarra
                barraDeProgreso.after(500,progreso(valorActual))
                barraDeProgreso.update()
                cola.encolar(Nodo.getIzq())
                cola.encolar(Nodo.getDer())
        archivo.close()
        botonAceptar = tk.Button(ventanaProgreso,text= "Hecho",command = ventanaProgreso.destroy, bg = "green")
        botonAceptar.pack()
        return True





ventana = tk.Tk()
app = Aplicacion(ventana)

ventana2 = tk.Tk()
ventana2.withdraw()
if msg.askyesno("Salir", "¿Quiere guardar los datos?"):
    #Quitar el cliente inicializador 
    resultadoBuscar = arbol.buscar("N")
    if resultadoBuscar[0]:
        arbol.eliminar(None,"N")
    app.guardar()


