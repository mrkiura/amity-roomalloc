import unittest
from populate import populate
from allocate import print_allocations


class AmityRoomAllocTestCase(unittest.TestCase):

    def test_populate(self):
    	"""Tests for populate.py's populate function
        Checks if offices and living spaces have been
        initialized correctly
        """

        lst = populate()

        # check offices randomly
        self.failUnlessEqual(lst[0][0], ('Narnia', 'OFFICE', 6, '0,0,0,0,0,0'))
        self.failUnlessEqual(lst[0][8], ('Orange', 'OFFICE', 6, '0,0,0,0,0,0'))
        self.failUnlessEqual(lst[0][6], ('Occulus', 'OFFICE', 6, '0,0,0,0,0,0'))
        self.failUnlessEqual(lst[0][4], ('Hogwarts', 'OFFICE', 6, '0,0,0,0,0,0'))

        self.failUnlessEqual(lst[1][0], ('Wood', 'LIVING', 4, '0,0,0,0'))
        self.failUnlessEqual(lst[1][3], ('Wick', 'LIVING', 4, '0,0,0,0'))
        self.failUnlessEqual(lst[1][9], ('Terra', 'LIVING', 4, '0,0,0,0'))
        self.failUnlessEqual(lst[1][5], ('Gryffindor', 'LIVING', 4, '0,0,0,0'))

    def test_print_allocations(self):
        """Tests for allocate.py's print_allocations function
        Checks if function ran correctly
        """

        msg = print_allocations()
        self.assertEqual(msg, "Success")

if __name__ == '__main__':
    unittest.main()
