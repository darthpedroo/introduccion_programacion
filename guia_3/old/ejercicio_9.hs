{-
Ejercicio 9.
A partir de las siguientes implementaciones en Haskell, 
describir en lenguaje natural qu ́e hacen y especificarlas.
-}



--9a La funcion "f1" toma una variable Float y devuelve un "1" si esa variable n vale 0, en cualquier otro caso devuelve un "0"

--9b La funcion "f2" toma una variable Float y devuelve un "15" si esa variable n vale 1, y si n vale -1 devuelve un "-15"

--9c La funcion "f3" toma una variable Float n y devuelve otro Float, especificamente si n es menor o igual a 9 devuelve un "7", y si n es mayor o igual a 3 devuelve un "5", de todas formas como Haskell ejecuta de arriba hacia abajo si n valiese 6 cumple primero con ser menor que 9 por lo que devuelve 7 por mas que tambien cumpla la condicion de mayor a 3.

--9d La funcion "f4" toma dos variables float x y devolviendo siempre la sumatoria entre ambas divididas por 2, osea su promedio

--9e La funcion "f5" hace lo mismo que la anterior pero tomando un par ordenado de floats (x,y), y devuelta devolviendo la suma entre ambos elementos de la tupla divididos por 2, osea su promedio

--9f La funcion "f6" toma una varibale a siendo esta un Float, y la devuelve como numero entero, si esta es igual a la variable entera de b devuelve un True, en otro caso devuelve un False