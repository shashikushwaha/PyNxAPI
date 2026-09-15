import sys
import NXOpen
from .DisplayableObject import DisplayableObject


class Body(DisplayableObject):
    def __init__(self, nxBody : NXOpen.Body):
        super().__init__(nxBody)

    @property
    def NXOpenBody(self) -> NXOpen.Body :
        return self.nxOpenTaggedObject

    @staticmethod
    def BodyByName(name: str) -> "Body":
        bodiesCol : NXOpen.BodyCollection = NXOpen.Session.GetSession().Parts.Work.Bodies
        allBodies = [onebody for onebody in bodiesCol if(onebody.Name == name)]
        if(len(allBodies) == 0):
            raise ValueError(f"{name} not found.") 
        return allBodies[0]

    # def __str__(self):
    #     return (f"{self.Name}, {self.Tag}")   