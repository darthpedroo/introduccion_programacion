import Test.HUnit
import SolucionT1

main = runTestTT tests

tests = test [
    "Rango que incluye varios abundantes" ~: f1 12 24 ~?= 4,

    -- CURSADA
    "lista vacia" ~: f2 [] ~?= [],
    "Cursada ejemplo tito" ~: f2 [("Algoritmos y Estructuras de Datos I", 2020, 2), ("Algoritmos y Estructuras de Datos II", 2022, 1)] ~?= ["Algoritmos y Estructuras de Datos I"],
    "todas vencidas" ~: f2 [("A1", 1993, 1), ("A12", 1993, 2),("A13", 1993, 1),("A14", 1993, 1),("A15", 1993, 1)] ~?= ["A1","A12","A13","A14","A15"],
    "ninguna vencida" ~: f2 [("A1", 2067, 1), ("A12", 2067, 2),("vamo pincha", 2021, 2),("A14", 2021, 2),("A15", 2021, 2)] ~?= [],
    "miti miti" ~: f2 [("A1", 2067, 1), ("A12", 2067, 2),("vamo pincha", 2021, 2),("A14", 2021, 2),("A15", 2021, 1),("RACING", 2000, 2),("CABJ", 2007, 2)] ~?= ["A15","RACING","CABJ"],
    "REPETIDOS" ~: f2 [("A1", 2000, 1), ("A1", 2006, 2),("A1", 2005, 1)] ~?= ["A1"],

    -- EJERCICIO 3

    "lista vacia" ~: f3 [] 67 ~?= [],
    "ejemplo base" ~: f3 [3,8,5,0,7,-2,4] 5 ~?= [3,5,5,0,5],
    "empieza en negativo" ~: f3 [-2,1,1,1,1,1,1,1,1] 67 ~?= [],
    "UNO!" ~: f3 [1,2,3,4,5,6,7] 1 ~?= [1,1,1,1,1,1,1],
    "BIG INT!" ~: f3 [1,2,3,4,5,6,7] (2^64) ~?= [1,2,3,4,5,6,7],
    "TERMINA EN NEGATIVO ASI Q NO PASA NADA!" ~: f3 [1,2,3,4,0,6,7,-2,-100] (2^64) ~?= [1,2,3,4,0
    ,6,7],

    -- EJERCICIO 4

    "lista vacia" ~: f4 [] 10 ~?= 0,
    "ejemplo base" ~: f4 [[-9,8,2,3],[2,7,-5,3],[-1,0,5,6]] 2 ~?= 2,
    "todos pares" ~: f4 [[0],[0],[0],[0]] 1 ~?= 4,
    "todos impares" ~: f4 [[0,1],[0,1],[0,1],[0,1]] 2 ~?= 0

    ]
    
