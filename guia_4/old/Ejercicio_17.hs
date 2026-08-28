fibonacci:: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n - 1) + fibonacci (n - 2)

esFibonacciAux::Integer->Integer->Bool
esFibonacciAux n i 
    | n < fibonacci i = False
    | n == fibonacci i = True
    | otherwise = esFibonacciAux n (i+1)

esFibonacci::Integer->Bool
esFibonacci n = esFibonacciAux n 1
