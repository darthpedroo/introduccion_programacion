def promediar_salidas(salidas: list[int])->tuple[int,float]:

    res:tuple[int,float]
    tiempo_total:int = 0
    cantidad_salidas:int = 0

    for salida in salidas: 
        if salida <= 60 and salida > 0:
            tiempo_total+=salida
            cantidad_salidas+=1

    if cantidad_salidas == 0:
        res = (0,0.0)
    else:
        res = (cantidad_salidas,tiempo_total/cantidad_salidas)
    
    return res

def promedio_de_salidas(registro:dict[str,list[int]])-> dict[str,tuple[int,float]]:
    
    salida_final:dict[str, tuple[int,float]] = {}
    
    for persona in registro.keys():
        tiempos = registro[persona]
        salida_final[persona] = promediar_salidas(tiempos)
    
    return salida_final
   
def tiempo_mas_rapido(tiempos_salas:list[int])->int:
    
    minimo:int = 61

    for tiempo in tiempos_salas:
        if tiempo <= 60 and tiempo > 0:
            if tiempo < minimo:
                minimo = tiempo

    return tiempos_salas.index(minimo)

def racha_mas_larga(tiempos: list[int])-> tuple[int,int]:
    
    racha_actual:int = 0
    racha_maxima:int = 0
    tupla_maxima:tuple[int,int] = (0,0)
    cursor_inicio:int = 0
    cursor_final:int = 0
    
    for tiempo in tiempos:
        if tiempo != 0 and tiempo != 61:
            cursor_final+=1
            racha_actual+=1
        else:
            if racha_actual > racha_maxima:
                racha_maxima = racha_actual
                tupla_actual = (cursor_inicio, cursor_final-1)
                tupla_maxima = tupla_actual
            
            racha_actual = 0
            cursor_final+=1
            cursor_inicio=cursor_final

    if racha_actual > racha_maxima:
        racha_maxima = racha_actual
        tupla_actual = (cursor_inicio, cursor_final-1)
        tupla_maxima = tupla_actual
    
    return (tupla_maxima)

def fue_el_tercero_pero_el_resto_no(sala: list[int])->bool:
    
    if sala[2] == 0:
        return False
    elif (sala[0] != 0) or (sala[1] != 0) or (sala[3] != 0):
        return False
    
    return True

def escape_en_solitario(amigos_por_salas: list[list[int]])->list[int]:
    # Devuelve los indicies de todas las filas en las cuales el primer,segundo y cuarto amigo no fueron, pero el tercero sí fue (independientemente de si salió o no)

    lista_de_indices:list[int] = []

    for i in range(len(amigos_por_salas)):
        if fue_el_tercero_pero_el_resto_no(amigos_por_salas[i]):
            lista_de_indices.append(i)

    return lista_de_indices
