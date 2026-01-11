class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        key_bytes = bytearray(key, encoding="UTF-8")
        sm = 0
        for i in range(len(key_bytes)):
            sm += key_bytes[i]
        index = sm % self.size
        return index

    def is_key(self, key):
        start_index = self.hash_fun(key)
        for i in range(self.size):
            index = (start_index + i) % self.size
            if self.slots[index] == key:
                return True

            if self.slots[index] is None:
                return False

        return False

    def put(self, key, value):
        start_index = self.hash_fun(key)
        for i in range(self.size):
            index = (start_index + i) % self.size
            if self.slots[index] == key or self.slots[index] is None:
                self.slots[index] = key
                self.values[index] = value
                return index

        return None

    def get(self, key):
        start_index = self.hash_fun(key)
        for i in range(self.size):
            index = (start_index + i) % self.size
            if self.slots[index] == key:
                return self.values[index]

            if self.slots[index] is None:
                return None

        return None
