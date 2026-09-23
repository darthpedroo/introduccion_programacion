import Test.HUnit ( (~:), (~?=), runTestTTAndExit, Test(TestList) )
import Parcial_Matrices (maximo,valoresDeCamino,esCaminoFibo)

testMaximo :: Test
testMaximo = TestList
  [ "una sola celda"               ~: maximo [[5]]                          ~?= 5
  , "una fila"                     ~: maximo [[3,8,2,6]]                    ~?= 8
  , "una columna"                  ~: maximo [[4],[9],[1]]                  ~?= 9
  , "máximo en la primera fila"    ~: maximo [[9,2],[3,4],[5,6]]            ~?= 9
  , "máximo en la última fila"     ~: maximo [[1,2],[3,4],[5,10]]           ~?= 10
  , "máximo en una fila del medio" ~: maximo [[1,2],[30,4],[5,6]]           ~?= 30
  , "máximo en la primera columna" ~: maximo [[1,2,3],[15,5,6]]             ~?= 15
  , "máximo en la última columna"  ~: maximo [[1,2,3],[4,5,16]]             ~?= 16
  , "máximo repetido"              ~: maximo [[7,1],[2,7],[7,3]]            ~?= 7
  , "todos iguales"                ~: maximo [[4,4,4],[4,4,4]]              ~?= 4
  , "tablero cuadrado 3x3"         ~: maximo [[1,2,3],[4,5,6],[7,8,9]]      ~?= 9
  , "máximo en esquina superior"   ~: maximo [[99,2,3],[4,5,6],[7,8,9]]     ~?= 99
  , "máximo en el centro"          ~: maximo [[1,2,3],[4,50,6],[7,8,9]]     ~?= 50
  , "números grandes"              ~: maximo [[1000,999],[1001,998]]        ~?= 1001
  ]

testValoresDeCamino :: Test
testValoresDeCamino = TestList
  [ "una sola celda"             ~: valoresDeCamino [[5]] [(1,1)]                 ~?= [5]
  , "recorre la primera fila"    ~: valoresDeCamino t3 [(1,1),(1,2),(1,3)]         ~?= [1,2,3]
  , "recorre la primera columna" ~: valoresDeCamino t3 [(1,1),(2,1),(3,1)]         ~?= [1,4,7]
  , "zigzag hasta la esquina"    ~: valoresDeCamino t3 [(1,1),(1,2),(2,2),(2,3),(3,3)] ~?= [1,2,5,6,9]
  , "no empieza en (1,1)"        ~: valoresDeCamino t3 [(2,2),(3,2)]               ~?= [5,8]
  , "una posición del medio"     ~: valoresDeCamino t3 [(2,3)]                     ~?= [6]
  , "tablero no cuadrado"        ~: valoresDeCamino [[1,2],[3,4],[5,6]] [(1,2),(2,2),(3,2)] ~?= [2,4,6]
  , "valores repetidos"          ~: valoresDeCamino [[7,7],[7,7]] [(1,1),(1,2),(2,2)] ~?= [7,7,7]
  ]
  where
    t3 = [[1,2,3],[4,5,6],[7,8,9]]
  
testEsCaminoFibo :: Test
testEsCaminoFibo = TestList
  [ "ejemplo del enunciado"      ~: esCaminoFibo [1,1,2,3,5] 1 ~?= True
  , "empieza en i = 3"           ~: esCaminoFibo [2,3,5] 3     ~?= True
  , "un solo elemento correcto"  ~: esCaminoFibo [3] 4         ~?= True
  , "un solo elemento incorrecto"~: esCaminoFibo [4] 4         ~?= False
  , "índice inicial equivocado"  ~: esCaminoFibo [2,3,5] 1     ~?= False
  , "falla en el medio"          ~: esCaminoFibo [1,2,3] 1     ~?= False
  , "falla en el último"         ~: esCaminoFibo [5,8,14] 5    ~?= False
  , "i = 0 siempre da False"     ~: esCaminoFibo [1,1] 0       ~?= False
  ]

todosLosTests :: Test
todosLosTests = TestList
  [ "maximo"          ~: testMaximo,
  "valoresDeCamino" ~: testValoresDeCamino,
  "caminoFibo" ~: testEsCaminoFibo
  ]

main :: IO ()
main = runTestTTAndExit todosLosTests