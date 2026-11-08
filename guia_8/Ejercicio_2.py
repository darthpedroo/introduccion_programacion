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

def cantidad_elementos(cola:Cola)-> int:
    copia_cola = copiar_cola(cola)
    
    acumulador:int = 0

    while not copia_cola.empty():
        acumulador+=1
        copia_cola.get()

    return acumulador

def buscar_el_maximo(c:Cola[int])->int:
    copia_cola = copiar_cola(c)
    maximo:int = copia_cola.get()
    
    while not copia_cola.empty():
        elemento :int = copia_cola.get()
        
        if elemento > maximo:
            maximo = elemento

    return maximo

def buscar_nota_minima(c:Cola[tuple[str,int]])->tuple[str,int]:

    copia_cola = copiar_cola(c)
    minimo:tuple[str,int] = copia_cola.get()

    while not copia_cola.empty():
        elemento = copia_cola.get()
        if elemento[1] < minimo[1]:
            minimo = elemento

    return minimo

def intercalar(c1:Cola, c2:Cola)->Cola:
    new_cola = Cola()
    while not c1.empty():
        elemento_c1= c1.get()
        elemento_c2= c2.get()
        new_cola.put(elemento_c1)
        new_cola.put(elemento_c2)

    return new_cola

def armar_secuencia_bingo() -> Cola[int]:
    carton_bingo = Cola()
    x = []
    for i in range(0,100):
        x.append(i)

    random.shuffle(x)

    for i in x:
        carton_bingo.put(i)
    
    return carton_bingo

def jugar_carton_de_bingo(carton:list[int], bolillero:Cola[int])->int:
    copia_bolillero: Cola = copiar_cola(bolillero)
    copia_carton :list = carton.copy()
    acumulador:int = 0

    while len(copia_carton) > 0:
        
        numero_actual = copia_bolillero.get()

        if numero_actual in copia_carton:
            copia_carton.remove(numero_actual)
        
        acumulador+=1

    return acumulador

def pacientes_urgentes(c:Cola(tuple[int,str,str]))->int:
    copia_cola:Cola = copiar_cola(c)
    acumulador:int = 0
    
    while not copia_cola.empty():
        elemento = copia_cola.get()

        if elemento[0] < 4:
            acumulador+=1

    return acumulador


