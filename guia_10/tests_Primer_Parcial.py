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

    def test_stock_de_producto_con_stock_cero(self):

        stock = [("Collar",5), ("Collar",0), ("Collar",3)]
        res = {"Collar": (0,5)
                }
        self.assertEqual(stock_productos(stock), res)

    def test_stock_de_producto_minimo_y_maximo_en_el_medio(self):

        stock = [("Arena",50), ("Arena",80), ("Arena",20), ("Arena",50)]
        res = {"Arena": (20,80)
                }
        self.assertEqual(stock_productos(stock), res)

    def test_stock_de_producto_lista_vacia(self):

        stock = []
        res = {}
        self.assertEqual(stock_productos(stock), res)

    # EJERCICIO 2


    def test_filtrar_codigos_primos_no_hay_ninguno(self):
        codigos = [222,444,666,888,912,1000,666666]

        self.assertEqual(filtrar_codigos_primos(codigos), []) # el 000 es 0, que no es primo

    def test_filtrar_codigos_primos_lista_vacia(self):
        codigos = []
        self.assertEqual(filtrar_codigos_primos(codigos), [])

    def test_filtar_codigos_primos_ejemplos_catedra(self):
        codigos = [1002,101,9011,107,103,100000103, 1000107]
        self.assertEqual(filtrar_codigos_primos(codigos), codigos)

    def test_filtrar_codigos_primos_algunos_nomas(self):
        codigos = [1002,444, 101, 222, 107,]
        self.assertEqual(filtrar_codigos_primos(codigos), [1002,101,107])

    def test_filtrar_codigos_primos_el_001_no_es_primo(self):
        codigos = [1001, 5001, 100]
        self.assertEqual(filtrar_codigos_primos(codigos), [])

    def test_filtrar_codigos_primos_un_digito_con_ceros_adelante(self):
        codigos = [100003, 100004, 100005, 100007, 100009]
        self.assertEqual(filtrar_codigos_primos(codigos), [100003, 100005, 100007])

    def test_filtrar_codigos_primos_bordes_de_tres_digitos(self):
        codigos = [997, 999, 4997, 1998]
        self.assertEqual(filtrar_codigos_primos(codigos), [997, 4997])

    def test_filtrar_codigos_primos_mantiene_el_orden(self):
        codigos = [107, 222, 2003, 101]
        self.assertEqual(filtrar_codigos_primos(codigos), [107, 2003, 101])

    # EJERCICIO 3

    def test_lista_mas_larga_es_la_unica(self):
        pacientes = ["perro", "perro", "perro", "perro"]
        self.assertEqual(subsecuencia_mas_larga(pacientes),0)

    def test_lista_mas_larga_surtido(self):
        pacientes = ["perro", "gato", "gato", "perro","perro","perro", "perro", "gato", "gato", "perro", "perro"]
        self.assertEqual(subsecuencia_mas_larga(pacientes), 0) # todos son perro o gato: la subsecuencia es la lista entera

    def test_hay_dos_listas_igual_de_largas_pero_gana_la_primera(self):
        pacientes = ["perro", "gato", "loro", "gato", "perro", "conejo"]
        self.assertEqual(subsecuencia_mas_larga(pacientes), 0)

    def test_dos_elementos_perro_y_gato(self):
        pacientes = ["perro", "gato"]
        self.assertEqual(subsecuencia_mas_larga(pacientes), 0)

    def test_lista_mas_larga_mezcla_perros_y_gatos(self):
        pacientes = ["perro", "loro", "gato", "perro", "gato", "conejo", "perro"]
        self.assertEqual(subsecuencia_mas_larga(pacientes), 2)

    def test_lista_mas_larga_empieza_con_otro_animal(self):
        pacientes = ["loro", "iguana", "gato"]
        self.assertEqual(subsecuencia_mas_larga(pacientes), 2)

    def test_lista_mas_larga_esta_al_final(self):
        pacientes = ["gato", "loro", "perro", "gato", "perro"]
        self.assertEqual(subsecuencia_mas_larga(pacientes), 2)

    def test_lista_mas_larga_un_solo_elemento(self):
        pacientes = ["gato"]
        self.assertEqual(subsecuencia_mas_larga(pacientes), 0)

    def test_lista_mas_larga_la_segunda_es_mas_larga_que_la_primera(self):
        pacientes = ["perro", "gato", "conejo", "gato", "gato", "perro", "loro", "perro"]
        self.assertEqual(subsecuencia_mas_larga(pacientes), 3)

    # EJERCICIO 4

    def test_un_responsable_por_turno_un_dia_todo_igual(self):
        grilla = [["Ana"], ["Ana"], ["Ana"], ["Ana"],
                  ["Beto"], ["Beto"], ["Beto"], ["Beto"]]
        self.assertEqual(un_responsable_por_turno(grilla), [(True, True)])

    def test_un_responsable_por_turno_un_dia_misma_persona_todo_el_dia(self):
        grilla = [["Ana"], ["Ana"], ["Ana"], ["Ana"],
                  ["Ana"], ["Ana"], ["Ana"], ["Ana"]]
        self.assertEqual(un_responsable_por_turno(grilla), [(True, True)])

    def test_un_responsable_por_turno_falla_manana_en_un_dia_y_tarde_en_otro(self):
        grilla = [["Ana", "Ana"],
                  ["Ana", "Ana"],
                  ["Beto", "Ana"],
                  ["Ana", "Ana"],
                  ["Caro", "Caro"],
                  ["Caro", "Dani"],
                  ["Caro", "Caro"],
                  ["Caro", "Caro"]]
        self.assertEqual(un_responsable_por_turno(grilla), [(False, True), (True, False)])

    def test_un_responsable_por_turno_bordes_entre_manana_y_tarde(self):
        grilla = [["Ana", "Ana", "Ana"],
                  ["Ana", "Ana", "Ana"],
                  ["Ana", "Ana", "Ana"],
                  ["Beto", "Ana", "Ana"],
                  ["Beto", "Beto", "Ana"],
                  ["Beto", "Beto", "Ana"],
                  ["Beto", "Beto", "Ana"],
                  ["Beto", "Beto", "Caro"]]
        self.assertEqual(un_responsable_por_turno(grilla), [(False, True), (True, True), (True, False)])

    def test_un_responsable_por_turno_semana_casi_completa(self):
        grilla = [["Ana", "Beto", "Caro", "Dani", "Eli", "Fede", "Gabi"],
                  ["Ana", "Beto", "Caro", "Dani", "Eli", "Fede", "Gabi"],
                  ["Ana", "Beto", "Caro", "Dani", "Eli", "Fede", "Gabi"],
                  ["Ana", "Beto", "Caro", "Dani", "Eli", "Fede", "Ana"],
                  ["Gabi", "Fede", "Eli", "Dani", "Caro", "Beto", "Ana"],
                  ["Gabi", "Fede", "Eli", "Dani", "Caro", "Beto", "Ana"],
                  ["Gabi", "Fede", "Eli", "Ana", "Caro", "Beto", "Ana"],
                  ["Gabi", "Fede", "Eli", "Dani", "Caro", "Beto", "Ana"]]
        self.assertEqual(un_responsable_por_turno(grilla), [(True, True), (True, True), (True, True), (True, False), (True, True), (True, True), (False, True)])


if __name__ == "__main__":
    unittest.main()