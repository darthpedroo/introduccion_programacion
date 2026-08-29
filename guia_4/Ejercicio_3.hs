esDivisible::Integer->Integer->Bool
esDivisible x y | x == 0 = True
                | x <= 0 = False
                | otherwise = esDivisible (x-y) y