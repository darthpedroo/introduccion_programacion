
fibonacci :: Integer -> Integer
fibonacci 1 = 1
fibonacci 0 = 0 
fibonacci n = fibonacci(n-1) + fibonacci(n-2)
