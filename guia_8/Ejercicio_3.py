from queue import LifoQueue as Pila
# Ejercicio 16

def promedio_por_estudiante(notas_list: [tuple[str,int]],estudiante:str)->float:
    copia_notas = notas_list.copy()
    
    suma_notas:int = 0
    cantidad_notas:int = 0

    for nota in copia_notas:
        if nota[0] == estudiante:
            suma_notas+=nota[1]
            cantidad_notas+=1

    return suma_notas/cantidad_notas

def calcular_promedio_por_estudiante(notas:list[tuple[str,float]])->dict[str,float]:
    
    copia_notas = notas.copy()

    diccionario_notas:dict[str,int] = {

    }

    for nota in copia_notas:
        estudiante:str = nota[0]
        if estudiante not in diccionario_notas:
            diccionario_notas[estudiante] = promedio_por_estudiante(copia_notas, estudiante)
    
    return diccionario_notas

def visitar_sitio(historiales:dict[str,Pila[str]],usuario:str, sitio:str):
    
    if usuario not in historiales:
        pila = Pila()
        pila.put(sitio)
        historiales[usuario] = pila
    else:
        historiales[usuario].put(sitio)

def navegar_atras(historiales:dict[str,Pila[str]],usuario:str)->str:
    return historiales[usuario].get()
