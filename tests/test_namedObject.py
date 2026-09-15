import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'NAL', 'Geometry')))
from NAL.Geometry.Part import Part

class TestNamedObject(unittest.TestCase):

    def setUp(self):
        self.filePath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'TestCases', 'NamedObject', 'part.prt'))
        self.part1 = Part.OpenPart(self.filePath)

    def tearDown(self):
        Part.CloseAll()

    def test_nxOpenNammedObject(self):
        nxPart = self.part1.NXOpenObject 
        self.assertIsNotNone(nxPart)   
    
    def test_nxOpenTaggedObject(self):
        nxPart = self.part1.NXOpenTaggedObject 
        self.assertIsNotNone(nxPart)   

    def test_Tag(self):
        nxPart = self.part1.Tag 
        self.assertIsNotNone(nxPart)     

    def test_Name(self):
        allBodies = Part.GetBodies(); 
        name = allBodies[0].Name
        self.assertEqual(name, "BODY_01")  