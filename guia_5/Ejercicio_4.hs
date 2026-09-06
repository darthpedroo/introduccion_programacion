module Ejercicio_4 where
import Ejercicio_1 (ultimo, principio, longitud)

type Texto = [Char] --Si agregamos esto, no cambia nada.

sacarBlancosRepetidos :: Texto -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x:[]) = [x]
sacarBlancosRepetidos (x:xs)
    | (x == ' ') && (head xs) == x = sacarBlancosRepetidos (xs)
    | otherwise = x : sacarBlancosRepetidos xs

sacarPrimerBlanco :: [Char] -> [Char]
sacarPrimerBlanco [] = []
sacarPrimerBlanco (x:xs) 
    | x == ' ' = xs
    | otherwise = (x:xs)

sacarUltimoBlanco :: [Char] -> [Char]
sacarUltimoBlanco [] = []
sacarUltimoBlanco xs 
    | ultimo xs == ' ' = principio xs
    | otherwise = xs

contarPalabrasAux:: [Char]-> Integer
contarPalabrasAux [] = 0
contarPalabrasAux (x:xs)
    | x == ' ' = 1 + contarPalabrasAux xs
    | otherwise = contarPalabrasAux xs

contarPalabras::[Char]-> Integer
contarPalabras [] = 0
contarPalabras (' ':[]) = 0
contarPalabras (x:[]) = 1
contarPalabras xs 
    | sacarUltimoBlanco (sacarPrimerBlanco (sacarBlancosRepetidos xs)) == [] = 0 --Hardcodeo este caso borde que me molestaba!!!
    | otherwise = contarPalabrasAux (sacarUltimoBlanco (sacarPrimerBlanco (sacarBlancosRepetidos xs))) + 1


obtenerPrimerPalabra :: [Char] -> [Char] -- Asumo que llega un [Char con un solo espacio por palabra]
obtenerPrimerPalabra [] = []
obtenerPrimerPalabra (x:[]) = [x]
obtenerPrimerPalabra (x:xs)
    | x /= ' ' = x : obtenerPrimerPalabra xs
    | otherwise = []

sacarPrimerPalabra :: [Char] -> [Char] -- Asumo que llega un [Char] con un solo espacio por palabra
sacarPrimerPalabra [] = []
sacarPrimerPalabra (x:[]) = []
sacarPrimerPalabra (x:xs) 
    | x /= ' ' = sacarPrimerPalabra xs
    | x == ' ' = xs

palabrasAux::[Char] -> [[Char]] --Se supone que llega un [Char] con un espacio por palabra
palabrasAux [] = []
palabrasAux (' ':[]) = []
palabrasAux (x:[]) = [[x]]
palabrasAux xs = obtenerPrimerPalabra xs : palabrasAux (sacarPrimerPalabra xs)

palabras ::[Char]->[[Char]]
palabras xs = palabrasAux (sacarUltimoBlanco (sacarPrimerBlanco (sacarBlancosRepetidos xs)))

palabraMasLargaAux :: [Char] -> [Char] -- Asumo que llega un [Char] con un espacio por palabra
palabraMasLargaAux [] = []
palabraMasLargaAux xs 
    | sacarPrimerPalabra xs == [] = sacarUltimoBlanco xs
    | longitud (obtenerPrimerPalabra xs) >= longitud (obtenerPrimerPalabra (sacarPrimerPalabra xs)) = palabraMasLargaAux ((obtenerPrimerPalabra xs) ++ [' ']++ (sacarPrimerPalabra (sacarPrimerPalabra xs))) 
    
    | otherwise = palabraMasLargaAux (obtenerPrimerPalabra (sacarPrimerPalabra xs) ++ [' ']++ (sacarPrimerPalabra (sacarPrimerPalabra xs)))

palabraMasLarga :: [Char]->[Char]
palabraMasLarga xs =  palabraMasLargaAux (sacarPrimerBlanco (sacarUltimoBlanco (sacarBlancosRepetidos xs)))

aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:[]) = x
aplanar (x:xs) = x ++ aplanar xs

aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos (x:[]) = x
aplanarConBlancos (x:xs) = x ++ " " ++ aplanarConBlancos xs

generarStringNBlancos:: Integer->String
generarStringNBlancos 0 = ""
generarStringNBlancos n = " " ++ generarStringNBlancos (n -1)

aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [] _ = []
aplanarConNBlancos (x:[]) _ = x
aplanarConNBlancos (x:xs) n = x ++ generarStringNBlancos n ++ aplanarConNBlancos xs n