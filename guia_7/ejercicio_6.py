def vaciar_lista(lista:list[bool]):
    while len(lista)>0:
        lista.pop()

def es_matriz(s:list[list[int]])->bool:
    if len(s) == 0 or len(s[0]) == 0:
        return False
        
    primer_fila :int = s[0]
    fila:list[int]

    for fila in s:
        if len(fila) != len(primer_fila):
            return False

    return True

def ordenados(s:list[int]) -> bool:
    
    i: int = 0

    while i < len(s)-1:
        if s[i] >= s[i+1]:
            return False
        i+=1

    return True

def filas_ordenadas(m:list[list[int]],res:list[bool]):

    vaciar_lista(res)
    
    fila: list[int]
    
    for fila in m:
        res.append(ordenados(fila))

def columna(m:list[list[int]],c:int)->list[int]:
    current_columna = []
    fila :list[int]
    
    for fila in m:
        current_columna.append(fila[c])

    return current_columna

def transponer(m:list[list[int]])->list[list[int]]:

    res :list[list[int]] = []
    c_columna:int
    
    for c_columna in range(len(m[0])):
        res.append(columna(m,c_columna))

    return res

def columnas_ordenadas(m:list[list[int]])->bool:
    res = []
    filas_ordenadas(transponer(m),res)
    return res

# falta el del TATEI =)
