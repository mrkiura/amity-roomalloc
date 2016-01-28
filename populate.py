import sqlite3
from models.rooms import Office, LivingSpace

# Initializes ten office spaces, from O1
# to O10
O1 = Office("Office1")
O2 = Office("Office2")
O3 = Office("Office3")
O4 = Office("Office4")
O5 = Office("Office5")
O6 = Office("Office6")
O7 = Office("Office7")
O8 = Office("Office8")
O9 = Office("Office9")
O10 = Office("Office10")

# Initializes ten living spaces, from L1
# to L10
L1 = LivingSpace("LivingSpace1")
L2 = LivingSpace("LivingSpace2")
L3 = LivingSpace("LivingSpace3")
L4 = LivingSpace("LivingSpace4")
L5 = LivingSpace("LivingSpace5")
L6 = LivingSpace("LivingSpace6")
L7 = LivingSpace("LivingSpace7")
L8 = LivingSpace("LivingSpace8")
L9 = LivingSpace("LivingSpace9")
L10 = LivingSpace("LivingSpace10")


"""Populate database with empty rooms"""
conn = sqlite3.connect("data/roomalloc.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS rooms
                  (name text PRIMARY KEY, type text, capacity integer, spaces text)""")

offices = [(O1.name, O1.type, O1.capacity, ",".join(O1.spaces)),
           (O2.name, O2.type, O2.capacity, ",".join(O2.spaces)),
           (O3.name, O3.type, O3.capacity, ",".join(O3.spaces)),
           (O4.name, O4.type, O4.capacity, ",".join(O4.spaces)),
           (O5.name, O5.type, O5.capacity, ",".join(O5.spaces)),
           (O6.name, O6.type, O6.capacity, ",".join(O6.spaces)),
           (O7.name, O7.type, O7.capacity, ",".join(O7.spaces)),
           (O8.name, O8.type, O8.capacity, ",".join(O8.spaces)),
           (O9.name, O9.type, O9.capacity, ",".join(O9.spaces)),
           (O10.name, O10.type, O10.capacity, ",".join(O10.spaces))]

livings = [(L1.name, L1.type, L1.capacity, ",".join(L1.spaces)),
           (L2.name, L2.type, L2.capacity, ",".join(L2.spaces)),
           (L3.name, L3.type, L3.capacity, ",".join(L3.spaces)),
           (L4.name, L4.type, L4.capacity, ",".join(L4.spaces)),
           (L5.name, L5.type, L5.capacity, ",".join(L5.spaces)),
           (L6.name, L6.type, L6.capacity, ",".join(L6.spaces)),
           (L7.name, L7.type, L7.capacity, ",".join(L7.spaces)),
           (L8.name, L8.type, L8.capacity, ",".join(L8.spaces)),
           (L9.name, L9.type, L9.capacity, ",".join(L9.spaces)),
           (L10.name, L10.type, L10.capacity, ",".join(L10.spaces))]

try:
    cursor.executemany("INSERT INTO rooms VALUES (?, ?, ?, ?)", offices)
    conn.commit()

    cursor.executemany("INSERT INTO rooms VALUES (?, ?, ?, ?)", livings)
    conn.commit()

    print "Database populated successfully"
except sqlite3.IntegrityError:
    print "Already populated"



