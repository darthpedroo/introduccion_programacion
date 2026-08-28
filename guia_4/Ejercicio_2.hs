parteEntera :: Float -> Integer
parteEntera x
  | x < 1     = 0
  | otherwise = 1 + parteEntera (x - 1)

{-- 
básicamente lo que hago aca es fijarme en el caso base si es menor a 1, entonces sumo 0 de una.

luego, si x no es menor a 1 , llamo recursivamente a parteEntera.  Esto me va sumando de A UN VALOR hasta que llegamos al caso base. 

El problema es que si busco la parte entera de 

--}