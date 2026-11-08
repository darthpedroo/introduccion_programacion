import unittest
from queue import Queue as Cola
from Ejercicio_2 import *


class TestsColas(unittest.TestCase):
    # EJERCICIO 8 and 9 

    def test_generar_nros_al_azar_con_cero_numeros(self):
        c = generar_nros_al_azar(0,0,10)
        
        self.assertEqual(cantidad_elementos(c),0)
    
    def test_generar_varios_numeros_al_azar(self):
        c = generar_nros_al_azar(10,10,100)
        self.assertEqual(cantidad_elementos(c),10)

    # EJERCICIO 10

    def test_buscar_el_maximo_al_final(self):
        c = generar_nros_al_azar(1000,1,100)
        maximo = 100000000
        c.put(maximo)
        self.assertEqual(buscar_el_maximo(c),maximo)

    def test_buscar_el_maximo_al_principio(self):
        c = Cola()
        c.put(1000)
        c.put(-10)
        c.put(0)

        self.assertEqual(buscar_el_maximo(c),1000)

    def test_buscar_el_maximo_esta_repetido(self):
        c = generar_nros_al_azar(100,777,777)
        c.put(-100)
        c.put(0)

        self.assertEqual(buscar_el_maximo(c),777)
    
    # EJERCICIO 11

    def test_buscar_nota_minima_solo_una_nota(self):
        c = Cola()
        notas = [("Meemaw",10)]
        for nota in notas:
            c.put(nota)
        self.assertEqual(buscar_nota_minima(c),notas[0])


    def test_buscar_nota_minima_solo_una_nota(self):
        c = Cola()
        notas = [("Meemaw",10)]
        for nota in notas:
            c.put(nota)
        self.assertEqual(buscar_nota_minima(c),notas[0])

    def test_buscar_nota_minima_varias_notas(self):
        c = Cola()
        notas = [("Meemaw",10),("El joven",1), ("Cooper",100)]
        for nota in notas:
            c.put(nota)
        self.assertEqual(buscar_nota_minima(c),notas[1])
    
    # Ejercicio 14

    def test_no_hay_pacientes_urgentes(self):
        c = Cola()
        pacientes = [(5,"porky", "doc"),(5,"porky", "doc"),(5,"porky", "doc"),(5,"porky", "doc")]
        for paciente in pacientes:
            c.put(paciente)

        self.assertEqual(pacientes_urgentes(c),0)

    def test_no_hay_pacientes_urgentes(self):
        c = Cola()
        pacientes = [(5,"porky", "doc"),(5,"porky", "doc"),(5,"porky", "doc"),(5,"porky", "doc")]
        for paciente in pacientes:
            c.put(paciente)

        self.assertEqual(pacientes_urgentes(c),0)

    def test_hay_un_paciente_urgente(self):
        c = Cola()
        pacientes = [(1,"porky", "doc"),(5,"porky", "doc"),(5,"porky", "doc"),(5,"porky", "doc")]
        for paciente in pacientes:
            c.put(paciente)

        self.assertEqual(pacientes_urgentes(c),1)

    def test_todos_pacientes_urgentes(self):
        c = Cola()
        pacientes = [(1,"porky", "doc"),(1,"porky", "doc"),(1,"porky", "doc"),(1,"porky", "doc")]
        for paciente in pacientes:
            c.put(paciente)

        self.assertEqual(pacientes_urgentes(c),4)

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

if __name__ == "__main__":
    unittest.main()
