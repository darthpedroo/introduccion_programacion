import Test.HUnit ( (~:), (~?=), runTestTTAndExit, Test(TestList) )
import Ejercicio_3 (sumatoria, productoria,maximo,sumarN,pares, minimo, ordenar,multiplosDeN)  
import Ejercicio_4 (sacarBlancosRepetidos,contarPalabras,palabras,palabraMasLarga,aplanar,aplanarConBlancos,aplanarConNBlancos)
import Test.HUnit (Test (TestList))

testSacarBlancosRepetidos :: Test
testSacarBlancosRepetidos = TestList
    [
        "lista vacia" ~: sacarBlancosRepetidos [] ~?= ([]),
        "no hay blancos repetidos" ~: sacarBlancosRepetidos "hoa" ~?= (['h', 'o', 'a']),
        "hay un solo blanco" ~: sacarBlancosRepetidos ['a','a',' ','a','a'] ~?= (['a','a',' ','a','a']),
        "hay varios blancos" ~: sacarBlancosRepetidos [' ',' ',' ','b','a','a',' ',' ',' ','1','2','3','4','5','6','7','8',' ',' ',' '] ~?= [' ','b','a','a',' ','1','2','3','4','5','6','7','8',' '],
        "todo blancos pares" ~: sacarBlancosRepetidos [' ',' ',' ',' '] ~?= [' '],
        "todo blancos impares" ~: sacarBlancosRepetidos [' ',' ',' ',' '] ~?= [' '],
        "un unico blanco" ~: sacarBlancosRepetidos [' '] ~?= [' '],
        "un unico caracter no blanco" ~: sacarBlancosRepetidos ['a'] ~?= ['a'],
        "blancos repetidos al principio" ~: sacarBlancosRepetidos [' ',' ',' ','a','b'] ~?= [' ','a','b'],
        "blancos repetidos al final" ~: sacarBlancosRepetidos ['a','b',' ',' ',' '] ~?= ['a','b',' '],
        "multiples bloques de blancos separados" ~: sacarBlancosRepetidos ['a',' ',' ','b',' ',' ',' ','c'] ~?= ['a',' ','b',' ','c']
    ]

testContarPalabras :: Test
testContarPalabras = TestList
    [ "lista vacia" ~: contarPalabras [] ~?= 0,
    "una sola palabra" ~: contarPalabras ['h','o','l','a'] ~?= 1,
    "dos palabras separadas por un blanco" ~: contarPalabras ['h','o','l','a',' ','c','h','a','u'] ~?= 2,
    "varias palabras separadas por un blanco" ~: contarPalabras ['a',' ','b',' ','c',' ','d'] ~?= 4,
    "palabras separadas por varios blancos seguidos" ~: contarPalabras ['a',' ',' ',' ','b'] ~?= 2,
    "blancos al principio" ~: contarPalabras [' ',' ','a','b'] ~?= 1,
    "blancos al final" ~: contarPalabras ['a','b',' ',' '] ~?= 1,
    "solo blancos" ~: contarPalabras [' ',' ',' '] ~?= 0,
    "un unico blanco" ~: contarPalabras [' '] ~?= 0,
    "un unico caracter no blanco" ~: contarPalabras ['a'] ~?= 1
    ]

testPalabras :: Test
testPalabras = TestList
    [ "lista vacia" ~: palabras [] ~?= [],

    "solo blancos" ~: palabras [' ',' ',' '] ~?= [],

    "un unico blanco" ~: palabras [' '] ~?= [],

    "una sola palabra" ~: palabras ['h','o','l','a'] ~?= [['h','o','l','a']],

    "un unico caracter" ~: palabras ['a'] ~?= [['a']],

    "dos palabras separadas por un blanco" ~: palabras ['h','o','l','a',' ','c','h','a','u'] ~?= [['h','o','l','a'],['c','h','a','u']],

    "varias palabras separadas por un blanco" ~: palabras ['a',' ','b',' ','c'] ~?= [['a'],['b'],['c']],

    "palabras separadas por varios blancos seguidos" ~: palabras ['a',' ',' ',' ','b'] ~?= [['a'],['b']],

    "blancos al principio" ~: palabras [' ',' ','a','b'] ~?= [['a','b']],

    "blancos al final" ~: palabras ['a','b',' ',' '] ~?= [['a','b']],

    "blancos al principio y al final" ~: palabras [' ',' ','a','b',' ',' '] ~?= [['a','b']],

    "varias palabras con blancos variados y bordes" ~: palabras [' ',' ','a',' ','b','b',' ',' ',' ','c'] ~?= [['a'],['b','b'],['c']]
    ]

testPalabraMasLarga :: Test
testPalabraMasLarga = TestList
    [ "lista vacia" ~: palabraMasLarga [] ~?= [],

    "un unico caracter" ~: palabraMasLarga ['a'] ~?= ['a'],

    "una sola palabra" ~: palabraMasLarga ['h','o','l','a'] ~?= ['h','o','l','a'],

    "dos palabras, la segunda mas larga" ~: palabraMasLarga ['h','o','l','a',' ','m','u','n','d','o'] ~?= ['m','u','n','d','o'],

    "dos palabras, la primera mas larga" ~: palabraMasLarga ['m','u','n','d','o',' ','h','o','l','a'] ~?= ['m','u','n','d','o'],

    "dos palabras de igual longitud" ~: palabraMasLarga ['h','o','l','a',' ','c','h','a','u'] ~?= ['h','o','l','a'],

    "varias palabras, la mas larga en el medio" ~: palabraMasLarga ['a',' ','b','b','b','b',' ','c','c'] ~?= ['b','b','b','b'],

    "varias palabras, la mas larga al final" ~: palabraMasLarga ['a',' ','b','b',' ','c','c','c','c'] ~?= ['c','c','c','c'],

    "varias palabras, la mas larga al principio" ~: palabraMasLarga ['a','a','a','a',' ','b','b',' ','c'] ~?= ['a','a','a','a'],

    "todas las palabras de igual longitud" ~: palabraMasLarga ['a','a',' ','b','b',' ','c','c'] ~?= ['a','a']
    ]

testAplanar :: Test
testAplanar = TestList
    [ "lista vacia" ~: aplanar [] ~?= [],

    "una sola palabra" ~: aplanar [['h','o','l','a']] ~?= ['h','o','l','a'],

    "dos palabras" ~: aplanar [['h','o','l','a'],['c','h','a','u']] ~?= ['h','o','l','a','c','h','a','u'],

    "varias palabras" ~: aplanar [['a'],['b','b'],['c','c','c']] ~?= ['a','b','b','c','c','c'],

    "incluye una palabra vacia en el medio" ~: aplanar [['a'],[],['b']] ~?= ['a','b'],

    "solo palabras vacias" ~: aplanar [[],[],[]] ~?= [],

    "un unico caracter" ~: aplanar [['a']] ~?= ['a'],

    "lista con una unica palabra vacia" ~: aplanar [[]] ~?= []
    ]

testAplanarConBlancos :: Test
testAplanarConBlancos = TestList
    [ "lista vacia" ~: aplanarConBlancos [] ~?= [],

    "una sola palabra" ~: aplanarConBlancos [['h','o','l','a']] ~?= ['h','o','l','a'],

    "dos palabras" ~: aplanarConBlancos [['h','o','l','a'],['c','h','a','u']] ~?= ['h','o','l','a',' ','c','h','a','u'],

    "varias palabras" ~: aplanarConBlancos [['a'],['b','b'],['c','c','c']] ~?= ['a',' ','b','b',' ','c','c','c'],

    "incluye una palabra vacia en el medio" ~: aplanarConBlancos [['a'],[],['b']] ~?= ['a',' ',' ','b'],

    "un unico caracter" ~: aplanarConBlancos [['a']] ~?= ['a'],

    "lista con una unica palabra vacia" ~: aplanarConBlancos [[]] ~?= []
    ]

testAplanarConNBlancos :: Test
testAplanarConNBlancos = TestList
    [ "lista vacia" ~: aplanarConNBlancos [] 3 ~?= [],

    "una sola palabra, no importa n" ~: aplanarConNBlancos [['h','o','l','a']] 5 ~?= ['h','o','l','a'],

    "dos palabras con n = 1" ~: aplanarConNBlancos [['a'],['b']] 1 ~?= ['a',' ','b'],

    "dos palabras con n = 2" ~: aplanarConNBlancos [['a'],['b']] 2 ~?= ['a',' ',' ','b'],

    "dos palabras con n = 3" ~: aplanarConNBlancos [['h','o','l','a'],['c','h','a','u']] 3 ~?= ['h','o','l','a',' ',' ',' ','c','h','a','u'],

    "varias palabras con n = 2" ~: aplanarConNBlancos [['a'],['b','b'],['c']] 2 ~?= ['a',' ',' ','b','b',' ',' ','c'],

    "n = 0, sin blancos entre palabras" ~: aplanarConNBlancos [['a'],['b'],['c']] 0 ~?= ['a','b','c'],

    "un unico caracter, no importa n" ~: aplanarConNBlancos [['a']] 4 ~?= ['a'],

    "lista con una unica palabra vacia" ~: aplanarConNBlancos [[]] 3 ~?= []
    ]


todosLosTests :: Test
todosLosTests = TestList
  [ "sacarBlancosRepetidos"    ~: testSacarBlancosRepetidos,
  "contarPalabras" ~: testContarPalabras,
  "palabraMasLarga" ~: testPalabraMasLarga,
  "aplanar" ~: testAplanar,
  "aplanarConBlancos" ~: testAplanarConBlancos,
  "aplanarConNBlancos" ~: testAplanarConNBlancos
  ]

main :: IO ()
main = runTestTTAndExit todosLosTests