def pertenece(s:list[int], e: int) -> bool:
    return e in s

def divide_a_todos(s:list[int],e:int)-> bool:
    
    elemento:int
    
    for elemento in s:
        if elemento % e != 0:
            return False
    
    return True

def suma_total(s:list[int])->int:
    
    acumulador :int = 0
    elemento:int

    for elemento in s:
        acumulador+=elemento 

    return acumulador

def maximo(s:list[int])->int:
    
    maximoTemporal :int = s[0]
    elemento :int

    for elemento in s:
        if elemento >= maximoTemporal:
            maximoTemporal  = elemento

    return maximoTemporal

def minimo(s:list[int])->int:
    
    maximoTemporal :int = s[0]
    elemento :int

    for elemento in s:
        if elemento <= maximoTemporal:
            maximoTemporal  = elemento

    return maximoTemporal

def ordenados(s:list[int]) -> bool:
    
    i: int = 0

    while i < len(s)-1:
        if s[i] >= s[i+1]:
            return False
        i+=1

    return True

def pos_maximo(s:list[int])->int:

    if len(s) == 0:
        return -1

    return s.index(maximo(s))

def reverso(s:list[int])->list[int]:
    
    i:int
    lista_reversa = []

    for i in range(len(s)):
        lista_reversa.append(s[-1-i])

    return lista_reversa

def ultimo_indice(s:list[int],e:int)->int:
    return len(s) - 1 - reverso(s).index(e)


def pos_minimo(s:list[int])->int:

    if len(s) == 0:
        return -1

    return ultimo_indice(s,minimo(s))


def long_mayorASiete(s: list[str]) -> bool:

    palabra:str

    for palabra in s:
        if len(palabra) > 7:
            return True

    return False

def concatenar_lista(s:list[str])->str:
    
    letra:str
    palabra :str = ""
    for letra in s:
        palabra+=letra
    return palabra

def es_palindroma(s:list[str])->True:
    return concatenar_lista(reverso(s)) == s

def iguales_consecutivos(s:list[int])->bool:
    
    tope: int = 3
    acumulador:int = 0
    i : int = 0
    
    while i < len(s)-1 and (acumulador+1) < tope:
        if s[i] == s[i+1]:
            acumulador +=1
        else:
            acumulador = 0
        i+=1

    return (acumulador+1) == tope

def cantidad_letras(palabra:str)->dict:
    letras = {}

    for letra in palabra:
        if letra not in letras:
            letras.update({letra:1})
        else:
            letras.update({letra:letras.get(letra)+1})
    return letras

def vocales_distintas(palabra:str)->dict:
    vocales :list[str ]= ["a","e","i","o","u"]
    cantidad_letras_en_palabra :dict = cantidad_letras(palabra)
    tope :int = 3
    acumulador: int = 0

    vocal :str
    for vocal in vocales:
        if vocal in cantidad_letras_en_palabra:
            acumulador+=1

    return acumulador >= tope

def obtener_ultimo_digito(numero:int)->int:
    return numero % 10 

def sacar_ultimo_digito(numero:int)->int:
    return (numero - obtener_ultimo_digito(numero)) / 10 

def digitos_impares(numero:int)->int:
    
    acumulador_numeros_impares: int = 0

    while numero > 0: 
        if obtener_ultimo_digito(numero) % 2 == 1:
            acumulador_numeros_impares += 1
        numero = sacar_ultimo_digito(numero)

    return acumulador_numeros_impares 
        

def cantidad_digitos_impares(s:list[int])->int:
    elemento: int
    acumulador:int = 0
    
    for elemento in s:
        acumulador += digitos_impares(elemento)

    return acumulador
