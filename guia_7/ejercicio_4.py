def ejecutar_movimiento(movimiento:tuple[str,int])->int:
    multiplier:int
    
    if movimiento[0] == "I":
        multiplier = 1
    else:
        multiplier = -1
    
    return multiplier*movimiento[1]
        

def saldoActual(movimientos:list[tuple[str,int]])-> int:
    
    movimiento: tuple[str,int]
    saldo_final :int = 0
    
    for movimiento in movimientos:
        saldo_final+=ejecutar_movimiento(movimiento)
        
    return saldo_final