borrarUltimoDigito:: Integer -> Integer
borrarUltimoDigito n = div (n - mod n 10) 10  

cantDigitos:: Integer -> Integer
cantDigitos 0 = 0
cantDigitos n = 1 + cantDigitos (borrarUltimoDigito n)

digitoUnidades:: Integer -> Integer
digitoUnidades n1 = mod n1 10

iesimoDigito:: Integer -> Integer -> Integer
iesimoDigito 0 i = 0 -- esta condición no es necesaria porque la especificación dice que i tiene que ser mayor o igual a 1 y menor o igual a la cantidad de digitos
iesimoDigito n i 
    | cantDigitos n == i = digitoUnidades n 
    | otherwise = iesimoDigito (borrarUltimoDigito n) i