menorDivisorAux:: Integer->Integer->Integer
menorDivisorAux 1 _ = 1
menorDivisorAux n i 
        | i == n = n
        | mod n i == 0 = i
        | otherwise = menorDivisorAux n (i+1)

menorDivisor :: Integer->Integer
menorDivisor n = menorDivisorAux n 2 

esPrimo:: Integer->Bool --hilarante definición!!!
esPrimo n = n == menorDivisor(n)

sonCoprimos::Integer->Integer->Bool
sonCoprimos x y = not (menorDivisor(x) == menorDivisor(y))