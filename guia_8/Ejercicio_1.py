import random
from queue import LifoQueue as Pila

## AUXILIARES
def copiar_pila(pila:Pila)->Pila:
    
    pila_temporal: Pila = Pila()
    copia_pila:Pila = Pila()
    
    #me paso los elementos a una pila temporal
    while not pila.empty():
        elemento = pila.get()
        pila_temporal.put(elemento)

    # los elementos están al reves y al mismo timepo me borré mi pila anterior, reordeno mi copia y rearmo la pila original.
    
    while not pila_temporal.empty():
        elemento = pila_temporal.get()
        pila.put(elemento)
        copia_pila.put(elemento)

    return copia_pila

def crear_pila_con_lista(lista:list)->Pila:
    pila = Pila()
    lista = reversed(lista)
    for elemento in lista:
        pila.put(elemento)

    return pila

def mostrar_pila(pila:Pila)->None:

    copia_pila = copiar_pila(pila)
    lista = []
    while not copia_pila.empty():
        elemento = copia_pila.get()
        lista.append(elemento)

    print(lista)

def reverse_pila(pila:Pila)->Pila:
    copia_pila = copiar_pila(pila)

    lista = []

    while not copia_pila.empty():
        elemento = copia_pila.get()
        lista.append(elemento)
    lista.reverse() 
    return crear_pila_con_lista(lista)

## EJERCICIO 1
def generar_nros_al_azar(cantidad: int, desde:int, hasta:int)->Pila[int]:
    
    pila: Pila = Pila()
    for i in range(0,cantidad,1):

        numero_random :int = random.randint(desde,hasta)
        pila.put(numero_random)

    return pila

## EJERCICIO 2
        
def cantidad_elementos(pila:Pila)->int:
    
    copia_pila = copiar_pila(pila)
    contador:int = 0
    
    while not copia_pila.empty():
        copia_pila.get()
        contador+=1

    return contador

## EJERCICIO 3

def buscar_el_maximo(p:Pila[int])->int:
    copia_pila = copiar_pila(p)
    maximo = copia_pila.get()

    while not copia_pila.empty():
        elemento = copia_pila.get()

        if elemento > maximo:
            maximo = elemento
    return maximo

## EJERCICIO 4
def buscar_nota_maxima(p: Pila[tuple[str,int]])->tuple[str,int]:
    copia_pila = copiar_pila(p)
    
    maximo = copia_pila.get()
    while not copia_pila.empty():
        elemento = copia_pila.get()
        if elemento[1] > maximo[1]:
            maximo = elemento

    return maximo

## EJERCICIO 5

def esta_bien_balanceada(s:str)->bool:
    # Algoritmo
    # Me guardo el parentesis en una lista
    # Bien Formada: 1 + (5+10)*2+(100+10)/2
    # Mal Formada 1: (10 + 20)*5+(1*2)+)
    # Mal Formada 2: )10 + 15 ) ((
    lista = []

    parentesis_apertura = 0

    for char in s:
        lista.append(char)
   
        if char == "(":
            parentesis_apertura+=1
        
        elif char  == ")":
            if parentesis_apertura == 0: #Estoy cerrando cosas q no debería cerrar.
                return False
            elif parentesis_apertura >0:
                parentesis_apertura -= 1
    
    if parentesis_apertura != 0:
        return False

    return True

def aplicar_operador(x:int,y:int,operador:str)->float:
    
    res = 0

    if operador == "+":
        res = x+y

    elif operador == "*":
        res = x*y

    elif operador == "-":
        res = y-x

    elif operador == "/":
        res = y/x

    return res

def evaluar_expresion(s:str)->float:
    
    operadores = ["+","-","*","/"]

    pila = Pila()

    for char in s.split(" "): 
        if char in operadores:
            x = pila.get()
            y = pila.get()
            res = aplicar_operador(x,y,char)
            pila.put(res)
        elif char != " ":
            numero = int(char)
            pila.put(numero)
    
    res = pila.get()
    return res

def intercalar(p1:Pila, p2:Pila)->Pila:
    
    copia_p1 = copiar_pila(p1)
    copia_p2 = copiar_pila(p2)
    res = Pila()
    

    while not copia_p1.empty():
        elemento_p1 = copia_p1.get()
        elemento_p2 = copia_p2.get()
        res.put(elemento_p1)
        res.put(elemento_p2)

    res = reverse_pila(res)
    return res

pila_1 = crear_pila_con_lista([1,3,5,7,9])
pila_2 = crear_pila_con_lista([2,4,6,8,10])
mostrar_pila(intercalar(pila_1,pila_2))
