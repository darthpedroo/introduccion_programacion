sumaInterna::Integer->Integer->Integer->Float
sumaInterna q p m 
    | q == m = fromInteger p /fromInteger q
    | otherwise = fromInteger p / fromInteger q + sumaInterna (q+1) p m

sumaExterna::Integer->Integer->Integer->Integer->Float
sumaExterna p q n m
    | p == n = sumaInterna q p m
    | otherwise = sumaInterna q p m + sumaExterna (p+1) q n m


sumaRacionalesAux::Integer->Integer->Integer->Integer->Float
sumaRacionalesAux p q n m = sumaExterna p q n m

sumaRacionales::Integer->Integer->Float
sumaRacionales n m = sumaRacionalesAux 1 1 n m
