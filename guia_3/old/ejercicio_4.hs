
productoIntero:: (Integer, Integer) -> (Integer, Integer) -> Integer
productoIntero n1 n2 = fst n1 * fst n2 + snd n1 * snd n2

esParMenor:: (Integer, Integer) -> (Integer, Integer) -> (Bool, Bool)
esParMenor n1 n2 = (fst n1 < fst n2, snd n1 < snd n2) 

distancia :: (Float, Float) -> (Float, Float) -> Float
distancia (a,b) (c,d) = sqrt ((c - a)**2 + (d - b)**2)

sumaTerna:: (Integer, Integer, Integer) -> Integer
sumaTerna (n1,n2,n3) = n1 + n2 + n3


sumarSoloMultiplos :: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos (a, b, c) d = valA + valB + valC
  where
    valA | mod a d == 0 = a
         | otherwise    = 0
    valB | mod b d == 0 = b
         | otherwise    = 0
    valC | mod c d == 0 = c
         | otherwise    = 0

{-
f)posPrimerPar
dada una terna de enteros, devuelve la posici ́on del primer n ́umero par si es que hay alguno, o devuelve
4 si son todos impares
-}

posPrimerPar:: (Int,Int,Int) -> Integer
posPrimerPar (a,b,c)  
    | mod a 2 == 0 = 0
    | mod b 2 == 0 = 1
    | mod c 2 == 0 = 2
    | otherwise = 4

{-
g)crearPar :: a -> b -> (a, b)
a partir de dos componentes, crea un par con esos valores. Debe funcionar para ele-
mentos de cualquier tipo
-}

crearPar:: a -> b -> (a,b)
crearPar a b = (a,b)

{-
h)invertir :: (a, b) -> (b, a): invierte los elementos del par pasado como par ́ametro. Debe funcionar para elementos
de cualquier tipo
-}

invertir :: (a, b) -> (b, a)
invertir (a,b) = (b,a)

{-
i) Reescribir los ejercicios productoInterno, esParMenor y distancia usando el siguiente renombre de tipos:
type Punto2D = (Float, Float)
-}

type Punto2D = (Float, Float)

productoIntero2D:: Punto2D -> Punto2D -> Float
productoIntero2D n1 n2 = fst n1 * fst n2 + snd n1 * snd n2