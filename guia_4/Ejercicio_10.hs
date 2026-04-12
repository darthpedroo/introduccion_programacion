{--
Ejercicio 10)
Especificar, implementar y dar el tipo de las siguientes funciones 
(simil Ejercicio 4 Practica 2 de Algebra 1.)
--}

{--
Esepecificación

problema f1(n:N):N{
    requiere:{n>=0}
    asegura: {res=sumatoria i = 0 hasta n 2**i}
}
--}
--
f1Aux :: Integer -> Integer -> Integer -> Integer
f1Aux i base n
    | i == n = base^i
    | otherwise = base^i + f1Aux (i + 1) base n

f1::Integer->Integer
f1 n = f1Aux 0 2 n 
 
f2::Integer->Integer->Integer
f2 base n = f1Aux 1 base n

f3::Integer->Integer->Integer
f3 base n = f1Aux 1 base (n*2)

f4::Integer->Integer->Integer
f4 base n = f1Aux n base (n*2)
