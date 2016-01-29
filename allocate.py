import sys
import sqlite3

conn = sqlite3.connect('data/roomalloc.db')
cursor = conn.cursor()
# allocate function
# will be called if sys.argv[1] is allocate and
# sys.argv[2] is a txt file


def allocate(thefile):
    temp = []

    with open(thefile) as f:
        # reads file and puts each line in temp list
        # the temp list will then be used for assignation

        for line in f:
            if len(line) > 2:
                temp = line.split()

                # check if len(temp) is 3 which means
                # it is a staff
                if len(temp) == 3:
                    # select all offices from db
                    # cursor = conn.execute("SELECT name, capacity, spaces from rooms where type = 'OFFICE' ")
                    cursor.execute("SELECT name, capacity, spaces from rooms where type = 'OFFICE' ")

                    # loop through rows. If a zero is found in spaces,
                    # assign room, break
                    for row in cursor:
                        list_of_spaces = row[2].split(',')
                        list_of_spaces = map(lambda x: x.encode('ascii'), list_of_spaces)  # remove unicode encoding

                        if '0' in list_of_spaces:  # if office not full
                            for index, item in enumerate(list_of_spaces):  # loop through the items in office
                                if item == '0':  # if one of the items in office is a zero
                                    # assign a name to that index, convert list to string and update in db
                                    list_of_spaces[index] = temp[0] + " " + temp[1]
                                    string_of_spaces = ",".join(list_of_spaces)

                                    cursor.execute("UPDATE rooms set spaces = ? where name = ?", (string_of_spaces, row[0]))
                                    conn.commit()
                                    print list_of_spaces
                                    break
                            break  # stop looping through row
                elif len(temp) == 4:  # a fellow
                    pass


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
