-- TestsEjercicio2.hs
import Test.HUnit ( (~:), (~?=), runTestTTAndExit, Test(TestList) )
import Ejercicio_3 (sumatoria, productoria,maximo,sumarN,pares, minimo, ordenar,multiplosDeN)  
import Test.HUnit (Test (TestList))

testSumatoria :: Test
testSumatoria = TestList
  [ "lista vacía"        ~: sumatoria [] ~?= (0),
   "suma gauss"        ~: sumatoria [1..100] ~?= (5050)
    ]

testProductoria :: Test
testProductoria = TestList
 [
    "lista vacia" ~: productoria [] ~?= (1),
    "factorial 5" ~: productoria [1..5] ~?= (120)
 ]

testMaximo :: Test
testMaximo = TestList
    [
        "un elemento" ~: maximo [1] ~?= (1),
        "todos iguales" ~: maximo [1,1,1,1,1] ~?= (1),
        "todos negativos" ~: maximo [-1,-2,-3,-4,-5,8000000,-6,-7,-1000] ~?= (8000000),
        "el primero es maximo" ~: maximo [8989,-1,-2,-3,-4,-5,-6,-7,-1000] ~?= (8989),
        "el ultimo es maximo" ~: maximo [-1,-2,-3,-4,-5,-6,-7,-1000,1000] ~?= (1000)
    ]

testMinimo :: Test
testMinimo = TestList
    [
        "un elemento" ~: minimo [1] ~?= (1),
        "todos iguales" ~: minimo [1,1,1,1,1] ~?= (1),
        "todos negativos" ~: minimo [-1,-2,-3,-4,-5,-6,-7,-1000] ~?= (-1000),
        "el primero es minimo" ~: minimo [-1000,8989,-1,-2,-3,-4,-5,-6,-7] ~?= (-1000),
        "el ultimo es minimo" ~: minimo [-1,-2,-3,-4,-5,-6,-7,-1000,1000,-1000000] ~?= (-1000000)
    ]

testSumarN :: Test
testSumarN = TestList
    [
        "lista vacia" ~: sumarN 0 [] ~?= ([]),
        "sumar 0" ~: sumarN 0 [1,2,3,4,5] ~?= ([1,2,3,4,5]),
        "sumar 20" ~: sumarN 20 [1,2,3,4,5] ~?= ([21,22,23,24,25]),
        "sumar -10" ~: sumarN (-10) [10,10,10,10] ~?= ([0,0,0,0])
    ]

testPares :: Test
testPares = TestList
    [
        "lista vacia" ~: pares [] ~?= ([]),
        "todos pares" ~: pares [0,2,4,6,8,10] ~?= ([0,2,4,6,8,10]),
        "todos impares" ~: pares [1,3,357585,97,77,33] ~?= ([]),
        "algunos pares y algunos impares" ~: pares [1,2,3,5,8,2] ~?= ([2,8,2])
    ]

testOrdenar :: Test
testOrdenar = TestList
    [
        "lista vacia" ~: ordenar [] ~?= ([]),
        "ordenado sin repetidos" ~: ordenar [1,2,3,4] ~?= ([1,2,3,4]),
        "repetidos ordenados" ~: ordenar [1,1,1,2,2,2,3,3,4,5,6,7,8,1000,1333] ~?= ([1,1,1,2,2,2,3,3,4,5,6,7,8,1000,1333]),
        "desordenado" ~: ordenar [10,-1,2,1000,13,-15,-13,88888] ~?= ([-15,-13,-1,2,10,13,1000,88888]),
        "desordenado con repetidos" ~: ordenar [88888, 10,-2, 10,2,1000,13,-15,-13,88888,88888] ~?= ([-15,-13,-2,2,10,10,13,1000,88888,88888,88888])
    ]

testsMultiplosDeN :: Test
testsMultiplosDeN = TestList
  [ "lista vacía"          ~: multiplosDeN 3 []               ~?= []
  , "ninguno cumple"       ~: multiplosDeN 5 [1,2,3,4]        ~?= []
  , "todos cumplen"        ~: multiplosDeN 2 [2,4,6,8]        ~?= [2,4,6,8]
  , "algunos cumplen"      ~: multiplosDeN 3 [1,3,5,6,9,10]   ~?= [3,6,9]
  , "conserva el orden"    ~: multiplosDeN 2 [7,4,9,2,8]      ~?= [4,2,8]
  , "conserva repetidos"   ~: multiplosDeN 3 [3,3,4,3]        ~?= [3,3,3]
  , "el cero es múltiplo"  ~: multiplosDeN 7 [0,1,7]          ~?= [0,7]
  , "n = 1 devuelve todo"  ~: multiplosDeN 1 [4,-9,0,17]      ~?= [4,-9,0,17]
  , "múltiplos negativos"  ~: multiplosDeN 3 [-6,-4,-3,5]     ~?= [-6,-3]
  , "n negativo"           ~: multiplosDeN (-3) [3,4,6]       ~?= [3,6]
  , "el primero cumple"    ~: multiplosDeN 5 [5,1,2]          ~?= [5]
  , "el último cumple"     ~: multiplosDeN 5 [1,2,5]          ~?= [5]
  ]

todosLosTests :: Test
todosLosTests = TestList
  [ "sumatoria"    ~: testSumatoria,
    "productoria" ~: testProductoria,
    "maximo" ~: testMaximo,
    "minimo"~: testMinimo,
    "sumarN" ~: testSumarN,
    "pares" ~: testPares,
    "multiplosDeN" ~: testsMultiplosDeN,
    "ordenar" ~: testOrdenar
    
  ]

main :: IO ()
main = runTestTTAndExit todosLosTests