import sqlite3
from models.rooms import Office, LivingSpace


def populate():
    # lists of the room names
    office_names = ["Narnia", "Camelot", "Krypton", "Valhalla", "Hogwarts",
                    "Mordor", "Occulus", "Midgard", "Orange", "Turqoise"]

    livingspace_names = ["Wood", "Paper", "Stone", "Wick", "Tower",
                         "Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw",
                         "Terra"]

    # will hold the rooms objects created from the models
    office_objects = []
    livingspace_objects = []

    # initialize office spaces
    for i in range(0, 10):
        office_objects.append(Office(office_names[i]))

    # initialize living spaces
    for i in range(0, 10):
        livingspace_objects.append(LivingSpace(livingspace_names[i]))

    # Populate database with empty rooms
    conn = sqlite3.connect("roomalloc.db")
    cursor = conn.cursor()

    # will hold tuples containing information for
    # each room to be written to the database
    office_populator = []
    livingspace_populator = []

    for i in range(0, 10):
        office_populator.append((office_objects[i].name,
                                 office_objects[i].type,
                                 office_objects[i].capacity,
                                ",".join(office_objects[i].spaces)))

    for i in range(0, 10):
        livingspace_populator.append((livingspace_objects[i].name,
                                     livingspace_objects[i].type,
                                     livingspace_objects[i].capacity,
                                     ",".join(livingspace_objects[i].spaces)))

    # create rooms table
    cursor.execute("""CREATE TABLE IF NOT EXISTS rooms
                   (name text PRIMARY KEY, type text, capacity integer, spaces text)""")

    # insert the data (empty rooms)
    try:
        #  insert offices
        cursor.executemany("INSERT INTO rooms VALUES (?, ?, ?, ?)", office_populator)
        conn.commit()

        # insert living spaces
        cursor.executemany("INSERT INTO rooms VALUES (?, ?, ?, ?)", livingspace_populator)
        conn.commit()

        print "Database populated successfully"
    except sqlite3.IntegrityError:
        print "Already populated"

    # for testing
    return [office_populator, livingspace_populator]

# call the populate function
populate()