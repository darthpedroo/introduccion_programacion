import Test.HUnit ( (~:), (~?=), runTestTTAndExit, Test(TestList) )
import Parcial_Perfectos_Amigos (divisoresPropios,sonAmigos,listaDeAmigos)

testDivisoresPropios :: Test
testDivisoresPropios = TestList
  [ "1"               ~: divisoresPropios 1 ~?= [],
    "Numero primo" ~: divisoresPropios 13 ~?= [1],
    "Ejemplo consigna" ~: divisoresPropios 6 ~?= [1,2,3],
    "Ejemplo consigna 220" ~: divisoresPropios 220 ~?= [1,2,4,5,10,11,20,22,44,55,110],
    "Ejemplo consigna 284" ~: divisoresPropios 284 ~?= [1,2,4,71,142]
  ]

testSonAmigos:: Test
testSonAmigos = TestList [
    "Son Amigos consigna" ~: sonAmigos 284 220 ~?= True,
    "No Son Amigos Big" ~: sonAmigos 284 15 ~?= False,
    "Jeje" ~: sonAmigos 1 300 ~?= False
    ]

testListaDeAmigos::Test
testListaDeAmigos = TestList [
    "Lista con 2 amigos" ~: listaDeAmigos [220,284] ~?= [(220,284)],
    "Lista larga" ~: listaDeAmigos [220,1184,5564,1210,999,666,777,333,222,111,5020,284] ~?= [(220,284),(1184,1210),(5564,5020)],
    "0 AMIGOS " ~: listaDeAmigos [1..100] ~?= []
    ]

todosLosTests :: Test
todosLosTests = TestList
  [ "testDivisoresPropios" ~: testDivisoresPropios,
  "testSonAmigos" ~: testSonAmigos,
  testListaDeAmigos
  ]

main :: IO ()
main = runTestTTAndExit todosLosTests