type Anio = Integer
type EsBisiesto = Bool

bisiesto:: Anio -> Bool
bisiesto anio 
    | mod anio 4 /= 0  = False
    | mod anio 100 == 0 && mod anio 400 /= 0 = False
    | otherwise = True
