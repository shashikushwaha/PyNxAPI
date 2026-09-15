import sys
import NXOpen
from .DisplayableObject import DisplayableObject

class Face(DisplayableObject):
    def __init__(self, nxDisplayableObject):
        super().__init__(nxDisplayableObject)

    @property
    def NXOpenFace(self) -> NXOpen.Face:
        return self.nxOpenTaggedObject