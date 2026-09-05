-- TestsEjercicio2.hs
import Test.HUnit ( (~:), (~?=), runTestTTAndExit, Test(TestList) )
import Ejercicio_2 (quitarTodos, eliminarRepetidos, mismosElementos,capicua) 
import Test.HUnit (Test (TestList))
import Text.Read (Lexeme(String))

testsQuitarTodos :: Test
testsQuitarTodos = TestList
  [ "lista vacía"        ~: quitarTodos 10 []        ~?= ([])
  , "no aparece"         ~: quitarTodos 10 [1,2,3]   ~?= [1,2,3]
  , "aparece una vez"     ~: quitarTodos 2 [1,2,3]    ~?= [1,3]
  , "aparece repetido"   ~: quitarTodos 1 [1,1,1]    ~?= ([])
  , "consecutivos"       ~: quitarTodos 1 [1,1,2,1]  ~?= [2]
  ]

testEliminarRepetidos :: Test
testEliminarRepetidos = TestList
  [
    "lista vacia" ~: eliminarRepetidos [] ~?= ([]::[String]),
    "no aparece" ~: eliminarRepetidos [1,2,3] ~?= ([1,2,3]),
    "aparece al principio" ~: eliminarRepetidos [10,10,11,12] ~?= ([10,11,12]::[Integer]),
    "aparece al final" ~: eliminarRepetidos [11,12,13,10,10] ~?= ([11,12,13,10]::[Integer]),
    "eliminar consecutivos" ~: eliminarRepetidos [1,2,1,3,1] ~?= ([1,2,3])
  ]

testMismosElementos :: Test
testMismosElementos  = TestList
  [
    "ambas vacias" ~: mismosElementos ([] :: [Integer]) [] ~?= (True),
    "una vacia" ~: mismosElementos [] [1,2,3,4] ~?= (False),
    "elementos random" ~: mismosElementos [1,1,1,1,1,1,1,1,1] [1,2,3,4] ~?= (False),
    "mismos elementos" ~: mismosElementos [1,2,3,4,5,6] [1,2,3,4,5,6] ~?= (True) 
  ]

testCapicua :: Test
testCapicua = TestList
  [ "vacía"                  ~: capicua ([] :: [Integer])   ~?= True
  , "un elemento"            ~: capicua [1]                 ~?= True
  , "dos iguales"            ~: capicua [7,7]               ~?= True
  , "dos distintos"          ~: capicua [7,8]               ~?= False
  , "impar capicúa"          ~: capicua [1,2,3,2,1]         ~?= True
  , "par capicúa"            ~: capicua [1,2,2,1]           ~?= True
  , "impar no capicúa"       ~: capicua [1,2,3,4,5]         ~?= False
  , "difieren solo el medio" ~: capicua [1,2,9,2,1]         ~?= True
  , "difieren solo extremos" ~: capicua [1,2,3,2,9]         ~?= False
  , "todos iguales"          ~: capicua [5,5,5,5]           ~?= True
  , "casi capicúa"           ~: capicua [1,2,3,3,2,9]       ~?= False
  , "strings"                ~: capicua "neuquen"           ~?= True
  , "string no capicúa"      ~: capicua "haskell"           ~?= False
  ]

todosLosTests :: Test
todosLosTests = TestList
  [ "quitarTodos"        ~: testsQuitarTodos,
   "eliminarRepetidos"  ~: testEliminarRepetidos,
   "mismosElementos" ~: testMismosElementos,
   "capicua" ~: testCapicua
  ]

main :: IO ()
main = runTestTTAndExit todosLosTests