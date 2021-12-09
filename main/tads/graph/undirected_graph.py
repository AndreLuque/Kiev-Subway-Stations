from typing import TypeVar, Iterator

from .elements.edge import Edge
from .elements.vertex import Vertex
from .mapgraph import MapGraph
from .iundirected_graph import IUndirectedGraph

V = TypeVar('V')
E = TypeVar('E')


class UndirectedAdjacencyListGraph(IUndirectedGraph[V, E]):
    """Representation of an undirected graph using the MapGraph class."""

    def __init__(self):
        """
        The constructor:

        **POST:** Creates an empty graph.
        """
        self.__map_graph: MapGraph[V, E] = MapGraph()

    def __iter__(self) -> Iterator[Vertex[V]]:
        return self.__map_graph.__iter__()

    def __str__(self) -> str:
        return self.__map_graph.__str__()

    def degree(self, v: Vertex[V]) -> int:
        return sum(1 for _ in self.edges_of(v))

    def edges(self) -> Iterator[Edge[V, E]]:
        return self.__map_graph.edges()

    def end_vertices(self, e: Edge[V, E]) -> (Vertex[V], Vertex[V]):
        return self.__map_graph.end_vertices(e)

    def insert_vertex(self, o: V) -> Vertex[V]:
        return self.__map_graph.insert_vertex(o)

    def set_n(self, n: Edge[V, E], e: E) -> E:
        return self.__map_graph.set_n(n, e)

    def num_vertices(self) -> int:
        return self.__map_graph.num_vertices()

    def are_adjacent(self, u: Vertex[V], v: Vertex[V]) -> bool:
        return self.__map_graph.get_edge(u, v) is not None

    def edges_of(self, v: Vertex[V]) -> Iterator[Edge[V, E]]:
        return self.__map_graph.edges_from(v)

    def insert_undirected_edge(self, u: Vertex[V], v: Vertex[V], x: E) -> Edge[V, E]:
        if self.__map_graph.get_edge(u, v) is not None:  # includes error checking
            raise ValueError('u and v are already adjacent')
        e: Edge[E] = Edge(u, v, x)
        self.__map_graph.insert_edge(e, u, v)
        self.__map_graph.insert_edge(e, v, u)  # both directions are represented
        return e

    def remove_edge(self, e: Edge[V, E]) -> E:
        v1, v2 = e.endpoints()
        self.__map_graph.remove_edge(e, v1, v2)
        self.__map_graph.remove_edge(e, v2, v1)  # both directions are represented
        return e.element

    def remove_vertex(self, v: Vertex[V]) -> V:
        self.__map_graph.remove_vertex(v)
        return v.element

    def opposite(self, v: Vertex[V], e: Edge[V, E]) -> Vertex[V]:
        v1, v2 = self.end_vertices(e)
        if v is v1:
            return v2
        elif v is v2:
            return v1
        else:
            raise ValueError('v is not in the edge e')

    @property
    def is_empty(self) -> bool:
        return self.__map_graph.num_vertices() == 0

    def num_edges(self) -> int:
        return sum(1 for _ in self.__map_graph.edges())

    def vertices(self) -> Iterator[Vertex[V]]:
        return self.__map_graph.vertices()
