def obtener_minimo_y_maximo_de_producto(stock:list[tuple[str,int]],nombre_producto:str)->tuple[int,int]:
    
    maximo_de_producto:int = 0
    minimo_de_producto:int = 0
    
    for producto in stock:
        if producto[0] == nombre_producto:
            
            if maximo_de_producto == 0 and minimo_de_producto == 0:
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
    
    if numero == 1:
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

