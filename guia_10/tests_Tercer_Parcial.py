import unittest
import copy
from Tercer_Parcial import *

DESVIA = "me desvío siempre"
NO_DESVIA = "me la banco y no me desvío"


class TestEnfrentamientoUnico(unittest.TestCase):
    """Torneos de 2 jugadores: se cubren las 4 combinaciones posibles."""

    def test_ambos_se_desvian(self):
        estrategias = {"Ana": DESVIA, "Beto": DESVIA}
        self.assertEqual(torneo_de_gallinas(estrategias), {"Ana": -10, "Beto": -10})

    def test_ninguno_se_desvia(self):
        estrategias = {"Ana": NO_DESVIA, "Beto": NO_DESVIA}
        self.assertEqual(torneo_de_gallinas(estrategias), {"Ana": -5, "Beto": -5})

    def test_primero_se_desvia_segundo_no(self):
        estrategias = {"Ana": DESVIA, "Beto": NO_DESVIA}
        self.assertEqual(torneo_de_gallinas(estrategias), {"Ana": -15, "Beto": 10})

    def test_primero_no_se_desvia_segundo_si(self):
        estrategias = {"Ana": NO_DESVIA, "Beto": DESVIA}
        self.assertEqual(torneo_de_gallinas(estrategias), {"Ana": 10, "Beto": -15})


class TestTorneosHomogeneos(unittest.TestCase):
    """Todos los jugadores usan la misma estrategia."""

    def test_tres_jugadores_todos_se_desvian(self):
        estrategias = {"A": DESVIA, "B": DESVIA, "C": DESVIA}
        self.assertEqual(torneo_de_gallinas(estrategias), {"A": -20, "B": -20, "C": -20})

    def test_tres_jugadores_ninguno_se_desvia(self):
        estrategias = {"A": NO_DESVIA, "B": NO_DESVIA, "C": NO_DESVIA}
        self.assertEqual(torneo_de_gallinas(estrategias), {"A": -10, "B": -10, "C": -10})

    def test_cinco_jugadores_todos_se_desvian(self):
        estrategias = {nombre: DESVIA for nombre in ["A", "B", "C", "D", "E"]}
        esperado = {nombre: -40 for nombre in estrategias}
        self.assertEqual(torneo_de_gallinas(estrategias), esperado)


class TestTorneosMixtos(unittest.TestCase):
    """Mezcla de estrategias con varios jugadores."""

    def test_dos_desvian_uno_no(self):
        # Desviadores: -10 (entre ellos) - 15 (contra C) = -25
        # C: +10 + 10 = 20
        estrategias = {"A": DESVIA, "B": DESVIA, "C": NO_DESVIA}
        self.assertEqual(torneo_de_gallinas(estrategias), {"A": -25, "B": -25, "C": 20})

    def test_uno_desvia_dos_no(self):
        # A: -15 - 15 = -30
        # B y C: +10 (contra A) - 5 (entre ellos) = 5
        estrategias = {"A": DESVIA, "B": NO_DESVIA, "C": NO_DESVIA}
        self.assertEqual(torneo_de_gallinas(estrategias), {"A": -30, "B": 5, "C": 5})

    def test_cuatro_jugadores_mitad_y_mitad(self):
        # Desviadores: -10 - 15 - 15 = -40
        # No desviadores: +10 + 10 - 5 = 15
        estrategias = {"A": DESVIA, "B": NO_DESVIA, "C": DESVIA, "D": NO_DESVIA}
        self.assertEqual(
            torneo_de_gallinas(estrategias), {"A": -40, "B": 15, "C": -40, "D": 15}
        )

    def test_resultado_con_puntaje_cero(self):
        # B y C: +10 (contra A) - 5 - 5 (contra los otros dos) = 0
        estrategias = {"A": DESVIA, "B": NO_DESVIA, "C": NO_DESVIA, "D": NO_DESVIA}
        self.assertEqual(
            torneo_de_gallinas(estrategias), {"A": -45, "B": 0, "C": 0, "D": 0}
        )

    def test_torneo_grande(self):
        # 6 desviadores y 4 no desviadores:
        # desviador: -10 * 5 - 15 * 4 = -110
        # no desviador: +10 * 6 - 5 * 3 = 45
        estrategias = {}
        for i in range(6):
            estrategias["desv" + str(i)] = DESVIA
        for i in range(4):
            estrategias["banca" + str(i)] = NO_DESVIA
        resultado = torneo_de_gallinas(estrategias)
        for i in range(6):
            self.assertEqual(resultado["desv" + str(i)], -110)
        for i in range(4):
            self.assertEqual(resultado["banca" + str(i)], 45)


class TestPropiedadesDelResultado(unittest.TestCase):
    """Chequeos sobre los 'asegura' y sobre el parámetro 'in'."""

    def test_claves_iguales(self):
        estrategias = {"A": DESVIA, "B": NO_DESVIA, "C": DESVIA}
        resultado = torneo_de_gallinas(estrategias)
        self.assertEqual(set(resultado.keys()), set(estrategias.keys()))

    def test_valores_enteros(self):
        estrategias = {"A": DESVIA, "B": NO_DESVIA, "C": DESVIA}
        for valor in torneo_de_gallinas(estrategias).values():
            self.assertIsInstance(valor, int)

    def test_no_modifica_estrategias(self):
        # estrategias es un parámetro 'in': no se debe modificar
        estrategias = {"A": DESVIA, "B": NO_DESVIA, "C": DESVIA}
        copia = copy.deepcopy(estrategias)
        torneo_de_gallinas(estrategias)
        self.assertEqual(estrategias, copia)

    def test_orden_de_insercion_no_importa(self):
        e1 = {"A": DESVIA, "B": NO_DESVIA, "C": NO_DESVIA}
        e2 = {"C": NO_DESVIA, "A": DESVIA, "B": NO_DESVIA}
        self.assertEqual(torneo_de_gallinas(e1), torneo_de_gallinas(e2))

    def test_nombres_largos_y_con_espacios(self):
        estrategias = {"Juan Pérez": DESVIA, "x": NO_DESVIA}
        self.assertEqual(
            torneo_de_gallinas(estrategias), {"Juan Pérez": -15, "x": 10}
        )

    def test_dos_llamadas_dan_lo_mismo(self):
        # Detecta estado compartido entre llamadas (p. ej. un dict global)
        estrategias = {"A": DESVIA, "B": NO_DESVIA}
        self.assertEqual(torneo_de_gallinas(estrategias), torneo_de_gallinas(estrategias))


COMUN = "común"
VIP = "vip"
 
 
# ---------- Helpers ----------
 
def armar_cola(elementos: list) -> Cola:
    cola = Cola()
    for e in elementos:
        cola.put(e)
    return cola
 
 
def cola_a_lista(cola: Cola) -> list:
    """Devuelve los elementos de la cola en orden SIN consumirla."""
    lista = []
    aux = Cola()
    while not cola.empty():
        e = cola.get()
        lista.append(e)
        aux.put(e)
    while not aux.empty():
        cola.put(aux.get())
    return lista
 
 
class BaseTest(unittest.TestCase):
    def assertReordena(self, clientes: list, esperado: list):
        fila = armar_cola(clientes)
        res = reordenar_cola_priorizando_vips(fila)
        self.assertIsInstance(res, Cola)
        self.assertEqual(cola_a_lista(res), esperado)
 
 
# ---------- Casos básicos ----------
 
class TestCasosBasicos(BaseTest):
 
    def test_cola_vacia(self):
        self.assertReordena([], [])
 
    def test_un_cliente_comun(self):
        self.assertReordena([("Ana", COMUN)], ["Ana"])
 
    def test_un_cliente_vip(self):
        self.assertReordena([("Ana", VIP)], ["Ana"])
 
    def test_comun_y_despues_vip(self):
        self.assertReordena([("Ana", COMUN), ("Beto", VIP)], ["Beto", "Ana"])
 
    def test_vip_y_despues_comun(self):
        self.assertReordena([("Ana", VIP), ("Beto", COMUN)], ["Ana", "Beto"])
 
 
# ---------- Colas homogéneas: el orden no cambia ----------
 
class TestColasHomogeneas(BaseTest):
 
    def test_todos_comunes(self):
        clientes = [("A", COMUN), ("B", COMUN), ("C", COMUN), ("D", COMUN)]
        self.assertReordena(clientes, ["A", "B", "C", "D"])
 
    def test_todos_vips(self):
        clientes = [("A", VIP), ("B", VIP), ("C", VIP), ("D", VIP)]
        self.assertReordena(clientes, ["A", "B", "C", "D"])
 
 
# ---------- Colas mixtas ----------
 
class TestColasMixtas(BaseTest):
 
    def test_ya_ordenada(self):
        clientes = [("A", VIP), ("B", VIP), ("C", COMUN), ("D", COMUN)]
        self.assertReordena(clientes, ["A", "B", "C", "D"])
 
    def test_orden_invertido(self):
        clientes = [("A", COMUN), ("B", COMUN), ("C", VIP), ("D", VIP)]
        self.assertReordena(clientes, ["C", "D", "A", "B"])
 
    def test_alternados_empezando_por_comun(self):
        clientes = [("A", COMUN), ("B", VIP), ("C", COMUN), ("D", VIP), ("E", COMUN)]
        self.assertReordena(clientes, ["B", "D", "A", "C", "E"])
 
    def test_alternados_empezando_por_vip(self):
        clientes = [("A", VIP), ("B", COMUN), ("C", VIP), ("D", COMUN), ("E", VIP)]
        self.assertReordena(clientes, ["A", "C", "E", "B", "D"])
 
    def test_un_vip_al_final(self):
        clientes = [("A", COMUN), ("B", COMUN), ("C", COMUN), ("D", VIP)]
        self.assertReordena(clientes, ["D", "A", "B", "C"])
 
    def test_un_comun_al_principio(self):
        clientes = [("A", COMUN), ("B", VIP), ("C", VIP), ("D", VIP)]
        self.assertReordena(clientes, ["B", "C", "D", "A"])
 
    def test_nombres_no_ordenados_alfabeticamente(self):
        # Detecta implementaciones que ordenan por nombre en vez de respetar la cola
        clientes = [("Zoe", COMUN), ("Mia", VIP), ("Ana", COMUN), ("Bruno", VIP)]
        self.assertReordena(clientes, ["Mia", "Bruno", "Zoe", "Ana"])
 
    def test_cola_grande(self):
        clientes = []
        vips_esperados = []
        comunes_esperados = []
        for i in range(50):
            nombre = "cliente" + str(i)
            if i % 3 == 0:
                clientes.append((nombre, VIP))
                vips_esperados.append(nombre)
            else:
                clientes.append((nombre, COMUN))
                comunes_esperados.append(nombre)
        self.assertReordena(clientes, vips_esperados + comunes_esperados)
 
 
# ---------- Propiedades de la especificación ----------
 
class TestPropiedades(unittest.TestCase):
 
    def setUp(self):
        self.clientes = [
            ("Ana", COMUN), ("Beto", VIP), ("Caro", COMUN),
            ("Dani", VIP), ("Eli", COMUN), ("Fede", VIP),
        ]
        self.fila = armar_cola(self.clientes)
        self.res = cola_a_lista(reordenar_cola_priorizando_vips(self.fila))
 
    def test_misma_longitud(self):
        self.assertEqual(len(self.res), len(self.clientes))
 
    def test_sin_repetidos(self):
        self.assertEqual(len(self.res), len(set(self.res)))
 
    def test_todo_valor_es_nombre_de_la_fila(self):
        nombres = [nombre for nombre, _ in self.clientes]
        for nombre in self.res:
            self.assertIn(nombre, nombres)
 
    def test_res_contiene_strings_no_tuplas(self):
        for elem in self.res:
            self.assertIsInstance(elem, str)
 
    def test_ningun_comun_antes_que_un_vip(self):
        tipo = dict(self.clientes)
        vio_comun = False
        for nombre in self.res:
            if tipo[nombre] == COMUN:
                vio_comun = True
            else:
                self.assertFalse(vio_comun, nombre + " (vip) aparece después de un común")
 
    def test_no_modifica_fila_clientes(self):
        # filaClientes es un parámetro 'in': al terminar debe seguir igual
        self.assertEqual(cola_a_lista(self.fila), self.clientes)
 
    def test_devuelve_una_cola_nueva(self):
        fila = armar_cola(self.clientes)
        res = reordenar_cola_priorizando_vips(fila)
        self.assertIsNot(res, fila)




if __name__ == "__main__":
    unittest.main(verbosity=2)
