import sys
import math
import NXOpen
from typing import List
from .NamedObject import NamedObject
from .Body import Body   
from .Edge import Edge
from .Face import Face

class Part(NamedObject) :    
    def __init__(self, nxOpenPart : NXOpen.Part):      
        self.session = NXOpen.Session.GetSession()
        self.workPart = self.session.Parts.Work 
        super().__init__(nxOpenPart)    

    @property
    def NXOpenPart(self) -> NXOpen.Part:
        return self.nxOpenTaggedObject    

    @staticmethod
    def OpenPart(filePath)-> "Part":
        results = NXOpen.Session.GetSession().Parts.OpenActiveDisplay(filePath, NXOpen.DisplayPartOption.AllowAdditional)
        # results = NXOpen.Session.GetSession().Parts.OpenBaseDisplay(filePath)
        openPart = results[0]
        part1 = Part(openPart)   
        return part1
    
    # def SaveAs():
    #     theSession : NXOpen.Session = NXOpen.Session.GetSession()
    
    @staticmethod
    def CloseAll():
        theSession : NXOpen.Session = NXOpen.Session.GetSession()
        partCloseRes : NXOpen.PartCloseResponses = theSession.Parts.NewPartCloseResponses()
        theSession.Parts.CloseAll(NXOpen.BasePart.CloseModified.CloseModified, partCloseRes)
        partCloseRes.Dispose()    

    @staticmethod
    def GetBodies() -> List[Body]:
        bodiesCol = NXOpen.Session.GetSession().Parts.Work.Bodies
        all_bodies = []
        for one_body in bodiesCol:
            all_bodies.append(Body(one_body))       
        return all_bodies    

    @staticmethod
    def GetFaces() -> List[Face]:
        allbodies = Part.GetBodies()
        # allFaces = [];
        allFaces = [Face(face) for body in allbodies for face in body.NXOpenBody.GetFaces()]
        # for body in allbodies:
        #     for face in body.NXOpenBody.GetFaces():
        #         allFaces.append(face)      

        return allFaces
    @staticmethod
    def GetEdges() -> List[Edge]:
        allfaces : List[Face] = Part.GetFaces() 
        allEdges = [Edge(edge) for face in allfaces for edge in face.NXOpenFace.GetEdges()]
        return allEdges
            
       