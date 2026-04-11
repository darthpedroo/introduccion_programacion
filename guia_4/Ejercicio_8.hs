{--
Ejercicio 8)
Especificar e implementar la funcion 
sumaDigitos :: Integer ->Integer 
que calcula la suma de digitos de un numero natural.
Para esta funcion pueden utilizar div y mod
--}


borrarUltimoDigito:: Integer -> Integer
borrarUltimoDigito n = div (n - mod n 10) 10

digitoUnidades:: Integer -> Integer
digitoUnidades n1 = mod n1 10

sumaDigitos:: Integer -> Integer
sumaDigitos 0 = 0
sumaDigitos n = digitoUnidades n + sumaDigitos (borrarUltimoDigito n)

