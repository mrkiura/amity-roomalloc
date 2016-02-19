"""Import statements."""
import unittest
from populate import populate
from amity import Amity
import sqlite3
import os.path


class AmityRoomAllocTestCase(unittest.TestCase):
    """Tests for Amity room allocation system."""

    def test_populate(self):
        """Test for populate.py's populate function.

        Checks if offices and living spaces have been
        initialized correctly
        """
        lst = populate()

        # check offices randomly
        self.failUnlessEqual(lst[0][0], ('Narnia', 'OFFICE', 6, '0,0,0,0,0,0'))
        self.failUnlessEqual(lst[0][8], ('Orange', 'OFFICE', 6, '0,0,0,0,0,0'))
        self.failUnlessEqual(lst[0][6],
                             ('Occulus', 'OFFICE', 6, '0,0,0,0,0,0'))
        self.failUnlessEqual(lst[0][4],
                             ('Hogwarts', 'OFFICE', 6, '0,0,0,0,0,0'))

        self.failUnlessEqual(lst[1][0], ('Wood', 'LIVING', 4, '0,0,0,0'))
        self.failUnlessEqual(lst[1][3], ('Wick', 'LIVING', 4, '0,0,0,0'))
        self.failUnlessEqual(lst[1][9], ('Terra', 'LIVING', 4, '0,0,0,0'))
        self.failUnlessEqual(lst[1][5], ('Gryffindor', 'LIVING', 4, '0,0,0,0'))

    def test_allocate_allocates_offices(self):
        """Ensure allocate function actually allocates offices."""
        building = Amity()

        building.allocate("test.txt")

        conn = sqlite3.connect('roomalloc.db')
        cursor = conn.cursor()

        cursor.execute("SELECT name, capacity, spaces from rooms where \
            type = 'OFFICE' ")

        for row in cursor:
            self.assertEqual(row[0], "Narnia")
            self.assertEqual(row[1], 6)
            self.assertNotEqual(row[2], '0,0,0,0,0,0')
            break

    def test_allocate_allocates_livingspaces(self):
        """Ensure allocate function actually allocates living spaces."""
        building = Amity()
        lst = building.allocate("test.txt")

        conn = sqlite3.connect('roomalloc.db')
        cursor = conn.cursor()

        cursor.execute("SELECT name, capacity, spaces from rooms where \
            type = 'LIVING' ")

        self.assertTrue(type(lst), "list")

        for row in cursor:
            self.assertEqual(row[0], "Wood")
            self.assertEqual(row[1], 4)
            self.assertNotEqual(row[2], '0,0,0,0')
            break

    def test_allocate_fails_on_wrong_input(self):
        """Ensure amity.py's allocate uses valid txt files."""
        building = Amity()
        msg = building.allocate("jbhvbhjbvhjv.tx")
        self.assertEqual(msg, "Not a txt file")

    def test_print_allocations(self):
        """Test for amity.py's print_allocations function.

        Checks if function ran correctly
        """
        building = Amity()
        msg = building.print_allocations()

        self.assertEqual(msg, "Success")
        self.failUnlessEqual(os.path.isfile("allocations.txt"), True)

    def test_print_members_returns_correctly(self):
        """Check print_members function returns error on wrong input."""
        building = Amity()
        msg = building.print_members("Pakistan")
        self.assertEqual(msg, "Error")

    def test_get_allocations(self):
        """Test get allocations finds something in db after allocations."""
        # ensure rooms table exists
        populate()

        # create amity building
        building = Amity()

        # allocate rooms
        building.allocate("test.txt")

        lst = building.get_allocations()
        self.assertTrue(len(lst) > 0)

        building.depopulate()

    def test_depopulate_runs_correctly(self):
        """Test for amity.py's depopulate function.

        Checks if function ran correctly
        """
        building = Amity()
        msg = building.depopulate()
        self.assertEqual(msg, "Success")

if __name__ == '__main__':
    unittest.main()
