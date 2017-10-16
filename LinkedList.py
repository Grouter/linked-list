"""DOUBLY LINKED-LIST"""


class Entry:
    def __init__(self, _data, _next, _prev):
        self.data = _data
        self.next = _next
        self.prev = _prev


class LinkedList:
    def __init__(self, linked_list=None):
        if linked_list is None:
            self.first = None
            self.last = None
            self.size = 0
        else:
            for element in linked_list:
                self.add(element)

    """ADDING TO LIST"""

    # add @new_entry at the end of the list (not supposed to be used by user)
    def entry_add(self, new_entry):
        self.last.next = new_entry
        self.last = new_entry
        self.size += 1

    def add_at_index(self, index, _data):
        """Add new element with @data at @index"""
        if index == 0:
            self.add_first(_data)
        else:
            e = Entry(_data, self.entry_get(index), self.entry_get(index - 1))
            self.entry_get(index).prev = e
            self.entry_get(index - 1).next = e
            self.size += 1

    def add_first(self, _data):
        """Add new element at the beginning of the list"""
        if self.size == 0:
            self.first = self.last = Entry(_data, None, None)
        else:
            e = Entry(_data, self.first, None)
            e.next.prev = e
            self.first = e
        self.size += 1

    def add(self, _data):
        """Add new element with @data to the end of the list"""
        if self.size == 0:
            self.first = self.last = Entry(_data, None, None)
        else:
            self.last.next = Entry(_data, None, self.last)
            self.last = self.last.next
        self.size += 1
        return True

    """REMOVING FROM LIST"""

    def entry_remove(self, entry):
        """Removes @entry (not supposed to be used by user)"""
        if self.size == 0:
            raise ValueError('List is empty')
        if entry == self.first:
            if self.size == 1:
                self.first = self.last = None
            else:
                self.first = self.first.next
                self.first.prev = None
        elif entry == self.last:
            if self.last.prev is not None:
                self.last.prev.next = None
                self.last = self.last.prev
        else:
            entry.next.prev = entry.prev
            entry.prev.next = entry.next
        self.size -= 1

    def remove_index(self, index):
        """Removes element at @index"""
        cur_index = 0
        cur_entry = self.first
        while cur_entry is not None:
            if cur_index == index:
                self.entry_remove(cur_entry)
                return cur_entry
            cur_entry = cur_entry.next
            cur_index += 1
        raise IndexError('Index out of range')

    def remove(self, _data):
        """Removes element with @data"""
        cur_entry = self.first
        while cur_entry is not None:
            if cur_entry.data == _data:
                self.entry_remove(cur_entry)
                return cur_entry
            cur_entry = cur_entry.next
        raise ValueError('No such element')

    def remove_first(self):
        """Removes first element of the list"""
        if self.size == 0:
            raise ValueError("No such element")
        else:
            r = self.first.data
            self.entry_remove(self.first)
            return r

    def remove_last(self):
        """Removes last element"""
        if self.size == 0:
            raise ValueError("No such element")
        else:
            r = self.last.data
            self.entry_remove(self.last)
            return r

    """GETTING FROM LIST"""

    def entry_get(self, index):
        """returns Entry object at @index (not supposed to be used by user)"""
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
        return entry

    def index_of(self, _data):
        """Returns first occurrence of element which data == @data (returns -1 if does not exist)"""
        index = 0
        for iter_data in self:
            if iter_data == _data:
                return index
            index += 1
        return -1

    def get(self, index):
        """Returns element at @index"""
        return self.entry_get(index).data

    def get_first(self):
        """Returns first element"""
        if self.size == 0:
            raise ValueError('No such element')
        return self.first.data

    def get_last(self):
        """Returns last element"""
        if self.size == 0:
            raise ValueError('No such element')
        return self.last.data

    """OTHER METHODS"""

    def set(self, index, _data):
        """Sets elements data at @index to @data"""
        self.entry_get(index).data = _data

    def swap(self, index_a, index_b):
        """Swaps element on @index_a with element at @index_b"""
        if 0 < index_a < self.size - 1 and 0 < index_b < self.size - 1:
            self.get(index_a).next, self.get(index_b).next = self.get(index_b).next, self.get(index_a).next
            self.get(index_a).prev, self.get(index_b).prev = self.get(index_b).prev, self.get(index_a).prev
        else:
            raise IndexError('No such index')

    def to_list(self):
        """Returns python list made from this list"""
        rtrn_list = []
        for iter_data in self:
            rtrn_list.append(iter_data)
        return rtrn_list

    def to_tuple(self):
        """Returns python tuple made from this list"""
        return tuple(self.to_list())

    def clear(self):
        """Removes all elements from list"""
        self.first = self.last = None
        self.size = 0

    def contains(self, _data):
        """Check if element with @data exists"""
        for iter_data in self:
            if iter_data == _data:
                return True
        return False

    def reverse(self):
        """Reverse list"""
        cur_entry = self.first
        while cur_entry is not None:
            cur_entry.next, cur_entry.prev = cur_entry.prev, cur_entry.next
            cur_entry = cur_entry.prev
        self.first, self.last = self.last, self.first

    def cut(self, index):
        """Create 2 lists cut at @index (element at @index will be included in first list)"""
        rtrn_list = [[],[]]
        cur_index = 0
        for el in self:
            if cur_index <= index:
                rtrn_list[0].append(el)
            else:
                rtrn_list[1].append(el)
            cur_index += 1
        return rtrn_list

    """PYTHON FUNCTIONS"""

    # MATHEMATICAL OPERATIONS
    def __len__(self):
        return self.size

    def __abs__(self):
        cur_entry = self.first
        while cur_entry is not None:
            if type(cur_entry.data) == int or type(cur_entry.data) == float:
                cur_entry.data = abs(cur_entry.data)
            cur_entry = cur_entry.next

    def __add__(self, other):
        cur_entry = other.first
        while cur_entry is not None:
            self.entry_add(cur_entry)
            cur_entry = cur_entry.next
        return self

    # LOGICAL OPERATIONS
    def __bool__(self):
        return self.size > 0

    # OTHER
    def __str__(self):
        return ",".join(str(val) for val in self)

    def __iter__(self):
        cur_entry = self.first
        while cur_entry is not None:
            yield cur_entry.data
            cur_entry = cur_entry.next

    def __contains__(self, item):
        return self.contains(item)

    def __copy__(self):
        return LinkedList(self)

    def __del__(self):
        self.clear()

    def __reversed__(self):
        rtrn_list = self.__copy__()
        rtrn_list.reverse()
        return rtrn_list
