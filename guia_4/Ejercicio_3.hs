{-Implementación usando el ejercicio Anterior-}

floor2:: Float -> Integer -> Integer
floor2 n iterator | n >= fromInteger iterator && n < fromInteger iterator +1 = iterator
    | otherwise = floor2 n (iterator +1)

parteEntera:: Float -> Integer
parteEntera n = floor2 n 0

esDivisible:: Integer -> Integer -> Bool
esDivisible dividendo divisor 
    | dividendo == divisor = True
    | dividendo >= divisor = fromInteger (parteEntera (fromInteger dividendo / fromInteger divisor)) ==  (fromInteger dividendo / fromInteger divisor) 

{-Implementación usando restas-}

esDivisible2:: Integer -> Integer ->Bool
esDivisible2 dividendo divisor
    | dividendo > 0 && dividendo < divisor = False
    | dividendo == 0 = True
    | otherwise = esDivisible (dividendo - divisor) divisor