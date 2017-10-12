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

    # add new element with @data at @index
    def add_at_index(self, index, _data):
        if index == 0:
            self.add_first(_data)
        else:
            e = Entry(_data, self.entry_get(index), self.entry_get(index - 1))
            self.entry_get(index).prev = e
            self.entry_get(index - 1).next = e
            self.size += 1

    # add new element at the beginning of the list
    def add_first(self, _data):
        if self.size == 0:
            self.first = self.last = Entry(_data, None, None)
        else:
            e = Entry(_data, self.first, None)
            e.next.prev = e
            self.first = e
        self.size += 1

    # add new element with @data to the end of the list
    def add(self, _data):
        if self.size == 0:
            self.first = self.last = Entry(_data, None, None)
        else:
            self.last.next = Entry(_data, None, self.last)
            self.last = self.last.next
        self.size += 1
        return True

    """REMOVING FROM LIST"""

    # removes @entry (not supposed to be used by user)
    def entry_remove(self, entry):
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

    # removes element at @index
    def remove_index(self, index):
        cur_index = 0
        cur_entry = self.first
        while cur_entry is not None:
            if cur_index == index:
                self.entry_remove(cur_entry)
                return cur_entry
            cur_entry = cur_entry.next
            cur_index += 1
        raise IndexError('Index out of range')

    # removes element with @data
    def remove(self, _data):
        cur_entry = self.first
        while cur_entry is not None:
            if cur_entry.data == _data:
                self.entry_remove(cur_entry)
                return cur_entry
            cur_entry = cur_entry.next
        raise ValueError('No such element')

    # removes first element of the list
    def remove_first(self):
        if self.size == 0:
            raise ValueError("No such element")
        else:
            r = self.first.data
            self.entry_remove(self.first)
            return r

    # removes last element
    def remove_last(self):
        if self.size == 0:
            raise ValueError("No such element")
        else:
            r = self.last.data
            self.entry_remove(self.last)
            return r

    """GETTING FROM LIST"""

    # returns Entry object at @index (not supposed to be used by user)
    def entry_get(self, index):
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

    # returns first occurrence of element which data == @data (returns -1 if does not exist)
    def index_of(self, _data):
        index = 0
        for iter_data in self:
            if iter_data == _data:
                return index
            index += 1
        return -1

    # returns element at @index
    def get(self, index):
        return self.entry_get(index).data

    # returns first element
    def get_first(self):
        if self.size == 0:
            raise ValueError('No such element')
        return self.first.data

    # returns last element
    def get_last(self):
        if self.size == 0:
            raise ValueError('No such element')
        return self.last.data

    """OTHER METHODS"""

    # sets elements data at @index to @data
    def set(self, index, _data):
        self.entry_get(index).data = _data

    # swaps element on @index_a with element at @index_b
    def swap(self, index_a, index_b):
        if 0 < index_a < self.size - 1 and 0 < index_b < self.size - 1:
            self.get(index_a).next, self.get(index_b).next = self.get(index_b).next, self.get(index_a).next
            self.get(index_a).prev, self.get(index_b).prev = self.get(index_b).prev, self.get(index_a).prev
        else:
            raise IndexError('No such index')

    # returns python list made from this list
    def to_list(self):
        rtrn_list = []
        for iterData in self:
            rtrn_list.append(iterData)
        return rtrn_list

    # returns python tuple made from this list
    def to_tuple(self):
        return tuple(self.to_list())

    # removes all elements from list
    def clear(self):
        self.first = self.last = None
        self.size = 0

    # check if element with @data exists
    def contains(self, _data):
        for iterData in self:
            if iterData == _data:
                return True
        return False

    def reverse(self):
        cur_entry = self.first
        while cur_entry is not None:
            cur_entry.next, cur_entry.prev = cur_entry.prev, cur_entry.next
            cur_entry = cur_entry.prev
        self.first, self.last = self.last, self.first

    # create 2 lists cut at @index (element at @index will be included in first list)
    def cut(self, index):
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
