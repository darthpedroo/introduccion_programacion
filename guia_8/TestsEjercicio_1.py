import unittest
from Ejercicio_1 import *

class TestGenerarNrosAlAzar(unittest.TestCase):

    def test_generar_un_numero_al_azar(self):
        res = generar_nros_al_azar(1,1,10000)
        self.assertTrue(cantidad_elementos(res)==1)

    def test_generar_varios_numeros_al_azar(self):
        res = generar_nros_al_azar(100,1,10000)
        self.assertTrue(cantidad_elementos(res)==100)


    ## EJERCICIO 3

    def test_buscar_el_maximo_hay_un_unico_elemento(self):
        pila = crear_pila_con_lista([1])
        self.assertTrue(buscar_el_maximo(pila)==1)

    def test_buscar_el_maximo_hay_muchos_elementos(self):
        pila = crear_pila_con_lista([1,2,3,4,5,6,100,-100,101010])
        self.assertTrue(buscar_el_maximo(pila)==101010)
    ## Buscar Nota Maxima

    def test_buscar_nota_maxima_hay_solo_una_nota(self):
        notas = crear_pila_con_lista([("Led Zeppelin",10)])
        self.assertTrue(buscar_nota_maxima(notas)==("Led Zeppelin",10))

    def test_buscar_nota_maxima_hay_varias_notas(self):
        notas = crear_pila_con_lista([("TOOL",10),("A Perfect Circle",9),("The Hives",6)])
        res=buscar_nota_maxima(notas)
        self.assertTrue(buscar_nota_maxima(notas)==("TOOL",10))
        self.assertTrue(buscar_nota_maxima(notas)==("TOOL",10))
    
    # EJERCICIO 5

    # Bien Formada: 1 + (5+10)*2+(100+10)/2
    # Mal Formada 1: (10 + 20)*5+(1*2)+)
    # Mal Formada 2: )10 + 15 ) ((
    def test_esta_bien_balanceada(self):
        expresion = "(10+1)"
        self.assertTrue(esta_bien_balanceada(expresion))
    
    def test_esta_bien_balanceada_no_tiene_parentesis(self):
        expresion = "5+10*123-1000"
        self.assertTrue(esta_bien_balanceada(expresion))

    def test_esta_balanceada_con_muchas_cosas(self):
        expresion = "1 + (5+10)*2+(100+10)/2"
        self.assertTrue(esta_bien_balanceada(expresion))
    
    def test_no_esta_balanceada(self):
        expresion = ")10 + (1200)("
        self.assertFalse(esta_bien_balanceada(expresion))

    def test_cadena_vacia(self):
        self.assertTrue(esta_bien_balanceada(""))

    def test_solo_espacios(self):
        self.assertTrue(esta_bien_balanceada("   "))

    def test_sin_parentesis(self):
        self.assertTrue(esta_bien_balanceada("1 + 2 * 3 - 4 / 5"))

    def test_un_solo_numero(self):
        self.assertTrue(esta_bien_balanceada("42"))

    # --- Casos verdaderos ---

    def test_par_vacio(self):
        self.assertTrue(esta_bien_balanceada("()"))

    def test_par_con_contenido(self):
        self.assertTrue(esta_bien_balanceada("(1 + 2)"))

    def test_anidados(self):
        self.assertTrue(esta_bien_balanceada("((()))"))

    def test_consecutivos(self):
        self.assertTrue(esta_bien_balanceada("()()()"))

    def test_anidados_y_consecutivos(self):
        self.assertTrue(esta_bien_balanceada("(()())(())"))

    def test_ejemplo_enunciado_1(self):
        self.assertTrue(esta_bien_balanceada("1 + (2 * 3 - (20 / 5))"))

    def test_ejemplo_enunciado_2(self):
        self.assertTrue(esta_bien_balanceada("10 * (1 + (2 * (-1)))"))

    def test_sin_espacios(self):
        self.assertTrue(esta_bien_balanceada("(1+2)*(3-4)/(5)"))

    def test_anidamiento_profundo(self):
        self.assertTrue(esta_bien_balanceada("(" * 100 + "1" + ")" * 100))

    # --- Falla la primera condición: distinta cantidad ---

    def test_solo_apertura(self):
        self.assertFalse(esta_bien_balanceada("("))

    def test_solo_cierre(self):
        self.assertFalse(esta_bien_balanceada(")"))

    def test_sobra_apertura(self):
        self.assertFalse(esta_bien_balanceada("((1 + 2)"))

    def test_sobra_cierre_al_final(self):
        self.assertFalse(esta_bien_balanceada("(1 + 2))"))

    def test_apertura_al_final(self):
        self.assertFalse(esta_bien_balanceada("(1 + 2) * ("))

    # --- Falla la segunda condición: misma cantidad, pero algún prefijo
    #     tiene más cierres que aperturas ---

    def test_invertidos(self):
        self.assertFalse(esta_bien_balanceada(")("))

    def test_cierre_prematuro_en_el_medio(self):
        self.assertFalse(esta_bien_balanceada("(1)) + ((2)"))

    def test_ejemplo_enunciado_falso(self):
        self.assertFalse(esta_bien_balanceada("1 + ) 2 * 3 ( ()"))

    def test_cierre_al_principio_con_contenido(self):
        self.assertFalse(esta_bien_balanceada(") 1 + 2 ("))

    # --- Fallan ambas condiciones ---

    def test_desbalanceado_y_mal_ordenado(self):
        self.assertFalse(esta_bien_balanceada(")(("))


## EJERCICIO 6

    def test_evaluar_expresion(self):
        expresion = "3 4 + 5 * 2 -"
        resultado = evaluar_expresion(expresion)
        self.assertTrue(resultado==33)
    

    def test_un_solo_numero(self):
        self.assertAlmostEqual(evaluar_expresion("5"), 5)

    def test_cero(self):
        self.assertAlmostEqual(evaluar_expresion("0"), 0)

    def test_numero_negativo_solo(self):
        self.assertAlmostEqual(evaluar_expresion("-7"), -7)

    def test_numero_de_varios_digitos(self):
        self.assertAlmostEqual(evaluar_expresion("1234"), 1234)

    # --- Cada operador por separado ---

    def test_suma(self):
        self.assertAlmostEqual(evaluar_expresion("3 4 +"), 7)

    def test_resta(self):
        self.assertAlmostEqual(evaluar_expresion("10 4 -"), 6)

    def test_multiplicacion(self):
        self.assertAlmostEqual(evaluar_expresion("6 7 *"), 42)

    def test_division_exacta(self):
        self.assertAlmostEqual(evaluar_expresion("20 5 /"), 4)

    # --- Orden de los operandos (operaciones no conmutativas) ---

    def test_resta_respeta_orden(self):
        self.assertAlmostEqual(evaluar_expresion("4 10 -"), -6)

    def test_division_respeta_orden(self):
        self.assertAlmostEqual(evaluar_expresion("2 8 /"), 0.25)

    # --- División real (el resultado es un número real) ---

    def test_division_no_entera(self):
        self.assertAlmostEqual(evaluar_expresion("7 2 /"), 3.5)

    def test_division_periodica(self):
        self.assertAlmostEqual(evaluar_expresion("1 3 /"), 1 / 3)

    def test_division_con_resultado_negativo(self):
        self.assertAlmostEqual(evaluar_expresion("-7 2 /"), -3.5)

    # --- Números negativos y cero como operandos ---

    def test_suma_con_negativo(self):
        self.assertAlmostEqual(evaluar_expresion("5 -3 +"), 2)

    def test_resta_de_negativo(self):
        self.assertAlmostEqual(evaluar_expresion("5 -3 -"), 8)

    def test_producto_de_negativos(self):
        self.assertAlmostEqual(evaluar_expresion("-2 -4 *"), 8)

    def test_multiplicar_por_cero(self):
        self.assertAlmostEqual(evaluar_expresion("123 0 *"), 0)

    def test_cero_dividido(self):
        self.assertAlmostEqual(evaluar_expresion("0 5 /"), 0)

    # --- Expresiones compuestas ---

    def test_ejemplo_enunciado(self):
        # (3 + 4) * 2
        self.assertAlmostEqual(evaluar_expresion("3 4 + 2 *"), 14)

    def test_operadores_encadenados(self):
        # ((1 + 2) + 3) + 4
        self.assertAlmostEqual(evaluar_expresion("1 2 + 3 + 4 +"), 10)

    def test_operandos_acumulados_en_la_pila(self):
        # 1 + (2 + (3 + 4)): se apilan todos antes de operar
        self.assertAlmostEqual(evaluar_expresion("1 2 3 4 + + +"), 10)

    def test_precedencia_implicita(self):
        # 2 + 3 * 4
        self.assertAlmostEqual(evaluar_expresion("2 3 4 * +"), 14)

    def test_dos_subexpresiones(self):
        # (5 + 1) * (6 - 2)
        self.assertAlmostEqual(evaluar_expresion("5 1 + 6 2 - *"), 24)

    def test_todos_los_operadores(self):
        # ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1))
        self.assertAlmostEqual(
            evaluar_expresion("15 7 1 1 + - / 3 * 2 1 1 + + -"), 5)

    def test_resultado_intermedio_no_entero(self):
        # (1 / 2) + (1 / 4)
        self.assertAlmostEqual(evaluar_expresion("1 2 / 1 4 / +"), 0.75)

    def test_resultado_negativo(self):
        # (2 - 5) * 3
        self.assertAlmostEqual(evaluar_expresion("2 5 - 3 *"), -9)
    
    # EJERCICIO 7
    # Las listas están en el mismo orden que usan crear_pila_con_lista y mostrar_pila.
    # Ej: [1,3,5,7,9] y [2,4,6,8,10] -> [1,2,3,4,5,6,7,8,9,10]

    def pila_a_lista(self, p: Pila) -> list:
        # Devuelve los elementos en el mismo orden que imprime mostrar_pila, sin modificar p.
        copia: Pila = copiar_pila(p)
        lista: list = []
        while not copia.empty():
            lista.append(copia.get())
        return lista

    def assertIntercala(self, l1: list, l2: list, esperado: list):
        res = intercalar(crear_pila_con_lista(l1), crear_pila_con_lista(l2))
        self.assertEqual(self.pila_a_lista(res), esperado)

    def test_pilas_vacias(self):
        res = intercalar(Pila(), Pila())
        self.assertTrue(res.empty())

    def test_un_elemento_cada_una(self):
        self.assertIntercala([1], [2], [1, 2])

    # --- Orden: alternado, empezando por p1 ---

    def test_ejemplo_main(self):
        self.assertIntercala([1, 3, 5, 7, 9], [2, 4, 6, 8, 10],
                             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_dos_elementos(self):
        self.assertIntercala([1, 2], ['a', 'b'], [1, 'a', 2, 'b'])

    def test_varios_elementos(self):
        self.assertIntercala([1, 2, 3, 4], ['a', 'b', 'c', 'd'],
                             [1, 'a', 2, 'b', 3, 'c', 4, 'd'])

    def test_elementos_no_ordenados(self):
        # Respeta el orden original aunque los valores no estén ordenados.
        self.assertIntercala([9, 1, 5], [3, 7, 2], [9, 3, 1, 7, 5, 2])

    # --- Elementos repetidos ---

    def test_repetidos_dentro_de_una_pila(self):
        self.assertIntercala([1, 1, 1], [2, 2, 2], [1, 2, 1, 2, 1, 2])

    def test_mismos_elementos_en_ambas(self):
        self.assertIntercala([1, 2, 3], [1, 2, 3], [1, 1, 2, 2, 3, 3])

    # --- Asegura: el tope de res es el tope de p2 (último de la lista) ---

    def test_tope_es_tope_de_p2(self):
        res = intercalar(crear_pila_con_lista([1, 2, 3]),
                         crear_pila_con_lista([10, 20, 30]))
        self.assertEqual(self.pila_a_lista(res)[-1], 30)

    def test_fondo_es_fondo_de_p1(self):
        res = intercalar(crear_pila_con_lista([1, 2, 3]),
                         crear_pila_con_lista([10, 20, 30]))
        self.assertEqual(self.pila_a_lista(res)[0], 1)

    # --- Asegura: el tamaño de res es el doble del de p1 ---

    def test_tamanio_doble(self):
        res = intercalar(crear_pila_con_lista([1, 2, 3, 4, 5]),
                         crear_pila_con_lista([6, 7, 8, 9, 10]))
        self.assertEqual(cantidad_elementos(res), 10)

    def test_tamanio_doble_un_elemento(self):
        res = intercalar(crear_pila_con_lista([1]), crear_pila_con_lista([2]))
        self.assertEqual(cantidad_elementos(res), 2)

    # --- Pilas grandes ---

    def test_pilas_grandes(self):
        l1 = list(range(0, 200, 2))   # pares
        l2 = list(range(1, 200, 2))   # impares
        self.assertIntercala(l1, l2, list(range(200)))

    # --- Parámetros "in": p1 y p2 no se modifican ---

    def test_no_modifica_p1(self):
        p1 = crear_pila_con_lista([1, 2, 3])
        p2 = crear_pila_con_lista([4, 5, 6])
        intercalar(p1, p2)
        self.assertEqual(self.pila_a_lista(p1), [1, 2, 3])

    def test_no_modifica_p2(self):
        p1 = crear_pila_con_lista([1, 2, 3])
        p2 = crear_pila_con_lista([4, 5, 6])
        intercalar(p1, p2)
        self.assertEqual(self.pila_a_lista(p2), [4, 5, 6])

    def test_res_es_pila_nueva(self):
        p1 = crear_pila_con_lista([1, 2])
        p2 = crear_pila_con_lista([3, 4])
        res = intercalar(p1, p2)
        self.assertIsNot(res, p1)
        self.assertIsNot(res, p2)

if __name__ == "__main__":
    unittest.main()

