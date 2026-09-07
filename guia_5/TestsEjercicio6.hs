import Test.HUnit ( (~:), (~?=), runTestTTAndExit, Test(TestList) )
import Test.HUnit (Test (TestList))
import Ejercicio_6 (enLosContactos, actualizarContacto,agregarContacto, eliminarContacto)

testEnLosContactos :: Test
testEnLosContactos = TestList
    [ "lista vacia" ~:
        enLosContactos "Pepe" []
        ~?= False,

      "no está en los contactos" ~:
        enLosContactos "Pepe"
          [("Juan", "1111111"),
           ("Pablo", "11111112"),
           ("Chicho", "11111116")]
        ~?= False,

      "esta como unico contacto" ~:
        enLosContactos "Pepe"
          [("Pepe", "1111111")]
        ~?= True,

      "esta al principio" ~:
        enLosContactos "Juan"
          [("Juan", "1111111"),
           ("Pablo", "11111112"),
           ("Chicho", "11111116")]
        ~?= True,

      "esta en el medio" ~:
        enLosContactos "Pablo"
          [("Juan", "1111111"),
           ("Pablo", "11111112"),
           ("Chicho", "11111116")]
        ~?= True,

      "esta al final" ~:
        enLosContactos "Chicho"
          [("Juan", "1111111"),
           ("Pablo", "11111112"),
           ("Chicho", "11111116")]
        ~?= True,

      "nombre igual pero telefono distinto" ~:
        enLosContactos "Pepe"
          [("Juan", "1111111"),
           ("Pepe", "2222222"),
           ("Pablo", "3333333")]
        ~?= True,

      "nombre parecido pero no igual" ~:
        enLosContactos "Pep"
          [("Pepe", "1111111"),
           ("Pablo", "2222222")]
        ~?= False,

      "mayusculas y minusculas" ~:
        enLosContactos "pepe"
          [("Pepe", "1111111")]
        ~?= False,

      "nombre repetido" ~:
        enLosContactos "Pepe"
          [("Juan", "1111111"),
           ("Pepe", "2222222"),
           ("Pepe", "3333333")]
        ~?= True,

      "varios contactos y esta uno" ~:
        enLosContactos "Chicho"
          [("Juan", "1111111"),
           ("Pablo", "2222222"),
           ("Pedro", "3333333"),
           ("Chicho", "4444444"),
           ("Maria", "5555555")]
        ~?= True
    ]

testActualizarContacto :: Test
testActualizarContacto = TestList
    [
        "lista vacia" ~:
            actualizarContacto ("Pedro","111") []
            ~?= [],

        "no estaba el contacto" ~:
            actualizarContacto ("Pedro","111")
                [("Pepe","11111")]
            ~?= [("Pepe","11111")],

        "actualizo el unico contacto" ~:
            actualizarContacto ("Pedro","111")
                [("Pedro","6767")]
            ~?= [("Pedro","111")],

        "actualizo el primer contacto" ~:
            actualizarContacto ("Pedro","111")
                [("Pedro","6767"), ("Pepe","222")]
            ~?= [("Pedro","111"), ("Pepe","222")],

        "actualizo el contacto del medio" ~:
            actualizarContacto ("Pedro","111")
                [("Pepe","222"), ("Pedro","6767"), ("Juan","333")]
            ~?= [("Pepe","222"), ("Pedro","111"), ("Juan","333")],

        "actualizo el ultimo contacto" ~:
            actualizarContacto ("Pedro","111")
                [("Pepe","222"), ("Juan","333"), ("Pedro","6767")]
            ~?= [("Pepe","222"), ("Juan","333"), ("Pedro","111")],

        "varios contactos y actualizo uno" ~:
            actualizarContacto ("Pedro","999")
                [("Juan","111"), ("Pedro","222"), ("Pepe","333"), ("Maria","444")]
            ~?= [("Juan","111"), ("Pedro","999"), ("Pepe","333"), ("Maria","444")],

        "mismo nombre y mismo telefono" ~:
            actualizarContacto ("Pedro","111")
                [("Pedro","111"), ("Pepe","222")]
            ~?= [("Pedro","111"), ("Pepe","222")],

        "hay nombres parecidos pero no iguales" ~:
            actualizarContacto ("Pedro","999")
                [("Pedrito","111"), ("Pedro","222")]
            ~?= [("Pedrito","111"), ("Pedro","999")],

        "varios contactos sin el buscado" ~:
            actualizarContacto ("Pedro","999")
                [("Juan","111"), ("Pepe","222"), ("Maria","333")]
            ~?= [("Juan","111"), ("Pepe","222"), ("Maria","333")]
    ]

testAgregarContacto :: Test
testAgregarContacto = TestList
    [
        "lista vacia" ~:
            agregarContacto ("Pedro","111") []
            ~?= [("Pedro","111")],

        "agrego contacto que no estaba" ~:
            agregarContacto ("Pedro","111")
                [("Pepe","222")]
            ~?= [("Pedro","111"),("Pepe","222")],

        "agrego contacto al final" ~:
            agregarContacto ("Maria","333")
                [("Juan","111"), ("Pedro","222")]
            ~?= [("Maria","333"),("Juan","111"), ("Pedro","222")],

        "actualizo contacto existente" ~:
            agregarContacto ("Pedro","999")
                [("Juan","111"), ("Pedro","222")]
            ~?= [("Juan","111"), ("Pedro","999")],

        "actualizo el primer contacto" ~:
            agregarContacto ("Juan","999")
                [("Juan","111"), ("Pedro","222"), ("Pepe","333")]
            ~?= [("Juan","999"), ("Pedro","222"), ("Pepe","333")],

        "actualizo el contacto del medio" ~:
            agregarContacto ("Pedro","999")
                [("Juan","111"), ("Pedro","222"), ("Pepe","333")]
            ~?= [("Juan","111"), ("Pedro","999"), ("Pepe","333")],

        "actualizo el ultimo contacto" ~:
            agregarContacto ("Pepe","999")
                [("Juan","111"), ("Pedro","222"), ("Pepe","333")]
            ~?= [("Juan","111"), ("Pedro","222"), ("Pepe","999")],

        "mismo nombre y mismo telefono" ~:
            agregarContacto ("Pedro","222")
                [("Juan","111"), ("Pedro","222")]
            ~?= [("Juan","111"), ("Pedro","222")],

        "nombres parecidos pero distintos" ~:
            agregarContacto ("Pedro","999")
                [("Pedrito","111"), ("Pedro","222")]
            ~?= [("Pedrito","111"), ("Pedro","999")],

        "agrego a una lista con varios contactos" ~:
            agregarContacto ("Maria","555")
                [("Juan","111"), ("Pedro","222"), ("Pepe","333")]
            ~?= [("Maria","555"),("Juan","111"), ("Pedro","222"), ("Pepe","333") ]
    ]

testEliminarContacto :: Test
testEliminarContacto = TestList
    [
        "lista vacia" ~:
            eliminarContacto "Pedro" []
            ~?= [],

        "contacto no estaba" ~:
            eliminarContacto "Pedro"
                [("Juan","111"), ("Pepe","222")]
            ~?= [("Juan","111"), ("Pepe","222")],

        "elimino el unico contacto" ~:
            eliminarContacto "Pedro"
                [("Pedro","111")]
            ~?= [],

        "elimino el primer contacto" ~:
            eliminarContacto "Juan"
                [("Juan","111"), ("Pedro","222"), ("Pepe","333")]
            ~?= [("Pedro","222"), ("Pepe","333")],

        "elimino el contacto del medio" ~:
            eliminarContacto "Pedro"
                [("Juan","111"), ("Pedro","222"), ("Pepe","333")]
            ~?= [("Juan","111"), ("Pepe","333")],

        "elimino el ultimo contacto" ~:
            eliminarContacto "Pepe"
                [("Juan","111"), ("Pedro","222"), ("Pepe","333")]
            ~?= [("Juan","111"), ("Pedro","222")],

        "elimino de una lista grande" ~:
            eliminarContacto "Pedro"
                [("Juan","111"), ("Pedro","222"), ("Pepe","333"),
                 ("Maria","444"), ("Luis","555")]
            ~?= [("Juan","111"), ("Pepe","333"),
                 ("Maria","444"), ("Luis","555")],

        "nombre parecido pero distinto" ~:
            eliminarContacto "Pedrito"
                [("Pedro","111"), ("Pedrito","222")]
            ~?= [("Pedro","111")],

        "telefono no importa" ~:
            eliminarContacto "Pedro"
                [("Juan","111"), ("Pedro","999999")]
            ~?= [("Juan","111")],

        "mayusculas y minusculas" ~:
            eliminarContacto "pedro"
                [("Pedro","111")]
            ~?= [("Pedro","111")]
    ]

todosLosTests :: Test
todosLosTests = TestList
  [ "testEnLosContactos"    ~: testEnLosContactos,
  "testActualizarContactos" ~: testActualizarContacto,
  "testAgregarContacto" ~: testAgregarContacto,
  "testEliminarContacto" ~: testEliminarContacto
  ]

main :: IO ()
main = runTestTTAndExit todosLosTests
