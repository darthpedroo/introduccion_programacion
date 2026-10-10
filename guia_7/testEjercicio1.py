import unittest
from types import FunctionType
 
import ejercicio_1 as sol 

class TestDivideATodos(unittest.TestCase):
    def test_lista_vacia(self):
        self.assertTrue(sol.divide_a_todos([], 3))
 
    def test_divide_a_todos(self):
        self.assertTrue(sol.divide_a_todos([2, 4, 6], 2))
 
    def test_no_divide_a_uno(self):
        self.assertFalse(sol.divide_a_todos([2, 4, 7], 2))
 
    def test_no_divide_al_primero(self):
        self.assertFalse(sol.divide_a_todos([3, 4, 6], 2))
 
    def test_con_cero_en_la_lista(self):
        self.assertTrue(sol.divide_a_todos([0, 9, 3], 3))
 
    def test_divisor_uno(self):
        self.assertTrue(sol.divide_a_todos([7, 11, 13], 1))
 
    def test_divisor_negativo(self):
        self.assertTrue(sol.divide_a_todos([4, 8], -2))
        self.assertFalse(sol.divide_a_todos([4, 9], -2))
 
    def test_elementos_negativos(self):
        self.assertTrue(sol.divide_a_todos([-4, -8, 12], 4))
 
 
# ---------------------------------------------------------------- 1.3
class TestSumaTotal(unittest.TestCase):
    def test_lista_vacia(self):
        self.assertEqual(sol.suma_total([]), 0)
 
    def test_un_elemento(self):
        self.assertEqual(sol.suma_total([5]), 5)
 
    def test_varios(self):
        self.assertEqual(sol.suma_total([1, 2, 3, 4]), 10)
 
    def test_con_negativos(self):
        self.assertEqual(sol.suma_total([10, -3, -7]), 0)
 
    def test_todos_negativos(self):
        self.assertEqual(sol.suma_total([-1, -2, -3]), -6)
 
 
# ---------------------------------------------------------------- 1.4
class TestMaximo(unittest.TestCase):
    def test_un_elemento(self):
        self.assertEqual(sol.maximo([4]), 4)
 
    def test_al_principio(self):
        self.assertEqual(sol.maximo([9, 1, 2]), 9)
 
    def test_en_el_medio(self):
        self.assertEqual(sol.maximo([1, 9, 2]), 9)
 
    def test_al_final(self):
        self.assertEqual(sol.maximo([1, 2, 9]), 9)
 
    def test_todos_negativos(self):
        self.assertEqual(sol.maximo([-3, -1, -7]), -1)
 
    def test_repetidos(self):
        self.assertEqual(sol.maximo([3, 3, 3]), 3)

class TestMinimo(unittest.TestCase):
    def test_un_elemento(self):
        self.assertEqual(sol.minimo([4]), 4)
 
    def test_al_principio(self):
        self.assertEqual(sol.minimo([1, 9, 2]), 1)
 
    def test_en_el_medio(self):
        self.assertEqual(sol.minimo([9, 1, 2]), 1)
 
    def test_al_final(self):
        self.assertEqual(sol.minimo([9, 2, 1]), 1)
 
    def test_todos_positivos(self):
        self.assertEqual(sol.minimo([3, 5, 7]), 3)
 
    def test_negativos(self):
        self.assertEqual(sol.minimo([-3, 0, -7]), -7)

class TestOrdenados(unittest.TestCase):
    def test_lista_vacia(self):
        self.assertTrue(sol.ordenados([]))
 
    def test_un_elemento(self):
        self.assertTrue(sol.ordenados([5]))
 
    def test_estrictamente_creciente(self):
        self.assertTrue(sol.ordenados([1, 2, 3, 10]))
 
    def test_con_iguales_consecutivos(self):
        self.assertFalse(sol.ordenados([1, 2, 2, 3]))
 
    def test_desordenado_al_final(self):
        self.assertFalse(sol.ordenados([1, 2, 3, 0]))
 
    def test_desordenado_al_principio(self):
        self.assertFalse(sol.ordenados([5, 1, 2, 3]))
 
    def test_decreciente(self):
        self.assertFalse(sol.ordenados([3, 2, 1]))
 
    def test_negativos(self):
        self.assertTrue(sol.ordenados([-5, -2, 0, 4]))

class TestPosMaximo(unittest.TestCase):
    def test_lista_vacia(self):
        self.assertEqual(sol.pos_maximo([]), -1)
 
    def test_un_elemento(self):
        self.assertEqual(sol.pos_maximo([7]), 0)
 
    def test_maximo_al_final(self):
        self.assertEqual(sol.pos_maximo([1, 2, 9]), 2)
 
    def test_maximo_en_el_medio(self):
        self.assertEqual(sol.pos_maximo([1, 9, 2]), 1)
 
    def test_repetido_devuelve_primera_aparicion(self):
        self.assertEqual(sol.pos_maximo([1, 9, 3, 9, 2]), 1)
 
    def test_todos_iguales(self):
        self.assertEqual(sol.pos_maximo([4, 4, 4]), 0)
 
    def test_todos_negativos(self):
        self.assertEqual(sol.pos_maximo([-5, -1, -3]), 1)
 
 
# ---------------------------------------------------------------- 1.8
class TestPosMinimo(unittest.TestCase):
    def test_lista_vacia(self):
        self.assertEqual(sol.pos_minimo([]), -1)
 
    def test_un_elemento(self):
        self.assertEqual(sol.pos_minimo([7]), 0)
 
    def test_minimo_al_principio(self):
        self.assertEqual(sol.pos_minimo([1, 2, 9]), 0)
 
    def test_minimo_en_el_medio(self):
        self.assertEqual(sol.pos_minimo([5, 1, 9]), 1)
 
    def test_repetido_devuelve_ultima_aparicion(self):
        self.assertEqual(sol.pos_minimo([3, 1, 5, 1, 4]), 3)
 
    def test_todos_iguales(self):
        self.assertEqual(sol.pos_minimo([4, 4, 4]), 2)
 
    def test_todos_positivos(self):
        self.assertEqual(sol.pos_minimo([5, 8, 3, 9]), 2)

class TestLongMayorASiete(unittest.TestCase):
    def test_lista_vacia(self):
        self.assertFalse(sol.long_mayorASiete([]))
 
    def test_ejemplo_del_enunciado(self):
        self.assertFalse(sol.long_mayorASiete(["termo", "gato", "tener", "jirafas"]))
 
    def test_exactamente_siete_no_alcanza(self):
        self.assertFalse(sol.long_mayorASiete(["jirafas"]))
 
    def test_ocho_alcanza(self):
        self.assertTrue(sol.long_mayorASiete(["elefante"]))
 
    def test_larga_al_principio(self):
        self.assertTrue(sol.long_mayorASiete(["murcielago", "sol", "mar"]))
 
    def test_larga_en_el_medio(self):
        self.assertTrue(sol.long_mayorASiete(["sol", "murcielago", "mar"]))
 
    def test_larga_al_final(self):
        self.assertTrue(sol.long_mayorASiete(["sol", "mar", "murcielago"]))
 
    def test_palabras_vacias(self):
        self.assertFalse(sol.long_mayorASiete(["", "", ""]))

class TestEsPalindroma(unittest.TestCase):
    def test_vacia(self):
        self.assertTrue(sol.es_palindroma(""))
 
    def test_un_caracter(self):
        self.assertTrue(sol.es_palindroma("a"))
 
    def test_longitud_par(self):
        self.assertTrue(sol.es_palindroma("abba"))
 
    def test_longitud_impar(self):
        self.assertTrue(sol.es_palindroma("neuquen"))
 
    def test_dos_caracteres_distintos(self):
        self.assertFalse(sol.es_palindroma("ab"))
 
    def test_no_palindroma(self):
        self.assertFalse(sol.es_palindroma("palabra"))
 
    def test_casi_palindroma(self):
        # Difieren solo los extremos
        self.assertFalse(sol.es_palindroma("abcbx"))
 
    def test_mayusculas_cuentan(self):
        self.assertFalse(sol.es_palindroma("Ana"))

class TestIgualesConsecutivos(unittest.TestCase):
    def test_lista_vacia(self):
        self.assertFalse(sol.iguales_consecutivos([]))
 
    def test_menos_de_tres(self):
        self.assertFalse(sol.iguales_consecutivos([1, 1]))
 
    def test_exactamente_tres_iguales(self):
        self.assertTrue(sol.iguales_consecutivos([4, 4, 4]))
 
    def test_al_principio(self):
        self.assertTrue(sol.iguales_consecutivos([2, 2, 2, 5, 6]))
 
    def test_en_el_medio(self):
        self.assertTrue(sol.iguales_consecutivos([1, 7, 7, 7, 3]))
 
    def test_al_final(self):
        self.assertTrue(sol.iguales_consecutivos([1, 2, 9, 9, 9]))
 
    def test_tres_iguales_no_consecutivos(self):
        self.assertFalse(sol.iguales_consecutivos([5, 5, 1, 5]))
 
    def test_pares_de_iguales(self):
        self.assertFalse(sol.iguales_consecutivos([1, 1, 2, 2, 3, 3]))

class TestVocalesDistintas(unittest.TestCase):
    def test_vacia(self):
        self.assertFalse(sol.vocales_distintas(""))
 
    def test_sin_vocales(self):
        self.assertFalse(sol.vocales_distintas("rtyplk"))
 
    def test_una_vocal_repetida(self):
        self.assertFalse(sol.vocales_distintas("banana"))
 
    def test_dos_vocales_distintas(self):
        self.assertFalse(sol.vocales_distintas("pera"))
 
    def test_muchas_vocales_pero_solo_dos_distintas(self):
        self.assertFalse(sol.vocales_distintas("aeaeaeae"))
 
    def test_tres_vocales_distintas(self):
        self.assertTrue(sol.vocales_distintas("casero"))
 
    def test_cinco_vocales(self):
        self.assertTrue(sol.vocales_distintas("murcielago"))
 
    def test_vocales_al_final(self):
        self.assertTrue(sol.vocales_distintas("xyzaei"))

class TestCantidadDigitosImpares(unittest.TestCase):
    def test_ejemplo_del_enunciado(self):
        self.assertEqual(sol.cantidad_digitos_impares([57, 2383, 812, 246]), 5)
 
    def test_lista_vacia(self):
        self.assertEqual(sol.cantidad_digitos_impares([]), 0)
 
    def test_cero(self):
        self.assertEqual(sol.cantidad_digitos_impares([0]), 0)
 
    def test_todos_pares(self):
        self.assertEqual(sol.cantidad_digitos_impares([2468, 20, 4]), 0)
 
    def test_todos_impares(self):
        self.assertEqual(sol.cantidad_digitos_impares([13579]), 5)
 
    def test_ceros_intermedios_y_finales(self):
        self.assertEqual(sol.cantidad_digitos_impares([1001, 300]), 3)
 
    def test_un_digito(self):
        self.assertEqual(sol.cantidad_digitos_impares([1, 2, 3]), 2)


if __name__ == "__main__":
    unittest.main()