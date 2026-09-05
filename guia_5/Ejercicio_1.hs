module Ejercicio_1 where

longitud :: (Eq a) => [a] -> Integer
longitud xs 
    | xs == [] = 0
    | otherwise = 1 + (longitud (tail xs))

ultimo :: (Eq t) => [t] -> t
ultimo xs
    | longitud xs == 1 = head xs
    | otherwise = ultimo (tail xs)

principio:: (Eq t) => [t] -> [t]
principio (x:xs) -- x es el primer elemento, xs es el resto de la lista
    | longitud (x:xs) == 1 = []
    | otherwise = x:(principio (xs))

reverso:: (Eq t) => [t] -> [t]
reverso [] = []
reverso (x:xs)
    | longitud (x:xs) == 1 = [x]
    | otherwise = ultimo xs : reverso (x: principio xs)

-- Caso base, si hay un solo elemento devuelve la lista con ese elemento
-- Caso Otherwise: Agarra el ultimo elemento y lo pone adelante de la lista con el primer elemento y el principio de la lista sin el primer elemento (osea lo pone adelante de la lista sin el último elemento), hacemos esto recursivamente y obtenemos el reverso.