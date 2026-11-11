# EJERCICIO 9
from queue import Queue as Cola

def puntos_ganados(estrategia_1:str, estrategia_2:str)->int:
    res:int = 0

    if estrategia_1 == estrategia_2:
        if estrategia_1 == "me desvío siempre":
            res = -10
        elif estrategia_1 == "me la banco y no me desvío":
            res = -5
    else:
        if estrategia_1 == "me desvío siempre":
            res = -15
        elif estrategia_1 == "me la banco y no me desvío":
            res = 10

    return res

def torneo_de_gallinas(estrategias:dict[str,str])->dict[str,int]:
    # "me desvío siempre"
    # "me la banco y no me desvío"

    # [porky, goga, dun, jhon pork]
    # 
    
    personas = estrategias.keys()
    
    res:dict[str,int] = {}

    personas_lista = []

    for i in personas:
        personas_lista.append(i)

    for persona in personas_lista:
        rivales = personas_lista.copy()
        rivales.remove(persona)
        
        puntos_de_persona:int = 0

        for rival in rivales:
            estrategia_rival = estrategias[rival]
            estrategia_personal = estrategias[persona]
            puntos_de_persona+= puntos_ganados(estrategia_personal, estrategia_rival)

        res[persona] = puntos_de_persona

    return res

# EJERCICIO 10
def copiar_cola(cola:Cola)->Cola:
    copia_cola = Cola()
    temp_cola = Cola()

    while not cola.empty():
        elemento = cola.get()
        copia_cola.put(elemento)
        temp_cola.put(elemento)

    while not temp_cola.empty():
        cola.put(temp_cola.get())

    return copia_cola

def mostrar_cola(cola:Cola)->None:
    copia_cola = copiar_cola(cola)
    
    x = []
    while not copia_cola.empty():
        x.append(copia_cola.get())

    print(x)

def reordenar_cola_priorizando_vips(filaClientes: Cola[str,str])->Cola[str]:
    copia_fila_clientes = copiar_cola(filaClientes)

    cola_vip = Cola()
    cola_plebe = Cola()
    cola_final = Cola()

    while not copia_fila_clientes.empty():
        cliente = copia_fila_clientes.get()
        nombre_cliente:str = cliente[0]
        categoria_cliente:str = cliente[1]

        if categoria_cliente == "vip":
            cola_vip.put(nombre_cliente)
        elif categoria_cliente == "común":
            cola_plebe.put(nombre_cliente)

    ## Ahora los tengo que intercalar pero bien
    
    while not cola_vip.empty():
        persona: str = cola_vip.get()
        cola_final.put(persona)

    while not cola_plebe.empty():
        persona: str = cola_plebe.get()
        cola_final.put(persona)

    return cola_final

