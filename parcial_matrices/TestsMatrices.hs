import Test.HUnit ( (~:), (~?=), runTestTTAndExit, Test(TestList) )
import Parcial_Matrices (maximo)

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

todosLosTests :: Test
todosLosTests = TestList
  [ "maximo" ~: testMaximo
  ]

main :: IO ()
main = runTestTTAndExit todosLosTests