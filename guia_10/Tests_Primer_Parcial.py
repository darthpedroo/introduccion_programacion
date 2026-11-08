import unittest
from Primer_Parcial import *

class TestVeterinaria(unittest.TestCase):
    
    # EJERCICIO 1

    def test_stock_de_producto_surtido(self):

        stock = [("Pipeta",10), ("Comida Perro", 100), ("Comida Gato",1), ("Pipeta", 3), ("Comida Abuela", 100),("Comida Perro", 68), ("Comida Gato", 200)]
        res = {"Pipeta": (3,10),
               "Comida Perro": (68,100),
               "Comida Gato": (1,200),
               "Comida Abuela": (100,100)
                }
        self.assertEqual(stock_productos(stock), res)

    def test_stock_de_producto_un_unico_producto(self):

        stock = [("Pipeta",1)]
        res = {"Pipeta": (1,1)
                }
        self.assertEqual(stock_productos(stock), res)
        
    # EJERCICIO 2


    def test_filtrar_codigos_primos_no_hay_ninguno(self):
        codigos = [222,444,666,888,912,1000,666666]

        self.assertEqual(len(filtrar_codigos_primos(codigos)),1) # el 000 es primo "jeje"

    def test_filtrar_codigos_primos_lista_vacia(self):
        codigos = []
        self.assertEqual(filtrar_codigos_primos(codigos), [])

    def test_filtar_codigos_primos_ejemplos_catedra(self):
        codigos = [1002,101,9011,107,103,100000103, 1000107]
        self.assertEqual(filtrar_codigos_primos(codigos), codigos)

    def test_filtrar_codigos_primos_algunos_nomas(self):
        codigos = [1002,444, 101, 222, 107,]
        self.assertEqual(filtrar_codigos_primos(codigos), [1002,101,107])

if __name__ == "__main__":
    unittest.main()

