"""
Test suite - Guía Práctica 7, Ejercicios 3 (resultadoMateria) y 4 (saldoActual)

Uso:
    python -m unittest test_ejercicio3_4.py -v

Ajustar la línea de import con el nombre del archivo donde están tus funciones.
"""
import unittest

import ejercicio_3 as sol  # <- cambiar "guia7" por el nombre de tu archivo (sin .py)


# ---------------------------------------------------------------- Ejercicio 3
class TestResultadoMateria(unittest.TestCase):
    # --- res = 1: todas >= 4 y promedio >= 7
    def test_promociona(self):
        self.assertEqual(sol.resultadoMateria([8, 9, 10]), 1)

    def test_promociona_una_sola_nota(self):
        self.assertEqual(sol.resultadoMateria([10]), 1)

    def test_promedio_exactamente_siete(self):
        # El 7 está incluido en el caso 1
        self.assertEqual(sol.resultadoMateria([7, 7, 7]), 1)
        self.assertEqual(sol.resultadoMateria([4, 10]), 1)

    def test_promociona_con_un_cuatro(self):
        # Un 4 no impide promocionar si el promedio da >= 7
        self.assertEqual(sol.resultadoMateria([4, 10, 10]), 1)

    # --- res = 2: todas >= 4 y 4 <= promedio < 7
    def test_aprueba(self):
        self.assertEqual(sol.resultadoMateria([5, 6, 5]), 2)

    def test_todas_cuatro(self):
        # El 4 está incluido en el caso 2
        self.assertEqual(sol.resultadoMateria([4, 4, 4]), 2)

    def test_un_solo_cuatro(self):
        self.assertEqual(sol.resultadoMateria([4]), 2)

    def test_promedio_casi_siete(self):
        # Promedio 6.67: atrapa a quien redondea el promedio con round()
        self.assertEqual(sol.resultadoMateria([7, 7, 6]), 2)

    def test_promedio_seis_y_medio(self):
        self.assertEqual(sol.resultadoMateria([7, 6]), 2)

    # --- res = 3: alguna < 4 (o promedio < 4)
    def test_desaprueba_todas_bajas(self):
        self.assertEqual(sol.resultadoMateria([1, 2, 3]), 3)

    def test_una_sola_nota_baja(self):
        self.assertEqual(sol.resultadoMateria([3]), 3)

    def test_un_aplazo_con_promedio_alto(self):
        # Promedio 7.67, pero hay un 3: atrapa a quien solo mira el promedio
        self.assertEqual(sol.resultadoMateria([10, 10, 3]), 3)

    def test_un_aplazo_con_promedio_de_aprobado(self):
        self.assertEqual(sol.resultadoMateria([6, 6, 2]), 3)

    def test_aplazo_al_principio(self):
        self.assertEqual(sol.resultadoMateria([0, 10, 10, 10]), 3)

    def test_aplazo_al_final(self):
        self.assertEqual(sol.resultadoMateria([10, 10, 10, 0]), 3)

    def test_tres_no_alcanza(self):
        # Borde: 3 < 4
        self.assertEqual(sol.resultadoMateria([3, 10]), 3)

    # --- otros
    def test_no_modifica_la_lista(self):
        notas = [8, 4, 10]
        sol.resultadoMateria(notas)
        self.assertEqual(notas, [8, 4, 10])

    def test_devuelve_entero(self):
        self.assertIsInstance(sol.resultadoMateria([8, 9]), int)


if __name__ == "__main__":
    unittest.main(verbosity=2)