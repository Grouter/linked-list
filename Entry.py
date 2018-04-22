class Entry:
    def __init__(self, data, next_, prev):
        self.data = data
        self.next = next_
        self.prev = prev

    """PYTHON FUNCTIONS"""

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "(Object)LinkedList Entry -> value: %s" % self.data
