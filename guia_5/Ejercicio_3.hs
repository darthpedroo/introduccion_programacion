module Ejercicio_3 where
import Ejercicio_1 (ultimo)
import Data.Bits (Bits(xor))
import Ejercicio_2 (quitar)

sumatoria::[Integer]->Integer
sumatoria [] = 0
sumatoria (x:[]) = x
sumatoria(x:xs) = x + sumatoria xs

productoria::[Integer]->Integer
productoria [] = 1
productoria (x:[]) = x
productoria (x:xs) = x * productoria xs

maximo::[Integer]->Integer
maximo (x:[]) = x
maximo (x:xs)
    | x >= head xs = (maximo (x : tail xs))
    | otherwise = (maximo ((head xs):(tail xs)))

minimo::[Integer]->Integer
minimo (x:[]) = x
minimo (x:xs)
    | x <= head xs = (minimo (x : tail xs))
    | otherwise = (minimo ((head xs):(tail xs)))

sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN 0 xs = xs
sumarN n (x:xs) = (x + n) : sumarN n xs

sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero xs = sumarN (head xs) xs

sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo xs = sumarN (ultimo xs) xs

pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) 
    | mod x 2 == 0 = x : pares xs
    | otherwise = pares xs

multiplosDeN::Integer -> [Integer]->[Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs)
    | mod x n == 0 = x : multiplosDeN n xs
    | otherwise = multiplosDeN n xs


ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar xs = minimo xs : ordenar (quitar (minimo xs) xs)
