sumaInterna :: Integer -> Integer -> Integer
sumaInterna base m | m <= 0     = 0
                   | otherwise  = base ^ m + sumaInterna base (m - 1)

sumaFinal :: Integer -> Integer -> Integer
sumaFinal n m | n <= 0    = 0
              | otherwise = sumaInterna n m + sumaFinal (n - 1) m

{--la gracia de este ejercicio es que uno estaria tentado a sumar incrementalmente, sin embargo se puede sumar al reves e ir restando, de esta manera nos ahorramos un montón de parametros que actúan como variables.--}