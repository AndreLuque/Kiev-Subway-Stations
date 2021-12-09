from typing import TypeVar, Optional, Set, Dict, Generic, Iterator, List, NoReturn

from .elements.edge import Edge
from .elements.vertex import Vertex

V = TypeVar('V')
E = TypeVar('E')


class MapGraph(Generic[V, E]):
    """
    Representation of graph using an adjacency map.
    It is used to implement both DirectedGraph and UnDirectedGraph classes.
    """

    # -------------------------- binary my_tree constructor --------------------------
    def __init__(self):
        """
        Create an empty undirected graph.
        """
        self.__outgoing: Dict[Vertex[V], Dict[Vertex[V], Edge[V, E]]] = {}

    # ------------------------- utility methods -----------------------------------

    def __iter__(self) -> Iterator[Vertex[V]]:
        return iter(self.__outgoing)

    def __str__(self) -> str:
        output: str = "Vertices: "
        for i in self.__outgoing.keys():
            output = output + str(i) + " "
        output = output + "\n" + "Edges: "
        for e in self.edges():
            output = output + str(e) + " "
        return output

    def __validate_vertex(self, v: Vertex[V]) -> NoReturn:
        """Verify that v is a Vertex of this graph."""
        if not isinstance(v, Vertex):
            raise TypeError('Vertex expected')
        if v not in self.__outgoing:
            raise ValueError('Vertex does not belong to this graph.')

    def __validate_edge(self, e: Edge[V, E]) -> NoReturn:
        """Verify that e is a Edge of this graph."""
        if not isinstance(e, Edge):
            raise TypeError('Edge expected')
        if e not in self.edges():
            raise ValueError('This edge does not belong to this graph.')

    # ------------------------- public methods -----------------------------------

    def get_edge(self, u: Vertex[V], v: Vertex[V]) -> Optional[Edge[V, E]]:
        """Return the edge from u to v, or None if not adjacent."""
        self.__validate_vertex(u)
        self.__validate_vertex(v)
        return self.__outgoing[u].get(v, None)  # returns None if u and v are not adjacent

    def edges(self) -> Iterator[Edge[V, E]]:
        """Return a set of all edges of the graph."""
        result: Set[Edge[E]] = set()  # avoid double-reporting edges of undirected graph
        for secondary_map in self.__outgoing.values():
            result.update(secondary_map.values())  # add edges to resulting set
        return iter(result)

    def end_vertices(self, e: Edge[V, E]) -> (Vertex[V], Vertex[V]):
        self.__validate_edge(e)
        return e.endpoints()

    def insert_vertex(self, x: V):
        """Insert and return a new Vertex with element x."""
        v: Vertex[V] = Vertex(x)
        self.__outgoing[v] = {}
        return v

    def set_n(self, n: Edge[V, E], e: E) -> E:
        self.__validate_edge(n)
        old = n.element
        n.element = e
        return old

    def num_vertices(self) -> int:
        return len(self.__outgoing.keys())

    def edges_from(self, v: Vertex[V]) -> Iterator[Edge[V, E]]:
        self.__validate_vertex(v)
        return iter(self.__outgoing[v].values())

    def edges_to(self, v: Vertex[V]) -> Iterator[Edge[V, E]]:
        self.__validate_vertex(v)
        edges: List[Edge[V, E]] = []
        e: Optional[Edge[V, E]]
        for u in self.__outgoing.keys():
            e = self.__outgoing[u].get(v, None)
            if e is not None:
                edges.append(e)
        return iter(edges)

    def insert_edge(self, e: Edge[V, E], u: Vertex[V], v: Vertex[V]) -> NoReturn:
        self.__outgoing[u][v] = e

    def remove_edge(self, e: Edge[V, E], v1: Vertex[V], v2: Vertex[V]) -> NoReturn:
        self.__validate_edge(e)
        self.__outgoing[v1].pop(v2)

    def remove_vertex(self, v: Vertex[V]) -> NoReturn:
        self.__validate_vertex(v)
        self.__outgoing.pop(v)
        for dict_aux in self.__outgoing.values():
            if v in dict_aux:
                dict_aux.pop(v)

    def vertices(self) -> Iterator[Vertex[V]]:
        return iter(self.__outgoing.keys())
