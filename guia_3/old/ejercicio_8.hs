signo :: Integer -> Integer
signo n| n == 0 = 0
    | n >= 1 = 1
    | otherwise = -1
    

absoluto :: Integer -> Integer
absoluto x = signo x * x

sumaUltimosDosDigitos:: Integer -> Integer
sumaUltimosDosDigitos x = mod (absoluto x) 10 + mod (div (absoluto x) 10) 10

comparar:: (Integer,Integer) -> Integer
comparar (a,b) 
    | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
    | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
    | sumaUltimosDosDigitos a == sumaUltimosDosDigitos b = 0
