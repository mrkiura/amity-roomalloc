class Room(object):
    """The superclass Room. All room types
    will inherit from this class. The init
    method initializes every room with a name"""
    def __init__(self, name):
        self.name = name


class Office(Room):
    capacity = 6
    type = "OFFICE"
    spaces = ['0', '0', '0', '0', '0', '0']

    def __repr__(self):
        return '{"name": \"%s\", "type" : \"%s\", "capacity" : %d, "spaces" : %s}' % (self.name, self.type, self.capacity, self.spaces)


class LivingSpace(Room):
    capacity = 4
    type = "LIVING"
    spaces = ['0', '0', '0', '0']

    def __repr__(self):
        return '{"name": \"%s\", "type" : \"%s\", "capacity" : %d, "spaces" : %s}' % (self.name, self.type, self.capacity, self.spaces)
