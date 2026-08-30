tomarUltimoDigito::Integer->Integer
tomarUltimoDigito n = mod n 10

sacarUltimoDigito::Integer->Integer
sacarUltimoDigito n = div (n - (tomarUltimoDigito n)) 10

cantDigitos:: Integer->Integer
cantDigitos n | n < 10 = 1
              |otherwise =  1 + cantDigitos(sacarUltimoDigito n)

iesimoDigito::Integer->Integer->Integer
iesimoDigito n i = mod (div n (10 ^ ((cantDigitos(n)-i)))) 10

sumaDigitos::Integer->Integer
sumaDigitos x 
    | x < 9 = tomarUltimoDigito x
    | otherwise = tomarUltimoDigito x + sumaDigitos (sacarUltimoDigito x)

