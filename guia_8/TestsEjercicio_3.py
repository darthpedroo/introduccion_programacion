import unittest
from queue import Queue as Cola
from Ejercicio_3 import *


class TestsDiccionarios(unittest.TestCase):

    # EJERCICIO 16

    def test_calcular_promedio_por_estudiante_catedra(self):
        x = [("Sole",9.5), ("Maxi",8.0), ("Sole",9.0)]
        res = {"Sole": 9.25, "Maxi": 8.0}
        self.assertEqual(calcular_promedio_por_estudiante(x),res)

        
    def assert_dicts_aprox(self, obtenido: dict, esperado: dict):
        self.assertEqual(set(obtenido.keys()), set(esperado.keys()))
        for clave in esperado:
            self.assertAlmostEqual(obtenido[clave], esperado[clave])

    def test_lista_vacia(self):
        self.assertEqual(calcular_promedio_por_estudiante([]), {})

    def test_un_estudiante_una_nota(self):
        x = [("Ana", 7.0)]
        res = {"Ana": 7.0}
        self.assert_dicts_aprox(calcular_promedio_por_estudiante(x), res)

    def test_varios_estudiantes_intercalados(self):
        # Distinta cantidad de notas por estudiante y en orden mezclado
        x = [("Ana", 10.0), ("Beto", 4.0), ("Ana", 6.0),
             ("Caro", 7.0), ("Beto", 8.0), ("Ana", 8.0)]
        res = {"Ana": 8.0, "Beto": 6.0, "Caro": 7.0}
        self.assert_dicts_aprox(calcular_promedio_por_estudiante(x), res)

    def test_promedios_periodicos_y_notas_extremas(self):
        # 23/3 = 7.666... y 20/3 = 6.666...; además incluye 0 y 10
        x = [("Dani", 7.0), ("Eli", 0.0), ("Dani", 8.0),
             ("Eli", 10.0), ("Dani", 8.0), ("Eli", 10.0)]
        res = {"Dani": 23 / 3, "Eli": 20 / 3}
        self.assert_dicts_aprox(calcular_promedio_por_estudiante(x), res)

    def test_no_modifica_la_entrada(self):
        x = [("Sole", 9.5), ("Maxi", 8.0), ("Sole", 9.0)]
        copia = x.copy()
        calcular_promedio_por_estudiante(x)
        self.assertEqual(x, copia)
    
    # EJERCICIO 17

    def test_usuario_existente_apila_el_sitio(self):
        p = Pila()
        p.put("google.com")
        p.put("x.com")
        h = {"Ana": p}
        visitar_sitio(h, "Ana", "uba.ar")
        self.assertEqual(set(h.keys()), {"Ana"})
        self.assertEqual(h["Ana"].get(), "uba.ar")
        self.assertEqual(h["Ana"].get(), "x.com")
        self.assertEqual(h["Ana"].get(), "google.com")
        self.assertTrue(h["Ana"].empty())

    def test_usuario_nuevo_crea_pila_con_solo_el_sitio(self):
        p = Pila()
        p.put("google.com")
        h = {"Ana": p}
        visitar_sitio(h, "Beto", "uba.ar")
        self.assertEqual(set(h.keys()), {"Ana", "Beto"})
        self.assertEqual(h["Beto"].get(), "uba.ar")
        self.assertTrue(h["Beto"].empty())
        self.assertEqual(h["Ana"].get(), "google.com")
        self.assertTrue(h["Ana"].empty())

    def test_diccionario_vacio(self):
        h = {}
        visitar_sitio(h, "Juan", "uba.ar")
        self.assertEqual(set(h.keys()), {"Juan"})
        self.assertEqual(h["Juan"].get(), "uba.ar")
        self.assertTrue(h["Juan"].empty())

    def test_no_modifica_otros_historiales(self):
        pa = Pila()
        pa.put("a.com")
        pb = Pila()
        pb.put("b1.com")
        pb.put("b2.com")
        pc = Pila()
        pc.put("c.com")
        h = {"Ana": pa, "Beto": pb, "Caro": pc}
        visitar_sitio(h, "Beto", "uba.ar")
        self.assertEqual(set(h.keys()), {"Ana", "Beto", "Caro"})
        self.assertEqual(h["Ana"].get(), "a.com")
        self.assertTrue(h["Ana"].empty())
        self.assertEqual(h["Caro"].get(), "c.com")
        self.assertTrue(h["Caro"].empty())
        self.assertEqual(h["Beto"].get(), "uba.ar")
        self.assertEqual(h["Beto"].get(), "b2.com")
        self.assertEqual(h["Beto"].get(), "b1.com")
        self.assertTrue(h["Beto"].empty())

    def test_visitar_dos_veces_el_mismo_sitio(self):
        h = {}
        visitar_sitio(h, "Ana", "uba.ar")
        visitar_sitio(h, "Ana", "uba.ar")
        self.assertEqual(h["Ana"].get(), "uba.ar")
        self.assertEqual(h["Ana"].get(), "uba.ar")
        self.assertTrue(h["Ana"].empty())

    def test_pila_con_un_solo_sitio(self):
        p = Pila()
        p.put("uba.ar")
        h = {"Ana": p}
        res = navegar_atras(h, "Ana")
        self.assertEqual(res, "uba.ar")
        self.assertEqual(set(h.keys()), {"Ana"})
        self.assertTrue(h["Ana"].empty())

    def test_devuelve_el_tope_y_deja_el_resto(self):
        p = Pila()
        p.put("google.com")
        p.put("x.com")
        p.put("uba.ar")
        h = {"Ana": p}
        res = navegar_atras(h, "Ana")
        self.assertEqual(res, "uba.ar")
        self.assertEqual(h["Ana"].get(), "x.com")
        self.assertEqual(h["Ana"].get(), "google.com")
        self.assertTrue(h["Ana"].empty())

    def test_no_modifica_otros_historiales(self):
        pa = Pila()
        pa.put("a.com")
        pb = Pila()
        pb.put("b1.com")
        pb.put("b2.com")
        pc = Pila()
        pc.put("c.com")
        h = {"Ana": pa, "Beto": pb, "Caro": pc}
        res = navegar_atras(h, "Beto")
        self.assertEqual(res, "b2.com")
        self.assertEqual(set(h.keys()), {"Ana", "Beto", "Caro"})
        self.assertEqual(h["Ana"].get(), "a.com")
        self.assertTrue(h["Ana"].empty())
        self.assertEqual(h["Caro"].get(), "c.com")
        self.assertTrue(h["Caro"].empty())
        self.assertEqual(h["Beto"].get(), "b1.com")
        self.assertTrue(h["Beto"].empty())

    def test_llamadas_sucesivas_hasta_vaciar(self):
        p = Pila()
        p.put("a.com")
        p.put("b.com")
        p.put("c.com")
        h = {"Ana": p}
        self.assertEqual(navegar_atras(h, "Ana"), "c.com")
        self.assertEqual(navegar_atras(h, "Ana"), "b.com")
        self.assertEqual(navegar_atras(h, "Ana"), "a.com")
        self.assertTrue(h["Ana"].empty())

    def test_despues_de_visitar_vuelve_al_ultimo_sitio(self):
        h = {}
        visitar_sitio(h, "Ana", "google.com")
        visitar_sitio(h, "Ana", "uba.ar")
        self.assertEqual(navegar_atras(h, "Ana"), "uba.ar")
        self.assertEqual(h["Ana"].get(), "google.com")
        self.assertTrue(h["Ana"].empty())

if __name__ == "__main__":
    unittest.main()
