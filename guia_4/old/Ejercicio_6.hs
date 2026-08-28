digitoUnidades:: Integer -> Integer
digitoUnidades n1 = mod n1 10

digitoDecenas:: Integer -> Integer
digitoDecenas n1 =  div (mod n1 100 - mod n1 10)  10

sonDosDigitosIguales:: Integer -> Integer -> Bool
sonDosDigitosIguales 0 n2 = True
sonDosDigitosIguales n1 n2 = n1 == n2 

todosDigitosIguales:: Integer -> Bool
todosDigitosIguales n 
    | n == 0 = True
    | sonDosDigitosIguales (digitoDecenas n) (digitoUnidades n) == False = False
    | otherwise = todosDigitosIguales (div (n - digitoDecenas n *10 - digitoUnidades n) 100)
