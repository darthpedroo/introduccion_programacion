-- Absoluto 
-- calcula el valor absoluto de un número entero

-- Problema absoluto(n:Z):Z {
-- require : True 
-- asegura: {(n≥0⟹res=n)∧(n<0⟹res=−n) }
--}


signo :: Integer -> Integer
signo n| n == 0 = 0
    | n >= 1 = 1
    | otherwise = -1
    

absoluto :: Integer -> Integer
absoluto x = signo x * x

-- b) maximoAbsoluto 
-- devuelve el máximo entre el valor absoluto de dos números enteros.

-- ProblemaMaximoAbsoluto (n1: Z, n2:Z) :Z{
-- requiere: {res = n1 or res = n2}
-- asegura: { if absoluto(n1) >= absoluto(n2) then n1 else n2 }}

maximoAbsoluto:: Integer -> Integer -> Integer 
maximoAbsoluto n1 n2 | absoluto n1 >= absoluto n2 = n1
    | otherwise = n2

-- c) maximo3: devuelve el máximo entre tres números enteros.

-- ProblemaMaximo3 (n1: Z, n2: Z, n3:Z): Z{
-- require: {True} 
-- asegura: { res >= a ∧ res >= b ∧ res >= c }

maximo3:: Integer -> Integer -> Integer -> Integer
maximo3 n1 n2 n3 | n1 >= n2 && n1 >= n3 = n1
                 | n2 >= n1 && n2 >= n3 = n2
                 | otherwise = n3

-- d) algunoEsCero
-- dados dos numeros racionales, decide si alguno es igual a 0 
-- (resolverlo con y sin pattern matching).

-- Problema algunoEsCero (n1: Q, n2: Q) : Bool{
-- require: {True} 
-- asegura: { res = (n1 == 0 or n2 == 0) }

-- Sin Pattern Matching
algunoEsCero:: Integer -> Integer -> Bool
algunoEsCero n1 n2 
    | n1 == 0 = True
    | n2 == 0 = True
    | otherwise = False

-- Con Pattern Matching
algunoEsCeroPatternMatching:: Integer -> Integer -> Bool
algunoEsCeroPatternMatching 0 n2 = True
algunoEsCeroPatternMatching n1 0 = True 
algunoEsCeroPatternMatching n1 n2 = False 

-- e) ambosSonCero:
-- dados dos n ́umeros racionales, decide si ambos son iguales a 0 
-- (resolverlo con y sin pattern matching).

-- Problema algunoEsCero (n1: Q, n2: Q) : Bool{
-- require: {True} 
-- asegura: { res = (n1 == 0 and n2 == 0) }

-- Sin Pattern Matching
ambosSonCero:: Integer -> Integer -> Bool
ambosSonCero n1 n2 
    | n1 == 0 && n2 == 0 = True
    | otherwise = False

-- Con PatternMatching
ambosSonCeroPatternMatching:: Integer -> Integer -> Bool
ambosSonCeroPatternMatching 0 0 = True
ambosSonCeroPatternMatching n1 n2 = False

{-
CONSIGNA:
f) esMismoIntervalo

dados dos números reales, indica si estan relacionados por la 
relacion de equivalencia en R cuyas
clases de equivalencia son: (−∞, 3],(3, 7] y (7, ∞),
o dicho de otra manera, si pertenecen al mismo intervalo.

ESPECIFICACIÓN:

Problema esMismoIntervalo(n1: R, n2: R): Bool {

    require:{True}
    asegura: {res = True <-> (n1 <= 3 && n2 <= 3) || ((n1 > 3 && n1 <= 7) && (n2 > 3 && n2 <= 7)) || (n1 > 7 && n2 > 7) }
}

-}

esMismoIntervalo:: Float -> Float -> Bool
esMismoIntervalo n1 n2 
    | n1 <= 3 && n2 <= 3 = True
    | (n1 > 3 && n1 <= 7) && (n2 > 3 && n2 <= 7) = True
    | n1 > 7 && n2 > 7 = True
    | otherwise = False

{-
g) sumaDistintos: que dados tres numeros enteros calcule 
la suma sin sumar repetidos (si los hubiera).
-}

sumarDistinto:: Integer -> Integer -> Integer
sumarDistinto n1 n2 
    | n1 == n2 = n1
    | otherwise = n1 +n2

sumaDistintos:: Integer -> Integer -> Integer -> Integer
sumaDistintos n1 n2 n3 
    |n1 /= n3 && n2 /= n3 = sumarDistinto n1 n2 + n3
    |otherwise = sumarDistinto n1 n2

{-
h) esMultiploDe
dados dos números naturales, decide si el primero es múltiplo del segundo
-}

esMultiploDe:: Integer -> Integer -> Bool
esMultiploDe n1 n2 = mod n2 n1 == 0

digitoUnidades:: Integer -> Integer
digitoUnidades n1 = mod n1 10

digitoDecenas:: Integer -> Integer
digitoDecenas n1 =  div (mod n1 100 - mod n1 10)  10