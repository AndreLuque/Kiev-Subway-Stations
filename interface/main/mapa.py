import time
from typing import Dict, TypeVar

from .algoritmo_a_star import a_star
from .tads.graph.iundirected_graph import * 
from .tads.graph.undirected_graph import *
from .tads.graph.elements.vertex import *

V = TypeVar('V')


def initializeGraph():
    # Creamos un grafo no dirigido, que se define según la interfaz IUndicerectedGraph
    g: IUndirectedGraph[int, int] = UndirectedAdjacencyListGraph()

    """
        Se crea una lista con los nombres de las paradas y una con los costes (para cada linea)
        El coste es la distancia que recorre el metro entre dos paradas adyacentes (en metros)
        Fuente:    https://www.eway.in.ua/en/cities/kyiv 
        coste[i] ----> nombres[i]---nombres[i+1]
    """
    nombres_linea1 = ["Akademmistechko", "Zhytomyrska", "Sviatoshyn", "Nyvky", "Beresteiska",
                      "Shuliavska", "Politekhnichnyi instytut", "Vokzalna", "Universytet", "Teatralna",
                      "Khreshchatyk", "Arsenalna", "Dnipro", "Hidropark", "Livoberezhna", "Darnytsia",
                      "Chernihivska", "Lisova"]
    costes_l1 = [1500, 1800, 1000, 1000, 2200, 1200, 1200, 1100, 800, 700, 1700, 1700, 1400,
                 1600, 1100, 1300, 1200]

    nombres_linea2 = ["Heroiv Dnipra", "Minska", "Obolon", "Petrivka", "Tarasa Shevchenka",
                      "Kontraktova ploshcha", "Poshtova ploshcha", "Maidan Nezalezhnosti",
                      "Ploshcha Lva Tolstoho", "Olimpiiska", "Palats Ukraina", "Lybidska", "Demiivska",
                      "Holosiivska", "Vasylkivska", "Vystavkovyi tsentr", "Ipodrom", "Teremky"]
    costes_l2 = [1200, 1200, 1700, 1500, 1200, 1000, 1300, 1000, 1100, 1100, 900, 1200,
                 1100, 1500, 1500, 900, 1500]

    nombres_linea3 = ["Syrets", "Dorohozhychi", "Lukianivska", "Zoloti vorota", "Palats sportu",
                      "Klovska", "Pecherska", "Druzhby narodiv", "Vydubychi", "Slavutych", "Osokorky",
                      "Pozniaky", "Kharkivska", "Vyrlytsia", "Boryspilska", "Chervonyi khutir"]
    costes_l3 = [1600, 2800, 3100, 800, 1100, 1200, 1100, 1900, 3400, 800, 1300, 1300,
                 1100, 1300, 1100]

    # Vertices de la linea 1:
    v110 = g.insert_vertex(110)
    v111 = g.insert_vertex(111)
    v112 = g.insert_vertex(112)
    v113 = g.insert_vertex(113)
    v114 = g.insert_vertex(114)
    v115 = g.insert_vertex(115)
    v116 = g.insert_vertex(116)
    v117 = g.insert_vertex(117)
    v118 = g.insert_vertex(118)
    v119 = g.insert_vertex(119)
    v120 = g.insert_vertex(120)
    v121 = g.insert_vertex(121)
    v122 = g.insert_vertex(122)
    v123 = g.insert_vertex(123)
    v124 = g.insert_vertex(124)
    v125 = g.insert_vertex(125)
    v126 = g.insert_vertex(126)
    v127 = g.insert_vertex(127)
    lista_vertices_l1 = [v110, v111, v112, v113, v114, v115, v116, v117, v118, v119,
                         v120, v121, v122, v123, v124, v125, v126, v127]

    # Vertices de la linea 2:
    v210 = g.insert_vertex(210)
    v211 = g.insert_vertex(211)
    v212 = g.insert_vertex(212)
    v213 = g.insert_vertex(213)
    v214 = g.insert_vertex(214)
    v215 = g.insert_vertex(215)
    v216 = g.insert_vertex(216)
    v217 = g.insert_vertex(217)
    v218 = g.insert_vertex(218)
    v219 = g.insert_vertex(219)
    v220 = g.insert_vertex(220)
    v221 = g.insert_vertex(221)
    v222 = g.insert_vertex(222)
    v223 = g.insert_vertex(223)
    v224 = g.insert_vertex(224)
    v225 = g.insert_vertex(225)
    v226 = g.insert_vertex(226)
    v227 = g.insert_vertex(227)
    lista_vertices_l2 = [v210, v211, v212, v213, v214, v215, v216, v217, v218,
                         v219, v220, v221, v222, v223, v224, v225, v226, v227]

    # Vertices de la linea 3:
    v310 = g.insert_vertex(310)
    v311 = g.insert_vertex(311)
    v312 = g.insert_vertex(312)
    # v313 = g.insert_vertex(313) -> no existe
    v314 = g.insert_vertex(314)
    v315 = g.insert_vertex(315)
    v316 = g.insert_vertex(316)
    v317 = g.insert_vertex(317)
    v318 = g.insert_vertex(318)
    v319 = g.insert_vertex(319)
    # v320 = g.insert_vertex(320) -> no existe
    v321 = g.insert_vertex(321)
    v322 = g.insert_vertex(322)
    v323 = g.insert_vertex(323)
    v324 = g.insert_vertex(324)
    v325 = g.insert_vertex(325)
    v326 = g.insert_vertex(326)
    v327 = g.insert_vertex(327)
    lista_vertices_l3 = [v310, v311, v312, v314, v315, v316, v317, v318, v319,
                         v321, v322, v323, v324, v325, v326, v327]

    """ Añadimos las aristas al grafo con sus correspondientes costes"""
    i = 0
    while i < len(lista_vertices_l1) - 1:
        # Definir el coste que sea en una lista
        g.insert_undirected_edge(lista_vertices_l1[i], lista_vertices_l1[i + 1], costes_l1[i])
        i = i + 1

    i = 0
    while i < len(lista_vertices_l2) - 1:
        # Definir el coste que sea en una lista
        g.insert_undirected_edge(lista_vertices_l2[i], lista_vertices_l2[i + 1], costes_l2[i])
        i = i + 1

    i = 0
    while i < len(lista_vertices_l3) - 1:
        # Definir el coste que sea en una lista
        g.insert_undirected_edge(lista_vertices_l3[i], lista_vertices_l3[i + 1], costes_l3[i])
        i = i + 1

    # Creamos diccionarios clave:vertice y valor: nombre de la parada (un dic por linea)
    dic1: Dict[Vertex[V], str] = dict()
    dic2: Dict[Vertex[V], str] = dict()
    dic3: Dict[Vertex[V], str] = dict()

    for i in range(len(nombres_linea1)):
        dic1[lista_vertices_l1[i]] = nombres_linea1[i]
        dic2[lista_vertices_l2[i]] = nombres_linea2[i]  # Aprovechamos que tienen el mismo length

    for i in range(len(nombres_linea3)):
        dic3[lista_vertices_l3[i]] = nombres_linea3[i]

    # Creamos el diccionario con todas las estaciones
    dic1_copia = dic1.copy()
    dic1_copia.update(dic2)
    dic1_copia.update(dic3)
    dic_total = dic1_copia

    # Creamos un diccionario clave:nombre parada, valor:vértice
    inverted_dict_total = dict(map(reversed, dic_total.items()))


    """
        TRANSBORDOS:    
        Aunque en los transbordos se recorre poco en distancia, en tiempo es mucho en comparación 
        con la misma distancia en metro, puesto que se hacen andando.
        
                                    500 m andando ~~ 450 segundos
                                    500 m en metro ~~ 50 segundos
                                            
        Para solucionar esto, en los transbordos se coge el tiempo que se tarda andando y se multiplica 
        por la velocidad en metro, hallando así el coste proporcional. 
        NOTA: o que buscamos es el camino más rápido no el más corto.
    """
    # Tiempo en seg (velocidad media metro en kiev: 10.03 m/s)
    VELOCIDAD_DEL_METRO = 10.03

    # trans1 ----> Zoloti Vorota(v314) <----> Teatralna(v119)
    # trans2 ----> Maidan Nezalezhnosti(v217) <----> Khreshchatyk(v120)
    # trans3 ----> Palats Sportu(v315) <----> Ploshcha Lva Tolstogo(v218)

    tiempo_trans1 = 240
    tiempo_trans2 = 240
    tiempo_trans3 = 300

    coste_trans1 = round(tiempo_trans1 * VELOCIDAD_DEL_METRO)
    coste_trans2 = round(tiempo_trans2 * VELOCIDAD_DEL_METRO)
    coste_trans3 = round(tiempo_trans3 * VELOCIDAD_DEL_METRO)

    # Añadimos al grafo las aristas que conforman los transbordos, con su correspondiente coste
    g.insert_undirected_edge(v314, v119, coste_trans1)
    g.insert_undirected_edge(v217, v120, coste_trans2)
    g.insert_undirected_edge(v315, v218, coste_trans3)

    return g, inverted_dict_total, dic_total

def ejecucion_a_star(grafo: IUndirectedGraph, vorigen: Vertex,
                     vdestino: Vertex, dicc: Dict[Vertex, str]):
    """
        PRE:
            ·grafo no dirigido
            ·vértices origen y destino, pertenecientes al grafo
            ·diccionario cuyas claves son los vértices y cuyos valores son el nombre de las paradas
        POST:
            Devuelve la ruta que hay que recorrer y el coste total
    """
    shortest_path = a_star(grafo, vorigen, vdestino, dicc)
    list_path = []
    for v in shortest_path:
        print(dicc[v])
        list_path += [dicc[v]]
    print("coste (en metros de tren): ", vdestino.cost)

    return list_path, vdestino.cost

"""
time1 = time.time()
ejecucion_a_star(g, inverted_dict_total['Arsenalna'], inverted_dict_total['Hidropark'], dic_total)
time2 = time.time()
print(f'{round(time2 - time1, 2)} segundos ha tardado la búsqueda')
"""
