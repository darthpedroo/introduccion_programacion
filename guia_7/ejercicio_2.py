def sin_vocales(palabra:str)->str:
    palabra_sin_vocales=""
    letra:str

    for letra in palabra:
        if letra not in ["a","e","i","o","u"]:
            palabra_sin_vocales+=letra
    
    return palabra_sin_vocales

def reemplaza_vocales(palabra:str)->str:
    palabra_sin_vocales=""
    letra:str

    for letra in palabra:
        if letra not in ["a","e","i","o","u"]:
            palabra_sin_vocales+=letra
        else:
            palabra_sin_vocales+="_"
    return palabra_sin_vocales

def concatenar_lista(s:list[str])->str:
    
    letra:str
    palabra :str = ""
    for letra in s:
        palabra+=letra
    return palabra
def reverso(s:list[int])->list[int]:
    
    i:int
    lista_reversa = []

    for i in range(len(s)):
        lista_reversa.append(s[-1-i])

    return lista_reversa

def da_vuelta_str(palabra:str)->str:
    return concatenar_lista(reverso(palabra))

def eliminar_repetidos(palabra:str)->str:
    lista_sin_repetidos = ""
    elemento:str
    
    for elemento in palabra:
        if elemento not in lista_sin_repetidos:
            lista_sin_repetidos+=elemento
    
    return lista_sin_repetidos
