module Parcial_Perfectos_Amigos where

-- EJERCICIO 1)

obtenerUltimo::[Integer]->Integer
obtenerUltimo (x:[]) = x
obtenerUltimo (x:xs) = obtenerUltimo xs

sacarUltimo::[Integer]->[Integer]
sacarUltimo(x:[]) = []
sacarUltimo(x:xs) = ( x: sacarUltimo xs)

reverso::[Integer]->[Integer]
reverso (x:[]) = [x]
reverso (xs) = (obtenerUltimo xs) : reverso (sacarUltimo xs)

divisoresPropiosDesde::Integer->Integer->[Integer]
divisoresPropiosDesde 1 _ = []
divisoresPropiosDesde x 1 = [1]
divisoresPropiosDesde x divisor 
    | mod x divisor == 0 = divisor : divisoresPropiosDesde x (divisor-1)
    | otherwise = divisoresPropiosDesde x (divisor -1)

divisoresPropios::Integer->[Integer]
divisoresPropios 1 = []
divisoresPropios x = reverso (divisoresPropiosDesde x (x-1) )

-- EJERCICIO 2)
sumatoria::[Integer]->Integer
sumatoria ([]) = 0
sumatoria (x:[]) = x
sumatoria (x:xs) = x + (sumatoria xs)

sonAmigos::Integer->Integer->Bool
sonAmigos n m 
    | n == m = False
    | otherwise = n == sumatoria (divisoresPropios m) && m == sumatoria(divisoresPropios n)

-- EJERCICIO 3) 

esPerfecto::Integer->Bool
esPerfecto x = (sumatoria (divisoresPropios x)) == x

losPrimerosNPerfectosAux::Integer->Integer->[Integer]
losPrimerosNPerfectosAux 0 _ = []
losPrimerosNPerfectosAux i x 
    | esPerfecto x = x: losPrimerosNPerfectosAux (i-1) (x+1)
    | otherwise = losPrimerosNPerfectosAux (i) (x+1)

losPrimerosNPerfectos::Integer->[Integer]
losPrimerosNPerfectos 0 = []
losPrimerosNPerfectos n = losPrimerosNPerfectosAux n 1

-- EJERCICIO 4)

generarTuplaAmigos::Integer->[Integer]->[(Integer,Integer)]
generarTuplaAmigos n (x:xs)
    | xs == [] && sonAmigos n x = [(n,x)]
    | xs == [] && not (sonAmigos n x) = []
    | sonAmigos n (x) = (n,x) : generarTuplaAmigos n xs
    | otherwise =  generarTuplaAmigos n xs

xd = [220,1184,5564,1210,999,666,777,333,222,111,5020,284]

listaDeAmigos::[Integer]->[(Integer,Integer)]
listaDeAmigos (x:[]) = []
listaDeAmigos (x:xs) = generarTuplaAmigos x xs ++ listaDeAmigos xs