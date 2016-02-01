import unittest
from populate import populate
from allocate import print_allocations, allocate


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

    def test_allocate_fails_on_wrong_input(self):
        '''Ensures allocate.py's allocate function only
        allocates when called with a valid txt file'''
        msg = allocate("jbhvbhjbvhjv.tx")
        self.assertEqual(msg, "Not a txt file")

if __name__ == '__main__':
    unittest.main()
