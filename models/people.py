class Person(object):
    def __init__(self, name, position):
        self.name = name
        self.position = position


class Fellow(Person):
    # Member variable for allocation
    # Staff can't be allocated living space
    position = "FELLOW"
    pass


class Staff(Person):
    # Member variable for allocation
    # Staff can't be allocated living space
    position = "STAFF"
    pass
