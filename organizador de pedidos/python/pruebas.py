def suma(arreglo):
    sum=0
    for i in range(len(arreglo)):
        sum += arreglo[i]
    return sum

def prioridad(cliente):
    fecha=cliente.getFechaDeEntrega()
    fecha=fecha.split("-")
    for i in range(len(fecha)):
        fecha[i]=int(fecha[i])
    priority=suma(fecha)
    return priority


