"""Import statements."""
import sys
from amity import Amity

# create object
building = Amity()

# call methods based on arguments given
if len(sys.argv) >= 2:
    # call allocate rooms
    if len(sys.argv) == 3 and sys.argv[1] == "allocate" and sys.argv[2][-3:] == "txt":
        building.allocate(sys.argv[2])

    # print the members of a given room
    if len(sys.argv) == 4:
        if sys.argv[1] == "print" and sys.argv[2] == "allocations" and sys.argv[3] is not None:
            building.print_members(sys.argv[3])

    # show all allocations on screen
    if len(sys.argv) == 3 and sys.argv[1] == "get" and sys.argv[2] == "allocations":
        building.get_allocations()

    # print all allocations to allocations.txt
    if len(sys.argv) == 3 and sys.argv[1] == "print" and sys.argv[2] == "allocations":
        building.print_allocations()

    # remove everything in db
    if len(sys.argv) == 2 and sys.argv[1] == "depopulate":
        building.depopulate()
else:
    print "No such command. Extra input required"
