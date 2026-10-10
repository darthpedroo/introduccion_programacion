def vaciar_lista(lista:list[bool]):
    while len(lista)>0:
        lista.pop()

def pertenece_a_cada_uno_version_1(s:list[list[int]],e:int, res:list[bool]):
    vaciar_lista(res)
    for lista in s:
        if e in lista:
            res.append(True)
        else: 
            res.append(False)

def pertenece_a_cada_uno_version_2(s:list[list[int]],e:int, res:list[bool]):
    vaciar_lista(res)
    for lista in s:
        if e in lista:
            res.append(True)
        else:
            res.append(False) 

def pertenece_a_cada_uno_version_3(s:list[list[int]],e:int)->list[bool]:
    
    res:list[bool] = []

    for lista in s:
        if e in lista:
            res.append(True)
        else: 
            res.append(False)

    return res

