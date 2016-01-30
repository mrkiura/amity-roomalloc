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
                if len(temp) == 3:  # STAFF
                    # select all offices from db
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
                elif len(temp) == 4:  # FELLOWS
                    # assign office to all fellows
                    if temp[3] == "N" or temp[3] == "Y":
                        # allocate offices to everyone
                        # select all offices from db
                        cursor.execute("SELECT name, capacity, spaces from rooms where type = 'OFFICE' ")

                        # loop through rows. If a zero is found in spaces,
                        # assign room, break
                        for row in cursor:
                            list_of_spaces = row[2].split(',')
                            list_of_spaces = map(lambda x: x.encode('ascii'), list_of_spaces)  # remove unicode encoding

                            if '0' in list_of_spaces:  # if office not full
                                # loop through the items in office
                                for index, item in enumerate(list_of_spaces):
                                    # if one of the items in office is a zero
                                    if item == '0':
                                        # assign a person name to that index,
                                        # convert list to string and update in db
                                        list_of_spaces[index] = temp[0] + " " + temp[1]
                                        string_of_spaces = ",".join(list_of_spaces)

                                        cursor.execute("UPDATE rooms set spaces = ? where name = ?", (string_of_spaces, row[0]))
                                        conn.commit()
                                        print list_of_spaces
                                        break  # stop looping through spaces
                                break  # stop looping through row

                    if temp[3] == "Y":
                        # allocate living space for those fellows
                        # who want it
                        # select all living spaces from db
                        cursor.execute("SELECT name, capacity, spaces from rooms where type = 'LIVING' ")

                        # loop through rows. If a zero is found in spaces,
                        # assign room, break
                        for row in cursor:
                            list_of_spaces = row[2].split(',')
                            list_of_spaces = map(lambda x: x.encode('ascii'), list_of_spaces)  # remove unicode encoding

                            if '0' in list_of_spaces:  # if office not full
                                # loop through the items in office
                                for index, item in enumerate(list_of_spaces):
                                    # if one of the items in office is a zero
                                    if item == '0':
                                        # assign a person name to that index,
                                        # convert list to string and update in db
                                        list_of_spaces[index] = temp[0] + " " + temp[1]
                                        string_of_spaces = ",".join(list_of_spaces)

                                        cursor.execute("UPDATE rooms set spaces = ? where name = ?", (string_of_spaces, row[0]))
                                        conn.commit()
                                        print list_of_spaces
                                        break  # stop looping through spaces
                                break  # stop looping through row

    print "Rooms allocated successfully"
    get_unallocated(thefile)

# get allocations function
# will be called if sys.argv[1] is get and
# sys.argv[2] is allocations
# shows the rooms and the people assigned
# to them onscreen


def get_allocations():
    cursor.execute("SELECT name, type, capacity, spaces FROM rooms")

    for row in cursor:
        list_of_spaces = row[3].split(',')
        list_of_spaces = map(lambda x: x.encode('ascii'), list_of_spaces)  # remove unicode encoding

        flag = False  # empty room

        for i in list_of_spaces:
            if i != '0':  # if room has at least one occupant
                flag = True  # set flag to true
                break

        if flag:
            print "----------------------------"
            print "ROOM TYPE: %s" % row[1]
            print "ROOM NAME: %s" % row[0]
            print "CAPACITY: %s\n" % row[2]
            print "**MEMBERS**"
            for item in list_of_spaces:
                if item != '0':
                    print item
            print "----------------------------"
            print "\n"


# print allocations function
# output allocations to a txt file
# will be called if sys.argv[1] is print
# and sys.argv[2] is allocations

def print_allocations():
    cursor.execute("SELECT name, type, capacity, spaces FROM rooms")

    with open("allocations.txt", "a") as fo:
        fo.write("^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
        fo.write("NEW LIST STARTS HERE\n")
        fo.write("^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")

    for row in cursor:
        list_of_spaces = row[3].split(',')
        list_of_spaces = map(lambda x: x.encode('ascii'), list_of_spaces)  # remove unicode encoding

        flag = False  # empty room

        for i in list_of_spaces:
            if i != '0':  # if room has at least one occupant
                flag = True  # set flag to true
                break

        if flag:
            with open("allocations.txt", "a") as fo:
                fo.write("----------------------------\n")
                fo.write("ROOM TYPE: %s\n" % row[1])
                fo.write("ROOM NAME: %s\n" % row[0])
                fo.write("CAPACITY: %s\n\n" % row[2])
                fo.write("**MEMBERS**\n")
                for item in list_of_spaces:
                    if item != '0':
                        fo.write("%s\n" % item)
                fo.write("----------------------------\n")
                fo.write("\n")

# will be given a room name and
# print the members allocated to it
# will be called if sys.argv[1] is print
# and sys.argv[2] is members
# and sys.argv[3] is a room name


def print_members(room):
    cursor.execute("SELECT type, capacity, spaces from rooms where name = ?", ([room]))

    theroom = cursor.fetchone()

    print "**********ROOM DETAILS************\n"
    print "ROOM TYPE: %s \t ROOM NAME: %s \t CAPACITY: %s \n\n" % (theroom[0], room, theroom[1])

    print "**********ROOM MEMBERS************\n"

    list_of_spaces = theroom[2].split(',')
    list_of_spaces = map(lambda x: x.encode('ascii'), list_of_spaces)  # remove unicode encoding

    for i in list_of_spaces:
        if i != '0':
            print i


# will be called at the end of the
# allocate function

def get_unallocated(thefile):
    temp = []
    unallocated_people = []

    with open(thefile) as f:
        # reads file and puts each line in temp list
        # the temp list will then be used for checking names

        for line in f:
            if len(line) > 2:
                temp = line.split()

                name = temp[0] + " " + temp[1]
                thereflag = False

                # select all offices from db
                cursor.execute("SELECT name, capacity, spaces from rooms where type = 'OFFICE' ")

                # loop through rows. If name is found in spaces,
                # assign thereflag true and  break
                for row in cursor:
                    list_of_spaces = row[2].split(',')
                    list_of_spaces = map(lambda x: x.encode('ascii'), list_of_spaces)  # remove unicode encoding

                    if name in list_of_spaces:  # if name exists in db
                        thereflag = True
                        break

                if thereflag is False:
                    unallocated_people.append(name)

    # check if anyone exists in the unallocated people list
    #  and print their name
    if len(unallocated_people) == 0:
        print "No Unallocated People"
    else:
        print "----------------------------"
        print "UNALLOCATED PEOPLE"
        print "----------------------------\n"
        for name in unallocated_people:
            print "%s\n" % name


# call methods
# allocate
if len(sys.argv) == 3 and sys.argv[1] == "allocate" and sys.argv[2][-3:] == "txt":
    allocate(sys.argv[2])

# print the members of a given room
if len(sys.argv) == 4:
    if sys.argv[1] == "print" and sys.argv[2] == "allocations" and sys.argv[3] is not None:
        print_members(sys.argv[3])

# show all allocations on screen
if len(sys.argv) == 3 and sys.argv[1] == "get" and sys.argv[2] == "allocations":
    get_allocations()

# print all allocations to allocations.txt
if len(sys.argv) == 3 and sys.argv[1] == "print" and sys.argv[2] == "allocations":
    print_allocations()
