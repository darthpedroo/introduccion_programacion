-- Definitions
f :: Integer -> Integer
f 1 = 8
f 4 = 131
f 16 = 16

g :: Integer -> Integer
g 8 = 16
g 16 = 4
g 131 = 1

h :: Integer -> Integer 
h 8  = f(g 8)
h 16  = f(g 16)
h 131  = f(g 131 )

k :: Integer -> Integer 
k 1  = g(f 1)
k 4  = g(f 4)
k 16  = g(f 16 )


-- También se puede hacer con composición desde la terminal con $
-- ejemplo: f $ g 8 == f(g 8)


