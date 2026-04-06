module UtilsPork where

signo :: Integer -> Integer
signo n| n == 0 = 0
    | n >= 1 = 1
    | otherwise = -1
    

absoluto :: Integer -> Integer
absoluto x = signo x * x