module SolucionT1 where

-- Ejercicio 1

divisoresDesde :: Integer -> Integer -> [Integer]
divisoresDesde 1 _ = []
divisoresDesde x y 
    | x == y = []
    | mod x y == 0 = y : divisoresDesde (x) (y+1)
    | otherwise = (divisoresDesde x (y+1))

sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

esNumeroAbundante :: Integer -> Bool
esNumeroAbundante x = sumatoria (divisoresDesde x 1) > x

f1 :: Integer -> Integer -> Integer
f1 inicio fin 
    | inicio == fin && esNumeroAbundante inicio = 1
    | inicio == fin &&  not (esNumeroAbundante inicio) = 0
    | esNumeroAbundante inicio = 1 + f1 (inicio+1) fin
    | otherwise = f1 (inicio+1) fin

-- EJERCICIO 2
materiaVencida::(String,Integer,Integer) -> Bool
materiaVencida (nombre,año,cuatrimestre)
    | año < 2021 = True
    | (año == 2021) && (cuatrimestre == 1 || cuatrimestre == 0) = True
    | otherwise = False

borrarElemento:: [String] -> String -> [String]
borrarElemento [] _ = []
borrarElemento (x:xs) elemento 
    | x /= elemento = (x) : borrarElemento xs elemento
    | otherwise = borrarElemento xs elemento

borrarRepetidos:: [String] -> [String]
borrarRepetidos [] = []
borrarRepetidos (x:xs) = (x) : borrarElemento xs x

f2Troll :: [(String, Integer, Integer)] -> [String]
f2Troll [] = []
f2Troll ((nombre,año,cuatrimestre):xs) 
    | materiaVencida (nombre,año,cuatrimestre) = nombre : f2Troll xs
    | otherwise = f2Troll xs

f2 :: [(String, Integer, Integer)] -> [String]
f2 jeje = borrarRepetidos (f2Troll jeje)

-- Ejercicio 3 (bravo vince)

f3 :: [Integer] -> Integer -> [Integer]
f3 [] _ = []
f3 (x:xs) u 
    | x < 0 = []
    | x >= 0 && x <= u = x : f3 xs u
    | x > u = u : f3 xs u

enesimoElemento::[Integer]->Integer->Integer
enesimoElemento (x:xs) 0 = x
enesimoElemento (x:xs) enesimo = (enesimoElemento xs (enesimo-1))

-- Ejercicio 4
f4 :: [[Integer]] -> Integer -> Integer
f4 [] columna = 0
f4 (x:xs) columna 
    | mod (enesimoElemento x (columna-1)) 2 == 0 = 1 + f4 xs columna
    | otherwise = f4 xs columna
