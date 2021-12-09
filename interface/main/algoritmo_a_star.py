import sys
from typing import List, TypeVar, NoReturn, Optional, Dict, Set

from .distanceBetweenCoordinates import getDistance
from .getCoordinates import coordinates
from .tads.graph.iundirected_graph import * 
from .tads.graph.undirected_graph import *
from .tads.graph.elements.vertex import *

V = TypeVar('V')
E = TypeVar('E')


def a_star(graph: IUndirectedGraph[V, E], from_v: Vertex[V], to_v: Vertex[V],
           num_name: Dict[Vertex[V], str]) -> List[Vertex[V]]:

    def min_f_function(open_list: Set[Vertex[V]]) -> Vertex[V]:
        """
        POST: Calcula cuál de los vertices en la lista abierta tiene mínima
        funcion f(n) --- > f(n)= g(n) + h(n) donde g es el coste real y h la heuristica
        """
        min: int = sys.maxsize
        min_v: Optional[Vertex[V]] = None
        for vertex in open_list:
            if vertex.cost + vertex.heuristic < min:
                min_v = vertex
                min = vertex.cost + vertex.heuristic
        return min_v

    def heuristic(vertex: Vertex, num_name: Dict[Vertex[V], str]) -> NoReturn:
        """
        PRE:
        num_name es un dict con clave: vértice, valor: nombre de la parada;
        POST:
        Creamos un atributo heuristic, que basicamente es la distancia en linea recta
        entre la estación dada y la estación destino
        """
        vertex.heuristic = getDistance(coordinates(num_name[vertex]), coordinates(num_name[to_v]))

    def shortest(to_v: Vertex[V], path: List[Vertex[V]]) -> NoReturn:
        """
        POST: una vez calculado el camino mínimo esta función lo construye desde from_v a to_v
        """
        if hasattr(to_v, "previous"):
            shortest(to_v.previous, path)
            path.append(to_v.previous)

    # Inicializamos las variables y el coste y heuristica del origen
    open_list: Set = set()
    close_list: Set = set()
    from_v.cost = 0
    heuristic(from_v, num_name)
    open_list.add(from_v)

    while open_list:
        # Hallamos el vértice con f(n) menor al from_v
        current_vertex = min_f_function(open_list)
        # Si el vértice en el que estamos no es el destino desarrollamos sus adyacentes
        if current_vertex != to_v:
            # Marcamos el vértice como visitado
            close_list.add(current_vertex)
            # Sacamos de la lista abierta el vértice con f(n) menor
            open_list.remove(current_vertex)
            # Recorremos sus vértices adyacentes
            for edge in graph.edges_of(current_vertex):
                next_vertex: Vertex[V] = graph.opposite(current_vertex, edge)
                # Comprobamos que no se haya visitado el vértice vecino a current_vertex
                if next_vertex not in close_list:
                    # Hallamos la heurística y la distancia solo si no tienen el atributo ya
                    if next_vertex not in open_list:
                        heuristic(next_vertex, num_name)
                        open_list.add(next_vertex)
                        next_vertex.cost = sys.maxsize
                    # Hallamos la f(n) por el camino from_v-....-current_vertex-next_vertex
                    new_f = current_vertex.cost + edge.element + next_vertex.heuristic
                    # Si esa f(n) es menor que la que tiene marcada next_vertex la actualizamos
                    if new_f < next_vertex.cost + next_vertex.heuristic:
                        next_vertex.cost = current_vertex.cost + edge.element
                        # Establece la flecha hacia su antecesor
                        next_vertex.previous = current_vertex
        # En caso de que sea el vértice actual el de destino, salimos del bucle
        else:
            break

    # We build the path
    path: List[Vertex[V]] = []
    shortest(to_v, path)
    path.append(to_v)
    return path
