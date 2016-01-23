import unittest
from populate import O1, L1


class AmityRoomAllocTestCase(unittest.TestCase):

    def test_populate(self):
    	"""Tests for populate.py
        Checks if offices and living spaces have been
        initialized correctly
        """
        self.failUnlessEqual(O1.name, "Office1")
        self.failUnlessEqual(O1.type, "OFFICE")
        self.failUnlessEqual(O1.capacity, 6)
        self.failUnlessEqual(O1.spaces, ['0', '0', '0', '0', '0', '0'])

        self.failUnlessEqual(L1.name, "LivingSpace1")
        self.failUnlessEqual(L1.type, "LIVING")
        self.failUnlessEqual(L1.capacity, 4)
        self.failUnlessEqual(L1.spaces, ['0', '0', '0', '0'])

if __name__ == '__main__':
    unittest.main()
