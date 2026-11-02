import random
from queue import Queue as Cola

def generar_nros_al_azar(cantidad: int, desde:int, hasta:int)->Pila[int]:
    cola:Cola = Cola() 
    
    for i in range(0,cantidad,1):

        numero_random :int = random.randint(desde,hasta)
        cola.put(numero_random)

    return cola

# 1,2,3

def copiar_cola(cola:Cola)->Cola:
    copia_cola = Cola()
    temp_cola = Cola()

    while not cola.empty():
        elemento = cola.get()
        temp_cola.put(elemento)

    while not temp_cola.empty():
        elemento = temp_cola.get()
        copia_cola.put(elemento)
        cola.put(elemento)

    return copia_cola

def mostrar_cola(cola:Cola)->None:
    copia_cola = copiar_cola(cola)
    lista = []
    while not copia_cola.empty():
        elemento = copia_cola.get()
        lista.append(elemento)

    print(lista)

cola = Cola()
cola.put(1)
cola.put(2)
cola.put(3)

mostrar_cola(cola)
