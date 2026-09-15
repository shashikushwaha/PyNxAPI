import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'NAL', 'Geometry')))
from NAL.Geometry.Part import Part
from NAL.Geometry.Part import Body

class TestBody(unittest.TestCase):
    def setUp(self):
        self.filePath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'TestCases', 'Body', 'body.prt'))
        self.part1 = Part.OpenPart(self.filePath)

    def tearDown(self):
        Part.CloseAll()
        
    def testGetBodyName(self):
        body = Body.BodyByName("BODY_01")
        self.assertIsNotNone(body)   

    def testFaliedGetBodyName(self):
        with self.assertRaises(ValueError) as context:            
            body = Body.BodyByName("BODY_011")
        self.assertEqual(str(context.exception), "BODY_011 not found.")   