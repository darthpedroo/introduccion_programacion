sumaInterna :: Integer -> Integer -> Float
sumaInterna n m | m <= 0     = 0
                   | otherwise  = (fromInteger m / fromInteger n) + sumaInterna (n) (m-1)

sumaFinal :: Integer ->  Integer -> Float
sumaFinal n m | n <= 0    = 0
              | otherwise = sumaInterna  n m + sumaFinal  (n - 1) m