{-
Ejercicio 5
Implementar la función
todosMenores :: (Integer, Integer, Integer) -> Bool

problema todosMenores (t : Z×Z×Z) : Bool {
requiere: {T rue}
asegura: {(res = true) ↔((f (t0) > g(t0)) ∧(f (t1) > g(t1)) ∧(f (t2) > g(t2)))}
}

problema f (n : Z) : Z{
requiere: {T rue}
asegura: {(n ≤7 →res = n2) ∧(n > 7 →res = 2n −1)}
}

problema g (n : Z) : Z{
requiere: {T rue}
asegura: {Si n es un n ́umero par entonces res = n/2, en caso contrario, res = 3n + 1}
}
-}

todosMenores:: (Integer, Integer, Integer) -> Bool 
todosMenores (n1,n2,n3) = (f n1 > g n1) && (f n2 > g n2) && (f n3 > g n3)

f :: Integer -> Integer
f n1 
    |n1 <= 7 = n1 * n1
    |n1 > 7 = 2*n1 -1 

g :: Integer -> Integer
g n 
    | mod n 2 == 0 = div n 2
    | otherwise = 3*n +1
