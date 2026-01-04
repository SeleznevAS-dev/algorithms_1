class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        value_bytes = bytearray(value, encoding="UTF-8")
        sm = 0
        for i in range(len(value_bytes)):
            sm += value_bytes[i]
        index = sm % self.size
        return index

    def seek_slot(self, value):
        index = self.hash_fun(value)
        start_index = index
        while True:
            if self.slots[index] is None:
                return index
            index = (index + self.step) % self.size
            if index == start_index:
                return None

    def put(self, value):
        index = self.hash_fun(value)
        start_index = index
        while True:
            if self.slots[index] is None:
                self.slots[index] = value
                return index
            index = (index + self.step) % self.size
            if index == start_index:
                return None

    def find(self, value):
        index = self.hash_fun(value)
        start_index = index
        while True:
            if self.slots[index] == value:
                return index
            if self.slots[index] is None:
                return None
            index = (index + self.step) % self.size
            if index == start_index:
                return None
