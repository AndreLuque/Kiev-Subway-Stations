from typing import TypeVar, Generic, NoReturn

from .vertex import Vertex

V = TypeVar('V')
E = TypeVar('E')


class Edge(Generic[V, E]):
    """Lightweight edge structure for a graph."""
    # __slots__ = '_origin', '_destination', '_element'

    def __init__(self, u: Vertex[V], v: Vertex[V], x: E):
        """Do not call constructor directly. Use Graph's insert_edge(u,v,x)."""
        self.__origin: Vertex[V] = u
        self.__destination: Vertex[V] = v
        self.__element: E = x

    def endpoints(self) -> (Vertex[V], Vertex[V]):
        """Return (u,v) tuple for vertices u and v."""
        return self.__origin, self.__destination

    def opposite(self, v: Vertex[V]) -> Vertex[V]:
        """Return the vertices that is opposite v on this edge."""
        if not isinstance(v, Vertex):
            raise TypeError('v must be a Vertex')
        if v is self.__origin:
            return self.__destination
        elif v is self.__destination:
            return self.__origin
        else:
            raise ValueError('v not incident to edge')

    @property
    def element(self) -> E:
        """Return element associated with this edge."""
        return self.__element

    @element.setter
    def element(self, e: E) -> NoReturn:
        self.__element = e

    def __str__(self) -> str:
        return '({0},{1},{2})'.format(self.__origin, self.__destination, self.__element)
