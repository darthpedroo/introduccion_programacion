tomarUltimoDigito::Integer->Integer
tomarUltimoDigito n = mod n 10

tomarAnteUltimoDigito::Integer->Integer
tomarAnteUltimoDigito n = tomarUltimoDigito (sacarUltimoDigito n)

sacarUltimoDigito::Integer->Integer
sacarUltimoDigito n = div (n - (tomarUltimoDigito n)) 10

todosDigitosIguales::Integer->Bool
todosDigitosIguales n 
    | n <= 9 = True
    | tomarUltimoDigito n /= tomarAnteUltimoDigito n = False
    | otherwise = todosDigitosIguales(sacarUltimoDigito n )

