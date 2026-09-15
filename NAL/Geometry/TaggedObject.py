import sys
import math
import NXOpen
# from .Part import Part

class TaggedObject :
    def __init__(self , nxOpenTaggedObject : NXOpen.TaggedObject):
        self.nxOpenTaggedObject = nxOpenTaggedObject

    @property
    def NXOpenTaggedObject(self) -> NXOpen.NXObject :
        return self.nxOpenTaggedObject

    @property
    def Tag(self):
        return self.nxOpenTaggedObject.Tag    

    # @property
    # @staticmethod
    # def GetWorkPart() -> "Part":
    #     part1 = NXOpen.Session.GetSession().Parts
    #     return Part(part1)         