
import copy
import unittest

import ejercicio_6 as sol 


def ordenados_ref(s: list[int]) -> bool:
    return all(s[i] < s[i + 1] for i in range(len(s) - 1))


# ---------------------------------------------------------------- 6.1
class TestEsMatriz(unittest.TestCase):
    def test_rectangular_mas_columnas(self):
        self.assertTrue(sol.es_matriz([[1, 2, 3], [4, 5, 6]]))

    def test_rectangular_mas_filas(self):
        self.assertTrue(sol.es_matriz([[1], [2], [3]]))

    def test_cuadrada(self):
        self.assertTrue(sol.es_matriz([[1, 2], [3, 4]]))

    def test_un_elemento(self):
        self.assertTrue(sol.es_matriz([[5]]))

    def test_una_fila(self):
        self.assertTrue(sol.es_matriz([[1, 2, 3, 4]]))

    def test_sin_filas(self):
        self.assertFalse(sol.es_matriz([]))

    def test_fila_vacia(self):
        self.assertFalse(sol.es_matriz([[]]))

    def test_todas_las_filas_vacias(self):
        # Todas tienen el mismo largo, pero |s[0]| > 0 no se cumple
        self.assertFalse(sol.es_matriz([[], [], []]))

    def test_segunda_fila_mas_corta(self):
        self.assertFalse(sol.es_matriz([[1, 2], [3]]))

    def test_segunda_fila_mas_larga(self):
        self.assertFalse(sol.es_matriz([[1], [2, 3]]))

    def test_ultima_fila_distinta(self):
        # Atrapa a quien no revisa todas las filas
        self.assertFalse(sol.es_matriz([[1, 2], [3, 4], [5, 6], [7]]))

    def test_fila_del_medio_vacia(self):
        self.assertFalse(sol.es_matriz([[1, 2], [], [5, 6]]))

    def test_no_modifica(self):
        m = [[1, 2], [3, 4]]
        sol.es_matriz(m)
        self.assertEqual(m, [[1, 2], [3, 4]])


# ---------------------------------------------------------------- 6.2
class TestFilasOrdenadas(unittest.TestCase):
    CASOS: list[list[list[int]]] = [
        [[1, 2, 3]],                          # una fila ordenada
        [[3, 2, 1]],                          # una fila desordenada
        [[1, 2], [2, 1], [5, 9]],             # mezcla
        [[1, 1], [1, 2]],                     # iguales: no ordenada (estricto)
        [[7], [3], [9]],                      # filas de un elemento: todas ordenadas
        [[1, 2, 3], [4, 5, 6], [9, 8, 7]],    # la última no
    ]

    def esperado(self, m: list[list[int]]) -> list[bool]:
        return [ordenados_ref(fila) for fila in m]

    def _probar(self, res_inicial: list[bool]):
        for m in self.CASOS:
            with self.subTest(m=m, res_inicial=res_inicial):
                res = list(res_inicial)
                sol.filas_ordenadas(m, res)
                esp = self.esperado(m)
                # Lo que exige la especificación: cada res[i] corresponde a la fila i
                for i in range(len(res)):
                    self.assertEqual(res[i], esp[i], f"res[{i}] incorrecto")

    def test_res_vacia(self):
        self._probar([])

    def test_res_con_basura(self):
        # res es "out": la función no puede asumir que viene vacía
        self._probar([False, True, False, True])

    def test_un_resultado_por_fila(self):
        for m in self.CASOS:
            with self.subTest(m=m):
                res: list[bool] = []
                sol.filas_ordenadas(m, res)
                self.assertEqual(res, self.esperado(m))

    def test_modifica_la_lista_recibida(self):
        res: list[bool] = []
        sol.filas_ordenadas([[1, 2], [2, 1]], res)
        self.assertEqual(res, [True, False])

    def test_no_devuelve_nada(self):
        self.assertIsNone(sol.filas_ordenadas([[1, 2]], []))

    def test_no_modifica_m(self):
        m = [[3, 1], [1, 2]]
        original = copy.deepcopy(m)
        sol.filas_ordenadas(m, [])
        self.assertEqual(m, original)


# ---------------------------------------------------------------- 6.3
class TestColumna(unittest.TestCase):
    M = [[1, 2, 3],
         [4, 5, 6]]

    def test_primera_columna(self):
        self.assertEqual(sol.columna(self.M, 0), [1, 4])

    def test_columna_del_medio(self):
        self.assertEqual(sol.columna(self.M, 1), [2, 5])

    def test_ultima_columna(self):
        self.assertEqual(sol.columna(self.M, 2), [3, 6])

    def test_una_fila(self):
        self.assertEqual(sol.columna([[7, 8, 9]], 1), [8])

    def test_una_columna(self):
        self.assertEqual(sol.columna([[1], [2], [3]], 0), [1, 2, 3])

    def test_mas_filas_que_columnas(self):
        m = [[1, 2], [3, 4], [5, 6], [7, 8]]
        self.assertEqual(sol.columna(m, 1), [2, 4, 6, 8])

    def test_un_elemento(self):
        self.assertEqual(sol.columna([[5]], 0), [5])

    def test_no_modifica_m(self):
        m = copy.deepcopy(self.M)
        sol.columna(m, 1)
        self.assertEqual(m, self.M)


# ---------------------------------------------------------------- 6.4
class TestColumnasOrdenadas(unittest.TestCase):
    def test_todas_ordenadas(self):
        m = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
        self.assertEqual(sol.columnas_ordenadas(m), [True, True, True])

    def test_ninguna_ordenada(self):
        m = [[9, 8],
             [1, 2]]
        self.assertEqual(sol.columnas_ordenadas(m), [False, False])

    def test_mezcla(self):
        m = [[1, 9, 5],
             [2, 3, 5],
             [3, 1, 6]]
        self.assertEqual(sol.columnas_ordenadas(m), [True, False, False])

    def test_largo_es_cantidad_de_columnas(self):
        m = [[1, 2, 3],
             [4, 0, 6]]
        self.assertEqual(sol.columnas_ordenadas(m), [True, False, True])

    def test_mas_filas_que_columnas(self):
        m = [[1, 5],
             [2, 4],
             [3, 3]]
        self.assertEqual(sol.columnas_ordenadas(m), [True, False])

    def test_una_fila(self):
        self.assertEqual(sol.columnas_ordenadas([[5, 1, 3]]), [True, True, True])

    def test_una_columna(self):
        self.assertEqual(sol.columnas_ordenadas([[1], [2], [0]]), [False])

    def test_no_confunde_filas_con_columnas(self):
        m = [[4, 5, 6],
             [1, 2, 3]]
        self.assertEqual(sol.columnas_ordenadas(m), [False, False, False])

    def test_no_modifica_m(self):
        m = [[1, 2], [3, 4]]
        sol.columnas_ordenadas(m)
        self.assertEqual(m, [[1, 2], [3, 4]])


# ---------------------------------------------------------------- 6.5
class TestTransponer(unittest.TestCase):
    def test_cuadrada(self):
        self.assertEqual(sol.transponer([[1, 2], [3, 4]]), [[1, 3], [2, 4]])

    def test_mas_columnas_que_filas(self):
        self.assertEqual(sol.transponer([[1, 2, 3], [4, 5, 6]]),
                         [[1, 4], [2, 5], [3, 6]])

    def test_mas_filas_que_columnas(self):
        self.assertEqual(sol.transponer([[1, 4], [2, 5], [3, 6]]),
                         [[1, 2, 3], [4, 5, 6]])

    def test_una_fila(self):
        self.assertEqual(sol.transponer([[1, 2, 3]]), [[1], [2], [3]])

    def test_una_columna(self):
        self.assertEqual(sol.transponer([[1], [2], [3]]), [[1, 2, 3]])

    def test_un_elemento(self):
        self.assertEqual(sol.transponer([[7]]), [[7]])

    def test_cuadrada_3x3(self):
        m = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
        self.assertEqual(sol.transponer(m), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

    def test_dimensiones(self):
        m = [[0] * 5 for _ in range(2)]
        mt = sol.transponer(m)
        self.assertEqual(len(mt), 5)
        for fila in mt:
            self.assertEqual(len(fila), 2)

    def test_posiciones(self):
        m = [[1, 2, 3, 4],
             [5, 6, 7, 8]]
        mt = sol.transponer(m)
        for i in range(len(m)):
            for j in range(len(m[0])):
                with self.subTest(i=i, j=j):
                    self.assertEqual(mt[j][i], m[i][j])

    def test_transponer_dos_veces(self):
        m = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(sol.transponer(sol.transponer(m)), m)

    def test_no_modifica_m(self):
        m = [[1, 2, 3], [4, 5, 6]]
        sol.transponer(m)
        self.assertEqual(m, [[1, 2, 3], [4, 5, 6]])

    def test_resultado_independiente_de_m(self):
        m = [[1], [2]]
        mt = sol.transponer(m)
        mt[0][0] = 99
        self.assertEqual(m, [[1], [2]])


if __name__ == "__main__":
    unittest.main(verbosity=2)