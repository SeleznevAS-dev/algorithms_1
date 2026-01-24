class BloomFilter:
    def __init__(self, f_len):
        self.filter_len = f_len
        self.bits = int(1 << f_len)
        self.num_hash1 = 17
        self.num_hash2 = 223

    def hash1(self, str1):
        # 17
        res = 0
        for c in str1:
            code = ord(c)
            res *= self.num_hash1
            res += code
            res %= self.filter_len

        res = 1 << res

        return res

    def hash2(self, str1):
        # 223
        res = 0
        for c in str1:
            code = ord(c)
            res *= self.num_hash2
            res += code
            res %= self.filter_len

        res = 1 << res

        return res

    def add(self, str1):
        mask1 = self.hash1(str1)
        self.bits = self.bits | mask1
        mask2 = self.hash2(str1)
        self.bits = self.bits | mask2

    def is_value(self, str1):
        mask1 = self.hash1(str1)
        mask1_res = (self.bits & mask1) != 0
        mask2 = self.hash2(str1)
        mask2_res = (self.bits & mask2) != 0

        if mask1_res and mask2_res:
            return True

        return False
