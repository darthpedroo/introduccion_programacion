
import Test.HUnit ( (~:), (~?=), runTestTTAndExit, Test(TestList) )
import Test.HUnit (Test (TestList))
import Ejercicio_5 (sumaAcumulada)

testSumaAcumulada :: Test
testSumaAcumulada = TestList
    [ "lista vacia" ~: sumaAcumulada [] ~?= [],

    "un unico elemento" ~: sumaAcumulada [5] ~?= [5],

    "dos elementos" ~: sumaAcumulada [1,2] ~?= [1,3],

    "el ejemplo del enunciado" ~: sumaAcumulada [1,2,3,4,5] ~?= [1,3,6,10,15],

    "varios elementos iguales" ~: sumaAcumulada [2,2,2,2] ~?= [2,4,6,8],

    "elementos crecientes" ~: sumaAcumulada [1,1,1,1,1] ~?= [1,2,3,4,5],

    "un solo elemento grande" ~: sumaAcumulada [100] ~?= [100],

    "tres elementos" ~: sumaAcumulada [3,1,4] ~?= [3,4,8]
    ]

todosLosTests :: Test
todosLosTests = TestList
  [ "testSumaAcumulada"    ~: testSumaAcumulada
  ]

main :: IO ()
main = runTestTTAndExit todosLosTests