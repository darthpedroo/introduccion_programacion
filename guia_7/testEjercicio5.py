
import copy
import unittest

import ejercicio_5 as sol  # <- cambiar "guia7" por el nombre de tu archivo (sin .py)


def esperado(s: list[list[int]], e: int) -> list[bool]:
    return [e in fila for fila in s]


# Casos (s, e) que se usan en las tres versiones
CASOS: list[tuple[list[list[int]], int]] = [
    ([], 3),                                  # s vacía
    ([[]], 3),                                # una sola lista vacía
    ([[], [], []], 3),                        # todas vacías
    ([[1, 2, 3]], 2),                         # una lista, está
    ([[1, 2, 3]], 7),                         # una lista, no está
    ([[1, 2], [3, 4], [2, 5]], 2),            # está en la primera y en la última
    ([[5, 6], [2], [7, 8]], 2),               # solo en la del medio
    ([[1], [2], [3], [4]], 4),                # solo en la última
    ([[9, 9, 9], [9]], 9),                    # repetido dentro de las listas
    ([[-1, -2], [1, 2], [0]], -2),            # negativos
    ([[1, 2, 3], [], [3]], 3),                # mezcla con lista vacía
]

# Valores iniciales de res para el parámetro out
RES_INICIALES: dict[str, list[bool]] = {
    "vacia": [],
    "mas_corta_con_basura": [True],
    "mas_larga_con_basura": [True, False, True, True, False, True, True, False],
}


# ---------------------------------------------------------------- Versión 1
class TestVersion1(unittest.TestCase):
    """|res| >= |s| y los primeros |s| elementos de res son los correctos."""

    def _probar(self, res_inicial: list[bool]):
        for s, e in CASOS:
            with self.subTest(s=s, e=e, res_inicial=res_inicial):
                res = list(res_inicial)
                sol.pertenece_a_cada_uno_version_1(s, e, res)
                self.assertGreaterEqual(len(res), len(s), "debe cumplirse |res| >= |s|")
                self.assertEqual(res[:len(s)], esperado(s, e))

    def test_res_vacia(self):
        self._probar(RES_INICIALES["vacia"])

    def test_res_con_basura_mas_corta(self):
        self._probar(RES_INICIALES["mas_corta_con_basura"])

    def test_res_con_basura_mas_larga(self):
        # Acá la versión 1 puede dejar elementos de sobra al final (|res| >= |s|)
        self._probar(RES_INICIALES["mas_larga_con_basura"])

    def test_modifica_la_lista_recibida(self):
        res: list[bool] = []
        sol.pertenece_a_cada_uno_version_1([[1], [2]], 1, res)
        self.assertEqual(res[:2], [True, False])

    def test_no_devuelve_nada(self):
        res: list[bool] = []
        self.assertIsNone(sol.pertenece_a_cada_uno_version_1([[1]], 1, res))

    def test_no_modifica_s(self):
        s = [[1, 2], [3]]
        original = copy.deepcopy(s)
        sol.pertenece_a_cada_uno_version_1(s, 2, [])
        self.assertEqual(s, original)


# ---------------------------------------------------------------- Versión 2
class TestVersion2(unittest.TestCase):
    """|res| = |s|: res tiene que quedar exactamente con el resultado."""

    def _probar(self, res_inicial: list[bool]):
        for s, e in CASOS:
            with self.subTest(s=s, e=e, res_inicial=res_inicial):
                res = list(res_inicial)
                sol.pertenece_a_cada_uno_version_2(s, e, res)
                self.assertEqual(len(res), len(s), "debe cumplirse |res| = |s|")
                self.assertEqual(res, esperado(s, e))

    def test_res_vacia(self):
        self._probar(RES_INICIALES["vacia"])

    def test_res_con_basura_mas_corta(self):
        self._probar(RES_INICIALES["mas_corta_con_basura"])

    def test_res_con_basura_mas_larga(self):
        self._probar(RES_INICIALES["mas_larga_con_basura"])

    def test_modifica_la_lista_recibida(self):
        res: list[bool] = [True, True, True]
        sol.pertenece_a_cada_uno_version_2([[1], [2]], 1, res)
        self.assertEqual(res, [True, False])

    def test_no_devuelve_nada(self):
        res: list[bool] = []
        self.assertIsNone(sol.pertenece_a_cada_uno_version_2([[1]], 1, res))

    def test_no_modifica_s(self):
        s = [[1, 2], [3]]
        original = copy.deepcopy(s)
        sol.pertenece_a_cada_uno_version_2(s, 2, [])
        self.assertEqual(s, original)


# ---------------------------------------------------------------- Versión 3
class TestVersion3(unittest.TestCase):
    """Devuelve el resultado como valor de retorno, con |res| = |s|."""

    def test_casos(self):
        for s, e in CASOS:
            with self.subTest(s=s, e=e):
                self.assertEqual(sol.pertenece_a_cada_uno_version_3(s, e), esperado(s, e))

    def test_devuelve_lista_nueva_cada_vez(self):
        a = sol.pertenece_a_cada_uno_version_3([[1]], 1)
        b = sol.pertenece_a_cada_uno_version_3([[2], [3]], 1)
        self.assertEqual(a, [True])
        self.assertEqual(b, [False, False])

    def test_devuelve_lista(self):
        self.assertIsInstance(sol.pertenece_a_cada_uno_version_3([[1]], 1), list)

    def test_no_modifica_s(self):
        s = [[1, 2], [3]]
        original = copy.deepcopy(s)
        sol.pertenece_a_cada_uno_version_3(s, 2)
        self.assertEqual(s, original)


if __name__ == "__main__":
    unittest.main(verbosity=2)