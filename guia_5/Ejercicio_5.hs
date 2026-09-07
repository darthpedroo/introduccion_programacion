module Ejercicio_5 where
import Ejercicio_1 (principio, ultimo, reverso)

menorDivisorAux:: Integer->Integer->Integer
menorDivisorAux 1 _ = 1
menorDivisorAux n i 
        | i == n = n
        | mod n i == 0 = i
        | otherwise = menorDivisorAux n (i+1)

menorDivisor :: Integer->Integer
menorDivisor n = menorDivisorAux n 2 

esPrimo:: Integer->Bool --hilarante definición!!!
esPrimo 1 = False
esPrimo n = n == menorDivisor(n)

nEsimoPrimoAux::Integer->Integer->Integer --revisar!!
nEsimoPrimoAux nFinal i  
        | nFinal == 0 = (i-1)
        | esPrimo i = nEsimoPrimoAux (nFinal-1) (i+1) 
        | otherwise = nEsimoPrimoAux nFinal (i+1) 

nEsimoPrimo::Integer->Integer
nEsimoPrimo n = nEsimoPrimoAux n 1

sumatoriaPro:: (Num t) => [t]-> t
sumatoriaPro [] = 0
sumatoriaPro (x:[]) = x
sumatoriaPro(x:xs) = x + sumatoriaPro xs

sumaAcumuladaAux :: (Num t, Eq t) => [t] -> [t] --Tuve q cambiar la firma aca pq sino se quejaba el compilador =)
sumaAcumuladaAux [] = []
sumaAcumuladaAux xs = (ultimo xs + sumatoriaPro (principio xs)) : sumaAcumuladaAux (principio xs)

sumaAcumulada :: (Num t , Eq t) => [t] -> [t]
sumaAcumulada xs = reverso (sumaAcumuladaAux xs)

descomponerEnPrimosLista :: [Integer] -> [[Integer]]
descomponerEnPrimosLista (x:[]) = [descomponerEnPrimos x]
descomponerEnPrimosLista (x:xs) = descomponerEnPrimos x : descomponerEnPrimosLista xs 

descomponerEnPrimos :: Integer -> [Integer]
descomponerEnPrimos x = descomponerEnPrimosAux x 2

descomponerEnPrimosAux :: Integer -> Integer -> [Integer]
descomponerEnPrimosAux 1 n = []
descomponerEnPrimosAux x n
        | mod x n == 0 = n : descomponerEnPrimosAux (div x n) (2)
        | otherwise = descomponerEnPrimosAux x (n+1)

{--
Inspiración:

- https://www.youtube.com/watch?v=46E0-XJuAXs
- https://www.youtube.com/watch?v=6OgDTCG1QCU

ALGORITMO

135

135 / 2 == 0 ? NO
135 / 3 == 0 ? SI 
45 / 3 == 0 ? SI
15 / 3 == 0 ? SI
5 / 3 == 0 ? NO
5 / 5 == 0 ? SI
1 / 1 == 0 ? SI

TIENE QUE HABER UN PASO PREVIO, EN EL QUE SE DETERMINE SI ES PRIMO.

--}
