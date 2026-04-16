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


