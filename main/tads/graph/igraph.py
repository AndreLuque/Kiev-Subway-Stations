from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Iterable, Iterator

from .elements.edge import Edge
from .elements.vertex import Vertex

V = TypeVar('V')
E = TypeVar('E')


class IGraph(ABC, Generic[V, E], Iterable[V]):

    @property
    @abstractmethod
    def is_empty(self) -> bool:
        """

        **POST:** Check whether the graph does not contain any vertices.
        """
        pass

    @abstractmethod
    def num_vertices(self) -> int:
        """

        **POST:** Returns the number of vertices of the graph.
        """
        pass

    @abstractmethod
    def num_edges(self) -> int:
        """

        **POST:** Returns the number of edges of the graph.
        """
        pass

    @abstractmethod
    def degree(self, v: Vertex[V]) -> int:
        """

        **PRE:** v is a valid vertices of this graph (raise ValueError | TypeError)

        **POST:** Return the degree of a given vertices.
        """
        pass

    @abstractmethod
    def edges(self) -> Iterator[Edge[V, E]]:
        """

        **POST:** Return an iterator over the edges of the graph
        """
        pass

    @abstractmethod
    def set_n(self, n: Edge[V, E], e: E) -> E:
        """

        **PRE:** n is a valid edge of this graph (raise ValueError | TypeError)

        **POST:** Replaces the element of a given edge with a new element and returns the old element.
        """
        pass

    @abstractmethod
    def insert_vertex(self, o: V) -> Vertex[V]:
        """

        **POST:** Insert and return a new vertices with a given element.
        """
        pass

    @abstractmethod
    def remove_vertex(self, v: Vertex[V]) -> V:
        """

        **PRE:** v is a valid vertices of this graph (raise ValueError | TypeError)

        **POST:** Remove a vertices and all its incident edges and return the element stored at the removed vertices.
        """
        pass

    @abstractmethod
    def remove_edge(self, e: Edge[V, E]) -> E:
        """

        **PRE:** e is a valid edge of this graph (raise ValueError | TypeError)

        **POST:** Remove the given edge and return its element.
        """
        pass

    @abstractmethod
    def vertices(self) -> Iterator[Vertex[V]]:
        """

        **POST:** Return an iterator over the vertices of the graph.
        """
        pass
