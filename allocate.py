import sys

print sys.argv[1]

# allocate function
# will be called if sys.argv[1] is allocate and
# sys.argv[2] is a txt file


def allocate(thefile):
    with open(thefile) as f:
        for line in f:
            print line


# get allocations function
# will be called if sys.argv[1] is get and
# sys.argv[2] is allocations
# shows the rooms and the people assigned
# to them onscreen

def get_allocations():
    pass


# print allocations function
# output allocations to a txt file
# will be called if sys.argv[1] is print
# and sys.argv[2] is allocations

def print_allocations():
    pass

# will be given a room name and
# print the members allocated to it
# will be called if sys.argv[1] is print
# and sys.argv[2] is members
# and sys.argv[3] is a room name


def print_members():
    pass


# call methods
# allocate
if sys.argv[1] == "allocate" and sys.argv[2][-3:] == "txt":
    allocate(sys.argv[2])
