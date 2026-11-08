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

if __name__ == "__main__":
    unittest.main()
