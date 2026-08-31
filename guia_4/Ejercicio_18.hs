digitoUnidades:: Integer -> Integer
digitoUnidades n1 = mod n1 10

digitoDecenas:: Integer -> Integer
digitoDecenas n1 =  div (mod n1 100 - mod n1 10)  10

sacarUnidades::Integer->Integer
sacarUnidades n = div n 10


mayorDigitoParAux::Integer->Integer->Integer
mayorDigitoParAux n digit 
    | (n == 0) && (digit == -1) = 0
    | (n == 0) && (digit /= -1) = digit
    | ((mod (digitoUnidades n) 2) == 0) && (digitoUnidades n > digit) = mayorDigitoParAux (sacarUnidades n) (digitoUnidades n) 
    | otherwise = mayorDigitoParAux (sacarUnidades n) digit

mayorDigitoPar::Integer->Integer
mayorDigitoPar n = mayorDigitoParAux n (-1)