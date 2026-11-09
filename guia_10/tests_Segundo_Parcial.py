import unittest
from Segundo_Parcial import *

class TestsSegundoParcial(unittest.TestCase):

    ## EJERCICIO 5

    def test_promedio_de_salidas_normal(self):
        registro = {
            "Pepe": [10,20,30,40,50,0,61],
            "Porky":[1,1,1,1,1,1,61],
            "Grep": [30,30,30,30,0,0,61]
        }

        expected_res = {
            "Pepe": (5,30),
            "Porky": (6,1),
            "Grep": (4,30)
        }
        self.assertEqual(promedio_de_salidas(registro),expected_res)

    def test_0_0_troll_face_quest(self):

        registro = {
            "Pepe": [10,20,30,40,50,0,0],
            "Porky":[61,61,61,61,61,61,61],
            "Grep": [30,30,30,30,0,0,0]
        }

        expected_res = {
            "Pepe": (5,30),
            "Porky": (0,0.0),
            "Grep": (4,30)
        }
        self.assertEqual(promedio_de_salidas(registro),expected_res)

    def test_promedio_de_salidas_no_fue_a_ninguna(self):
        registro = {
            "Eli": [0,0,0],
            "Fede": [0,20,0]
        }

        expected_res = {
            "Eli": (0,0.0),
            "Fede": (1,20.0)
        }
        self.assertEqual(promedio_de_salidas(registro),expected_res)

    def test_promedio_de_salidas_bordes_1_y_60_cuentan(self):
        registro = {
            "Caro": [1,60,0,61]
        }

        expected_res = {
            "Caro": (2,30.5)
        }
        self.assertEqual(promedio_de_salidas(registro),expected_res)

    def test_promedio_de_salidas_promedio_con_decimales(self):
        registro = {
            "Dani": [10,15,0],
            "Gabi": [10,10,11]
        }

        expected_res = {
            "Dani": (2,12.5),
            "Gabi": (3,31/3)
        }
        self.assertEqual(promedio_de_salidas(registro),expected_res)

    def test_promedio_de_salidas_un_solo_integrante_un_solo_tiempo(self):
        registro = {
            "Ana": [45]
        }

        expected_res = {
            "Ana": (1,45.0)
        }
        self.assertEqual(promedio_de_salidas(registro),expected_res)

    ## EJERCICIO 6

    def test_tiempo_mas_rapido_hay_un_unico_tiempo(self):
        tiempo = [30]

        self.assertEqual(tiempo_mas_rapido(tiempo),0)

    def test_hay_varios_tiempos(self):
        tiempo = [1,3,5,20,30,20,20,30,20,30]

        self.assertEqual(tiempo_mas_rapido(tiempo),0)

    def test_el_ultimo(self):
        tiempo = [10,9,8,61,7,61,5,3,2,1]
        self.assertEqual(tiempo_mas_rapido(tiempo),9)

    def test_tiempo_mas_rapido_ignora_0_y_61(self):
        tiempo = [0,61,45,0,20,61]
        self.assertEqual(tiempo_mas_rapido(tiempo),4)

    def test_tiempo_mas_rapido_empate_gana_el_primero(self):
        tiempo = [40,10,61,10,0]
        self.assertEqual(tiempo_mas_rapido(tiempo),1)

    def test_tiempo_mas_rapido_un_unico_valido_entre_invalidos(self):
        tiempo = [0,61,0,59,61]
        self.assertEqual(tiempo_mas_rapido(tiempo),3)

    def test_tiempo_mas_rapido_primero_invalido_despues_valido_mas_lento(self):
        tiempo = [0,60,61]
        self.assertEqual(tiempo_mas_rapido(tiempo),1)

    ## EJERCICIO 7

    def test_racha_mas_larga_solo_un_elemento(self):
        tiempos = [30]
        expected_res = (0,0)
        self.assertEqual(racha_mas_larga(tiempos),expected_res)


    def test_racha_mas_larga_en_el_medio(self):
        tiempos = [1,2,61,0,1,32,30,50,56,61,1,2,3]
        expected_res = (4,8)
        self.assertEqual(racha_mas_larga(tiempos),expected_res)

    def test_racha_mas_larga_al_final(self):
        tiempos = [1,2,61,0,1,32,30,61,1,2,3,4,5,6]
        expected_res = (8,13)
        self.assertEqual(racha_mas_larga(tiempos),expected_res)

    def test_hay_dos_rachas_iguales_gana_las_del_principio(self):
        tiempos = [1,2,3,4,61,1,2,3,4,61,1,2,3,4,61]
        expected_res = (0,3)
        self.assertEqual(racha_mas_larga(tiempos),expected_res)

    def test_racha_mas_larga_el_0_tambien_corta(self):
        tiempos = [1,2,0,3,4,5]
        expected_res = (3,5)
        self.assertEqual(racha_mas_larga(tiempos),expected_res)

    def test_racha_mas_larga_empieza_con_invalidos(self):
        tiempos = [0,61,10,20]
        expected_res = (2,3)
        self.assertEqual(racha_mas_larga(tiempos),expected_res)

    def test_racha_mas_larga_un_unico_valido_entre_invalidos(self):
        tiempos = [0,61,25,0]
        expected_res = (2,2)
        self.assertEqual(racha_mas_larga(tiempos),expected_res)

    def test_racha_mas_larga_la_segunda_es_mas_larga(self):
        tiempos = [10,61,10,20,30,0,10,20]
        expected_res = (2,4)
        self.assertEqual(racha_mas_larga(tiempos),expected_res)

    def test_racha_mas_larga_empate_de_rachas_de_uno(self):
        tiempos = [5,0,6,61,7]
        expected_res = (0,0)
        self.assertEqual(racha_mas_larga(tiempos),expected_res)

    def test_racha_mas_larga_todos_validos(self):
        tiempos = [5,10,15]
        expected_res = (0,2)
        self.assertEqual(racha_mas_larga(tiempos),expected_res)

    def test_racha_mas_larga_bordes_1_y_60_son_validos(self):
        tiempos = [60,1,61,0,30]
        expected_res = (0,1)
        self.assertEqual(racha_mas_larga(tiempos),expected_res)

    ## EJERCICIO 8

    def test_escape_en_solitario_normal(self):
        amigos_por_salas = [[0,0,30,0],
                            [0,0,61,0],
                            [10,0,30,0],
                            [0,0,0,0]]
        self.assertEqual(escape_en_solitario(amigos_por_salas),[0,1])

    def test_escape_en_solitario_ninguna(self):
        amigos_por_salas = [[0,0,0,0],
                            [5,5,5,5],
                            [0,0,20,61]]
        self.assertEqual(escape_en_solitario(amigos_por_salas),[])

    def test_escape_en_solitario_todas(self):
        amigos_por_salas = [[0,0,1,0],
                            [0,0,60,0],
                            [0,0,61,0]]
        self.assertEqual(escape_en_solitario(amigos_por_salas),[0,1,2])

    def test_escape_en_solitario_el_61_cuenta_como_que_fue(self):
        amigos_por_salas = [[61,0,20,0],
                            [0,61,20,0],
                            [0,0,20,61],
                            [0,0,20,0]]
        self.assertEqual(escape_en_solitario(amigos_por_salas),[3])

    def test_escape_en_solitario_una_sola_sala(self):
        amigos_por_salas = [[0,0,45,0]]
        self.assertEqual(escape_en_solitario(amigos_por_salas),[0])


if __name__ == "__main__":
    unittest.main()
