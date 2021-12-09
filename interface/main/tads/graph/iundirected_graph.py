from abc import abstractmethod
from typing import TypeVar, Iterator

from .elements.edge import Edge
from .elements.vertex import Vertex
from .igraph import IGraph


V = TypeVar('V')
E = TypeVar('E')


class IUndirectedGraph(IGraph[V, E]):

    @abstractmethod
    def end_vertices(self, e: Edge[V, E]) -> (Vertex[V], Vertex[V]):
        """

        **PRE:** e is a valid edge of this graph (raise ValueError | TypeError)

        **POST:** Returns a tuple containing the end vertices of an edge.
        """
        pass

    @abstractmethod
    def insert_undirected_edge(self, u: Vertex[V], v: Vertex[V], x: E) -> Edge[V, E]:
        """

        **PRE:** u and v are vertices of the graph and u and v are not already adjacent (raise ValueError | TypeError)

        **POST:** Insert and return a new edge between u to v with element x.
        """
        pass

    @abstractmethod
    def opposite(self, v: Vertex[V], e: Edge[V, E]) -> Vertex[V]:
        """

        **PRE:** v is a valid vertices of this graph, e is a valid edge and v is in e (raise ValueError | TypeError)

        **POST:** Return the other endvertex of an incident edge.
        """
        pass

    @abstractmethod
    def are_adjacent(self, u: Vertex[V], v: Vertex[V]) -> bool:
        """

        **PRE:** u and v are valid edges of this graph (raise ValueError | TypeError)

        **POST:** Check whether two vertices are adjacent.
        """
        pass

    @abstractmethod
    def edges_of(self, v: Vertex[V]) -> Iterator[Edge[V, E]]:
        """

        **PRE:** v is a valid vertices of this graph (raise ValueError | TypeError)

        **POST:** Returns the edges connected to the vertices.
        """
        pass
