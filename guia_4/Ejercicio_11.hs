{--
 Ejercicio 11. a) Especificar e implementar una funcion eAprox :: Integer ->Float que aproxime el valor del numero e a partir de la siguiente sumatoria: 

problema eAprox(n:Z):R{
    requiere:{n >= 0}
    asegura: {res=sumatoria de i=0 hasta n (1/i!)}
--}



factorial::Integer->Integer
factorial 0 = 1
factorial n = n * factorial(n-1)

sumatoria::Integer->Integer->Float
sumatoria i n 
    | i == n = (1 / fromInteger(factorial i))
    | otherwise = (1 / fromInteger(factorial i)) + sumatoria (i+1) n


eAprox :: Integer -> Float
eAprox n = sumatoria 0 n
