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

sonCoprimos::Integer->Integer->Bool
sonCoprimos x y = not (menorDivisor(x) == menorDivisor(y))

nEsimoPrimoAux::Integer->Integer->Integer --revisar!!
nEsimoPrimoAux nFinal i  
        | nFinal == 0 = (i-1)
        | esPrimo i = nEsimoPrimoAux (nFinal-1) (i+1) 
        | otherwise = nEsimoPrimoAux nFinal (i+1) 

nEsimoPrimo::Integer->Integer
nEsimoPrimo n = nEsimoPrimoAux n 1
