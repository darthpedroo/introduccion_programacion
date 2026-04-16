obtenerUltimoDigito:: Integer -> Integer
obtenerUltimoDigito n = mod n 10

borrarUltimoDigito:: Integer -> Integer
borrarUltimoDigito n = div (n - mod n 10) 10

mayorDigitoParAux::Integer->Integer->Integer
mayorDigitoParAux n mayor 
    |   n == 0 = mayor
    |   mod (obtenerUltimoDigito n) 2 == 0 && obtenerUltimoDigito n > mayor = mayorDigitoParAux (borrarUltimoDigito n) (obtenerUltimoDigito n)
    |   otherwise = mayorDigitoParAux (borrarUltimoDigito n) mayor

mayorDigitoPar::Integer->Integer
mayorDigitoPar n = mayorDigitoParAux n (-1)