class Room(object):

    def __init__(self, name):
        self.name = name


class Office(Room):
    capacity = 6

    def __init__(self, name):
        pass


class LivingSpace(Room):
    capacity = 4

    def __init__(self, name):
        pass
