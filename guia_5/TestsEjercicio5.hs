import Test.HUnit ( (~:), (~?=), runTestTTAndExit, Test(TestList) )
import Test.HUnit (Test (TestList))


todosLosTests :: Test
todosLosTests = TestList
  [ "sumatoria"    ~: testSacarBlancosRepetidos,
  ]

main :: IO ()
main = runTestTTAndExit todosLosTests