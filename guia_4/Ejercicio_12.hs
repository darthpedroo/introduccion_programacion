sucesionCool::Integer->Float
sucesionCool 1 = 2
sucesionCool n = 2 + (1 / sucesionCool (n -1))

raizDe2Aprox::Integer->Float
raizDe2Aprox n = (sucesionCool n) - 1