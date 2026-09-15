import sys
import math
import NXOpen
from typing import List
from .TaggedObject import TaggedObject


class NamedObject(TaggedObject):
    def __init__(self, nxobject: NXOpen.NXObject):
        super().__init__(nxobject)

    @property
    def NXOpenObject(self) -> NXOpen.NXObject :
        return self.nxOpenTaggedObject

    @property
    def Name(self) ->str :
        return self.nxOpenTaggedObject.Name
