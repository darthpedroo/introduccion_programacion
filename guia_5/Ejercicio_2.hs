module Ejercicio_2 where
import Ejercicio_1 (reverso)

longitud :: (Eq a) => [a] -> Integer
longitud xs 
    | xs == [] = 0
    | otherwise = 1 + (longitud (tail xs))

pertenece:: (Eq t) => t -> [t] -> Bool
pertenece t (x:xs) 
    | t == x = True
    | xs == [] = False
    | otherwise = pertenece t xs


todosIguales::(Eq t)=>[t] ->Bool
todosIguales [] = True
todosIguales (x:[]) = True
todosIguales (x:xs) = x == head xs && todosIguales xs

todosDistintos::(Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:[]) = True
todosDistintos (x:xs) = not (pertenece x xs) && todosDistintos xs

hayRepetidos::(Eq t) => [t] -> Bool
hayRepetidos lista = not (todosDistintos lista)

quitar::(Eq t) => t -> [t]->[t]
quitar _ [] = []
quitar t (x:xs)
    | t == x = xs
    | xs == [] = [x]
    | t /= x = (x : quitar t xs)

quitarTodos:: (Eq t) => t -> [t]->[t]
quitarTodos _ [] = []
quitarTodos t (x:xs)
    | t == x  = (quitarTodos t (xs))
    | t /= x = (x : quitarTodos t xs)

eliminarRepetidos::(Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:[]) = [x]
eliminarRepetidos (x:xs) 
    | not (pertenece x xs) = x : eliminarRepetidos xs --Si x no pertenece a xs (osea si no vuelve a aparecer) no hacemos nada, seguimos recurseando
    | otherwise = x : eliminarRepetidos (quitarTodos x xs)

esSubSet::(Eq t)=>[t]->[t]->Bool --revisa si una lista esta contenida en otra lista
esSubSet [] [] = True
esSubSet [] _ = True
esSubSet _ [] = False
esSubSet (x:xs) ys = pertenece x ys && esSubSet xs ys

mismosElementos::(Eq t)=>[t]->[t]->Bool
mismosElementos xs ys = esSubSet xs ys && esSubSet ys xs

capicua::(Eq t) =>[t]->Bool
capicua xs = xs == reverso xs