class Person(object):
    def __init__(self, name):
        self.name = name


class Fellow(Person):
    # Member variable for allocation
    # Staff can't be allocated living space
    position = "FELLOW"
    rooms_allocated = ['0', '0']

    def __repr__(self):
        return '{"name": \"%s\", "position": \"%s\", "rooms_allocated": %s}' % (self.name, self.position, self.rooms_allocated)


class Staff(Person):
    # Member variable for allocation
    # Staff can't be allocated living space
    position = "STAFF"
    rooms_allocated = ['0']

    def __repr__(self):
        return '{"name": \"%s\", "position": \"%s\", "rooms_allocated": %s}' % (self.name, self.position, self.rooms_allocated)
