
import unittest

import ejercicio_4 as sol  
# ---------------------------------------------------------------- Ejercicio 4
class TestSaldoActual(unittest.TestCase):
    def test_sin_movimientos(self):
        self.assertEqual(sol.saldoActual([]), 0)

    def test_ejemplo_del_enunciado(self):
        movimientos = [("I", 2000), ("R", 20), ("R", 1000), ("I", 300)]
        self.assertEqual(sol.saldoActual(movimientos), 1280)

    def test_un_ingreso(self):
        self.assertEqual(sol.saldoActual([("I", 500)]), 500)

    def test_un_retiro(self):
        # La especificación no exige saldo >= 0
        self.assertEqual(sol.saldoActual([("R", 500)]), -500)

    def test_solo_ingresos(self):
        self.assertEqual(sol.saldoActual([("I", 100), ("I", 200), ("I", 300)]), 600)

    def test_solo_retiros(self):
        self.assertEqual(sol.saldoActual([("R", 100), ("R", 200)]), -300)

    def test_saldo_cero(self):
        self.assertEqual(sol.saldoActual([("I", 750), ("R", 750)]), 0)

    def test_retiro_antes_que_ingreso(self):
        # El orden no importa para el saldo final
        self.assertEqual(sol.saldoActual([("R", 300), ("I", 1000)]), 700)

    def test_retiro_al_final(self):
        # Atrapa a quien ignora el último movimiento
        self.assertEqual(sol.saldoActual([("I", 1000), ("I", 500), ("R", 1)]), 1499)

    def test_muchos_movimientos(self):
        movimientos = [("I", 10)] * 50 + [("R", 3)] * 50
        self.assertEqual(sol.saldoActual(movimientos), 350)

    def test_no_modifica_la_lista(self):
        movimientos = [("I", 2000), ("R", 20)]
        sol.saldoActual(movimientos)
        self.assertEqual(movimientos, [("I", 2000), ("R", 20)])

    def test_devuelve_entero(self):
        self.assertIsInstance(sol.saldoActual([("I", 10)]), int)


if __name__ == "__main__":
    unittest.main(verbosity=2)