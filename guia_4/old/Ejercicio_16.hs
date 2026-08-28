{--
Ejercicio 16)

 --}

{-
 
-}

esPrimoAux::Integer->Integer->Bool
esPrimoAux n i
    | n == 1 = False 
    | i == n = True
    | i /= n && mod n i == 0 = False
    | otherwise = esPrimoAux n (i+1)

esPrimo::Integer->Bool
esPrimo n = esPrimoAux n 2


menorDivisorAux::Integer->Integer->Integer
menorDivisorAux n i 
    |n == 1 = 1
    |n == i = i
    |mod n i == 0 = i
    |otherwise = menorDivisorAux n (i+1)
    
menorDivisor::Integer->Integer
menorDivisor n = menorDivisorAux n 2

sonCoprimosAux::Integer->Integer->Integer->Bool
sonCoprimosAux n1 n2 i
    | n1 == 1 || n2 == 1 = True
    | i > n1 || i > n2 = True
    | mod n1 i == 0 && mod n2 i == 0 = False
    | otherwise = sonCoprimosAux n1 n2 (i+1)

sonCoprimos::Integer->Integer->Bool
sonCoprimos n1 n2 = sonCoprimosAux n1 n2 2



nEsimoPrimoAux::Integer->Integer->Integer->Integer
nEsimoPrimoAux n i primoCounter
    | esPrimo(i) && primoCounter /= n = nEsimoPrimoAux n (i+1) (primoCounter+1)
    | esPrimo(i) && primoCounter == n = i
    | otherwise = nEsimoPrimoAux n (i+1) primoCounter

nEsimoPrimo::Integer->Integer
nEsimoPrimo n = nEsimoPrimoAux n 1 0
