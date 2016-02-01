import unittest
from populate import populate
from allocate import print_allocations, allocate, depopulate
import sqlite3


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

    def test_allocate_allocates_offices(self):
        '''Ensures allocate function actually allocates
        offices'''
        allocate("test.txt")

        conn = sqlite3.connect('roomalloc.db')
        cursor = conn.cursor()

        cursor.execute("SELECT name, capacity, spaces from rooms where type = 'OFFICE' ")

        for row in cursor:
            self.assertEqual(row[0], "Narnia")
            self.assertEqual(row[1], 6)
            self.assertNotEqual(row[2], '0,0,0,0,0,0')
            break

        cursor.execute("SELECT name, capacity, spaces from rooms where type = 'LIVING' ")

    def test_allocate_allocates_livingspaces(self):
        '''Ensures allocate function actually allocates
        living spaces'''
        allocate("test.txt")

        conn = sqlite3.connect('roomalloc.db')
        cursor = conn.cursor()

        cursor.execute("SELECT name, capacity, spaces from rooms where type = 'LIVING' ")

        for row in cursor:
            self.assertEqual(row[0], "Wood")
            self.assertEqual(row[1], 4)
            self.assertNotEqual(row[2], '0,0,0,0')
            break

    def test_allocate_fails_on_wrong_input(self):
        '''Ensures allocate.py's allocate function only
        allocates when called with a valid txt file'''
        msg = allocate("jbhvbhjbvhjv.tx")
        self.assertEqual(msg, "Not a txt file")

    def test_print_allocations(self):
        """Tests for allocate.py's print_allocations function
        Checks if function ran correctly
        """

        msg = print_allocations()
        self.assertEqual(msg, "Success")

    def test_depopulate_runs_correctly(self):
        """Tests for allocate.py's depopulate function
        Checks if function ran correctly
        """

        msg = depopulate()
        self.assertEqual(msg, "Success")

if __name__ == '__main__':
    unittest.main()
