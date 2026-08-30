sumaTroll::Integer->Integer->Integer
sumaTroll base exponente = base ^ exponente

sumatoriaInterna::Integer->Integer->Integer->Integer
sumatoriaInterna m j base
        | m+1 <= j = 0
        | otherwise = (sumaTroll base j) + sumatoriaInterna m (j+1) base

sumatoriaExterna::Integer->Integer->Integer->Integer->Integer
sumatoriaExterna n i m j
        | n+1 <= i = 0
        | otherwise = (sumatoriaInterna m j i) + (sumatoriaExterna n (i+1) m j)

sumaFinal::Integer->Integer->Integer
sumaFinal n m = sumatoriaExterna n 1 m 1