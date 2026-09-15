import sys
import NXOpen
from .DisplayableObject import DisplayableObject


class Edge(DisplayableObject):
    def __init__(self, nxEdge ):
        super().__init__(nxEdge)

    @property
    def NXOpenEdge(self) -> NXOpen.Edge:
        return self.nxOpenTaggedObject


