from __future__ import annotations

from typing import TypeVar, Generic

V = TypeVar('V')


class Vertex(Generic[V]):
    """Lightweight inmutable vertex structure for a graph."""
    # __slots__ = '_element'

    def __init__(self, x: V):
        """Do not call constructor directly. Use Graph's insert_vertex(x)."""
        self.__element = x

    @property
    def element(self) -> V:
        """Return element associated with this vertices."""
        return self.__element

    def __str__(self) -> str:
        return str(self.__element)
