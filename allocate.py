import sys
import sqlite3
import random

conn = sqlite3.connect('roomalloc.db')
cursor = conn.cursor()


def allocate(thefile):
    """Reads a formatted text file of names and allocates
    rooms to random people

    Called by this command:
        python allocate.py allocate <nameoffile>

    Calls the get_unallocated function when it exits which
        prints the names of unallocated people

    Args:
        The file name

    Returns:
        Prints a message on success
    """

    # check if the file is a txt file
    if thefile[-3:] != "txt":
        return "Not a txt file"
        quit()

    # will hold list of items from a read line
    one_temp = []

    # list containing lists of all the read lines in the file
    alllines = []

    with open(thefile) as f:
        # reads file and puts each line in alllines list
        # as a temp list which will then be used for assignation

        for line in f:
            if len(line) > 2:
                # split current line into a list
                one_temp = line.split()

                # add current line to list of all lines
                alllines.append(one_temp)

    # randomize people before allocation
    random.shuffle(alllines)

    # loop through all the lines from file and allocate people rooms
    for temp in alllines:
        if len(temp) == 3:  # STAFF e.g CHIDIEBERE NNADI STAFF
            # select all offices from db (allocate only to office)
            cursor.execute("SELECT name, capacity, spaces from rooms where type = 'OFFICE' ")

            # loop through rows. If a zero is found in spaces,
            # assign room to current staff member then exit
            for row in cursor:
                # split string of spaces from db into a list
                list_of_spaces = row[2].split(',')

                # remove unicode encoding
                list_of_spaces = map(lambda x: x.encode('ascii'), list_of_spaces)

                # if office not full
                if '0' in list_of_spaces:
                    # loop through the items in office
                    for index, item in enumerate(list_of_spaces):
                        # if current item is zero
                        if item == '0':
                            # assign a name to that index, convert list
                            # to string and update in db
                            list_of_spaces[index] = temp[0] + " " + temp[1]
                            string_of_spaces = ",".join(list_of_spaces)

                            # update database with new name
                            cursor.execute("UPDATE rooms set spaces = ? where name = ?", (string_of_spaces, row[0]))
                            conn.commit()

                            # stop looping through db spaces
                            break

                    # stop looping through row
                    break
        elif len(temp) == 4:  # FELLOWS e.g AMOS OMONDI FELLOW Y
            # assign office to all fellows regardless of Y or N
            if temp[3] == "N" or temp[3] == "Y":
                # select all offices from db
                cursor.execute("SELECT name, capacity, spaces from rooms where type = 'OFFICE' ")

                # loop through rows. If a zero is found in spaces,
                # assign room, break
                for row in cursor:
                    # split string of spaces from db into a list
                    list_of_spaces = row[2].split(',')

                    # remove unicode encoding
                    list_of_spaces = map(lambda x: x.encode('ascii'), list_of_spaces)

                    # if office not full
                    if '0' in list_of_spaces:
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

                                # stop looping through spaces
                                break

                        # stop looping through row
                        break

            if temp[3] == "Y":
                # allocate living space for those fellows
                # who want it

                # select all living spaces from db
                cursor.execute("SELECT name, capacity, spaces from rooms where type = 'LIVING' ")

                # loop through rows. If a zero is found in spaces,
                # assign room, break
                for row in cursor:
                    # split string of spaces from db into a list
                    list_of_spaces = row[2].split(',')

                    # remove unicode encoding
                    list_of_spaces = map(lambda x: x.encode('ascii'), list_of_spaces)

                    # if office not full
                    if '0' in list_of_spaces:
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

                                # stop looping through spaces
                                break

                        # stop looping through row
                        break

    # Notify user of success
    print "Rooms allocated successfully"

    # call get_unallocated function to print
    # list of unallocated people if any
    get_unallocated(thefile)


def get_allocations():
    """Lists all the rooms and all their members on
    screen

    Called by this command:
        python allocate.py get allocations

    Returns:
        Prints members of non-empty rooms
    """
    # select all details from all rooms
    cursor.execute("SELECT name, type, capacity, spaces FROM rooms")

    # loop through rooms
    for row in cursor:
        # for each room, split it's spaces into a list
        list_of_spaces = row[3].split(',')

        # remove unicode encoding
        list_of_spaces = map(lambda x: x.encode('ascii'), list_of_spaces)

        # set flag to false i.e. assume the room is empty
        flag = False

        # loop through the spaces
        for i in list_of_spaces:
            # if room has at least one occupant
            # set flag to true and exit
            if i != '0':
                flag = True
                break

        # when flag is true i.e. at least one person has been found
        # in that room, print the details of that room
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


def print_allocations():
    """Prints all the rooms and all their members in a text
    file called allocations.txt

    Called by this command:
        python allocate.py print allocations

    Returns:
        Prints members of non-empty rooms in
        allocations.txt and returns Success
    """
    # select all details from all rooms
    cursor.execute("SELECT name, type, capacity, spaces FROM rooms")

    # create file allocations.txt and add heading
    with open("allocations.txt", "a") as fo:
        fo.write("^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
        fo.write("NEW LIST STARTS HERE\n")
        fo.write("^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")

    # loop through selected rooms
    for row in cursor:
        # for each room, split it's spaces into a list
        list_of_spaces = row[3].split(',')

        # remove unicode encoding
        list_of_spaces = map(lambda x: x.encode('ascii'), list_of_spaces)

        # set flag to false i.e. assume the room is empty
        flag = False

        # loop through the spaces
        for i in list_of_spaces:
            # if room has at least one occupant
            if i != '0':
                # set flag to true and exit
                flag = True
                break

        # if flag is true, print the details to allocations.txt
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

    print "Room details printed to allocations.txt"
    return "Success"


def print_members(room):
    """Shows the list of people allocated to a room
    Called by command:
        python allocate.py print allocations <roomname>

    Args:
        A room name

    Returns:
        A list of room members on screen

    Raises:
        A "No such room" sqlite3 Error
    """

    try:
        # select required room from databse
        cursor.execute("SELECT type, capacity, spaces from rooms where name = ?", ([room]))
    except sqlite3.Error:
        print "Error occurred"

    # fetch and assign the result into theroom list
    theroom = cursor.fetchone()

    # exit if no room found
    if theroom is None:
        print "No such room"
        quit()

    # print the info in theroom list
    print "**********ROOM DETAILS************\n"
    print "ROOM TYPE: %s \t ROOM NAME: %s \t CAPACITY: %s \n\n" % (theroom[0], room, theroom[1])

    print "**********ROOM MEMBERS************\n"

    list_of_spaces = theroom[2].split(',')
    list_of_spaces = map(lambda x: x.encode('ascii'), list_of_spaces)  # remove unicode encoding

    for i in list_of_spaces:
        if i != '0':
            print i


def get_unallocated(thefile):
    """Shows the list of unallocated people
    Called by the allocate function before it exits

    Args:
        A txt file

    Returns:
        A message "No Unallocated People" otherwise
            prints a list of unallocated people on screen
    """

    #  will hold a line from the file temporarily
    temp = []
    #  will hold names of unallocated people
    unallocated_people = []

    with open(thefile) as f:
        # reads file and puts each line in temp list
        # the temp list will then be used for checking names

        for line in f:
            # put line in temp only if it's length is greater
            # than two
            if len(line) > 2:
                temp = line.split()

                # get name of the person in current line
                name = temp[0] + " " + temp[1]

                # assume person is unallocated.
                # this flag will be set to true if person
                # is actually allocated
                thereflag = False

                # select all offices from db
                cursor.execute("SELECT name, capacity, spaces from rooms where type = 'OFFICE' ")

                # loop through rows. If name is found in spaces,
                # assign thereflag true and  break
                for row in cursor:
                    list_of_spaces = row[2].split(',')
                    # remove unicode encoding
                    list_of_spaces = map(lambda x: x.encode('ascii'), list_of_spaces)

                    if name in list_of_spaces:  # if name exists in db
                        thereflag = True
                        break

                if thereflag is False:  # person not found
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


def depopulate():
    """Deletes the rooms table from the database.
    Called by this command:
        python allocate.py depopulate

    Args:
        None

    Returns:
        A success message: Depopulation successful.
              Run populate.py again to repopulate.

    Raises:
        sqlite3Error: An error occurred while dropping the table.
    """
    try:
        cursor.execute("DROP TABLE rooms")
        conn.commit()
        print "Depopulation successful. Run populate.py again to repopulate."
    except sqlite3.Error:
        print "Depopulation already done. Run populate.py."

    return "Success"


# call methods based on arguments given
if len(sys.argv) >= 2:
    # call allocate rooms
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

    # remove everything in db
    if len(sys.argv) == 2 and sys.argv[1] == "depopulate":
        depopulate()
else:
    print "No such command. Extra input required"
