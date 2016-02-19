"""Room module."""


class Room(object):
    """The superclass Room which all rooms inherit from."""

    def __init__(self, name):
        """Room constructor initializing room with name."""
        self.name = name


class Office(Room):
    """Office class inheriting from room class."""

    capacity = 6
    type = "OFFICE"
    spaces = ['0', '0', '0', '0', '0', '0']

    def __repr__(self):
        """Representation of an Office.

        Returns:
            A dict with the room's details
        """
        return '{"name": \"%s\", "type" : \"%s\", "capacity" : %d, \
        "spaces" : %s}' % (self.name, self.type, self.capacity, self.spaces)


class LivingSpace(Room):
    """Living Space class inheriting from room class."""

    capacity = 4
    type = "LIVING"
    spaces = ['0', '0', '0', '0']

    def __repr__(self):
        """Representation of a Living Space.

        Returns:
            A dict with the room's details
        """
        return '{"name": \"%s\", "type" : \"%s\", "capacity" : %d, \
        "spaces" : %s}' % (self.name, self.type, self.capacity, self.spaces)
