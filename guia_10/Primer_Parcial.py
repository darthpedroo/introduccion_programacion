def obtener_minimo_y_maximo_de_producto(stock:list[tuple[str,int]],nombre_producto:str)->tuple[int,int]:
    
    maximo_de_producto:int = -1
    minimo_de_producto:int = -1
    
    for producto in stock:
        if producto[0] == nombre_producto:
            
            if maximo_de_producto == -1 and minimo_de_producto == -1:
                maximo_de_producto = producto[1]
                minimo_de_producto = producto[1]
            elif producto[1] > maximo_de_producto:
                maximo_de_producto = producto[1]
            elif producto[1] < minimo_de_producto:
                minimo_de_producto = producto[1]

    return (minimo_de_producto, maximo_de_producto)

def stock_productos(stock_cambios:list[tuple[str,int]])->dict[str,tuple[int,int]]:
    
    cambios_copia = stock_cambios.copy()

    dict_malware:dict[str,tuple[int,int]] = {}
    
    for stock in cambios_copia:
        nombre_producto:str = stock[0]
        if nombre_producto not in dict_malware:
            dict_malware[nombre_producto] = obtener_minimo_y_maximo_de_producto(cambios_copia, nombre_producto)

    return dict_malware

# EJERCICIO 2

def es_primo(numero:int)->bool:
    
    if numero <= 1:
        return False

    for i in range(2,numero,1):
        if numero % i == 0:
            return False
    
    return True

def obtener_ultimos_tres_digitos(numero:int)->int:
    return numero % 1000

def filtrar_codigos_primos(codigos_barra: list[int])->list[int]:
    copia_codigos_barra:list[int] = codigos_barra.copy()
    filtered_codigos:list[int] = []

    for codigo in copia_codigos_barra:
        if es_primo(obtener_ultimos_tres_digitos(codigo)):
            filtered_codigos.append(codigo)

    return filtered_codigos

# EJERCICIO 3

def subsecuencia_mas_larga(tipos_pacientes_atendidos:list[str])->int:
    # REHACER
    # REHACER
    # REHACER
    # REHACER
    # REHACER
    # REHACER
    # REHACER
    # REHACER
    # REHACER
    # Este lei mal el enunciado, entendi que solo podian ser perros y gatos =).
    copia_tipos_pacientes_atendidos = tipos_pacientes_atendidos.copy()

    la_mas_larga:list[str] = []
    lista_actual:list[str] = []
    
    paciente_actual = copia_tipos_pacientes_atendidos[0]
    indice_inicio = 0
    indice_inicio_actual = 0
    
    for i in range(len(copia_tipos_pacientes_atendidos)):
        paciente = copia_tipos_pacientes_atendidos[i] 

        if paciente != paciente_actual:
            paciente_actual = paciente
            

            if len(lista_actual) > len(la_mas_larga):
                la_mas_larga = lista_actual.copy()
                indice_inicio = indice_inicio_actual
                indice_inicio_actual = i

            lista_actual = []
            lista_actual.append(paciente)
        else:
            lista_actual.append(paciente)
    
    return indice_inicio 


def obtener_columna(grilla_horario:list[list][str], numero_columna:int)->list[str]:
    columna :list = []

    for fila in grilla_horario:
        columna.append(fila[numero_columna])

    return columna

def lista_desde_hasta(lista:list,desde:int, hasta:int)->list:
    new_list:list = []
    for i in range(desde,hasta+1): #tuve un error de indice y me olvide de poner este +1 =)
        new_list.append(lista[i])

    return new_list

def obtener_turno(dia_laboral:list[str],turno:str)->list[str]:
    res: list
    if turno == "MAÑANA":
        res = lista_desde_hasta(dia_laboral,0,3)
    else:
        res = lista_desde_hasta(dia_laboral,4,7)

    return res

def todos_iguales(lista:list[str])->bool:
    res = True
    original = lista[0]

    for elemento in lista:
        if elemento != original:
            res = False

    return res


def un_responsable_por_turno(grilla_horario:list[list[str]])->list[(bool,bool)]:
    res:list[tuple[bool,bool]] = []
    for i in range(len(grilla_horario[0])):
        dia = obtener_columna(grilla_horario,i)
        tupla = todos_iguales(obtener_turno(dia,"MAÑANA")),todos_iguales(obtener_turno(dia,"TARDE"))
        res.append(tupla)

    return res
