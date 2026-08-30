tomarUltimoDigito::Integer->Integer
tomarUltimoDigito n = mod n 10

sacarUltimoDigito::Integer->Integer
sacarUltimoDigito n = div (n - (tomarUltimoDigito n)) 10


cantDigitos:: Integer->Integer
cantDigitos n | n < 10 = 1
              |otherwise =  1 + cantDigitos(sacarUltimoDigito n)

iesimoDigito::Integer->Integer->Integer
iesimoDigito n i = mod (div n (10 ^ ((cantDigitos(n)-i)))) 10

sacarPrimerDigito::Integer->Integer
sacarPrimerDigito n = n - ((iesimoDigito n 1) * 10 ^ ((cantDigitos n) -1))

sumaDigitos::Integer->Integer
sumaDigitos x 
    | x < 9 = tomarUltimoDigito x
    | otherwise = tomarUltimoDigito x + sumaDigitos (sacarUltimoDigito x)


esCapicua::Integer->Bool
esCapicua x 
    | x < 9 = True 
    | iesimoDigito x 1 /= tomarUltimoDigito x  = False
    | otherwise = esCapicua (sacarUltimoDigito (sacarPrimerDigito x) )