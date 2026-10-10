"""
Test suite - Guía Práctica 7, Ejercicio 2 (ítems 3 a 6)

Uso:
    python -m unittest test_ejercicio2.py -v

Ajustar la línea de import con el nombre del archivo donde están tus funciones.
"""
import unittest

import ejercicio_2 as sol  # <- cambiar "guia7" por el nombre de tu archivo (sin .py)

# Caracter con el que reemplaza_vocales sustituye cada vocal (según la especificación: '_')
REEMPLAZO: str = "_"


# ---------------------------------------------------------------- 2.3
class TestSinVocales(unittest.TestCase):
    def test_vacia(self):
        self.assertEqual(sol.sin_vocales(""), "")

    def test_sin_vocales_queda_igual(self):
        self.assertEqual(sol.sin_vocales("rtyplk"), "rtyplk")

    def test_solo_vocales(self):
        self.assertEqual(sol.sin_vocales("aeiou"), "")

    def test_palabra(self):
        self.assertEqual(sol.sin_vocales("murcielago"), "mrclg")

    def test_vocales_al_principio_y_al_final(self):
        self.assertEqual(sol.sin_vocales("arbole"), "rbl")

    def test_vocales_consecutivas(self):
        # Atrapa a quien recorre por índice y se saltea un caracter al borrar
        self.assertEqual(sol.sin_vocales("buuueno"), "bn")

    def test_conserva_espacios(self):
        # No se agregan espacios, pero los que ya estaban se conservan
        self.assertEqual(sol.sin_vocales("hola mundo"), "hl mnd")

    def test_conserva_orden(self):
        res = sol.sin_vocales("programacion")
        self.assertEqual(res, "prgrmcn")

    def test_devuelve_string(self):
        self.assertIsInstance(sol.sin_vocales("casa"), str)


# ---------------------------------------------------------------- 2.4
class TestReemplazaVocales(unittest.TestCase):
    def esperado(self, s: str) -> str:
        return "".join(REEMPLAZO if c in "aeiou" else c for c in s)

    def test_vacia(self):
        self.assertEqual(sol.reemplaza_vocales(""), "")

    def test_sin_vocales_queda_igual(self):
        self.assertEqual(sol.reemplaza_vocales("rtyplk"), "rtyplk")

    def test_solo_vocales(self):
        self.assertEqual(sol.reemplaza_vocales("aeiou"), REEMPLAZO * 5)

    def test_palabra(self):
        self.assertEqual(sol.reemplaza_vocales("murcielago"), self.esperado("murcielago"))

    def test_vocales_consecutivas(self):
        self.assertEqual(sol.reemplaza_vocales("buuueno"), self.esperado("buuueno"))

    def test_conserva_longitud(self):
        for s in ["", "a", "casa", "hola mundo", "xyz"]:
            with self.subTest(s=s):
                self.assertEqual(len(sol.reemplaza_vocales(s)), len(s))

    def test_consonantes_en_su_lugar(self):
        s = "programacion"
        res = sol.reemplaza_vocales(s)
        for i in range(len(s)):
            with self.subTest(i=i):
                if s[i] in "aeiou":
                    self.assertEqual(res[i], REEMPLAZO)
                else:
                    self.assertEqual(res[i], s[i])

    def test_no_agrega_espacios(self):
        self.assertNotIn(" ", sol.reemplaza_vocales("murcielago"))

    def test_devuelve_string(self):
        self.assertIsInstance(sol.reemplaza_vocales("casa"), str)


# ---------------------------------------------------------------- 2.5
class TestDaVueltaStr(unittest.TestCase):
    def test_vacia(self):
        self.assertEqual(sol.da_vuelta_str(""), "")

    def test_un_caracter(self):
        self.assertEqual(sol.da_vuelta_str("a"), "a")

    def test_dos_caracteres(self):
        self.assertEqual(sol.da_vuelta_str("ab"), "ba")

    def test_palabra(self):
        self.assertEqual(sol.da_vuelta_str("hola"), "aloh")

    def test_palindromo_queda_igual(self):
        self.assertEqual(sol.da_vuelta_str("neuquen"), "neuquen")

    def test_con_espacios_y_simbolos(self):
        self.assertEqual(sol.da_vuelta_str("ab c!"), "!c ba")

    def test_conserva_longitud(self):
        self.assertEqual(len(sol.da_vuelta_str("programacion")), len("programacion"))

    def test_dos_veces_vuelve_al_original(self):
        s = "introduccion"
        self.assertEqual(sol.da_vuelta_str(sol.da_vuelta_str(s)), s)

    def test_devuelve_string(self):
        self.assertIsInstance(sol.da_vuelta_str("casa"), str)


# ---------------------------------------------------------------- 2.6
class TestEliminarRepetidos(unittest.TestCase):
    """La especificación NO fija el orden del resultado: solo pide que no haya
    repetidos, que estén todos los caracteres de s y que |res| <= |s|.
    Por eso se chequean esas propiedades en lugar de comparar con un string fijo."""

    def cumple_especificacion(self, s: str):
        res = sol.eliminar_repetidos(s)
        self.assertLessEqual(len(res), len(s), "|res| debe ser <= |s|")
        for c in s:
            self.assertIn(c, res, f"falta '{c}' en el resultado")
        for i in range(len(res)):
            for j in range(len(res)):
                if i != j:
                    self.assertNotEqual(res[i], res[j], f"'{res[i]}' aparece repetido")
        for c in res:
            # Implícito en la especificación: |res| <= |s| junto con lo anterior
            # obliga a que res tenga exactamente los caracteres de s
            self.assertIn(c, s, f"'{c}' no estaba en s")

    def test_vacia(self):
        self.assertEqual(sol.eliminar_repetidos(""), "")

    def test_un_caracter(self):
        self.assertEqual(sol.eliminar_repetidos("a"), "a")

    def test_sin_repetidos(self):
        self.cumple_especificacion("abc")
        self.assertEqual(len(sol.eliminar_repetidos("abc")), 3)

    def test_todos_iguales(self):
        self.assertEqual(sol.eliminar_repetidos("aaaa"), "a")

    def test_repetidos_consecutivos(self):
        self.cumple_especificacion("aabbcc")
        self.assertEqual(len(sol.eliminar_repetidos("aabbcc")), 3)

    def test_repetidos_no_consecutivos(self):
        # Atrapa a quien solo compara con el caracter anterior
        self.cumple_especificacion("abcabc")
        self.assertEqual(len(sol.eliminar_repetidos("abcabc")), 3)

    def test_palabra(self):
        self.cumple_especificacion("murcielago")
        self.cumple_especificacion("programacion")
        self.assertEqual(len(sol.eliminar_repetidos("programacion")), 9)

    def test_espacios_cuentan_como_caracter(self):
        self.cumple_especificacion("a b a b")
        self.assertEqual(len(sol.eliminar_repetidos("a b a b")), 3)

    def test_mayusculas_son_distintas(self):
        self.cumple_especificacion("Aa")
        self.assertEqual(len(sol.eliminar_repetidos("Aa")), 2)

    def test_devuelve_string(self):
        self.assertIsInstance(sol.eliminar_repetidos("casa"), str)


if __name__ == "__main__":
    unittest.main(verbosity=2)