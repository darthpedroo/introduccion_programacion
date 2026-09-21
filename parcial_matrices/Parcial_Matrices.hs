module Parcial_Matrices where

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

type Fila = [Integer]
type Tablero = [Fila]
type Posicion = (Integer,Integer)
type Camino = [Posicion]

maximoFila::Fila->Integer
maximoFila (x:[]) = x
maximoFila (x:xs) 
    | x >= head xs = maximoFila ( x:(tail xs) )
    | otherwise = maximoFila xs

filaLol = [1000,2,3,4,5,6,7,100,10,1,1,2,3000]
filaJeje = [1]

tablero = [[13,7,6,4],[1,1,32,25],[9,2,14,7],[7,3,5,16],[27,2,8,8]]

obtenerMaximoFilas::Fila->Fila->Fila
obtenerMaximoFilas fila1 fila2 
    | maximoFila fila1 >= maximoFila fila2 = fila1
    | otherwise = fila2

maximo::Tablero->Integer
maximo (fila:[]) = maximoFila fila
maximo (fila:tablero) 
    | obtenerMaximoFilas fila (head tablero) == fila = maximo (fila:(tail tablero))
    | otherwise = maximo ((head tablero):(tail tablero))


-- EJERCICIO 2

granFila::Tablero->[Integer]
granFila (fila:[]) = fila
granFila (fila:tablero) = (fila) ++ (granFila tablero)

elementosUnicosTablero::Tablero->[Integer]
elementosUnicosTablero tablero = eliminarRepetidos (granFila tablero)

cantidadAparicionesFila::[Integer]->Integer->Integer
cantidadAparicionesFila [] _ = 0 
cantidadAparicionesFila (x:xs) elemento
    | x == elemento = 1 + cantidadAparicionesFila xs elemento
    | otherwise = cantidadAparicionesFila xs elemento

cantidadApariciones::Tablero->Integer->Integer
cantidadApariciones tablero elemento = cantidadAparicionesFila (granFila tablero) elemento

masRepetidoAux::Tablero->[Integer]->Integer
masRepetidoAux tablero (x:[]) = x 
masRepetidoAux tablero (x:xs) 
    | cantidadApariciones tablero x >= cantidadApariciones tablero (head xs) = masRepetidoAux tablero (x:(tail xs))
    | otherwise = masRepetidoAux tablero xs


masRepetido::Tablero->Integer
masRepetido tablero = masRepetidoAux tablero (elementosUnicosTablero tablero)