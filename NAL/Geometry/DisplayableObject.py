import sys
import NXOpen
from .NamedObject import NamedObject

class DisplayableObject(NamedObject):

    def __init__(self, nxDisplayableObject : NXOpen.DisplayableObject):
        super().__init__(nxDisplayableObject)