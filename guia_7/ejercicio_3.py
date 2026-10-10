def todos_los_elementos_son_mayores_o_iguales_a(notas:list[int],valor)->bool:

    nota:int

    for nota in notas:
        if nota < valor:
            return False

    return True

def algun_elemento_es_menor_a(notas:list[int],valor:int)->bool:
    nota :int
    for nota in notas:
        if nota < valor:
            return True

    return False

def promedio_notas(notas:list[int])->int:
    nota:int
    acumulador:int = 0
    for nota in notas:
        acumulador+=nota

    return acumulador / len(notas)


def resultadoMateria(notas:list[int])->int:
    if todos_los_elementos_son_mayores_o_iguales_a(notas,4) and promedio_notas(notas) >=7:
        return 1

    elif todos_los_elementos_son_mayores_o_iguales_a(notas,4) and (promedio_notas(notas)>=4 or promedio_notas(notas)<7):
        return 2

    else:
        return 3
