sumaInterna :: Integer -> Integer -> Integer -> Integer
sumaInterna base n m | m <= 0     = 0
                   | otherwise  = base ^ (n+m) + sumaInterna base (n) (m-1)

sumaFinal :: Integer -> Integer -> Integer -> Integer
sumaFinal base n m | n <= 0    = 0
              | otherwise = sumaInterna base n m + sumaFinal base (n - 1) m