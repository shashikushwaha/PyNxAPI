import unittest
import sys
import math

sys.path.append("..")
sys.path.append(r"..\NxLibrary")  # Ensure the main project is accessible
#from NxLibrary import NXSession

class TestNXSession(unittest.TestCase):
    def test_get_parts(self):
        #part = NXSession()
        #basepart = part.open_part( r"C:\Shashi\PyNxLibrary\NxLibrary\TestCases\Part\part.prt")
        #bodies = part.get_bodies()
        #self.assertEqual(len(bodies), 2)
        print("Hello world")
        self.assertEqual(2, 2)

if __name__ == '__main__':
    unittest.main()