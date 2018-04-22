from Entry import *


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add(self, _data):
        if self.size == 0:
            self.first = Entry(_data, None, None)
            self.last = self.first
        else:
            self.last.next = Entry(_data, None, self.last)
            self.last = self.last.next
        self.size += 1
        return True

    def remove_index(self, index):
        curIndex = 0
        curList = self.first
        while curList is not None:
            if curIndex == index:
                self.remove_entry(curList)
                self.size -= 1
                return curList
            curList = curList.next
            curIndex += 1
        raise IndexError('Index out of range')

    def remove(self, data):
        curList = self.first
        while curList is not None:
            if curList.data == data:
                self.remove_entry(curList)
                self.size -= 1
                return curList
            curList = curList.next
        raise ValueError('No such element')

    def remove_entry(self, entry):
        if entry == self.first:
            self.first = entry.next
            if entry.next is not None:
                entry.next.prev = None
        elif entry == self.last:
            self.last = entry.prev
            if entry.prev is not None:
                entry.prev.next = None
        else:
            entry.next.prev = entry.prev
            entry.prev.next = entry.next

    def contains(self, data):
        curList = self.first
        while curList is not None:
            if curList.data == data:
                return True
            curList = curList.next
        return False

    def get_index(self, value):
        index = 0
        curList = self.first
        while curList.next is not None:
            if curList.get_data == value:
                return index
            index += 1
            curList = curList.next
        return -1

    def get(self, index):
        if index < self.size / 2:
            entry = self.first
            while index > 0:
                entry = entry.next
                index -= 1
        else:
            entry = self.last
            while index + 1 < self.size:
                entry = entry.prev
                index += 1
        return entry.data

    def get_first(self):
        if self.size == 0:
            raise ValueError('No such element')
        return self.first.data

    def get_last(self):
        if self.size == 0:
            raise ValueError('No such element')
        return self.last.data

    """PYTHON FUNCTIONS"""

    def __len__(self):
        return self.size

    def __str__(self):
        values = ""
        curList = self.first
        while curList is not None:
            values += "%s, " % str(curList.data)
            curList = curList.next
        return "[%s]" % values[:-2]
