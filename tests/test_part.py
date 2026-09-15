import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'NAL', 'Geometry')))
sys.path.append("..")
sys.path.append(r"..\NAL")  # Ensure the main project is accessible
from NAL.Geometry.Part import Part

class testPart(unittest.TestCase): 

    def setUp(self):
        self.filePath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'TestCases', 'Part', 'part.prt'))
        self.part1 = Part.OpenPart(self.filePath)

    def tearDown(self):
        Part.CloseAll()

    def test_getbodies(self):
        allBodies = Part.GetBodies()
        print(allBodies[0])
        self.assertEqual( len(allBodies),1)

    def test_getFaces(self):
        allfaces = Part.GetFaces()
        self.assertEqual( len(allfaces),6)
    
    def test_getEdges(self):
        allfaces = Part.GetEdges()
        self.assertEqual( len(allfaces), 24)
    
    def test_nxOpenPart(self):
        nxPart = self.part1.NXOpenPart 
        self.assertIsNotNone(nxPart)       

if __name__ == '__main__':
    unittest.main()        