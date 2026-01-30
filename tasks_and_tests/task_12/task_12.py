class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        key_bytes = bytearray(key, encoding="UTF-8")
        sm = 0
        for i in range(len(key_bytes)):
            sm += key_bytes[i]
        index = sm % self.size
        return index

    def put(self, key, value):
        start_index = self.hash_fun(key)
        lowest_hits_index = start_index
        for i in range(self.size):
            index = (start_index + i) % self.size
            if self.hits[index] < self.hits[lowest_hits_index]:
                lowest_hits_index = index

            if self.slots[index] == key or self.slots[index] is None:
                self.slots[index] = key
                self.values[index] = value
                self.hits[index] = 0
                return index

        self.slots[lowest_hits_index] = key
        self.values[lowest_hits_index] = value
        self.hits[lowest_hits_index] = 0
        return lowest_hits_index

    def get(self, key):
        start_index = self.hash_fun(key)
        for i in range(self.size):
            index = (start_index + i) % self.size
            if self.slots[index] == key:
                self.hits[index] = self.hits[index] + 1
                return self.values[index]

            if self.slots[index] is None:
                return None

        return None
