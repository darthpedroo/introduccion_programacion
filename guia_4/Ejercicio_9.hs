{--
Ejercicio 9).
Especificar e implementar una funcion esCapicua :: Integer->Bool que dado n ∈N≥0 determina si n es un numero capicua

problema esCapicua(n:N):Bool{
    requiere:{True}
    asegura:{ True <-> n[0+i] == n[] } ¿¿¿???
}

--}

borrarUltimoDigito:: Integer -> Integer
borrarUltimoDigito n = div (n - mod n 10) 10

digitoUnidades:: Integer -> Integer
digitoUnidades n1 = mod n1 10

sumaDigitos:: Integer -> Integer
sumaDigitos 0 = 0
sumaDigitos n = digitoUnidades n + sumaDigitos (borrarUltimoDigito n)

obtenerUltimoDigito:: Integer -> Integer
obtenerUltimoDigito n = mod n 10
					.
compararDecimal::Integer->Integer->Integer
compararDecimal n multiplicador  
    | n > multiplicador && n > multiplicador *10 = compararDecimal n (multiplicador *10)
    |otherwise = multiplicador

obtenerPrimerDigito::Integer -> Integer
obtenerPrimerDigito n = div n (compararDecimal n 1)

borrarPrimerDigito:: Integer -> Integer
borrarPrimerDigito n = n - (obtenerPrimerDigito n * (compararDecimal n 1))

esCapicua::Integer->Bool
esCapicua 0 = True
esCapicua n | obtenerPrimerDigito n == obtenerUltimoDigito n = esCapicua (borrarPrimerDigito (borrarUltimoDigito n)) | otherwise = False
