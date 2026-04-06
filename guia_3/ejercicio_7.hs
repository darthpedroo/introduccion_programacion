{-
Ejercicio 7)
Implementar la funcion:
distanciaManhattan:: (Float, Float, Float) -> (Float, Float, Float) -> Float
-}

distanciaManhattan:: (Float, Float,Float) -> (Float,Float,Float) -> Float
distanciaManhattan (x1, x2, x3) (y1, y2, y3) = sqrt ((x1 - y1)**2) + sqrt ((x2 - y2)**2) + sqrt ((x3 - y3)**2) 

type Punto3D = (Float,Float,Float)

distanciaManhattanPunto3D:: Punto3D -> Punto3D -> Float
distanciaManhattanPunto3D (x1, y1, z1) (x2, y2, z2) = sqrt ((x1 - x2)**2) + sqrt ((y1 - y2)**2) + sqrt ((z1 - z2)**2)
