module Ejercicio_2 where 

{-
Ejercicio 2. Implementar una funcion parteEntera :: Float ->Integer 
segun la siguiente especificacion:

problema parteEntera (x: R) : Z {
requiere: { x ≥0 }
asegura: { resultado ≤x < resultado + 1 }
-}

floor2:: Float -> Integer -> Integer
floor2 n iterator | n >= fromInteger iterator && n < fromInteger iterator +1 = iterator
    | otherwise = floor2 n (iterator +1)

parteEntera:: Float -> Integer
parteEntera n = floor2 n 0



